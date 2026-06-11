import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="Pro Hoops Predictor 2026", page_icon="🏀", layout="centered")
st.title("🏀 Pro Hoops 2026 Matrix Prediction Engine")
st.markdown("### Google Sheets Advanced Spreadsheet Math Pipeline (v2026.3)")
st.markdown("---")

# =========================================================================
# COMPLETE COMPREHENSIVE BASKETBALL REGISTRY DATABASE (2025-2026)
# Fully expanded registries for accurate top-tier matchup matrices
# =========================================================================
BASKETBALL_MASTER_DB = {
    "Spain (Liga ACB)": {
        "avg_pace": 77.2, "avg_ortg": 112.4, "source": "RealGM Advanced Stats / EuroBasket",
        "teams": {
            "FC Barcelona": {"ORTG": 116.8, "DRTG": 107.5, "PACE": 77.2},
            "Real Madrid": {"ORTG": 118.6, "DRTG": 106.5, "PACE": 76.3},
            "Unicaja Malaga": {"ORTG": 116.5, "DRTG": 107.2, "PACE": 77.1},
            "Valencia Basket": {"ORTG": 114.4, "DRTG": 109.8, "PACE": 78.0},
            "Saski Baskonia": {"ORTG": 112.5, "DRTG": 111.4, "PACE": 76.8},
            "CB 1939 Canarias (Tenerife)": {"ORTG": 113.9, "DRTG": 109.1, "PACE": 75.8},
            "UCAM Murcia": {"ORTG": 111.2, "DRTG": 110.5, "PACE": 76.4},
            "Club Joventut Badalona": {"ORTG": 110.8, "DRTG": 111.2, "PACE": 77.5},
            "Bilbao Basket": {"ORTG": 109.5, "DRTG": 110.1, "PACE": 76.9},
            "Bàsquet Girona": {"ORTG": 106.1, "DRTG": 109.9, "PACE": 76.1},
            "Baxi Manresa": {"ORTG": 109.2, "DRTG": 111.5, "PACE": 78.4},
            "CB Gran Canaria": {"ORTG": 111.8, "DRTG": 110.2, "PACE": 76.2},
            "Zunder Palencia": {"ORTG": 104.5, "DRTG": 112.8, "PACE": 77.0},
            "Casademont Zaragoza": {"ORTG": 108.4, "DRTG": 111.9, "PACE": 77.9},
            "Coviran Granada": {"ORTG": 106.8, "DRTG": 111.2, "PACE": 76.5},
            "Monbus Obradoiro": {"ORTG": 107.2, "DRTG": 110.8, "PACE": 75.9},
            "MoraBanc Andorra": {"ORTG": 109.0, "DRTG": 111.4, "PACE": 77.6},
            "Río Breogán": {"ORTG": 105.1, "DRTG": 109.5, "PACE": 75.4}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.2, "source": "RealGM Advanced Stats / LNB.fr",
        "teams": {
            "AS Monaco": {"ORTG": 116.9, "DRTG": 104.1, "PACE": 74.5},
            "Paris Basketball": {"ORTG": 115.2, "DRTG": 107.5, "PACE": 77.1},
            "LDLC ASVEL (Lyon-Villeurbanne)": {"ORTG": 113.6, "DRTG": 109.4, "PACE": 75.4},
            "JL Bourg": {"ORTG": 111.4, "DRTG": 107.9, "PACE": 75.1},
            "JDA Dijon": {"ORTG": 108.8, "DRTG": 109.5, "PACE": 74.2},
            "Nanterre 92": {"ORTG": 110.5, "DRTG": 111.2, "PACE": 76.8},
            "Cholet Basket": {"ORTG": 108.1, "DRTG": 108.9, "PACE": 75.5},
            "Le Mans Sarthe": {"ORTG": 107.9, "DRTG": 109.1, "PACE": 76.0},
            "SIG Strasbourg": {"ORTG": 109.2, "DRTG": 110.4, "PACE": 75.9},
            "Saint-Quentin": {"ORTG": 106.4, "DRTG": 105.8, "PACE": 73.8},
            "SLUC Nancy": {"ORTG": 108.5, "DRTG": 111.0, "PACE": 76.4},
            "Blois": {"ORTG": 105.3, "DRTG": 112.1, "PACE": 76.2},
            "Chalon/Saône": {"ORTG": 106.9, "DRTG": 111.5, "PACE": 75.1},
            "Gravelines-Dunkerque": {"ORTG": 104.2, "DRTG": 108.5, "PACE": 74.8},
            "Metropolitans 92": {"ORTG": 103.8, "DRTG": 113.4, "PACE": 77.0},
            "Roanne": {"ORTG": 107.5, "DRTG": 114.1, "PACE": 77.5},
            "Limoges CSP": {"ORTG": 106.1, "DRTG": 109.9, "PACE": 74.9},
            "Le Portel": {"ORTG": 105.8, "DRTG": 110.6, "PACE": 75.6}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.4, "avg_ortg": 111.5, "source": "easyCredit BBL Advanced Tracking",
        "teams": {
            "FC Bayern Munich": {"ORTG": 117.9, "DRTG": 106.5, "PACE": 77.9},
            "ALBA Berlin": {"ORTG": 112.1, "DRTG": 110.9, "PACE": 79.3},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 107.4, "PACE": 77.1},
            "ratiopharm ulm": {"ORTG": 112.8, "DRTG": 112.1, "PACE": 78.5},
            "Telekom Baskets Bonn": {"ORTG": 113.5, "DRTG": 111.2, "PACE": 77.8},
            "MHP Riesen Ludwigsburg": {"ORTG": 110.1, "DRTG": 109.4, "PACE": 77.5},
            "Veolia Towers Hamburg": {"ORTG": 109.4, "DRTG": 112.8, "PACE": 79.6},
            "EWE Baskets Oldenburg": {"ORTG": 111.6, "DRTG": 111.9, "PACE": 78.9},
            "Brose Bamberg": {"ORTG": 110.5, "DRTG": 113.2, "PACE": 79.1},
            "Würzburg Baskets": {"ORTG": 111.2, "DRTG": 108.1, "PACE": 76.8},
            "Basketball Löwen Braunschweig": {"ORTG": 107.5, "DRTG": 109.0, "PACE": 78.0},
            "Rasta Vechta": {"ORTG": 110.8, "DRTG": 111.5, "PACE": 78.4},
            "BG Göttingen": {"ORTG": 107.2, "DRTG": 114.0, "PACE": 79.5},
            "Syntainics MBC": {"ORTG": 108.9, "DRTG": 114.6, "PACE": 79.2},
            "Academia Tigers Tübingen": {"ORTG": 105.1, "DRTG": 113.9, "PACE": 78.6},
            "Hakro Merlins Crailsheim": {"ORTG": 106.4, "DRTG": 115.2, "PACE": 79.9},
            "Heidelberg": {"ORTG": 106.8, "DRTG": 114.8, "PACE": 79.0},
            "Rostock Seawolves": {"ORTG": 108.0, "DRTG": 112.9, "PACE": 78.7}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.2, "avg_ortg": 112.1, "source": "Lega Basket Advanced Logs",
        "teams": {
            "Olimpia Milano (EA7)": {"ORTG": 116.2, "DRTG": 107.1, "PACE": 75.2},
            "Virtus Segafredo Bologna": {"ORTG": 117.6, "DRTG": 108.2, "PACE": 76.3},
            "Germani Brescia": {"ORTG": 115.1, "DRTG": 108.9, "PACE": 76.5},
            "Umana Reyer Venezia": {"ORTG": 111.2, "DRTG": 109.8, "PACE": 76.1},
            "Aquila Basket Trento": {"ORTG": 110.8, "DRTG": 110.4, "PACE": 76.9},
            "Derthona Basket Tortona": {"ORTG": 111.5, "DRTG": 110.1, "PACE": 75.8},
            "Pallacanestro Reggiana": {"ORTG": 110.2, "DRTG": 110.6, "PACE": 75.5},
            "Pistoia Basket 2000": {"ORTG": 107.8, "DRTG": 109.5, "PACE": 74.9},
            "Dinamo Sassari": {"ORTG": 109.5, "DRTG": 111.8, "PACE": 77.2},
            "Scafati Basket": {"ORTG": 111.0, "DRTG": 114.2, "PACE": 77.8},
            "NutriBullet Treviso": {"ORTG": 108.4, "DRTG": 112.5, "PACE": 76.6},
            "Openjobmetis Varese": {"ORTG": 112.6, "DRTG": 117.9, "PACE": 80.4},
            "Vanoli Cremona": {"ORTG": 106.5, "DRTG": 108.2, "PACE": 74.4},
            "Napoli Basket": {"ORTG": 109.1, "DRTG": 112.9, "PACE": 77.0},
            "Carpegna Prosciutto Pesaro": {"ORTG": 106.9, "DRTG": 113.4, "PACE": 76.2},
            "Happy Casa Brindisi": {"ORTG": 105.8, "DRTG": 111.9, "PACE": 75.6}
        }
    }
}

# =========================================================================
# UI REGION: DESIGN INTERFACE
# =========================================================================
selected_db = st.sidebar.selectbox("🏀 Select Active Basketball League", list(BASKETBALL_MASTER_DB.keys()))
cfg = BASKETBALL_MASTER_DB[selected_db]

st.sidebar.caption(f"Infrastructure Baseline: {cfg['source']}")

st.subheader(f"🏟️ Setup Matchup Projections: {selected_db}")
col_h, col_a = st.columns(2)
with col_h:
    home = st.selectbox("🏡 Select Home Team", sorted(cfg["teams"].keys()), index=0)
with col_a:
    away = st.selectbox("✈️ Select Away Team", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

st.markdown(" ")
initiate_analysis = st.button("🚀 Initiate Advanced Matchup Simulation", type="primary", use_container_width=True)
st.markdown("---")

if initiate_analysis:
    if home == away:
        st.error("⚠️ System Mapping Error: Select two unique teams to initiate analysis.")
    else:
        # Load Operational Team Metrics
        h_data, a_data = cfg["teams"][home], cfg["teams"][away]
        
        # 1. Predict Game Pace: (Home Pace + Away Pace) - League Average Pace
        predicted_pace = (h_data["PACE"] + a_data["PACE"]) - cfg["avg_pace"]
        
        # 2. Predict Home Score (Includes +2.5 Spreadsheet Home Court Advantage Factor)
        projected_home_ft = ((h_data["ORTG"] + a_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100) + 2.5
        
        # 3. Predict Away Score
        projected_away_ft = ((a_data["ORTG"] + h_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100)
        
        # 4. Calculate Point Spread Model Value (Negative value indicates Away team favorite)
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
            st.markdown(f"#### League Infrastructure Baseline (2025–2026 Season Parameters)")
            st.text(f"Cell B1 (League Average Pace): {cfg['avg_pace']} possessions")
            st.text(f"Cell B2 (League Average Offense Rating): {cfg['avg_ortg']}")
            
            st.markdown("---")
            st.markdown(f"#### Active Raw Advanced Metrics Dataset Breakdown")
            col_sh1, col_sh2 = st.columns(2)
            with col_sh1:
                st.markdown(f"**🏡 {home} (Column B Variables)**")
                st.text(f"Cell B6 (Offensive Rating): {h_data['ORTG']}")
                st.text(f"Cell B7 (Defensive Rating): {h_data['DRTG']}")
                st.text(f"Cell B8 (Team Total Pace): {h_data['PACE']}")
            with col_sh2:
                st.markdown(f"**✈️ {away} (Column C Variables)**")
                st.text(f"Cell C6 (Offensive Rating): {a_data['ORTG']}")
                st.text(f"Cell C7 (Defensive Rating): {a_data['DRTG']}")
                st.text(f"Cell C8 (Team Total Pace): {a_data['PACE']}")
                
            st.markdown("---")
            st.markdown("#### Formula Step Calculation Outputs")
            st.markdown(f"* Predicted Dynamic Game Pace (Cell B10 Output): `{predicted_pace:.2f}` possessions")
            st.markdown(f"* Raw Sheet Spread Target (Cell B14 Output): `{model_spread:+.1f}` points")
else:
    st.info("💡 System Ready. Configure teams and click the button above to execute calculations.")
