# ==========================================
# CONFIGURATION VARIABLES
# ==========================================

HIGH_COMPLIANCE_STATES = {
    "AL", "AZ", "AR", "CA", "CT", "GA", "IL", "ID", "WY", "LA",
    "MD", "DC", "VA", "MI", "NY", "OH", "PA", "TX"
}

NON_DISCLOSURE_STATES = {
    "AK", "ID", "KS", "MT", "NM", "ND", "LA", "MS", "MO", "TX",
    "UT", "WY"
}

us_states = {
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "DC"
}

# Maps state codes to full names used in links_data
STATE_CODE_TO_NAME = {
    "AL": "Alabama", "AK": "Alaska", "AZ": "Arizona", "AR": "Arkansas",
    "CA": "California", "CT": "Connecticut", "DC": "DC", "FL": "Florida",
    "GA": "Georgia", "ID": "Idaho", "IL": "Illinois", "LA": "Louisiana",
    "MD": "Maryland", "MI": "Michigan", "NY": "New York", "OH": "Ohio",
    "PA": "Pennsylvania", "TX": "Texas", "VA": "Virginia", "WY": "Wyoming"
}

NON_DISCLOSURE_LINK = "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Non-Disclosure-States_sunI0gf8?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lubO-OFK"
FALLBACK_COMPLIANCE_LINK = "https://coda.io/d/Compliance-Pod_d_gKRbO285-/State-Compliance_suSOtqcU?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lug_RLEv"

links_data = {
    "Alabama": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Alabama_suaojIG0?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu_-jA6U", "brokerage": "All"},
    "Arizona": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Arizona_sugeuyv9?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luYFhkpq", "brokerage": "Coldwell Banker"},
    "Arkansas": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Arkansas_sujMHmpf?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luYRjkOk", "brokerage": "All"},
    "California": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/California_suQO6kOP?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu66fBv6", "brokerage": "All"},
    "Connecticut": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Connecticut_sutmv2Lr?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luUrFEby", "brokerage": "All"},
    "Florida": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Florida-Pending-Under-Construction_suqMn8p4?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Georgia": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Georgia_suywVlKL?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luMHhYrD", "brokerage": "All"},
    "Illinois": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Idaho-Wyoming-Illinois_suRBJgaV?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Illinois (Compass)": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Idaho-Wyoming-Illinois_suRBJgaV?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "Compass"},
    "Idaho": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Idaho-Wyoming-Illinois_suRBJgaV?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Wyoming": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Idaho-Wyoming-Illinois_suRBJgaV?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Louisiana": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Louisiana_suo1_XNE?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Maryland": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Maryland-DC-Virginia_suSohLAO?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "Compass"},
    "DC": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Maryland-DC-Virginia_suSohLAO?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "Compass"},
    "Virginia": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Maryland-DC-Virginia_suSohLAO?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "Compass"},
    "Michigan": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Michigan_su66hCRX?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "New York": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/New-York_su7jkkMk?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Ohio": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Ohio_suibv6F-?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Pennsylvania": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Pennsylvania_sucYZ2U-?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Texas": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Texas_su9Wm6Wq?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
    "Alaska": {"url": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Alaska_suXBSoJh?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ", "brokerage": "All"},
}

mls_boards = {
    "AAAR - Athens Area Association of REALTORS, Inc. / Classic MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/AAAR-Athens-Area-Association-of-REALTORS-Inc-Classic-MLS_sudFJFuD",
    "AARMLS - Ann Arbor Area Board of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/AARMLS-Ann-Arbor-Area-Board-of-REALTORS_su12uvr4",
    "BAREIS - Bay Area Real Estate Information Service": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/BAREIS-Bay-Area-Real-Estate-Information-Service_suxEaa7H",
    "BCRA - Bay County REALTORS® Association": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/BCRA-Bay-County-REALTORS-Association_susJ7qT5",
    "BEAR - Bay East Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/BEAR-Bay-East-Association-of-REALTORS_suBoivvf",
    "BCSR - Bryan-College Station Regional MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/BCSR-Bryan-College-Station-Regional-MLS_sukjm_lk",
    "Bright MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Bright-MLS_suVP1qzD",
    "Canopy MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Canopy-MLS_sukNsdra",
    "CBR - Columbus Board of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CBR-Columbus-Board-of-REALTORS_suWQ4sNK",
    "CCAR - Coastal Carolinas Association of REALTORS MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CCAR-Coastal-Carolinas-Association-of-REALTORS-MLS_sugQRzuL",
    "CCAR - Corpus Christi Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CCAR-Corpus-Christi-Association-of-REALTORS_sumCVcZT",
    "CLAW - Combined L.A./Westside MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CLAW-Combined-L-A-Westside-MLS_sulw-3ZA",
    "CREA - Canadian Real Estate Association": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CREA-Canadian-Real-Estate-Association_suXfSGQ1",
    "CREN - Colorado Real Estate Network": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CREN-Colorado-Real-Estate-Network_suzreQP0",
    "CTXMLS - Central Texas MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CTXMLS-Central-Texas-MLS_suWXP5HG",
    "CVRMLS - Central Virginia Regional MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CVRMLS-Central-Virginia-Regional-MLS_su2Y9PFR",
    "KAAR - East Tennessee Realtors® (Knoxville Area Association of REALTORS)": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/KAAR-East-Tennessee-Realtors-Knoxville-Area-Association-of-REALT_suYcqkpp",
    "FMLS - First Georgia MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/FMLS-First-Georgia-MLS_su7qSU44",
    "GAAR - Greater Augusta Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GAAR-Greater-Augusta-Association-of-REALTORS_su-Uylwa",
    "GCBOR - Central Hill Country Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GCBOR-Central-Hill-Country-Board-of-REALTORS_suTNwN35",
    "Georgia MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Georgia-MLS_suEqijNb",
    "GIAR - Golden Isles Association of Realtors": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GIAR-Golden-Isles-Association-of-Realtors_suL-jKYZ",
    "GMAR / MetroMLS/ WIREX - Greater Milwaukee Association of Realtors": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GMAR-MetroMLS-WIREX-Greater-Milwaukee-Association-of-Realtors_su5hDk2n",
    "GLAR - Greater Lansing Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GLAR-Greater-Lansing-Association-of-REALTORS_suDsXXIe",
    "GARMLS - Greenwich Association of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/GARMLS-Greenwich-Association-of-REALTORS_su5oDMkd",
    "Greater Scranton MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Greater-Scranton-MLS_su8US_Iw",
    "HAR - Houston Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/HAR-Houston-Association-of-REALTORS_sut2ZZih",
    "Heartland MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Heartland-MLS_sudJ_u9H",
    "Highland Lakes Association of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Highland-Lakes-Association-of-REALTORS_sut5U3Wu",
    "Lake Superior Area REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Lake-Superior-Area-REALTORS_suDV-K_q",
    "Lawrence Board of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Lawrence-Board-of-REALTORS_suhCpm-C",
    "SWMRIC - Michigan Regional Information Center, LLC": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SWMRIC-Michigan-Regional-Information-Center-LLC_suMm-sQZ",
    "MARIS - Mid America Regional Information Systems": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MARIS-Mid-America-Regional-Information-Systems_suL4pbrO",
    "MBOR - Midland Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MBOR-Midland-Board-of-REALTORS_suDj-5Jn",
    "MIBOR - Metropolitan Indianapolis Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MIBOR-Metropolitan-Indianapolis-Board-of-REALTORS_subWh_6M",
    "MiRealSource": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MiRealSource_suOE2zvx",
    "MRED - Midwest Real Estate Data": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MRED-Midwest-Real-Estate-Data_suNzufhG",
    "MREIS - Maine Listings Real Estate Information System": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MREIS-Maine-Listings-Real-Estate-Information-System_su-AHa_i",
    "MLSListings": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MLSListings_suhVjZSk",
    "MLSOK - Oklahoma City Metropolitan Association Of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/MLSOK-Oklahoma-City-Metropolitan-Association-Of-REALTORS_suuKO1Ja",
    "NCBoR - Mountain Home MLS / North Central Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NCBoR-Mountain-Home-MLS-North-Central-Board-of-REALTORS_suZUd6PM",
    "NEIRBR - Northeast Iowa Regional Board of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NEIRBR-Northeast-Iowa-Regional",
    "NEGBOR - Northeast Georgia Board of REALTORS, Inc.": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NEGBOR-Northeast-Georgia-Board-of-REALTORS-Inc_su0Vy-dp",
    "NJMLS - MLS - New Jersey MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NJMLS-MLS-New-Jersey-MLS_suSINi2l",
    "NGLRMLS - Northern Great Lakes MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NGLRMLS-Northern-Great-Lakes-MLS_suGxMk7n",
    "NoCoast MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NoCoast-MLS_su0tSt6y",
    "Northstar MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Northstar-MLS_suQfwcJu",
    "Northwest Indiana REALTOR Association": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Northwest-Indiana-REALTOR-Association_suvdTMZv",
    "NTREIS - North Texas Real Estate Information Systems": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NTREIS-North-Texas-Real-Estate-Information-Systems_suoIHh5L",
    "NWMLS - North West MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/NWMLS-North-West-MLS_suK73GGO",
    "OneKey® MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/OneKey-MLS_suBp5eXW",
    "elevateMLS (formerly known as Pikes Peak MLS)": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/elevateMLS-formerly-known-as-Pikes-Peak-MLS_sun4bQ5v",
    "PAAR - Prescott Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/PAAR-Prescott-Association-of-REALTORS_su5O04ua",
    "PrimeMLS (NNEREN)- New England Real Estate Network": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/PrimeMLS-NNEREN-New-England-Real-Estate-Network_suMtfTri",
    "RANW - REALTOR® Association of Northeast Wisconsin": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/RANW-REALTOR-Association-of-Northeast-Wisconsin_suL1upMi",
    "REALCOMP - c II LTD.": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/REALCOMP-c-II-LTD_suKa_Urx",
    "Realtracs": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Realtracs_suPRUGtr",
    "REBNY - Real Estate Board of New York": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/REBNY-Real-Estate-Board-of-New-York_suebDORe",
    "REcolorado": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/REcolorado_suHDKx1B",
    "RMLS Alliance": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/RMLS-Alliance_su_aqi5u",
    "RMLS - Portland Regional MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/RMLS-Portland-Regional-MLS_suV6hXzX",
    "SCK MLS - South Central Kansas MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SCK-MLS-South-Central-Kansas-MLS_suKcXQyM",
    "Stellar MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Stellar-MLS_suMZp6nJ",
    "SWMLS - Southwest MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SWMLS-Southwest-MLS_suQkzVhN",
    "WVMLS - Willamette Valley MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/WVMLS-Willamette-Valley-MLS_suFvHq3M",
    "WWBR - Water Wonderland Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/WWBR-Water-Wonderland-Board-of-REALTORS_suLfLI1p",
    "CO - Grand County Board of REALTORS (GCBOR)": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/CO-Grand-County-Board-of-REALTORS-GCBOR_su0UR25F",
    "SABOR - Savannah Multi-List Corporation": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SABOR-Savannah-Multi-List-Corporation_subI83nI",
    "SABOR - San Antonio Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SABOR-San-Antonio-Board-of-REALTORS_suFxNm-6",
    "SDMLS - San Diego": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/SDMLS-San-Diego_su-tRT3B",
    "Southern Missouri Regional - SOMO MLS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Southern-Missouri-Regional-SOMO-MLS_suSr4nY6",
    "Spartanburg Association of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Spartanburg-Association-of-REALTORS_suqjqctP",
    "Spokane Association of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Spokane-Association-of-REALTORS_suCL-6Zr",
    "Sunflower Association of REALTORS®": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Sunflower-Association-of-REALTORS_su0Z3nNI",
    "TAR - Tucson Association of Realtors/MLS of Southern Arizona": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/TAR-Tucson-Association-of-Realtors-MLS-of-Southern-Arizona_suK7Ekoi",
    "TIFT - Tiftarea Board of REALTORS": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/TIFT-Tiftarea-Board-of-REALTORS_suwdhtpw",
    "Unlock MLS - ACTRIS Austin/Central Texas Realty Information Service": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Unlock-MLS-ACTRIS-Austin-Central-Texas-Realty-Information-Servic_suLbhF50",
    "VBR - Real Estate Board of Greater Vancouver": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/VBR-Real-Estate-Board-of-Greater-Vancouver_suETQbsL",
    "WVMLS - Willamette Valley Multiple Listing Service": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/WVMLS-Willamette-Valley-Multiple-Listing-Service_su6NytWY",
}

partnerships_brokerage = {
    "@properties": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/properties_suhdrlI5?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luunMMwY",
    "The Agency": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/The-Agency_suQi8EYd?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luBtgu3l",
    "Avenue 8": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Avenue-8_suwzRwx3?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lum9mx91",
    "Compass": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Compass-Compliance_suWRUr9I?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luVsyzdu",
    "Berkshire Hathaway HomeServices": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Berkshire-Hathaway-HomeServices_suesI3AC?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lupDwmCx",
    "Coldwell Banker": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Coldwell-Banker-Compliance_suRSMJ2d?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lurJq-YV",
    "Corcoran": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Corcoran-Compliance_suFyZs_e?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu5B_vEc",
    "Christie's International Real Estate": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Christies-International-RE-Compliance_supXga1y?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luVJr0P4",
    "Engel & Völkers": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Engel-Volkers_sujYuHU7?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luSTGTST",
    "eXp Realty": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/eXp-Realty-Compliance_suluOtM5?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luVTYkm5",
    "Harcourts North America": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Harcourts-North-America_suYI723Y?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luOG6sGw",
    "Howard Hanna Real Estate": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Howard-Hanna_sueM0Dh2?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luiFyRX7",
    "RE/MAX": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/REMAX-Compliance_suW51cW2?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luO_kg6_",
    "Side": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Side-Compliance_sugaGL2M?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luHJGYfh",
    "Sotheby's International Realty": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Sotheby-s-International-Realty-Compliance_suqYXHyr?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lupPhsiX",
    "William Raveis Real Estate": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/William-Raveis-Real-Estate-Compliance_suuThCkA?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luJsSRM0",
    "Real": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Real_su0aEAV4?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lueW4NL2"
}

non_partnerships_brokerage = {
    "Century 21": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Century-21_suhJ1SNm?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu5RuPFa",
    "Douglas Elliman": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Douglas-Elliman-Compliance_suadq334?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lum1-XsY",
    "Keller Williams Realty": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Keller-Williams-Realty-Compliance_supIou_v?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luGqkFUT",
    "Madison Allied LLC": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Madison-Allied-LLC-Pending_suZOusbp?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu2VVMhT",
    "Michael Saunders & Company": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Michael-Saunders-Company-Compliance_su1NhrUY?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luP3hpKe",
    "Realty Austin": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Realty-Austin_suap8nIb?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luJ-UT98",
    "Ryan Serhant": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Ryan-Serhant_suae1hDy?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu1Ck3n7",
    "Windermere": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Windermere-Compliance_sudrw8zy?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luMCBNpd",
    "Realty One Group": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Realty-One-Group_suUtEr-8?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_lu2_G1Y6",
    "Vanguard Properties": "https://coda.io/d/Compliance-Pod_d_gKRbO285-/Vanguard-Properties_suzCz2QJ?loginId=amFuaWVsbHV5QGx1eHVyeXByZXNlbmNlLmNvbQ#_luXG_1eC"
}

# ==========================================
# MAIN LOGIC
# ==========================================

def get_state_compliance_info(state_code: str, brokerage: str = "") -> dict:
    state = state_code.strip().upper()
    state_name = STATE_CODE_TO_NAME.get(state)
    brokerage_clean = brokerage.strip().lower()

    is_non_disclosure = state in NON_DISCLOSURE_STATES

    # Non-disclosure states always get the non-disclosure link first
    if is_non_disclosure:
        state_entry = links_data.get(state_name, {})
        return {
            "high compliance": state in HIGH_COMPLIANCE_STATES,
            "non_disclosure": True,
            "compliance_link": state_entry.get("url", FALLBACK_COMPLIANCE_LINK) if state in HIGH_COMPLIANCE_STATES else None,
            "non_disclosure_link": NON_DISCLOSURE_LINK,
            "required_brokerage": state_entry.get("brokerage") if state_entry.get("brokerage") != "All" else None
        }

    # Try to find brokerage-specific entry first (e.g. "Illinois (Compass)")
    if state_name and brokerage_clean:
        for key, val in links_data.items():
            if state_name.lower() in key.lower() and val["brokerage"].lower() in brokerage_clean:
                return {
                    "high compliance": state in HIGH_COMPLIANCE_STATES,
                    "non_disclosure": False,
                    "compliance_link": val["url"],
                    "non_disclosure_link": None,
                    "required_brokerage": val["brokerage"]
                }

    # Fall back to generic state entry
    if state_name and state_name in links_data:
        entry = links_data[state_name]
        return {
            "high compliance": state in HIGH_COMPLIANCE_STATES,
            "non_disclosure": False,
            "compliance_link": entry["url"],
            "non_disclosure_link": None,
            "required_brokerage": entry["brokerage"] if entry["brokerage"] != "All" else None
        }

    # No data for this state
    return {
        "high compliance": state in HIGH_COMPLIANCE_STATES,
        "non_disclosure": False,
        "compliance_link": FALLBACK_COMPLIANCE_LINK,
        "non_disclosure_link": None,
        "required_brokerage": None
    }

def get_brokerage_compliance_info(brokerage: str) -> dict:
    """Returns compliance link and partnership status for a given brokerage."""
    if not brokerage:
        return None
    if brokerage in partnerships_brokerage:
        return {"url": partnerships_brokerage[brokerage], "partnership": True}
    if brokerage in non_partnerships_brokerage:
        return {"url": non_partnerships_brokerage[brokerage], "partnership": False}
    return {"url": None, "partnership": None}