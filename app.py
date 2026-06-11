import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="Pro Hoops Predictor 2026", page_icon="🏀", layout="centered")
st.title("🏀 Pro Hoops 2026 Matrix Prediction Engine")
st.markdown("### Google Sheets Advanced Spreadsheet Math Pipeline (v2026.5)")
st.markdown("---")

# =========================================================================
# HARDCODED ADVANCED REALGM CORE DATASET BASELINE (2025-2026)
# =========================================================================
BASKETBALL_MASTER_DB = {
    "Spain (Liga ACB)": {
        "avg_pace": 77.2, "avg_ortg": 112.4,
        "teams": {
            "FC Barcelona": {"ORTG": 116.8, "DRTG": 107.5, "PACE": 77.2},
            "Real Madrid": {"ORTG": 118.6, "DRTG": 106.5, "PACE": 76.3},
            "Unicaja Malaga": {"ORTG": 116.5, "DRTG": 107.2, "PACE": 77.1},
            "Valencia Basket": {"ORTG": 114.4, "DRTG": 109.8, "PACE": 78.0},
            "Saski Baskonia": {"ORTG": 112.5, "DRTG": 111.4, "PACE": 76.8},
            "UCAM Murcia": {"ORTG": 111.2, "DRTG": 110.5, "PACE": 76.4},
            "Club Joventut Badalona": {"ORTG": 110.8, "DRTG": 111.2, "PACE": 77.5},
            "CB Gran Canaria": {"ORTG": 111.8, "DRTG": 110.2, "PACE": 76.2},
            "Casademont Zaragoza": {"ORTG": 108.4, "DRTG": 111.9, "PACE": 77.9},
            "MoraBanc Andorra": {"ORTG": 109.0, "DRTG": 111.4, "PACE": 77.6}
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
            "SIG Strasbourg": {"ORTG": 109.2, "DRTG": 110.4, "PACE": 75.9}
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
            "Rasta Vechta": {"ORTG": 110.8, "DRTG": 111.5, "PACE": 78.4}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.2, "avg_ortg": 112.1,
        "teams": {
            "Olimpia Milano (EA7)": {"ORTG": 116.2, "DRTG": 107.1, "PACE": 75.2},
            "Virtus Segafredo Bologna": {"ORTG": 117.6, "DRTG": 108.2, "PACE": 76.3},
            "Germani Brescia": {"ORTG": 115.1, "DRTG": 108.9, "PACE": 76.5},
            "Umana Reyer Venezia": {"ORTG": 111.2, "DRTG": 109.8, "PACE": 76.1},
            "Aquila Basket Trento": {"ORTG": 110.8, "DRTG": 110.4, "PACE": 76.9},
            "Derthona Basket Tortona": {"ORTG": 111.5, "DRTG": 110.1, "PACE": 75.8},
            "Pallacanestro Reggiana": {"ORTG": 110.2, "DRTG": 110.6, "PACE": 75.5},
            "Openjobmetis Varese": {"ORTG": 112.6, "DRTG": 117.9, "PACE": 80.4}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 80.1, "avg_ortg": 107.5,
        "teams": {
            "Cheshire Phoenix": {"ORTG": 112.2, "DRTG": 107.6, "PACE": 80.6},
            "Leicester Riders": {"ORTG": 108.9, "DRTG": 107.2, "PACE": 79.7},
            "London Lions": {"ORTG": 115.5, "DRTG": 101.9, "PACE": 80.9},
            "Newcastle Eagles": {"ORTG": 108.6, "DRTG": 108.8, "PACE": 80.4},
            "Sheffield Sharks": {"ORTG": 104.2, "DRTG": 105.1, "PACE": 78.9},
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
            "Vitória SC": {"ORTG": 104.9, "DRTG": 110.4, "PACE": 79.0}
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
            "Darüşşafaka Lassa": {"ORTG": 110.1, "DRTG": 114.8, "PACE": 78.6}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 84.2, "avg_ortg": 112.8,
        "teams": {
            "Vaqueros de Bayamón": {"ORTG": 116.9, "DRTG": 108.5, "PACE": 83.2},
            "Capitanes de Arecibo": {"ORTG": 116.5, "DRTG": 113.4, "PACE": 84.9},
            "Criollos de Caguas": {"ORTG": 117.8, "DRTG": 112.1, "PACE": 85.5},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.1},
            "Atléticos de San Germán": {"ORTG": 114.8, "DRTG": 109.8, "PACE": 84.6},
            "Mets de Guaynabo": {"ORTG": 113.8, "DRTG": 112.9, "PACE": 83.3},
            "Osos de Manatí": {"ORTG": 114.5, "DRTG": 116.4, "PACE": 85.1},
            "Cangrejeros de Santurce": {"ORTG": 111.4, "DRTG": 112.8, "PACE": 83.8}
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
            "Otago Nuggets": {"ORTG": 107.5, "DRTG": 112.1, "PACE": 84.1}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.8, "avg_ortg": 110.8,
        "teams": {
            "Panathinaikos": {"ORTG": 120.5, "DRTG": 103.2, "PACE": 74.5},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 74.1},
            "Peristeri": {"ORTG": 111.4, "DRTG": 110.5, "PACE": 75.0},
            "Promitheas Patras": {"ORTG": 112.8, "DRTG": 112.1, "PACE": 75.9},
            "AEK Athens": {"ORTG": 110.1, "DRTG": 112.4, "PACE": 75.6},
            "Aris Salonika": {"ORTG": 106.4, "DRTG": 105.8, "PACE": 74.3},
            "PAOK Salonika": {"ORTG": 107.9, "DRTG": 111.2, "PACE": 74.8}
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
            "Shanghai Sharks": {"ORTG": 111.5, "DRTG": 112.4, "PACE": 89.4}
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
            "SKN St. Pölten": {"ORTG": 102.5, "DRTG": 108.1, "PACE": 77.2}
        }
    }
}

# =========================================================================
# UI REGION: DESIGN INTERFACE & WEEKLY STATS OVERRIDES
# =========================================================================
selected_db = st.sidebar.selectbox("🏀 Select Active Basketball League", list(BASKETBALL_MASTER_DB.keys()))
cfg = BASKETBALL_MASTER_DB[selected_db]

# Dynamic Weekly Configuration Updates Panel
st.sidebar.markdown("---")
st.sidebar.markdown("### 🗓️ Weekly Advanced Stats Override Panel")
st.sidebar.caption("Adjust current weekly league configurations instantly without editing raw arrays.")

weekly_pace = st.sidebar.number_input(
    "Adjust League Average Pace Base", 
    min_value=60.0, max_value=110.0, value=float(cfg["avg_pace"]), step=0.1
)
weekly_ortg = st.sidebar.number_input(
    "Adjust League Average Offense Rating", 
    min_value=90.0, max_value=130.0, value=float(cfg["avg_ortg"]), step=0.1
)

st.sidebar.caption("Data Normalized: RealGM.com Advanced Tracker Registry")

st.subheader(f"🏟️ Setup Matchup Projections: {selected_db}")
col_h, col_a = st.columns(2)
with col_h:
    home = st.selectbox("🏡 Select Home Team", sorted(cfg["teams"].keys()), index=0)
with col_a:
    away = st.selectbox("✈️ Select Away Team", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

# Optional Team-Specific Override Section
with st.expander("📝 Edit Individual Selected Team Core Stats (Optional Weekly Tuning)"):
    col_t1, col_t2 = st.columns(2)
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
        # 1. Predict Game Pace using configured overrides
        predicted_pace = (h_pace + a_pace) - weekly_pace
        
        # 2. Predict Home Score (Includes updated +3.5 Home Court Factor requested)
        projected_home_ft = ((h_ortg + a_drtg) - weekly_ortg) * (predicted_pace / 100) + 3.5
        
        # 3. Predict Away Score
        projected_away_ft = ((a_ortg + h_drtg) - weekly_ortg) * (predicted_pace / 100)
        
        # 4. Calculate Point Spread Model Value
        model_spread = projected_away_ft - projected_home_ft
        
        # Output Logic Targets
        winner_team = home if projected_home_ft > projected_away_ft else away
        winner_icon = "🏡" if winner_team == home else "✈️"

        # -------------------------------------------------------------------------
        # DISPLAY SECTION: SIMULATION RESULT GENERATIONS
        # -------------------------------------------------------------------------
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

        # -------------------------------------------------------------------------
        # ADVANCED SPREADSHEET CELL LOGGER AUDIT EXPANDER
        # -------------------------------------------------------------------------
        with st.expander("🔍 View 2026 Cell Variables & Sheet Calculation Logs"):
            st.markdown(f"#### Active League Infrastructure Baseline (Weekly Tuning)")
            st.text(f"Adjusted League Average Pace Base: {weekly_pace} possessions")
            st.text(f"Adjusted League Average Offense Rating Base: {weekly_ortg}")
            st.text(f"Applied Home Court Advantage Variable Constant: +3.5 points")
            
            st.markdown("---")
            st.markdown(f"#### Evaluated Operational Advanced Metrics Matrix")
            col_sh1, col_sh2 = st.columns(2)
            with col_sh1:
                st.markdown(f"**🏡 {home}**")
                st.text(f"Offensive Rating Coefficient: {h_ortg}")
                st.text(f"Defensive Rating Coefficient: {h_drtg}")
                st.text(f"Pace Coefficient: {h_pace}")
            with col_sh2:
                st.markdown(f"**✈️ {away}**")
                st.text(f"Offensive Rating Coefficient: {a_ortg}")
                st.text(f"Defensive Rating Coefficient: {a_drtg}")
                st.text(f"Pace Coefficient: {a_pace}")
                
            st.markdown("---")
            st.markdown("#### Formula Step Calculation Outputs")
            st.markdown(f"* Predicted Dynamic Game Pace: `{predicted_pace:.2f}` possessions")
            st.markdown(f"* Raw Sheet Spread Target Value: `{model_spread:+.1f}` points")
else:
    st.info("💡 System Ready. Configure teams and click the button above to execute calculations.")
