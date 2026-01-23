import pandas as pd

# Your company list (keep as-is)
companies = [
    "ADVAITECH STUDIOS LLP", "AHUJA & CO.", "A.K.PACKAGING", "ALFA PACKAGING", 
    "AKAR LABELS PVT.LTD.", "AMALA EARTH PVT LTD", "AMBICA AGARBATHIES AROMA & INDUSTRIES PVT LTD",
    "AMAZING GROUPS", "AMAZING GRAPHICS", "ANAND ENTERPRISES", "ANMOL CORRUPACK PVT LTD",
    "AOVI & PRIYANSH DIGITAL PRINTER LLP", "ARIHANT ADVERTISING", "ARIHANT ENTERPRISE",
    "ASHISH JUMBO XEROX", "AURORA", "AWARD GALAXY", "SHREE BALAJI PRINTERS",
    "BANKE BIHARI TIMBER CO.", "BARCODE SOLUTION", "BHAUSAHEB B. PATIL", "BHAGWATI THERMOPACK",
    "BIHAR ELECTRIC TRADERS ASSOCIATION", "BLUE BOX CONSULTING", "BOARDSIGN",
    "BPMK VISUAL SOLUTIONS PVT LTD", "BHAGAVATI PRINTING AND TRADING CO.", "BHARGAVA BROTHERS",
    "BRAINTECH MEDIA", "BS PUBLICITY", "CAMPAIGN MASTERS", "CHHAYA ENTERPRISES",
    "CHINTAMANI ENTERPRISES", "CHITRA INDUSTRIES", "CLARKS INN SUITES GWALIOR",
    "CPAS TECHNOLOGIES PRIVATE LIMITED", "CREATIVE HOUSE", "CRYSTALLYZE",
    "CLASSIC STATIONER MART", "DASS CONTINENTAL", "DB ENTERPRISE", "DBRIGHT ADVERTISING",
    "DOODLE COLLECTION PVT LTD", "DESHMUKH ADVERTISERS", "DESIGN BRIDGE", "DEV PACKAGING",
    "DIGITAL PLUS", "DIGITAL SYSTEMS", "D K ENTERPRISE", "DRV INN LIMITED LIABILITY PARTNERSHIP",
    "D.N. ENTERPRISES", "DOT BADGES", "DASS POLYMERS PVT. LTD.", "DURGA TRADERS",
    "DWARIKA PRINT SOLUTION", "EARTH POLY PACK", "EEXCITED DIGITAL SOLUTIONS LLP",
    "E-MOTION FACTORY", "ENSEMBLE INTERNATIONAL", "EVEREST HOLOVISIONS LIMITED",
    "EXOTIC MILE PRIVATE LIMITED", "FAIR OPTICS", "FAX-CARE", "F.C.INFOTECH",
    "GATEWAY MICE", "GREAT EASTERN TRADING CO - WB", "GLASS MALL", "GLOBAL ELECTRONICS",
    "GLOBAL GIFTS", "GREAT EASTERN RETAIL PVT.LTD.", "GRAPH TECH", "GANPATI STEEL",
    "GUNJAN TIME", "GYANESH PACKAGING", "GYANESH PRINT AND PACK", "HABSUN MOTORS",
    "HIMALAYA INTERNATIONAL", "HIRA PRINT SOLUTIONS PVT LTD", "HOTEL LE WESTERN",
    "HMT GHADI WALA", "HOTEL SVN LAKE PALACE", "HOTEL GRAND KAILASH",
    "HOTEL OM TUNGA VIHAR", "HINDUSTAN PRAKASHAN SANTHA", "HOTEL ROYAL INTERNATIONAL",
    "HARI SIGN SYSTEMS", "INDIAMART INTERMESH LTD", "INEXT INNOVATIONS PRIVATE LIMITED",
    "INFOTRONICS INTEGRATORS (INDIA) PVT. LTD.", "IMAGINE MARKETING LIMITED",
    "INOTECH ADVERTISING", "INDIGO PRINTS (PROP. TRIDEV KAPOOR)", "INFINITI RETAIL LIMITED",
    "IMAGINARIUM RAPID PVT. LTD", "INNOVATIVEX SOLUTIONS", "JAHANVI ADVT & MKT",
    "JAY SHREE SHYAM ELECTRICALS", "JIVO ENTERPRISES", "JK COMPUTER", "JOHNY AND JINNY",
    "KALA ADS", "KANKAI ENTERPRISES", "K AND S ADVERTISING", "KALLU BOX & SONS",
    "KHUSHI COMMUNICATION MEHATWARA", "KHUSHI GRAPHICS", "KALYAN JEWELLERS INDIA LIMITED",
    "KHUSHI MULTIPACK SOLUTIONS LLP", "KMUNOTAG PRIVATE LIMITED", "K P GRAPHIC",
    "KRISHNA CROCKERY", "KRITIKA ADVERTISING", "KINGS TRADING CO", "KULODAY COMPU FORMS",
    "KUMBHAR ENTERPRISE", "LABDHI ENTERPRISES", "LATA ENTERPRISES", "LAXMI GRAPHICS",
    "LAXMI ENFRATECH", "LEO GRAPHICS", "LINTAS INDIA PVT LTD", "M3 PRODUCTIONS",
    "MAA NARAYANI CREATION", "MAA AMBE CREATION", "MAX ANGEL CORPORATION",
    "MAHARASHTRA METAL WORKS PVT LIMITED", "MAHARANI HOTEL", "MANAV ENTERPRISES",
    "MARKET SEARCH INDIA PVT. LTD.", "MATRIX TECHNOLOGIES", "MAHANAGARI VARTAHAR",
    "MAHAVIR COMPUTER STATIONERY AND XEROX", "METCO CREATIONS", "M M ADVERTISING AGENCY",
    "M.M. ENTERPRISES", "MOKSH TRADING CO", "MOTEL BLUE SAPPHIRE",
    "MAGIC RETAIL VENTURES PVT. LTD.", "MR XEROX & STATIONERY", "M/S SIMRAN AD",
    "M/S D3 SIGNAGE", "MODICLE STUDIOS PVT LTD", "MUKTA PACKAGING",
    "NISSAN ADVERTISING CO.", "NATIONAL SECURITIES DEPOSITORY LIMITED",
    "NAVBHARAT ELECTRICALS", "NEELANJ BUSINESS SOLUTION LLP", "NEO PACK (INDIA)",
    "NIKHIL ASSOCIATES", "NOVELTY STATIONERY & COMPUTERS", "NUWORLD RETAIL PRIVATE LIMITED",
    "NEW VAMA INTERNATIONAL", "NEW WAY ENTERPRISES", "OM ELECTRONIC & ELECTRICAL",
    "ONE LEAP SOLUTIONS PVT.LTD", "OMKAR MULTIPACK INDUSTRIES",
    "OMNY ADVERTISING AGENCY INDIA PVT LTD", "P.P.PRODUCTS", "PARIKHYAT LIVING",
    "PARTH FOOD VENTURES", "PARTAP COMPUGRAPHICS", "PERFECT PACKERS", "PRINT LINE",
    "POONAM ENTERPRISES", "PRUPADU PRINT & ADD 'S", "PADMAVATI PRINT & PACK",
    "PRIME OPTICS", "PRINTZONE", "PRINT MARK", "PRINT SHOPPE", "PRINTSOUK",
    "PW PRINTWAYS INDIA PRIVATE LIMITED", "RAJESH DESIGN'S STUDIO", "RAMAYA PACKAGING",
    "RAVECHI STATIONERY STORES", "RIDDISIDDHI BULLIONS LTD", "RHYTHM CORNER ENTERPRISES",
    "RIYANSH PACKAGING", "RK FLEX PRINTERS AND DIGITAL WORKS",
    "RAM LAL RAM CHANDRA (INDIA) LTD.", "R.K.PRINTERS", "RAJ RAJENDRA GOLD",
    "RELIANCE RETAIL LIMITED", "RUSHABHDEV ENTERPRISES", "SAHIL ADVERTISING",
    "SANJAY ARTS", "SARASWATI ADVERTISERS", "SATYAM ELECTRONIC AND ELECTRICALS",
    "SHREE BALAJI DHARMAJAGRUTI SAMITI", "SBGI", "SUPREME CORRUGATING INDUSTRIES PVT.LTD.",
    "SHAVI ADVERTISING CO", "SHIVAM ENTERPRISES", "SHIVAM PACKAGING",
    "SHREE VINAYAK MARKETING", "SHRADDHA SALES", "SHREEJI ENTERPRISES", "SIGN ADS",
    "SINGHANIA OVERSEAS PVT LTD", "SRI KRISHNA CASSETTES", "SUN LABEL MANUFACTURING",
    "SAKSHI MOBILES", "SHIV MAHIMA ENTERPRISES", "SRI MADHAV PACKERS",
    "SUMMIT MOD STYLES", "SHREE PARASHNATH PACKAGING", "SHIVOM PRINTERS",
    "SHREE PATITAPABAN STORE", "SUSHMA RAJBHAR", "SS COMMERCIAL",
    "SSJ NOVELTIES AND SUBLIMATION", "SHIV SHAKTI PACKAGING INDUSTRIES",
    "SALASAR TRADING CO", "STELLAR ADEVENT", "SUMAN ENTERPRISES", "SUPER SALES",
    "TECHNOLOGIES 2000", "TELEPORTERS TRAVEL SOLUTIONS LLP", "THE FLAG COMPANY",
    "TRAVELLERS INN HOTELS INDIA PVT LTD", "TITAN WORLD", "TOTAL POLY PRINT PRIVATE LIMITED",
    "TRAVELEBRIUM PRIVATE LIMITED", "TRAVELLERS DEN GROUP", "TRUPTI FARSAN",
    "TURTLE HELMET COMPANY", "TWOBROS AND CO", "USHA ELECTRO TRADE AGENCIES INDIA PVT. LTD.",
    "UNICORN DISPLAY", "UTTAM FASHION HOUSE", "VANSHIKA ADVERTISING",
    "VENUS DATA PRODUCTS PVT. LTD.", "VERTEX PEN INDUSTRIES", "VICKY TRADING COMPANY",
    "VISUAL CREATION", "VISHWAS ELECTRICALS & GENERAL STORES", "VIVAAN ENTERPRISE",
    "VALUE BOX", "VENUS PRINTS", "WAAYS PROMOTION", "WORLD OF GADGETS",
    "WONDERCHEF HOME APPLIANCES PVT LTD", "WAYS PROMOTIONS & ADVERTISING",
    "WS TRADING", "XIAOMI TECHNOLOGY INDIA PRIVATE LIMITED", "YAASHVI ENTERPRISES",
    "ZALANI COLLECTION NX"
]

# Set for fast membership testing (case-insensitive)
COMPANY_SET = {c.strip().upper() for c in companies if isinstance(c, str)}

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
        "Order Date": "Order_Date",
        "Last Receiving No.": "Last_Receiving_No"
    })

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
    df_po = df_po[df_po["PO_No"].isin(rm_po_list)].copy()

    # ────────────────────────────────────────────────
    # STEP 1: Vendor Filter (FIRST)
    if filter_to_key_vendors:
        df_po = df_po[df_po["Vendor"].str.upper().isin(COMPANY_SET)].copy()
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