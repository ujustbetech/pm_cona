import pandas as pd
import numpy as np
from datetime import datetime


def run_component2(df: pd.DataFrame):
    """
    Component 2 — Inventory Dormancy Analysis
    On-hand items only
    Dormancy = today - last posting date
    Value-based visualisation (UOM-safe)
    """

    # ----------------------------
    # COPY & CLEAN
    # ----------------------------
    df = df.copy()
    df.columns = df.columns.str.strip()

    required_cols = [
        "Item No.",
        "Location Code",
        "Posting Date",
        "Remaining Quantity",
        "Cost Amount (Actual)",
        "Description",
        "Item Category Code",
        "Item Subcategory Code",
        "Unit of Measure Code"
    ]
    df = df[required_cols]

    # ----------------------------
    # TYPE CLEANING
    # ----------------------------
    df["Posting Date"] = pd.to_datetime(df["Posting Date"], errors="coerce", dayfirst=True)
    df["Remaining Quantity"] = pd.to_numeric(df["Remaining Quantity"], errors="coerce").fillna(0)
    df["Cost Amount (Actual)"] = pd.to_numeric(df["Cost Amount (Actual)"], errors="coerce").fillna(0)

    df["Location Code"] = (
        df["Location Code"]
        .astype(str)
        .str.strip()
        .replace("nan", "UNKNOWN")
    )

    # ----------------------------
    # FILTER: ON-HAND ONLY
    # ----------------------------
    df = df[df["Remaining Quantity"] > 0]

    today = pd.Timestamp(datetime.now().date())

    # ----------------------------
    # LAST POSTING DATE
    # ----------------------------
    last_posting = (
        df.groupby(["Item No.", "Location Code"])["Posting Date"]
        .max()
        .reset_index()
        .rename(columns={"Posting Date": "Last Posting Date"})
    )

    # ----------------------------
    # CURRENT STOCK
    # ----------------------------
    current_stock = (
        df.groupby(["Item No.", "Location Code", "Unit of Measure Code"])
        .agg(
            Description=("Description", "first"),
            Category=("Item Category Code", "first"),
            Subcategory=("Item Subcategory Code", "first"),
            On_Hand=("Remaining Quantity", "sum"),
            Stock_Value=("Cost Amount (Actual)", "sum"),
        )
        .reset_index()
    )

    # ----------------------------
    # MERGE & DORMANCY
    # ----------------------------
    result = current_stock.merge(
        last_posting,
        on=["Item No.", "Location Code"],
        how="left"
    )

    result["Days Dormant"] = (today - result["Last Posting Date"]).dt.days

    # ----------------------------
    # STATUS CLASSIFICATION
    # ----------------------------
    result["Status"] = "Active"
    result.loc[result["Days Dormant"] > 60, "Status"] = "Slow-Moving"
    result.loc[result["Days Dormant"] > 365, "Status"] = "Dead"

    # ----------------------------
    # 🔑 VALUE-BASED CHART COLUMNS (ENGINE SAFE)
    # ----------------------------
    result["Active_Value"] = np.where(
        result["Status"] == "Active",
        result["Stock_Value"],
        0
    )

    result["Slow_Moving_Value"] = np.where(
        result["Status"] == "Slow-Moving",
        result["Stock_Value"],
        0
    )
        # ------------------------------------------------
# 🔑 ENSURE ONE BAR PER UOM (ENGINE SAFE)
# ------------------------------------------------
    uom_value_map = (
        result[result["Status"] == "Slow-Moving"]
        .groupby("Unit of Measure Code")["Slow_Moving_Value"]
        .sum()
        .to_dict()
    )

    # Rank rows per UOM so only first row carries the value
    result["_uom_rank"] = (
        result.groupby("Unit of Measure Code").cumcount()
    )

    result["Slow_Moving_Value"] = np.where(
        result["_uom_rank"] == 0,
        result["Unit of Measure Code"].map(uom_value_map).fillna(0),
        0
    )

    result.drop(columns="_uom_rank", inplace=True)


    result["Dead_Value"] = np.where(
        result["Status"] == "Dead",
        result["Stock_Value"],
        0
    )

    # ----------------------------
    # DISPLAY FIELDS
    # ----------------------------
    result["On_Hand_Display"] = result["On_Hand"].round(0).astype("Int64")
    result["Last Posting Date"] = result["Last Posting Date"].dt.strftime("%d-%m-%Y")

    # ----------------------------
    # KPI SUMMARY (VALUE BASED)
    # ----------------------------
    status_value = result.groupby("Status")["Stock_Value"].sum()
    total_value = status_value.sum()

    summary = {
        "Total Items": len(result),
        "Active Items": int((result["Status"] == "Active").sum()),
        "Slow-Moving Items": int((result["Status"] == "Slow-Moving").sum()),
        "Dead Items": int((result["Status"] == "Dead").sum()),
        "Total Value": total_value,
        "Active Value": status_value.get("Active", 0),
        "Slow-Moving Value": status_value.get("Slow-Moving", 0),
        "Dead Value": status_value.get("Dead", 0),
        "Active %": round(status_value.get("Active", 0) / total_value * 100, 1) if total_value else 0,
        "Slow-Moving %": round(status_value.get("Slow-Moving", 0) / total_value * 100, 1) if total_value else 0,
        "Dead %": round(status_value.get("Dead", 0) / total_value * 100, 1) if total_value else 0,
    }

    # ----------------------------
    # FINAL COLUMN ORDER
    # ----------------------------
    result = result[
        [
            "Item No.",
            "Location Code",
            "Unit of Measure Code",
            "Description",
            "Category",
            "Subcategory",
            "On_Hand_Display",
            "Stock_Value",
            "Status",
            "Days Dormant",
            "Last Posting Date",
            "Active_Value",
            "Slow_Moving_Value",
            "Dead_Value",
        ]
    ]

    return summary, result
