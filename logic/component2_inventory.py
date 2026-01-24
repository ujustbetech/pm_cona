import pandas as pd
import numpy as np
from datetime import datetime


def run_component2(df: pd.DataFrame):
    """
    Component 2 — Inventory Dormancy Analysis
    Optimized for web execution (PythonAnywhere-safe)
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
        "Unit of Measure Code",
    ]

    df = df[required_cols]

    # ----------------------------
    # EARLY FILTERS (CRITICAL)
    # ----------------------------
    df["Remaining Quantity"] = pd.to_numeric(
        df["Remaining Quantity"], errors="coerce"
    ).fillna(0)

    df = df[df["Remaining Quantity"] > 0]

    df["Posting Date"] = pd.to_datetime(
        df["Posting Date"], errors="coerce", dayfirst=True
    )

    cutoff_date = pd.Timestamp("2025-01-01")
    df = df[df["Posting Date"] >= cutoff_date]

    # ----------------------------
    # TYPE CLEANING
    # ----------------------------
    df["Cost Amount (Actual)"] = pd.to_numeric(
        df["Cost Amount (Actual)"], errors="coerce"
    ).fillna(0)

    df["Location Code"] = (
        df["Location Code"].astype(str).str.strip().replace("nan", "UNKNOWN")
    )

    today = pd.Timestamp(datetime.now().date())

    # ----------------------------
    # LAST POSTING DATE (FAST VERSION)
    # ----------------------------
    last_posting = (
        df.groupby(["Item No.", "Location Code"], as_index=False)
          .agg(Last_Posting_Date=("Posting Date", "max"))
    )

    # ----------------------------
    # CURRENT STOCK (AGGREGATION)
    # ----------------------------
    current_stock = (
        df.groupby(
            ["Item No.", "Location Code", "Unit of Measure Code"],
            as_index=False
        )
        .agg(
            Description=("Description", "first"),
            Category=("Item Category Code", "first"),
            Subcategory=("Item Subcategory Code", "first"),
            On_Hand=("Remaining Quantity", "sum"),
            Stock_Value=("Cost Amount (Actual)", "sum"),
        )
    )

    # ----------------------------
    # MERGE & DORMANCY
    # ----------------------------
    result = current_stock.merge(
        last_posting,
        on=["Item No.", "Location Code"],
        how="left",
    )

    result["Days Dormant"] = (
        today - result["Last_Posting_Date"]
    ).dt.days

    # ----------------------------
    # STATUS CLASSIFICATION
    # ----------------------------
    result["Status"] = "Active"
    result.loc[result["Days Dormant"] > 60, "Status"] = "Slow-Moving"
    result.loc[result["Days Dormant"] > 365, "Status"] = "Dead"

    # ----------------------------
    # VALUE COLUMNS
    # ----------------------------
    result["Active_Value"] = np.where(
        result["Status"] == "Active", result["Stock_Value"], 0
    )
    result["Slow_Moving_Value"] = np.where(
        result["Status"] == "Slow-Moving", result["Stock_Value"], 0
    )
    result["Dead_Value"] = np.where(
        result["Status"] == "Dead", result["Stock_Value"], 0
    )

    # ----------------------------
    # DISPLAY FIELDS
    # ----------------------------
    result["On_Hand_Display"] = (
        result["On_Hand"].round(0).astype("Int64")
    )

    result["Last Posting Date"] = (
        result["Last_Posting_Date"].dt.strftime("%d-%m-%Y")
    )

    # ----------------------------
    # KPI SUMMARY
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
        "Active %": round(
            status_value.get("Active", 0) / total_value * 100, 1
        ) if total_value else 0,
        "Slow-Moving %": round(
            status_value.get("Slow-Moving", 0) / total_value * 100, 1
        ) if total_value else 0,
        "Dead %": round(
            status_value.get("Dead", 0) / total_value * 100, 1
        ) if total_value else 0,
    }

    # ----------------------------
    # HARD SAFETY CAP (WEB SAFE)
    # ----------------------------
    MAX_TABLE_ROWS = 2000

    if len(result) > MAX_TABLE_ROWS:
        result = (
            result.sort_values(
                ["Status", "Stock_Value"],
                ascending=[True, False]
            )
            .head(MAX_TABLE_ROWS)
        )

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
            "Last Posting Date",
            "Status",
            "Days Dormant",
            "Active_Value",
            "Slow_Moving_Value",
            "Dead_Value",
        ]
    ]

    return summary, result
