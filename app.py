import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Global Hoops Predictor 2026", page_icon="🏀", layout="centered")
st.title("🏀 Pro Basketball 2026 Matrix Prediction Engine")
st.markdown("### Google Sheets Advanced Spreadsheet Math Pipeline (v2026.10)")
st.markdown("---")

# =========================================================================
# SYSTEM MASTER ADVANCED METRICS REGISTRY - 12 COUNTRIES COMPLETE
# =========================================================================
BASKETBALL_MASTER_DB = {
    "Puerto Rico (BSN)": {
        "avg_pace": 84.2, "avg_ortg": 112.8,
        "teams": {
            "Atléticos de San Germán": {"ORTG": 114.8, "DRTG": 109.8, "PACE": 84.6},
            "Cangrejeros de Santurce": {"ORTG": 111.4, "DRTG": 112.8, "PACE": 83.8},
            "Capitanes de Arecibo": {"ORTG": 116.5, "DRTG": 113.4, "PACE": 84.9},
            "Criollos de Caguas": {"ORTG": 117.8, "DRTG": 112.1, "PACE": 85.5},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.1},
            "Indios de Mayagüez": {"ORTG": 110.9, "DRTG": 112.2, "PACE": 85.0},
            "Leones de Ponce": {"ORTG": 111.2, "DRTG": 114.3, "PACE": 83.9},
            "Mets de Guaynabo": {"ORTG": 113.8, "DRTG": 112.9, "PACE": 83.3},
            "Osos de Manatí": {"ORTG": 114.5, "DRTG": 116.4, "PACE": 85.1},
            "Piratas de Quebradillas": {"ORTG": 113.0, "DRTG": 114.8, "PACE": 85.6},
            "Santeros de Aguada": {"ORTG": 112.5, "DRTG": 113.1, "PACE": 84.4},
            "Vaqueros de Bayamón": {"ORTG": 116.9, "DRTG": 108.5, "PACE": 83.2}
        }
    },
    "Spain (Liga ACB)": {
        "avg_pace": 77.2, "avg_ortg": 112.4,
        "teams": {
            "FC Barcelona": {"ORTG": 116.8, "DRTG": 107.5, "PACE": 77.2},
            "Real Madrid": {"ORTG": 118.6, "DRTG": 106.5, "PACE": 76.3},
            "Unicaja Malaga": {"ORTG": 116.5, "DRTG": 107.2, "PACE": 77.1},
            "Valencia Basket": {"ORTG": 114.4, "DRTG": 109.8, "PACE": 78.0},
            "Saski Baskonia": {"ORTG": 112.5, "DRTG": 111.4, "PACE": 76.8},
            "UCAM Murcia": {"ORTG": 111.2, "DRTG": 110.5, "PACE": 76.4},
            "Joventut Badalona": {"ORTG": 110.8, "DRTG": 111.2, "PACE": 77.5},
            "CB Gran Canaria": {"ORTG": 111.8, "DRTG": 110.2, "PACE": 76.2},
            "Casademont Zaragoza": {"ORTG": 108.4, "DRTG": 111.9, "PACE": 77.9},
            "MoraBanc Andorra": {"ORTG": 109.0, "DRTG": 111.4, "PACE": 77.6},
            "La Laguna Tenerife": {"ORTG": 113.1, "DRTG": 109.5, "PACE": 75.8},
            "Bilbao Basket": {"ORTG": 109.5, "DRTG": 110.1, "PACE": 76.5},
            "Bàsquet Girona": {"ORTG": 107.2, "DRTG": 112.4, "PACE": 78.1},
            "Baxi Manresa": {"ORTG": 111.0, "DRTG": 111.8, "PACE": 79.2},
            "Coviran Granada": {"ORTG": 106.8, "DRTG": 113.2, "PACE": 76.9},
            "Leyma Coruña": {"ORTG": 108.1, "DRTG": 114.0, "PACE": 78.4},
            "Hiopos Lleida": {"ORTG": 107.5, "DRTG": 113.5, "PACE": 77.3},
            "Río Breogán": {"ORTG": 105.9, "DRTG": 110.8, "PACE": 75.9}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.2,
        "teams": {
            "AS Monaco": {"ORTG": 116.9, "DRTG": 104.1, "PACE": 74.5},
            "Paris Basketball": {"ORTG": 115.2, "DRTG": 107.5, "PACE": 77.1},
            "LDLC ASVEL": {"ORTG": 113.6, "DRTG": 109.4, "PACE": 75.4},
            "JL Bourg": {"ORTG": 111.4, "DRTG": 107.9, "PACE": 75.1},
            "JDA Dijon": {"ORTG": 108.8, "DRTG": 109.5, "PACE": 74.2},
            "Nanterre 92": {"ORTG": 110.5, "DRTG": 111.2, "PACE": 76.8},
            "Cholet Basket": {"ORTG": 108.1, "DRTG": 108.9, "PACE": 75.5},
            "SIG Strasbourg": {"ORTG": 109.2, "DRTG": 110.4, "PACE": 75.9},
            "Le Mans Sarthe": {"ORTG": 109.0, "DRTG": 110.1, "PACE": 76.2},
            "Élan Chalon": {"ORTG": 107.4, "DRTG": 112.5, "PACE": 76.8},
            "SLUC Nancy": {"ORTG": 109.6, "DRTG": 111.9, "PACE": 77.0},
            "Boulazac Dordogne": {"ORTG": 105.5, "DRTG": 109.2, "PACE": 74.8},
            "Limoges CSP": {"ORTG": 107.9, "DRTG": 111.4, "PACE": 75.2},
            "Gravelines-Dunkerque": {"ORTG": 106.2, "DRTG": 108.5, "PACE": 74.4},
            "Saint-Quentin": {"ORTG": 108.7, "DRTG": 107.2, "PACE": 73.9},
            "ESSM Le Portel": {"ORTG": 106.0, "DRTG": 112.1, "PACE": 75.6}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.4, "avg_ortg": 111.5,
        "teams": {
            "FC Bayern Munich": {"ORTG": 117.9, "DRTG": 106.5, "PACE": 77.9},
            "ALBA Berlin": {"ORTG": 112.1, "DRTG": 110.9, "PACE": 79.3},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 107.4, "PACE": 77.1},
            "ratiopharm ulm": {"ORTG": 112.8, "DRTG": 112.1, "PACE": 78.5},
            "Telekom Baskets Bonn": {"ORTG": 113.5, "DRTG": 111.2, "PACE": 77.8},
            "MHP Riesen Ludwigsburg": {"ORTG": 110.1, "DRTG": 109.4, "PACE": 77.5},
            "Würzburg Baskets": {"ORTG": 111.2, "DRTG": 108.1, "PACE": 76.8},
            "Rasta Vechta": {"ORTG": 110.8, "DRTG": 111.5, "PACE": 78.4},
            "Bamberg Baskets": {"ORTG": 110.4, "DRTG": 112.8, "PACE": 79.0},
            "Löwen Braunschweig": {"ORTG": 108.2, "DRTG": 109.9, "PACE": 77.4},
            "Syntainics MBC": {"ORTG": 109.5, "DRTG": 114.2, "PACE": 79.5},
            "BG Göttingen": {"ORTG": 106.4, "DRTG": 115.1, "PACE": 78.1},
            "EWE Baskets Oldenburg": {"ORTG": 111.6, "DRTG": 110.5, "PACE": 78.9},
            "SKYLINERS Frankfurt": {"ORTG": 105.1, "DRTG": 110.9, "PACE": 76.2},
            "PS Karlsruhe Lions": {"ORTG": 104.8, "DRTG": 113.4, "PACE": 77.9},
            "Towers Hamburg": {"ORTG": 109.2, "DRTG": 114.6, "PACE": 80.2},
            "MLP Academics Heidelberg": {"ORTG": 108.9, "DRTG": 113.1, "PACE": 79.1},
            "Rostock Seawolves": {"ORTG": 107.6, "DRTG": 112.4, "PACE": 78.6}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.2, "avg_ortg": 112.1,
        "teams": {
            "Olimpia Milano": {"ORTG": 116.2, "DRTG": 107.1, "PACE": 75.2},
            "Virtus Bologna": {"ORTG": 117.6, "DRTG": 108.2, "PACE": 76.3},
            "Germani Brescia": {"ORTG": 115.1, "DRTG": 108.9, "PACE": 76.5},
            "Reyer Venezia": {"ORTG": 111.2, "DRTG": 109.8, "PACE": 76.1},
            "Aquila Basket Trento": {"ORTG": 110.8, "DRTG": 110.4, "PACE": 76.9},
            "Derthona Tortona": {"ORTG": 111.5, "DRTG": 110.1, "PACE": 75.8},
            "Pallacanestro Reggiana": {"ORTG": 110.2, "DRTG": 110.6, "PACE": 75.5},
            "Openjobmetis Varese": {"ORTG": 112.6, "DRTG": 117.9, "PACE": 80.4},
            "Dinamo Sassari": {"ORTG": 109.4, "DRTG": 111.5, "PACE": 76.0},
            "Pistoia Basket": {"ORTG": 108.5, "DRTG": 111.2, "PACE": 75.4},
            "Scafati Basket": {"ORTG": 110.9, "DRTG": 114.1, "PACE": 77.8},
            "Treviso Basket": {"ORTG": 109.1, "DRTG": 113.5, "PACE": 77.2},
            "Vanoli Cremona": {"ORTG": 106.4, "DRTG": 109.5, "PACE": 74.6},
            "Napoli Basket": {"ORTG": 108.0, "DRTG": 114.6, "PACE": 77.5},
            "Trapani Shark": {"ORTG": 113.2, "DRTG": 112.0, "PACE": 78.3},
            "Pallacanestro Cantù": {"ORTG": 107.1, "DRTG": 109.0, "PACE": 75.1}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 80.1, "avg_ortg": 107.5,
        "teams": {
            "London Lions": {"ORTG": 115.5, "DRTG": 101.9, "PACE": 80.9},
            "Cheshire Phoenix": {"ORTG": 112.2, "DRTG": 107.6, "PACE": 80.6},
            "Manchester Basketball": {"ORTG": 109.5, "DRTG": 109.1, "PACE": 81.2},
            "Sheffield Sharks": {"ORTG": 104.2, "DRTG": 105.1, "PACE": 78.9},
            "Leicester Riders": {"ORTG": 108.9, "DRTG": 107.2, "PACE": 79.7},
            "Bristol Flyers": {"ORTG": 106.5, "DRTG": 107.8, "PACE": 79.1},
            "Surrey 89ers": {"ORTG": 107.1, "DRTG": 110.2, "PACE": 80.5},
            "Newcastle Eagles": {"ORTG": 108.6, "DRTG": 108.8, "PACE": 80.4},
            "Caledonia Gladiators": {"ORTG": 106.8, "DRTG": 108.0, "PACE": 80.2}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 78.3, "avg_ortg": 107.1,
        "teams": {
            "SL Benfica": {"ORTG": 113.9, "DRTG": 103.5, "PACE": 77.7},
            "FC Porto": {"ORTG": 112.2, "DRTG": 105.1, "PACE": 78.5},
            "Sporting CP": {"ORTG": 111.2, "DRTG": 106.5, "PACE": 78.9},
            "Ovarense": {"ORTG": 105.8, "DRTG": 108.2, "PACE": 77.8},
            "UD Oliveirense": {"ORTG": 106.4, "DRTG": 109.1, "PACE": 78.2},
            "Vitória SC": {"ORTG": 104.9, "DRTG": 110.4, "PACE": 79.0},
            "AD Galomar": {"ORTG": 102.1, "DRTG": 109.8, "PACE": 77.1},
            "Esgueira Aveiro": {"ORTG": 103.5, "DRTG": 111.2, "PACE": 78.4},
            "Póvoa TSC": {"ORTG": 104.2, "DRTG": 109.5, "PACE": 77.6},
            "CA Queluz": {"ORTG": 101.8, "DRTG": 112.5, "PACE": 79.2},
            "Imortal Albufeira": {"ORTG": 103.0, "DRTG": 111.9, "PACE": 78.0},
            "CD Povoa": {"ORTG": 103.9, "DRTG": 108.9, "PACE": 77.3}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.6, "avg_ortg": 113.5,
        "teams": {
            "Anadolu Efes": {"ORTG": 119.2, "DRTG": 107.5, "PACE": 77.1},
            "Fenerbahce Beko": {"ORTG": 118.9, "DRTG": 106.8, "PACE": 76.8},
            "Pınar Karşıyaka": {"ORTG": 114.5, "DRTG": 111.2, "PACE": 78.2},
            "Besiktas Emlakjet": {"ORTG": 112.1, "DRTG": 109.8, "PACE": 77.9},
            "Galatasaray Ekmas": {"ORTG": 113.5, "DRTG": 113.1, "PACE": 77.5},
            "Tofaş Bursa": {"ORTG": 111.8, "DRTG": 112.4, "PACE": 78.0},
            "Türk Telekom": {"ORTG": 109.4, "DRTG": 108.9, "PACE": 76.2},
            "Darüşşafaka Lassa": {"ORTG": 110.1, "DRTG": 114.8, "PACE": 78.6},
            "Bahçeşehir Koleji": {"ORTG": 113.9, "DRTG": 109.2, "PACE": 76.5},
            "Bursaspor Info Yatırım": {"ORTG": 110.5, "DRTG": 112.9, "PACE": 77.8},
            "Manisa BBSK": {"ORTG": 109.2, "DRTG": 113.4, "PACE": 78.3},
            "Aliağa Petkimspor": {"ORTG": 111.0, "DRTG": 110.6, "PACE": 76.9},
            "Merkezefendi Denizli": {"ORTG": 108.4, "DRTG": 114.0, "PACE": 78.1},
            "Büyükçekmece Basket": {"ORTG": 109.7, "DRTG": 112.5, "PACE": 77.2},
            "Yalovaspor BK": {"ORTG": 106.5, "DRTG": 115.2, "PACE": 78.5},
            "Mersin MSK": {"ORTG": 108.9, "DRTG": 111.8, "PACE": 76.7}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.8, "avg_ortg": 110.5,
        "teams": {
            "Canterbury Rams": {"ORTG": 115.1, "DRTG": 106.4, "PACE": 84.4},
            "Auckland Tuatara": {"ORTG": 112.8, "DRTG": 108.9, "PACE": 85.2},
            "Wellington Saints": {"ORTG": 115.5, "DRTG": 111.5, "PACE": 85.8},
            "Taranaki Airs": {"ORTG": 114.2, "DRTG": 111.8, "PACE": 86.5},
            "Franklin Bulls": {"ORTG": 109.8, "DRTG": 109.2, "PACE": 83.9},
            "Otago Nuggets": {"ORTG": 107.5, "DRTG": 112.1, "PACE": 84.1},
            "Nelson Giants": {"ORTG": 108.9, "DRTG": 110.4, "PACE": 83.6},
            "Hawke's Bay Hawks": {"ORTG": 110.2, "DRTG": 114.5, "PACE": 86.1},
            "Whai Basketball": {"ORTG": 105.4, "DRTG": 111.2, "PACE": 83.2},
            "Southland Sharks": {"ORTG": 106.1, "DRTG": 115.9, "PACE": 85.4},
            "Manawatu Jets": {"ORTG": 104.8, "DRTG": 117.2, "PACE": 86.9}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.8, "avg_ortg": 110.8,
        "teams": {
            "Panathinaikos AKTOR": {"ORTG": 120.5, "DRTG": 103.2, "PACE": 74.5},
            "Olympiacos Piraeus": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 74.1},
            "Peristeri": {"ORTG": 111.4, "DRTG": 110.5, "PACE": 75.0},
            "Promitheas Patras": {"ORTG": 112.8, "DRTG": 112.1, "PACE": 75.9},
            "AEK Athens": {"ORTG": 110.1, "DRTG": 112.4, "PACE": 75.6},
            "Aris Salonika": {"ORTG": 106.4, "DRTG": 105.8, "PACE": 74.3},
            "PAOK Salonika": {"ORTG": 107.9, "DRTG": 111.2, "PACE": 74.8},
            "Kolossos Rodou": {"ORTG": 108.2, "DRTG": 113.1, "PACE": 75.1},
            "Maroussi BC": {"ORTG": 109.0, "DRTG": 112.5, "PACE": 76.0},
            "Karditsa AS": {"ORTG": 106.1, "DRTG": 111.8, "PACE": 74.5},
            "Iraklis Salonika": {"ORTG": 105.5, "DRTG": 110.9, "PACE": 74.9},
            "BC Mykonos": {"ORTG": 106.9, "DRTG": 112.0, "PACE": 75.3}
        }
    },
    "China (CBA)": {
        "avg_pace": 88.5, "avg_ortg": 111.9,
        "teams": {
            "Liaoning Flying Leopards": {"ORTG": 115.1, "DRTG": 104.2, "PACE": 87.5},
            "Xinjiang Flying Tigers": {"ORTG": 112.8, "DRTG": 105.5, "PACE": 88.1},
            "Zhejiang Golden Bulls": {"ORTG": 117.1, "DRTG": 107.9, "PACE": 88.9},
            "Guangdong Southern Tigers": {"ORTG": 116.5, "DRTG": 109.1, "PACE": 91.1},
            "Zhejiang Guangsha Lions": {"ORTG": 114.2, "DRTG": 106.8, "PACE": 86.9},
            "Shanghai Sharks": {"ORTG": 111.5, "DRTG": 112.4, "PACE": 89.4},
            "Beijing Ducks": {"ORTG": 109.8, "DRTG": 106.1, "PACE": 86.2},
            "Guangzhou Loong Lions": {"ORTG": 110.4, "DRTG": 111.5, "PACE": 88.0},
            "Shenzhen Leopards": {"ORTG": 112.1, "DRTG": 111.9, "PACE": 87.8},
            "Qingdao Eagles": {"ORTG": 109.2, "DRTG": 108.5, "PACE": 88.3},
            "Shanxi Loongs": {"ORTG": 113.6, "DRTG": 115.2, "PACE": 90.5},
            "Nanjing Monkey Kings": {"ORTG": 108.5, "DRTG": 111.8, "PACE": 89.0}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.8, "avg_ortg": 106.1,
        "teams": {
            "Swans Gmunden": {"ORTG": 110.1, "DRTG": 102.1, "PACE": 76.4},
            "Flyers Wels": {"ORTG": 107.4, "DRTG": 104.8, "PACE": 77.1},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 76.5},
            "UBSC Graz": {"ORTG": 105.4, "DRTG": 106.4, "PACE": 77.4},
            "Oberwart Gunners": {"ORTG": 103.8, "DRTG": 104.5, "PACE": 76.0},
            "SKN St. Pölten": {"ORTG": 102.5, "DRTG": 108.1, "PACE": 77.2},
            "Arkadia Traiskirchen Lions": {"ORTG": 105.0, "DRTG": 103.9, "PACE": 75.8},
            "Bulls Kapfenberg": {"ORTG": 104.2, "DRTG": 107.5, "PACE": 76.9},
            "Vienna Timberwolves": {"ORTG": 100.8, "DRTG": 111.4, "PACE": 77.5},
            "BC Vienna": {"ORTG": 106.8, "DRTG": 109.0, "PACE": 78.1}
        }
    }
}

# =========================================================================
# CONTROL SIDEBAR: LIVE CONFIGURATION & WEEKLY ADVANCED OVERRIDES
# =========================================================================
selected_db = st.sidebar.selectbox("🏀 Select Active Basketball League", list(BASKETBALL_MASTER_DB.keys()))
cfg = BASKETBALL_MASTER_DB[selected_db]

st.sidebar.markdown("---")
st.sidebar.markdown("### 🗓️ Weekly Advanced Stats Override Panel")
st.sidebar.caption("Tweak baseline league mechanics dynamically based on live RealGM data updates.")

weekly_pace = st.sidebar.number_input(
    "Adjust League Average Pace Base", 
    min_value=60.0, max_value=110.0, value=float(cfg["avg_pace"]), step=0.1
)
weekly_ortg = st.sidebar.number_input(
    "Adjust League Average Offense Rating", 
    min_value=90.0, max_value=130.0, value=float(cfg["avg_ortg"]), step=0.1
)

st.sidebar.caption("Data Registry Source: RealGM.com Active 2026 Profiles")

# Matchup Configuration Panel
st.subheader(f"🏟️ Setup Matchup Projections: {selected_db}")
col_h, col_a = st.columns(2)
with col_h:
    home = st.selectbox("🏡 Select Home Team", sorted(cfg["teams"].keys()), index=0)
with col_a:
    away = st.selectbox("✈️ Select Away Team", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

# Weekly Dynamic Overrides Panel for Specific Selected Teams
with st.expander("📝 Edit Individual Selected Team Core Stats (Optional Weekly Tuning)"):
    col_t1, col_t2 = col_h, col_a # match alignment blocks
    with col_t1:
        st.markdown(f"**🏡 {home} overrides**")
        h_pace = st.number_input("Team Pace", value=float(cfg["teams"][home]["PACE"]), key="hp", step=0.1)
        h_ortg = st.number_input("Offensive Rating", value=float(cfg["teams"][home]["ORTG"]), key="ho", step=0.1)
        h_drtg = st.number_input("Defensive Rating", value=float(cfg["teams"][home]["DRTG"]), key="hd", step=0.1)
    with col_t2:
        st.markdown(f"**✈️ {away} overrides**")
        a_pace = st.number_input("Team Pace", value=float(cfg["teams"][away]["PACE"]), key="ap", step=0.1)
        a_ortg = st.number_input("Offensive Rating", value=float(cfg["teams"][away]["ORTG"]), key="ao", step=0.1)
        a_drtg = st.number_input("Defensive Rating", value=float(cfg["teams"][away]["DRTG"]), key="ad", step=0.1)

st.markdown(" ")
initiate_analysis = st.button("🚀 Initiate Advanced Matchup Simulation", type="primary", use_container_width=True)
st.markdown("---")

if initiate_analysis:
    if home == away:
        st.error("⚠️ System Mapping Error: Select two unique teams to initiate analysis.")
    else:
        # 1. Advanced Sheet Metric Calculus: Game Pace
        predicted_pace = (h_pace + a_pace) - weekly_pace
        
        # 2. Predicted Home Score Formula (Includes Strict Home Court Advantage Factor of +3.5)
        projected_home_ft = ((h_ortg + a_drtg) - weekly_ortg) * (predicted_pace / 100) + 3.5
        
        # 3. Predicted Away Score Formula
        projected_away_ft = ((a_ortg + h_drtg) - weekly_ortg) * (predicted_pace / 100)
        
        # 4. Computed Spread Vector line
        model_spread = projected_away_ft - projected_home_ft
        
        # Assign UI Output Flags
        winner_team = home if projected_home_ft > projected_away_ft else away
        winner_icon = "🏡" if winner_team == home else "✈️"

        # Display Data Targets
        st.markdown("## 🏆 Model Consensus Selections")
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="Outright Winner", value=f"{winner_icon} {winner_team}")
        with m2:
            st.metric(label="Calculated Model Point Spread Line", value=f"{winner_team} {abs(model_spread):-.1f}")

        st.markdown(" ")
        st.subheader("📊 Performance Projections Summary Matrix Table")
        
        matrix_df = pd.DataFrame({
            "Team Segment": [f"🏡 {home} (Home Team)", f"✈️ {away} (Away Team)"],
            "Final Score Projections": [f"{projected_home_ft:.1f}", f"{projected_away_ft:.1f}"],
            "Model Point Spread Line": [f"{-model_spread:+.1f}", f"{model_spread:+.1f}"]
        })
        
        st.table(matrix_df)

        # Audit Registry Expander Panel
        with st.expander("🔍 View 2026 Cell Variables & Sheet Calculation Logs"):
            st.markdown(f"#### Active League Infrastructure Baseline")
            st.text(f"Adjusted League Average Pace Base: {weekly_pace} possessions")
            st.text(f"Adjusted League Average Offense Rating Base: {weekly_ortg}")
            st.text(f"Applied Home Court Advantage Variable Constant: +3.5 points")
            st.markdown("---")
            st.markdown("#### Formula Step Calculation Outputs")
            st.markdown(f"* Predicted Dynamic Game Pace: `{predicted_pace:.2f}` possessions")
            st.markdown(f"* Raw Sheet Spread Target Value: `{model_spread:+.1f}` points")
else:
    st.info("💡 System Ready. Configure teams and click the button above to execute calculations.")
