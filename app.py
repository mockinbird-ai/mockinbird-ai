import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="MiHoops Analytics", page_icon="🏀", layout="centered")
st.title("🏀 MiHoops Analytics Engine")
st.markdown("### High-Efficiency Power Rating Model")
st.markdown("---")

# =========================================================================
# COMPACT REGISTRY (Sourced via Basketball-Reference / RealGM Benchmarks)
# =========================================================================
LEAGUE_DB = {
    "NBA": {
        "avg_pace": 99.2, "avg_ortg": 115.6, "hca": 2.1,
        "teams": {
            "Atlanta Hawks": {"ORTG": 114.2, "DRTG": 116.5, "PACE": 100.8},
            "Boston Celtics": {"ORTG": 122.1, "DRTG": 111.4, "PACE": 97.5},
            "Brooklyn Nets": {"ORTG": 111.5, "DRTG": 115.2, "PACE": 96.9},
            "Charlotte Hornets": {"ORTG": 109.8, "DRTG": 117.4, "PACE": 98.2},
            "Chicago Bulls": {"ORTG": 113.1, "DRTG": 115.9, "PACE": 99.4},
            "Cleveland Cavaliers": {"ORTG": 116.2, "DRTG": 111.8, "PACE": 97.1},
            "Dallas Mavericks": {"ORTG": 117.0, "DRTG": 114.9, "PACE": 99.9},
            "Denver Nuggets": {"ORTG": 122.6, "DRTG": 114.3, "PACE": 96.8},
            "Detroit Pistons": {"ORTG": 110.4, "DRTG": 116.8, "PACE": 98.5},
            "Golden State Warriors": {"ORTG": 116.9, "DRTG": 114.5, "PACE": 100.5},
            "Houston Rockets": {"ORTG": 113.8, "DRTG": 111.2, "PACE": 99.1},
            "Indiana Pacers": {"ORTG": 120.5, "DRTG": 118.4, "PACE": 101.5},
            "LA Clippers": {"ORTG": 114.9, "DRTG": 112.1, "PACE": 97.2},
            "Los Angeles Lakers": {"ORTG": 114.8, "DRTG": 115.1, "PACE": 101.2},
            "Memphis Grizzlies": {"ORTG": 110.2, "DRTG": 112.5, "PACE": 100.3},
            "Miami Heat": {"ORTG": 116.7, "DRTG": 111.5, "PACE": 96.2},
            "Milwaukee Bucks": {"ORTG": 117.5, "DRTG": 115.0, "PACE": 100.2},
            "Minnesota Timberwolves": {"ORTG": 116.8, "DRTG": 108.4, "PACE": 97.2},
            "New Orleans Pelicans": {"ORTG": 115.4, "DRTG": 112.9, "PACE": 98.0},
            "New York Knicks": {"ORTG": 119.8, "DRTG": 112.4, "PACE": 95.8},
            "Oklahoma City Thunder": {"ORTG": 118.9, "DRTG": 111.0, "PACE": 100.1},
            "Orlando Magic": {"ORTG": 112.8, "DRTG": 110.5, "PACE": 97.4},
            "Philadelphia 76ers": {"ORTG": 115.2, "DRTG": 113.0, "PACE": 97.8},
            "Phoenix Suns": {"ORTG": 116.1, "DRTG": 114.2, "PACE": 98.7},
            "Portland Trail Blazers": {"ORTG": 108.9, "DRTG": 116.0, "PACE": 98.9},
            "Sacramento Kings": {"ORTG": 116.5, "DRTG": 115.1, "PACE": 99.3},
            "San Antonio Spurs": {"ORTG": 110.8, "DRTG": 114.6, "PACE": 101.1},
            "Toronto Raptors": {"ORTG": 113.2, "DRTG": 118.1, "PACE": 99.7},
            "Utah Jazz": {"ORTG": 114.5, "DRTG": 119.3, "PACE": 100.6},
            "Washington Wizards": {"ORTG": 110.1, "DRTG": 118.9, "PACE": 102.1}
        }
    },
    "WNBA": {
        "avg_pace": 80.8, "avg_ortg": 103.5, "hca": 2.1,
        "teams": {
            "Atlanta Dream": {"ORTG": 102.5, "DRTG": 101.2, "PACE": 80.1},
            "Chicago Sky": {"ORTG": 98.8, "DRTG": 103.4, "PACE": 81.2},
            "Connecticut Sun": {"ORTG": 101.4, "DRTG": 99.1, "PACE": 79.4},
            "Dallas Wings": {"ORTG": 104.2, "DRTG": 103.8, "PACE": 82.5},
            "Golden State Valkyries": {"ORTG": 103.1, "DRTG": 101.5, "PACE": 81.8},
            "Indiana Fever": {"ORTG": 105.1, "DRTG": 104.9, "PACE": 83.1},
            "Las Vegas Aces": {"ORTG": 108.2, "DRTG": 103.1, "PACE": 82.9},
            "Los Angeles Sparks": {"ORTG": 110.4, "DRTG": 113.4, "PACE": 80.3},
            "Minnesota Lynx": {"ORTG": 112.5, "DRTG": 101.0, "PACE": 81.3},
            "New York Liberty": {"ORTG": 107.8, "DRTG": 102.2, "PACE": 80.9},
            "Phoenix Mercury": {"ORTG": 100.5, "DRTG": 103.2, "PACE": 82.4},
            "Portland Fire": {"ORTG": 99.1, "DRTG": 103.5, "PACE": 81.1},
            "Seattle Storm": {"ORTG": 94.5, "DRTG": 102.0, "PACE": 81.7},
            "Toronto Tempo": {"ORTG": 104.0, "DRTG": 104.5, "PACE": 80.8},
            "Washington Mystics": {"ORTG": 101.2, "DRTG": 105.1, "PACE": 80.5}
        }
    }
}

# League Selection
selected_league = st.sidebar.selectbox("Active Matrix", list(LEAGUE_DB.keys()))
cfg = LEAGUE_DB[selected_league]

# Matchup Input Columns
col1, col2 = st.columns(2)
with col1:
    home = st.selectbox("🏡 Home Team", sorted(cfg["teams"].keys()), index=0)
with col2:
    away = st.selectbox("✈️ Away Team", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

if home == away:
    st.error("Select two unique matching teams.")
else:
    # -------------------------------------------------------------------------
    # HIGH-ACCURACY EFFICIENCY MATHEMATICS ENGINE
    # -------------------------------------------------------------------------
    h_data, a_data = cfg["teams"][home], cfg["teams"][away]
    
    # Expected Matchup Pace modeled against Selected League Baseline
    proj_pace = (h_data["PACE"] * a_data["PACE"]) / cfg["avg_pace"]
    
    # Regression Efficiency Calculations using League Offensive Baseline
    h_exp_eff = (h_data["ORTG"] * a_data["DRTG"]) / cfg["avg_ortg"]
    a_exp_eff = (a_data["ORTG"] * h_data["DRTG"]) / cfg["avg_ortg"]
    
    # Exact Scoring Projections
    score_home = (h_exp_eff * (proj_pace / 100)) + cfg["hca"]
    score_away = (a_exp_eff * (proj_pace / 100))
    
    # Calculated Margins
    spread = score_away - score_home
    winner_team = home if score_home > score_away else away
    winner_icon = "🏡" if winner_team == home else "✈️"
    
    # -------------------------------------------------------------------------
    # EXCLUSIVE WINNER CALLOUT SECTION
    # -------------------------------------------------------------------------
    st.markdown("## 🏆 Model Consensus Winner Selection")
    
    with st.container():
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="Outright Winner Pick", value=f"{winner_icon} {winner_team}")
        with m2:
            st.metric(label="Calculated Model Line Spread", value=f"{winner_team} {abs(spread):-.1f}")
            
    st.markdown("---")
    
    # -------------------------------------------------------------------------
    # MATCHUP BREAKDOWN DATA MATRIX TABLE
    # -------------------------------------------------------------------------
    st.subheader("📊 Matchup Projections Summary Matrix Table")
    
    matrix_summary = pd.DataFrame({
        "Team Segment": [f"🏡 {home} (Home)", f"✈️ {away} (Away)"],
        "Half Time (HT) Projection": [f"{score_home * 0.5:.1f}", f"{score_away * 0.5:.1f}"],
        "Final Score (FT) Projection": [f"{score_home:.1f}", f"{score_away:.1f}"],
        "Model Point Spread Line": [f"{spread:+.1f}", f"{-spread:+.1f}"]
    })
    
    st.table(matrix_summary)

    # -------------------------------------------------------------------------
    # DYNAMIC ADVANCED STATS EXPANDER
    # -------------------------------------------------------------------------
    with st.expander("🔍 View Raw Advanced Analytical Variables Used"):
        col_st1, col_st2 = st.columns(2)
        with col_st1:
            st.markdown(f"**Expected Matchup Pace Line:** `{proj_pace:.2f}` possessions")
            st.markdown(f"**League Average Pace ({selected_league}):** `{cfg['avg_pace']}`")
        with col_st2:
            st.markdown(f"**League Average Offensive Rating ({selected_league}):** `{cfg['avg_ortg']}`")
            st.markdown(f"**Applied Home Court Advantage Value:** `+{cfg['hca']}` points")
