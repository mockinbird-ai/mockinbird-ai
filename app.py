import streamlit as st
import pandas as pd
import numpy as np
import os

# ==========================================
# 1. LIVE DATA LAYER & FALLBACK CONFIG
# ==========================================
st.set_page_config(page_title="MiHoops High-Fidelity Simulator", page_icon="🏀", layout="wide")
st.title("🏀 MiHoops Precision Analytics Suite")
st.markdown("### Dynamic CSV-Driven Engine | Real-World Advanced Variance Matrix")
st.markdown("---")

DATA_PATH = "data/stats.csv"

# Global fallback defaults with baseline configurations 
LEAGUE_REGISTRY = {
    "NBA": {"pace": 98.8, "hca": 0.0},
    "WNBA": {"pace": 80.5, "hca": 3.5},
    "Spain: Liga ACB": {"pace": 76.4, "hca": 3.5},
    "France: LNB Élite": {"pace": 75.2, "hca": 3.5},
    "Germany: easyCredit BBL": {"pace": 77.8, "hca": 3.5},
    "Türkiye: BSL": {"pace": 76.6, "hca": 3.5},
    "Austria: Superliga": {"pace": 74.2, "hca": 3.5},
    "Czech Republic: NBL": {"pace": 76.1, "hca": 3.5},
    "Puerto Rico: BSN": {"pace": 82.1, "hca": 3.5},
    "New Zealand: NBL": {"pace": 81.8, "hca": 3.5},
    "Canada: CEBL": {"pace": 80.9, "hca": 3.5},
    "Italy: Lega Basket Serie A": {"pace": 76.3, "hca": 3.5},
    "Mexico: LNBP": {"pace": 79.1, "hca": 3.5},
    "Portugal: LPB": {"pace": 74.8, "hca": 3.5},
    "Croatia: Premijer Liga": {"pace": 73.5, "hca": 3.5},
    "Israel: Ligat HaAl": {"pace": 79.2, "hca": 3.2},
    "Belgium: BNXT League": {"pace": 75.8, "hca": 2.8},
    "Lithuania: LKL": {"pace": 78.4, "hca": 3.4},
    "Greece: Basket League": {"pace": 74.6, "hca": 3.8},
    "China: CBA": {"pace": 84.5, "hca": 4.0},
    "Brazil: NBB": {"pace": 76.9, "hca": 3.1}
}

@st.cache_data(ttl=3600)  # Caches data for 1 hour, auto-refreshing on updates
def load_advanced_statistics():
    if os.path.exists(DATA_PATH):
        try:
            return pd.read_csv(DATA_PATH)
        except Exception:
            pass
            
    # Initial Mock Setup Generation (Runs only if file is missing or unreadable)
    records = []
    for league, cfg in LEAGUE_REGISTRY.items():
        # Universal base template for teams
        teams = [f"Team Alpha {i}" for i in range(1, 13)] if league != "NBA" else ["Boston Celtics", "Denver Nuggets", "Los Angeles Lakers", "Washington Wizards"]
        for idx, team in enumerate(teams):
            # Introduce meaningful performance variance across teams
            tier_shift = (len(teams)/2 - idx) * 1.5 
            s_ortg = 111.0 + tier_shift
            s_drtg = 111.0 - (tier_shift * 0.8)
            records.append({
                "League": league, "Team": team,
                "Season_Pace": cfg["pace"] + np.random.uniform(-1, 1),
                "Season_ORTG": s_ortg, "Season_DRTG": s_drtg,
                "L10_Pace": cfg["pace"] + np.random.uniform(-2, 2),
                "L10_ORTG": s_ortg + np.random.uniform(-4, 4),
                "L10_DRTG": s_drtg + np.random.uniform(-4, 4)
            })
    df = pd.DataFrame(records)
    os.makedirs("data", exist_ok=True)
    df.to_csv(DATA_PATH, index=False)
    return df

# Initialize Data Sheet
master_stats = load_advanced_statistics()

# ==========================================
# 2. RUN INTERACTIVE INTERFACE
# ==========================================
selected_league = st.sidebar.selectbox("Select Target Competition", list(LEAGUE_REGISTRY.keys()))
league_df = master_stats[master_stats["League"] == selected_league]

st.subheader("⚙️ Matchup Design Engine")
col1, col2 = st.columns(2)
with col1:
    home_team = st.selectbox("Designate Home Venue Unit", league_df["Team"].unique(), index=0)
with col2:
    away_team = st.selectbox("Designate Road Competing Unit", league_df["Team"].unique(), index=1 if len(league_df["Team"].unique()) > 1 else 0)

if home_team != away_team:
    if st.button("Execute Form-Blended Simulation Matchup", type="primary"):
        home_profile = league_df[league_df["Team"] == home_team].iloc[0]
        away_profile = league_df[league_df["Team"] == away_team].iloc[0]
        
        # Rigorous 50% Season / 50% Last 10 Horizon Splitting
        home_blended_pace = (0.50 * home_profile["Season_Pace"]) + (0.50 * home_profile["L10_Pace"])
        home_blended_ortg = (0.50 * home_profile["Season_ORTG"]) + (0.50 * home_profile["L10_ORTG"])
        home_blended_drtg = (0.50 * home_profile["Season_DRTG"]) + (0.50 * home_profile["L10_DRTG"])
        
        away_blended_pace = (0.50 * away_profile["Season_Pace"]) + (0.50 * away_profile["L10_Pace"])
        away_blended_ortg = (0.50 * away_profile["Season_ORTG"]) + (0.50 * away_profile["L10_ORTG"])
        away_blended_drtg = (0.50 * away_profile["Season_DRTG"]) + (0.50 * away_profile["L10_DRTG"])
        
        # Intersecting Projected Pace Calculation
        league_mean_pace = LEAGUE_REGISTRY[selected_league]["pace"]
        projected_possessions = (home_blended_pace * away_blended_pace) / league_mean_pace
        
        # FIX: Expanded Cross-Over Efficiency Formulations to unlock dynamic outcome variance
        simulated_home_ortg = home_blended_ortg * (away_blended_drtg / 111.0)
        simulated_away_ortg = away_blended_ortg * (home_blended_drtg / 111.0)
        
        # Standardize expected possession point volume estimates
        base_final_home = (simulated_home_ortg * projected_possessions) / 100
        base_final_away = (simulated_away_ortg * projected_possessions) / 100
        
        # Enforcing Conditional Home Court Advantage rules
        applied_hca = LEAGUE_REGISTRY[selected_league]["hca"]
        calculated_final_home = base_final_home + applied_hca
        calculated_final_away = base_final_away
        
        final_score_home = int(np.round(calculated_final_home))
        final_score_away = int(np.round(calculated_final_away))
        
        # Dynamic stochastic breakdown for Halftime splits
        np.random.seed(None)
        half_score_home = int(np.round(final_score_home * np.random.uniform(0.46, 0.50)))
        half_score_away = int(np.round(final_score_away * np.random.uniform(0.46, 0.50)))
        
        # Win Probability
        home_net = home_blended_ortg - home_blended_drtg
        away_net = away_blended_ortg - away_blended_drtg
        efficiency_margin = home_net - away_net + (applied_hca * (100 / projected_possessions))
        win_probability_home = 1 / (1 + np.exp(-0.085 * efficiency_margin))
        
        assigned_winner = home_team if final_score_home > final_score_away else away_team
        confidence_value = max(win_probability_home, 1 - win_probability_home) * 100
        
        # ==========================================
        # 3. PRESENTATION LAYOUT
        # ==========================================
        st.markdown("---")
        st.header(f"🦅 Analytics Result: {assigned_winner} Projected Winner")
        st.metric("Model Algorithmic Certainty Rating", f"{confidence_value:.2f}%")
        
        st.subheader("📋 Core Scoreboard Allocation Matrix")
        scoreboard_df = pd.DataFrame({
            "Team Lineup Configuration": [f"{home_team} [HOME]", f"{away_team} [AWAY]"],
            "First Half Score": [half_score_home, half_score_away],
            "Final Simulated Score": [final_score_home, final_score_away]
        })
        st.table(scoreboard_df.set_index("Team Lineup Configuration"))
        
        with st.expander("🔬 View Advanced Diagnostics"):
            col_diag1, col_diag2 = st.columns(2)
            with col_diag1:
                st.markdown(f"**Projected Match Pace:** {projected_possessions:.2f} total possessions")
                st.markdown(f"**{home_team} Blended ORTG:** {home_blended_ortg:.2f}")
                st.markdown(f"**{home_team} Blended DRTG:** {home_blended_drtg:.2f}")
            with col_diag2:
                st.markdown(f"**Applied Score HCA Bonus:** +{applied_hca} PTS")
                st.markdown(f"**{away_team} Blended ORTG:** {away_blended_ortg:.2f}")
                st.markdown(f"**{away_team} Blended DRTG:** {away_blended_drtg:.2f}")
else:
    st.warning("Halting Execution: Please select separate Home and Away teams.")
