import streamlit as st
import pandas as pd
import numpy as np

# Set up page configurations
st.set_page_config(page_title="MiHoops Sheets Model", page_icon="🏀", layout="centered")
st.title("🏀 MiHoops Precision Sheets Engine")
st.markdown("### Hardcoded Weekly Engine | Pure Formula Matrix")
st.markdown("---")

# ==========================================
# STEP 1: LEAGUE BASELINE CONFIGURATION
# ==========================================
# 📝 UPDATE THESE EVERY WEEK IF THE LEAGUE-WIDE AVERAGES SHIFT
LEAGUE_AVG_PACE = 99.2    # Cell B1: League Average Pace
LEAGUE_AVG_ORTG = 115.6   # Cell B2: League Average Offense
HCA_BONUS = 2.5           # Home Court Advantage adjustment

# ==========================================
# WEEKLY DATA REGISTRY (REWRITE THIS SECTION WEEKLY)
# ==========================================
# 📝 Swap out, add, or edit these numbers directly every Sunday morning.
# Source: Basketball-Reference.com -> Advanced Team Stats table.
TEAM_DATABASE = {
    "Boston Celtics": {"ORTG": 122.1, "DRTG": 111.4, "PACE": 97.5},
    "Los Angeles Lakers": {"ORTG": 114.8, "DRTG": 115.1, "PACE": 101.2},
    "Denver Nuggets": {"ORTG": 117.8, "DRTG": 114.3, "PACE": 96.8},
    "Oklahoma City Thunder": {"ORTG": 118.3, "DRTG": 111.0, "PACE": 100.1},
    "Minnesota Timberwolves": {"ORTG": 114.6, "DRTG": 108.4, "PACE": 97.2},
    "New York Knicks": {"ORTG": 117.3, "DRTG": 112.4, "PACE": 95.8},
    "Dallas Mavericks": {"ORTG": 117.0, "DRTG": 114.9, "PACE": 99.9},
    "Milwaukee Bucks": {"ORTG": 117.5, "DRTG": 115.0, "PACE": 100.2},
    "Miami Heat": {"ORTG": 113.3, "DRTG": 111.5, "PACE": 96.2},
    "Golden State Warriors": {"ORTG": 116.9, "DRTG": 114.5, "PACE": 100.5}
}

# Display Active Baselines in Sidebar
st.sidebar.markdown("### 📋 Active Baseline Reference")
st.sidebar.metric("League Avg Pace", f"{LEAGUE_AVG_PACE}")
st.sidebar.metric("League Avg Offense", f"{LEAGUE_AVG_ORTG}")
st.sidebar.caption("To update, edit the top variables directly in `app.py`.")

# ==========================================
# STEP 2: MATCHUP CALCULATOR INTERFACE
# ==========================================
st.subheader("⚙️ Matchup Selection")

col1, col2 = st.columns(2)
with col1:
    st.markdown("**🏡 HOME TEAM**")
    home_team = st.selectbox("Select Home Team", sorted(TEAM_DATABASE.keys()), index=0)
    
    # Pre-populates fields with editable numbers (Cell B6, B7, B8 blueprint)
    h_ortg = st.number_input("Home Offensive Rating", value=float(TEAM_DATABASE[home_team]["ORTG"]), step=0.1, key="h_ortg")
    h_drtg = st.number_input("Home Defensive Rating", value=float(TEAM_DATABASE[home_team]["DRTG"]), step=0.1, key="h_drtg")
    h_pace = st.number_input("Home Pace", value=float(TEAM_DATABASE[home_team]["PACE"]), step=0.1, key="h_pace")

with col2:
    st.markdown("**✈️ AWAY TEAM**")
    away_team = st.selectbox("Select Away Team", sorted(TEAM_DATABASE.keys()), index=1 if len(TEAM_DATABASE) > 1 else 0)
    
    # Pre-populates fields with editable numbers (Cell C6, C7, C8 blueprint)
    a_ortg = st.number_input("Away Offensive Rating", value=float(TEAM_DATABASE[away_team]["ORTG"]), step=0.1, key="a_ortg")
    a_drtg = st.number_input("Away Defensive Rating", value=float(TEAM_DATABASE[away_team]["DRTG"]), step=0.1, key="a_drtg")
    a_pace = st.number_input("Away Pace", value=float(TEAM_DATABASE[away_team]["PACE"]), step=0.1, key="a_pace")

st.markdown("---")

# ==========================================
# STEP 3 & 4: THE MATHEMATICAL FORMULAS
# ==========================================
if home_team == away_team:
    st.warning("⚠️ Please select two different teams to run the projections.")
else:
    # 1. Predict the Game Pace: =(B8 + C8) - B1
    predicted_pace = (h_pace + a_pace) - LEAGUE_AVG_PACE

    # 2. Predict the Home Score: =((B6 + C7) - B2) * (B10 / 100) + 2.5
    predicted_home_score = ((h_ortg + a_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100) + HCA_BONUS

    # 3. Predict the Away Score: =((C6 + B7) - B2) * (B10 / 100)
    predicted_away_score = ((a_ortg + h_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100)

    # 4. Calculate Model Spread: =C12 - B12
    model_spread = predicted_away_score - predicted_home_score

    # Display Calculated Output Scoreboard
    st.subheader("📋 Predicted Final Results")
    
    col_sc1, col_sc2, col_sc3 = st.columns(3)
    col_sc1.metric(f"🏀 {home_team} (Home)", f"{predicted_home_score:.1f}")
    col_sc2.metric(f"🚀 {away_team} (Away)", f"{predicted_away_score:.1f}")
    col_sc3.metric("📈 Game Pace", f"{predicted_pace:.1f} Possessions")

    st.markdown("---")
    
    # Model Spread Display
    st.subheader("📊 Step 4: Point Spread Projection")
    sign = "+" if model_spread > 0 else ""
    st.metric(label=f"Model Spread (Relative to {home_team})", value=f"{sign}{model_spread:.1f}")
    st.caption(f"Interpretation: The spreadsheet math projects **{home_team}** to win by **{abs(model_spread):.1f}** points.")

    st.markdown("---")

    # ==========================================
    # STEP 5: BOOKIE LINE COMPARATOR
    # ==========================================
    st.subheader("🟢 Step 5: Edge Finder Matrix")
    
    # Enter what the live sportsbook is offering for the game
    bookie_line = st.number_input(f"Sportsbook Line: {home_team} Spread (e.g. -13.0)", value=float(np.round(model_spread)), step=0.5)
    
    spread_differential = bookie_line - model_spread
    
    st.markdown("#### Optimal Play Decision:")
    if spread_differential > 1.0:
        st.success(f"🟢 **Bet {home_team} {bookie_line}** | The bookie is giving the home team less credit than your math.")
    elif spread_differential < -1.0:
        st.success(f"🟢 **Bet {away_team} +{abs(bookie_line)}** | The bookie is making the home team too big of a favorite.")
    else:
        st.error(f"❌ **Pass / Do Not Bet** | The bookie's line closely matches your model.")
    
