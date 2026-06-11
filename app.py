import streamlit as st
import pandas as pd
import numpy as np

# Set up page configurations
st.set_page_config(page_title="MiHoops Global Engine", page_icon="🏀", layout="centered")
st.title("🏀 MiHoops Multi-League Precision Sheets Engine")
st.markdown("### Hardcoded Global Registry | Pure Formula Sheet Simulator")
st.markdown("---")

# ==========================================
# MASTER HARDCODED DATA REGISTRY
# ==========================================
# 📝 EDIT AND REWRITE THIS REGISTRY COMPLETELY EVERY WEEK FOR DATA UPDATES
# Metrics gathered from Basketball-Reference (Advanced Tables) & FIBA Data portals.
GLOBAL_LEAGUE_DATABASE = {
    "NBA": {
        "avg_pace": 99.2,
        "avg_ortg": 115.6,
        "hca_bonus": 2.5,
        "teams": {
            "Boston Celtics": {"ORTG": 122.1, "DRTG": 111.4, "PACE": 97.5},
            "Los Angeles Lakers": {"ORTG": 114.8, "DRTG": 115.1, "PACE": 101.2},
            "Denver Nuggets": {"ORTG": 122.6, "DRTG": 114.3, "PACE": 96.8},
            "Oklahoma City Thunder": {"ORTG": 118.9, "DRTG": 111.0, "PACE": 100.1},
            "Minnesota Timberwolves": {"ORTG": 116.8, "DRTG": 108.4, "PACE": 97.2},
            "New York Knicks": {"ORTG": 119.8, "DRTG": 112.4, "PACE": 95.8},
            "Dallas Mavericks": {"ORTG": 117.0, "DRTG": 114.9, "PACE": 99.9},
            "Milwaukee Bucks": {"ORTG": 117.5, "DRTG": 115.0, "PACE": 100.2},
            "Miami Heat": {"ORTG": 116.7, "DRTG": 111.5, "PACE": 96.2},
            "Golden State Warriors": {"ORTG": 116.9, "DRTG": 114.5, "PACE": 100.5}
        }
    },
    "WNBA": {
        "avg_pace": 81.2,
        "avg_ortg": 102.4,
        "hca_bonus": 2.5,
        "teams": {
            "New York Liberty": {"ORTG": 108.5, "DRTG": 96.4, "PACE": 80.1},
            "Las Vegas Aces": {"ORTG": 107.2, "DRTG": 99.1, "PACE": 82.4},
            "Connecticut Sun": {"ORTG": 103.1, "DRTG": 94.8, "PACE": 78.9},
            "Minnesota Lynx": {"ORTG": 105.4, "DRTG": 97.2, "PACE": 80.8},
            "Seattle Storm": {"ORTG": 101.9, "DRTG": 98.0, "PACE": 81.5},
            "Indiana Fever": {"ORTG": 102.8, "DRTG": 106.1, "PACE": 82.9},
            "Phoenix Mercury": {"ORTG": 100.5, "DRTG": 103.4, "PACE": 82.1},
            "Chicago Sky": {"ORTG": 98.2, "DRTG": 102.9, "PACE": 80.4},
            "Atlanta Dream": {"ORTG": 96.7, "DRTG": 101.5, "PACE": 79.8},
            "Washington Mystics": {"ORTG": 97.4, "DRTG": 102.8, "PACE": 80.2},
            "Los Angeles Sparks": {"ORTG": 95.9, "DRTG": 104.7, "PACE": 79.5},
            "Dallas Wings": {"ORTG": 99.1, "DRTG": 107.4, "PACE": 81.7}
        }
    },
    "Spain (Liga ACB)": {
        "avg_pace": 76.4,
        "avg_ortg": 112.1,
        "hca_bonus": 2.5,
        "teams": {
            "Real Madrid": {"ORTG": 119.5, "DRTG": 105.2, "PACE": 75.8},
            "FC Barcelona": {"ORTG": 116.2, "DRTG": 108.4, "PACE": 77.1},
            "Unicaja Malaga": {"ORTG": 115.8, "DRTG": 107.2, "PACE": 76.5},
            "Valencia Basket": {"ORTG": 113.4, "DRTG": 110.1, "PACE": 78.0},
            "Baskonia": {"ORTG": 111.9, "DRTG": 111.5, "PACE": 76.9}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8,
        "avg_ortg": 110.5,
        "hca_bonus": 2.5,
        "teams": {
            "AS Monaco": {"ORTG": 117.2, "DRTG": 104.1, "PACE": 74.9},
            "Paris Basketball": {"ORTG": 115.4, "DRTG": 107.9, "PACE": 77.2},
            "LDLC ASVEL": {"ORTG": 112.1, "DRTG": 109.4, "PACE": 75.3},
            "JL Bourg": {"ORTG": 110.2, "DRTG": 108.1, "PACE": 74.5}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.2,
        "avg_ortg": 111.2,
        "hca_bonus": 2.5,
        "teams": {
            "Bayern Munich": {"ORTG": 118.1, "DRTG": 105.9, "PACE": 77.4},
            "ALBA Berlin": {"ORTG": 112.4, "DRTG": 110.2, "PACE": 79.1},
            "Ratiopharm Ulm": {"ORTG": 113.0, "DRTG": 111.1, "PACE": 78.5}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.1,
        "avg_ortg": 111.8,
        "hca_bonus": 2.5,
        "teams": {
            "Olimpia Milano": {"ORTG": 116.5, "DRTG": 106.2, "PACE": 75.1},
            "Virtus Bologna": {"ORTG": 115.9, "DRTG": 107.0, "PACE": 75.8},
            "Reyer Venezia": {"ORTG": 110.4, "DRTG": 109.8, "PACE": 76.7}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.5,
        "avg_ortg": 113.2,
        "hca_bonus": 2.5,
        "teams": {
            "Vaqueros de Bayamon": {"ORTG": 115.2, "DRTG": 111.0, "PACE": 83.1},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.0},
            "Capitanes de Arecibo": {"ORTG": 116.8, "DRTG": 113.4, "PACE": 82.9}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.1,
        "avg_ortg": 109.8,
        "hca_bonus": 2.5,
        "teams": {
            "Canterbury Rams": {"ORTG": 114.2, "DRTG": 106.5, "PACE": 83.8},
            "Auckland Tuatara": {"ORTG": 112.1, "DRTG": 108.2, "PACE": 84.5},
            "Wellington Saints": {"ORTG": 113.9, "DRTG": 111.0, "PACE": 85.2}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.2,
        "avg_ortg": 110.1,
        "hca_bonus": 2.5,
        "teams": {
            "Panathinaikos": {"ORTG": 120.4, "DRTG": 103.2, "PACE": 73.9},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 73.5},
            "Peristeri": {"ORTG": 108.5, "DRTG": 110.4, "PACE": 74.8}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 77.9,
        "avg_ortg": 107.5,
        "hca_bonus": 2.5,
        "teams": {
            "SL Benfica": {"ORTG": 114.2, "DRTG": 103.5, "PACE": 77.2},
            "FC Porto": {"ORTG": 112.8, "DRTG": 105.1, "PACE": 78.1},
            "Sporting CP": {"ORTG": 110.5, "DRTG": 107.9, "PACE": 78.4}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 82.8,
        "avg_ortg": 111.4,
        "hca_bonus": 2.5,
        "teams": {
            "Niagara River Lions": {"ORTG": 114.5, "DRTG": 109.2, "PACE": 82.1},
            "Vancouver Bandits": {"ORTG": 113.1, "DRTG": 110.8, "PACE": 83.5},
            "Scarborough Shooting Stars": {"ORTG": 112.4, "DRTG": 112.0, "PACE": 82.9}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 79.5,
        "avg_ortg": 106.8,
        "hca_bonus": 2.5,
        "teams": {
            "London Lions": {"ORTG": 114.8, "DRTG": 101.2, "PACE": 80.2},
            "Leicester Riders": {"ORTG": 108.2, "DRTG": 106.5, "PACE": 79.1},
            "Caledonia Gladiators": {"ORTG": 106.1, "DRTG": 107.4, "PACE": 78.8}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.2,
        "avg_ortg": 105.4,
        "hca_bonus": 2.5,
        "teams": {
            "Swans Gmunden": {"ORTG": 110.2, "DRTG": 102.1, "PACE": 75.8},
            "Flyers Wels": {"ORTG": 107.5, "DRTG": 104.9, "PACE": 76.5},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 75.9}
        }
    },
    "Croatia (Premijer Liga)": {
        "avg_pace": 75.5,
        "avg_ortg": 107.2,
        "hca_bonus": 2.5,
        "teams": {
            "KK Zadar": {"ORTG": 113.4, "DRTG": 103.1, "PACE": 74.8},
            "KK Split": {"ORTG": 109.2, "DRTG": 106.4, "PACE": 75.9},
            "Cibona Zagreb": {"ORTG": 106.8, "DRTG": 109.1, "PACE": 76.1}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 77.4,
        "avg_ortg": 108.1,
        "hca_bonus": 2.5,
        "teams": {
            "ERA Nymburk": {"ORTG": 116.5, "DRTG": 101.4, "PACE": 78.1},
            "BK Opava": {"ORTG": 109.4, "DRTG": 107.2, "PACE": 76.9},
            "BK Decin": {"ORTG": 107.8, "DRTG": 108.5, "PACE": 77.6}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.2,
        "avg_ortg": 113.4,
        "hca_bonus": 2.5,
        "teams": {
            "Anadolu Efes": {"ORTG": 119.8, "DRTG": 107.5, "PACE": 76.8},
            "Fenerbahce Beko": {"ORTG": 119.2, "DRTG": 106.9, "PACE": 76.4},
            "Besiktas": {"ORTG": 112.5, "DRTG": 110.1, "PACE": 77.9},
            "Pinar Karsiyaka": {"ORTG": 114.0, "DRTG": 112.4, "PACE": 78.1}
        }
    },
    "Brazil (NBB)": {
        "avg_pace": 76.8,
        "avg_ortg": 109.5,
        "hca_bonus": 2.5,
        "teams": {
            "Flamengo": {"ORTG": 115.4, "DRTG": 103.2, "PACE": 76.1},
            "Franca Sesi": {"ORTG": 114.1, "DRTG": 105.6, "PACE": 75.9},
            "Minas Storm": {"ORTG": 111.8, "DRTG": 108.4, "PACE": 77.3}
        }
    }
}

# ==========================================
# LEAGUE SELECTION CONTROL LAYER
# ==========================================
selected_league_name = st.sidebar.selectbox("Target Competition Registry", sorted(GLOBAL_LEAGUE_DATABASE.keys()))

# Extract isolated parameters matching the selected competition
LEAGUE_CONTEXT = GLOBAL_LEAGUE_DATABASE[selected_league_name]
LEAGUE_AVG_PACE = LEAGUE_CONTEXT["avg_pace"]
LEAGUE_AVG_ORTG = LEAGUE_CONTEXT["avg_ortg"]
HCA_BONUS = LEAGUE_CONTEXT["hca_bonus"]
TEAM_DATABASE = LEAGUE_CONTEXT["teams"]

# Display Contextual Metrics in the sidebar
st.sidebar.markdown(f"### 📋 {selected_league_name} Baselines")
st.sidebar.metric("League Average Pace", f"{LEAGUE_AVG_PACE}")
st.sidebar.metric("League Average Offense", f"{LEAGUE_AVG_ORTG}")

# ==========================================
# INTERACTIVE CALCULATOR INTERFACE
# ==========================================
st.subheader(f"⚙️ Matchup Design Engine: {selected_league_name}")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**🏡 HOME TEAM**")
    home_team = st.selectbox("Select Home Team", sorted(TEAM_DATABASE.keys()), index=0)
    
    # Pre-populates baseline cells with manual override overrides
    h_ortg = st.number_input("Home Offensive Rating", value=float(TEAM_DATABASE[home_team]["ORTG"]), step=0.1, key="h_ortg")
    h_drtg = st.number_input("Home Defensive Rating", value=float(TEAM_DATABASE[home_team]["DRTG"]), step=0.1, key="h_drtg")
    h_pace = st.number_input("Home Pace", value=float(TEAM_DATABASE[home_team]["PACE"]), step=0.1, key="h_pace")

with col2:
    st.markdown("**✈️ AWAY TEAM**")
    away_team = st.selectbox("Select Away Team", sorted(TEAM_DATABASE.keys()), index=1 if len(TEAM_DATABASE) > 1 else 0)
    
    a_ortg = st.number_input("Away Offensive Rating", value=float(TEAM_DATABASE[away_team]["ORTG"]), step=0.1, key="a_ortg")
    a_drtg = st.number_input("Away Defensive Rating", value=float(TEAM_DATABASE[away_team]["DRTG"]), step=0.1, key="a_drtg")
    a_pace = st.number_input("Away Pace", value=float(TEAM_DATABASE[away_team]["PACE"]), step=0.1, key="a_pace")

st.markdown("---")

# ==========================================
# ANALYTICAL MATHEMATICAL FORMULAS
# ==========================================
if home_team == away_team:
    st.warning("⚠️ Please select two different teams to process model forecasts.")
else:
    # 1. Predict Game Pace: =(Home Pace + Away Pace) - League Average Pace
    predicted_pace = (h_pace + a_pace) - LEAGUE_AVG_PACE

    # 2. Predict Home Score: =((Home Offense + Away Defense) - League Average Offense) * (Predicted Pace / 100) + HCA
    predicted_home_score = ((h_ortg + a_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100) + HCA_BONUS

    # 3. Predict Away Score: =((Away Offense + Home Defense) - League Average Offense) * (Predicted Pace / 100)
    predicted_away_score = ((a_ortg + h_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100)

    # 4. Calculate Model Point Spread: = Away Score - Home Score
    model_spread = predicted_away_score - predicted_home_score

    # Output Metric Matrix Display
    st.subheader("📋 Predicted Final Scores")
    col_sc1, col_sc2, col_sc3 = st.columns(3)
    col_sc1.metric(f"🏀 {home_team} (Home)", f"{predicted_home_score:.1f}")
    col_sc2.metric(f"🚀 {away_team} (Away)", f"{predicted_away_score:.1f}")
    col_sc3.metric("📈 Game Pace", f"{predicted_pace:.1f} Poss")

    st.markdown("---")
    
    # Model Spread Matrix Element
    st.subheader("📊 Point Spread Projections")
    sign = "+" if model_spread > 0 else ""
    st.metric(label=f"Model Spread Line (Relative to {home_team})", value=f"{sign}{model_spread:.1f}")
    st.caption(f"Interpretation: Your spreadsheet model favors **{home_team}** by **{abs(model_spread):.1f}** points.")

    st.markdown("---")

    # ==========================================
    # BOOKIE EDGE MATRIX COMPARATOR
    # ==========================================
    st.subheader("🟢 Step 5: Edge Finder Matrix")
    bookie_line = st.number_input(f"Sportsbook Market Line: {home_team} Spread", value=float(np.round(model_spread)), step=0.5)
    
    spread_differential = bookie_line - model_spread
    
    st.markdown("#### Optimal Play Recommendation:")
    if spread_differential > 1.0:
        st.success(f"🟢 **Bet {home_team} {bookie_line}** | The bookie is giving the home team less credit than your math.")
    elif spread_differential < -1.0:
        st.success(f"🟢 **Bet {away_team} +{abs(bookie_line)}** | The bookie is making the home team too big of a favorite.")
    else:
        st.error(f"❌ **Pass / Do Not Bet** | The bookie's line perfectly matches your model calculation.")
