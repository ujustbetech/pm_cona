import pandas as pd

# Your company list (keep as-is)
codes = [
    "ADV-2003", "AHC-2599", "AKP-1179", "ALF-0653", "ALP-2195",
    "AMA-2038", "AMB-2082", "AMG-2410", "AMG-2497", "ANA-2081",
    "ANM-0674", "AOV-0677", "ARI-2009", "ART-0686", "ASH-2012",
    "AUR-2344", "AWA-2148", "BAL-0706", "BAN-2116", "BAR-2110",
    "BBP-0141", "BHA-0265", "BIH-0467", "BLU-0471", "BOA-1987",
    "BPM-2030", "BPT-2446", "BRG-0040", "BRM-2454", "BSP-0731",
    "CAM-1554", "CHE-2211", "CHI-0277", "CHI-2471", "CLA-0379",
    "CPA-1458", "CRE-0747", "CRY-2378", "CSM-2331", "DAS-2129",
    "DBE-2193", "DBR-0750", "DCP-2506", "DES-2108", "DES-2118",
    "DEV-0287", "DIG-0157", "DIG-091",   "DKE-0770", "DLP-2175",
    "DNE-1979", "DOT-2377", "DPP-2422", "DUR-065",  "DWA-2096",
    "EAR-0781", "EEX-2132", "EMO-2337", "ENI-2214", "EVE-0788",
    "EXM-2593", "FAI-2078", "FAX-0486", "FCI-2525", "GAT-1415",
    "GET-2493", "GLA-2010", "GLO-2136", "GLO-2158", "GRE-2157",
    "GRT-2234", "GST-2265", "GTM-2463", "GYA-0823", "GYP-2166",
    "HAB-2131", "HIM-0322", "HIR-0842", "HLW-1498", "HMT-2176",
    "HOT-2105", "HOT-2134", "HOT-2435", "HPS-2543", "HRI-2527",
    "HSS-2613", "IIL-2618", "IIP-2192", "IIP-2249", "IIP-2263",
    "IMA-0724", "INA-2613", "IND-2436", "INF-2130", "INF-2143",
    "IRP-0849", "IXS-2468", "JA&-1312", "JAY-1994", "JIV-2514",
    "JKC-2233", "JOH-0880", "KAL-2077", "KAN-0342", "KAS-1710",
    "KBS-2409", "KCM-0904", "KHG-2659", "KJI-0886", "KMS-0903",
    "KMU-0910", "KPG-2588", "KRI-2048", "KRI-579",  "KTC-1019",
    "KUL-0921", "KUM-0360", "LAB-0492", "LAE-2603", "LAX-0521",
    "LAX-1978", "LGR-2173", "LIP-2512", "M3P-0934", "MAA-0104",
    "MAA-2273", "MAC-2592", "MAH-2025", "MAH-2133", "MAN-0372",
    "MAR-2019", "MAT-0376", "MAV-2441", "MCS-1670", "MET-0967",
    "MMA-2486", "MME-2582", "MOK-0825", "MOT-2123", "MRV-2170",
    "MRX-2425", "MSA-1200", "MSD-2573", "MSP-1671", "MUK-0982",
    "NAC-1006", "NAT-2031", "NAV-2013", "NEE-2070", "NEP-2420",
    "NIK-2018", "NS&-1491", "NUW-1011", "NVI-0999", "NWE-1000",
    "OEE-2266", "OLS-1017", "OMI-1015", "OMN-2094", "P.P-430",
    "PAR-1999", "PAR-2067", "PAR-412",  "PER-0338", "PLN-1059",
    "POO-417",  "PPA-2182", "PPP-2591", "PRI-2121", "PRI-2159",
    "PRM-2656", "PSH-1061", "PSK-1062", "PWP-1071", "RAJ-1975",
    "RAM-433",  "RAV-1094", "RBL-1103", "RCE-2502", "RIY-437",
    "RKF-2119", "RLR-1118", "RPR-0310", "RRG-1440", "RRL-2177",
    "RRL-2242", "RSE-2600", "SAH-1129", "SAN-448",  "SAR-1147",
    "SAT-2147", "SBD-2533", "SBG-2045", "SCI-1243", "SHA-2050",
    "SHI-0313", "SHP-2523", "SHR-0017", "SHR-2141", "SHR-463",
    "SIG-2150", "SIN-2049", "SKC-2191", "SLM-1234", "SMB-2178",
    "SME-1172", "SMP-0936", "SMS-0524", "SPP-1188", "SPR-1173",
    "SPS-2430", "SRJ-2210", "SS -0218", "SSJ-2180", "SSP-0691",
    "STC-2485", "STE-2076", "SUM-0408", "SUP-2474", "TEC-2442",
    "TEL-1484", "TFC-2212", "TIH-1729", "TIW-2264", "TOT-2104",
    "TPP-1258", "TRA-2072", "TRA-2124", "TRF-2489", "TUR-1976",
    "TWO-1262", "UET-2179", "UND-2517", "UTT-2047", "VAN-2075",
    "VDP-2639", "VER-1973", "VIC-1290", "VIS-0517", "VIS-2142",
    "VIV-1306", "VLB-2342", "VNP-1289", "WAA-1313", "WOG-2476",
    "WON-1977", "WP&-1315", "WST-2062", "XIA-0968", "YAA-0501",
    "ZAL-1330"
]
# Set for fast membership testing (case-insensitive)
COMPANY_SET = {c.strip().upper() for c in codes}



def run_component5a_rm(
    df_items: pd.DataFrame,
    df_po: pd.DataFrame,
    df_receipts: pd.DataFrame,
    df_lines: pd.DataFrame,
    filter_to_key_vendors: bool = True
):
    """
    Component 5A — RM Purchase Order SLA
    Matches backup code: same-quarter On-Time, completion on all lines
    """
    # COPY & CLEAN
    df_items = df_items.copy()
    df_po = df_po.copy()
    df_receipts = df_receipts.copy()
    df_lines = df_lines.copy()

    for df in [df_items, df_po, df_receipts, df_lines]:
        df.columns = df.columns.str.strip()

    # 1. GET TRUE RM ITEM CODES
    df_items = df_items.rename(columns={
        "No.": "Item_No",
        "Inventory Posting Group": "Posting_Group"
    })

    rm_items = (
        df_items[df_items["Posting_Group"] == "RM"]["Item_No"]
        .astype(str)
        .str.strip()
        .unique()
    )

    rm_items_set = set(rm_items)

    # 2. FIND POs THAT CONTAIN AT LEAST ONE RM ITEM
    df_lines = df_lines.rename(columns={
        "Document No.": "PO_No",
        "No.": "Item_No",
        "Outstanding Quantity": "Outstanding_Qty"
    })

    df_lines["PO_No"] = df_lines["PO_No"].astype(str).str.strip().str.upper()
    df_lines["Item_No"] = df_lines["Item_No"].astype(str).str.strip()
    df_lines["Outstanding_Qty"] = pd.to_numeric(
        df_lines["Outstanding_Qty"], errors="coerce"
    ).fillna(0)

    rm_po_list = (
        df_lines[df_lines["Item_No"].isin(rm_items_set)]["PO_No"]
        .unique()
        .tolist()
    )

    if not rm_po_list:
        metrics = {"Total_RM_POs": 0, "On_Time_POs": 0, "Late_POs": 0, "On_Time_Pct": 0.0}
        table_df = pd.DataFrame(columns=["PO_No", "Vendor", "Order_Date", "Last_Receipt_Date",
                                        "Days_To_Receive", "Order_Quarter", "On_Time"])
        return metrics, table_df

    # 3. PURCHASE ORDER MASTER (RM ONLY)
    df_po = df_po.rename(columns={
        "No.": "PO_No",
        "Buy-from Vendor Name": "Vendor",
         "Buy-from Vendor No.": "Vendor_No",
        "Order Date": "Order_Date",
        "Last Receiving No.": "Last_Receiving_No"
    })

    df_po["Vendor_No"] = (
    df_po["Vendor_No"]
    .fillna("")
    .astype(str)
    .str.strip()
    .str.upper()
    )

    df_po["PO_No"] = df_po["PO_No"].astype(str).str.strip().str.upper()
    df_po["Last_Receiving_No"] = df_po["Last_Receiving_No"].fillna('').astype(str).str.strip().str.upper()
    df_po["Vendor"] = df_po["Vendor"].fillna("Unknown").astype(str).str.strip()

    # Robust Excel date parsing
    def to_date(val):
        if pd.isna(val):
            return pd.NaT
        if isinstance(val, (int, float)):
            try:
                return pd.to_datetime(val, unit='D', origin='1899-12-30')
            except:
                return pd.NaT
        return pd.to_datetime(val, errors='coerce', dayfirst=True)

    df_po["Order_Date"] = df_po["Order_Date"].apply(to_date)
    df_po = df_po.dropna(subset=["Order_Date"])

    # Filter to POs containing RM items (still early for efficiency)
    

    # ────────────────────────────────────────────────
    # STEP 1: Vendor Filter (FIRST)
    if filter_to_key_vendors:
        df_po = df_po[df_po["Vendor_No"].str.upper().isin(COMPANY_SET)].copy()
        print(f"DEBUG STEP 1 - After Vendor filter: {len(df_po)} POs remaining | Sample vendors: {df_po['Vendor'].unique()[:10].tolist()}")
    # ────────────────────────────────────────────────

    # ────────────────────────────────────────────────
    # STEP 2: Completion Filter (SECOND)
    po_completion = df_lines.groupby("PO_No")["Outstanding_Qty"].sum()
    completed_pos = po_completion[po_completion == 0].index.tolist()

    df_po = df_po[df_po["PO_No"].isin(completed_pos)]
    print(f"DEBUG STEP 2 - After Completion filter: {len(df_po)} POs remaining | Sample vendors: {df_po['Vendor'].unique()[:10].tolist()}")
    # ────────────────────────────────────────────────

    if df_po.empty:
        metrics = {"Total_RM_POs": 0, "On_Time_POs": 0, "Late_POs": 0, "On_Time_Pct": 0.0}
        table_df = pd.DataFrame(columns=["PO_No", "Vendor", "Order_Date", "Last_Receipt_Date",
                                        "Days_To_Receive", "Order_Quarter", "On_Time"])
        return metrics, table_df

    # 5. RECEIPT DATE MAPPING
    df_receipts = df_receipts.rename(columns={
        "No.": "Receipt_No",
        "Posting Date": "Posting_Date"
    })

    df_receipts["Receipt_No"] = df_receipts["Receipt_No"].astype(str).str.strip().str.upper()
    df_receipts["Posting_Date"] = df_receipts["Posting_Date"].apply(to_date)

    receipt_map = dict(zip(df_receipts["Receipt_No"], df_receipts["Posting_Date"]))
    df_po["Receipt_Date"] = df_po["Last_Receiving_No"].map(receipt_map)

    # ────────────────────────────────────────────────
    # STEP 3: Valid receipt & days >=0 filter (THIRD)
    df_po["Days_To_Receive"] = (df_po["Receipt_Date"] - df_po["Order_Date"]).dt.days

    df_po = df_po[
        df_po["Receipt_Date"].notna() &
        (df_po["Days_To_Receive"] >= 0)
    ].copy()

    print(f"DEBUG STEP 3 - After valid receipt & days >=0 filter: {len(df_po)} POs remaining | Sample vendors: {df_po['Vendor'].unique()[:10].tolist()}")
    # ────────────────────────────────────────────────

    if df_po.empty:
        metrics = {"Total_RM_POs": 0, "On_Time_POs": 0, "Late_POs": 0, "On_Time_Pct": 0.0}
        table_df = pd.DataFrame(columns=["PO_No", "Vendor", "Order_Date", "Last_Receipt_Date",
                                        "Days_To_Receive", "Order_Quarter", "On_Time"])
        return metrics, table_df

    # Same-quarter logic (unchanged)
    df_po["Order_Quarter"] = df_po["Order_Date"].dt.to_period("Q")
    df_po["Receipt_Quarter"] = df_po["Receipt_Date"].dt.to_period("Q")
    df_po["SLA_Status"] = (df_po["Receipt_Quarter"] == df_po["Order_Quarter"]).map({
        True: "On-Time",
        False: "Delayed"
    })

    df_po["Quarter"] = df_po["Order_Date"].dt.to_period("Q").astype(str)
    df_po["Month"] = df_po["Order_Date"].dt.to_period("M").astype(str)

    # 8. PERIOD SUMMARY (unchanged)
    summary = (
        df_po.groupby(["Month", "Quarter", "SLA_Status"])
        .size()
        .reset_index(name="PO_Count")
    )

    total_per_period = (
        summary.groupby(["Month", "Quarter"])["PO_Count"]
        .sum()
        .reset_index(name="Total_POs")
    )

    on_time_per_period = (
        summary[summary["SLA_Status"] == "On-Time"]
        .groupby(["Month", "Quarter"])["PO_Count"]
        .sum()
        .reset_index(name="On_Time_POs")
    )

    df_period = total_per_period.merge(
        on_time_per_period, on=["Month", "Quarter"], how="left"
    ).fillna(0)

    df_period["Within_SLA_Pct"] = (
        df_period["On_Time_POs"] / df_period["Total_POs"] * 100
    ).round(2)

    df_final = df_po.merge(
        df_period[["Month", "Quarter", "Within_SLA_Pct"]],
        on=["Month", "Quarter"],
        how="left"
    )

    # 9. OVERALL METRICS (initially on all vendors)
    overall_total = len(df_final)
    overall_on_time = len(df_final[df_final["SLA_Status"] == "On-Time"])

    metrics = {
        "Total_RM_POs": int(overall_total),
        "On_Time_POs": int(overall_on_time),
        "Late_POs": int(overall_total - overall_on_time),
        "On_Time_Pct": round((overall_on_time / overall_total) * 100, 2)
        if overall_total else 0.0
    }

    # 10. TABLE VIEW (unchanged)
    table_df = df_final[[
        "PO_No", "Vendor", "Order_Date", "Receipt_Date",
        "Days_To_Receive", "Quarter", "SLA_Status"
    ]].copy()

    table_df = table_df.rename(columns={
        "Receipt_Date": "Last_Receipt_Date",
        "Quarter": "Order_Quarter",
        "SLA_Status": "On_Time"
    })

    # Formatting for display / Excel (unchanged)
    if "Order_Quarter" in table_df.columns:
        table_df["Order_Quarter"] = table_df["Order_Quarter"].astype(str)

    if "Order_Date" in table_df.columns:
        table_df["Order_Date"] = table_df["Order_Date"].dt.strftime("%d-%m-%Y")

    if "Last_Receipt_Date" in table_df.columns:
        table_df["Last_Receipt_Date"] = table_df["Last_Receipt_Date"].dt.strftime("%d-%m-%Y")

    if "Days_To_Receive" in table_df.columns:
        table_df["Days_To_Receive"] = (
            pd.to_numeric(table_df["Days_To_Receive"], errors="coerce")
            .round(0)
            .astype("Int64")
        )

    if "Order_Quarter" in table_df.columns:
        table_df["Order_Quarter"] = (
            pd.PeriodIndex(table_df["Order_Quarter"], freq="Q")
            .strftime("Q%q-%Y")
        )

    return metrics, table_df