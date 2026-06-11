import streamlit as st
import numpy as np

# Set up page configurations
st.set_page_config(page_title="MiHoops Global Engine", page_icon="🏀", layout="centered")
st.title("🏀 MiHoops Multi-League Predictive Engine")
st.markdown("### Pure Strategic Formula Output Simulator")
st.markdown("---")

# =========================================================================
# HARDCODED GLOBAL LEAGUE REGISTRY
# Data source anchors: Basketball-Reference (NBA/WNBA) | RealGM (International)
# =========================================================================
GLOBAL_LEAGUE_DATABASE = {
    "NBA": {
        "avg_pace": 99.2, "avg_ortg": 115.6, "hca_bonus": 2.5,
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
        "avg_pace": 81.2, "avg_ortg": 102.4, "hca_bonus": 2.5,
        "teams": {
            "Atlanta Dream": {"ORTG": 96.7, "DRTG": 101.5, "PACE": 79.8},
            "Chicago Sky": {"ORTG": 98.2, "DRTG": 102.9, "PACE": 80.4},
            "Connecticut Sun": {"ORTG": 103.1, "DRTG": 94.8, "PACE": 78.9},
            "Dallas Wings": {"ORTG": 99.1, "DRTG": 107.4, "PACE": 81.7},
            "Indiana Fever": {"ORTG": 102.8, "DRTG": 106.1, "PACE": 82.9},
            "Las Vegas Aces": {"ORTG": 107.2, "DRTG": 99.1, "PACE": 82.4},
            "Los Angeles Sparks": {"ORTG": 95.9, "DRTG": 104.7, "PACE": 79.5},
            "Minnesota Lynx": {"ORTG": 105.4, "DRTG": 97.2, "PACE": 80.8},
            "New York Liberty": {"ORTG": 108.5, "DRTG": 96.4, "PACE": 80.1},
            "Phoenix Mercury": {"ORTG": 100.5, "DRTG": 103.4, "PACE": 82.1},
            "Seattle Storm": {"ORTG": 101.9, "DRTG": 98.0, "PACE": 81.5},
            "Washington Mystics": {"ORTG": 97.4, "DRTG": 102.8, "PACE": 80.2}
        }
    },
    "Spain (Liga ACB)": {
        "avg_pace": 76.4, "avg_ortg": 112.1, "hca_bonus": 2.5,
        "teams": {
            "FC Barcelona": {"ORTG": 116.2, "DRTG": 108.4, "PACE": 77.1},
            "Baskonia": {"ORTG": 111.9, "DRTG": 111.5, "PACE": 76.9},
            "Real Madrid": {"ORTG": 119.5, "DRTG": 105.2, "PACE": 75.8},
            "Unicaja Malaga": {"ORTG": 115.8, "DRTG": 107.2, "PACE": 76.5},
            "Valencia Basket": {"ORTG": 113.4, "DRTG": 110.1, "PACE": 78.0}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.5, "hca_bonus": 2.5,
        "teams": {
            "AS Monaco": {"ORTG": 117.2, "DRTG": 104.1, "PACE": 74.9},
            "LDLC ASVEL": {"ORTG": 112.1, "DRTG": 109.4, "PACE": 75.3},
            "Paris Basketball": {"ORTG": 115.4, "DRTG": 107.9, "PACE": 77.2}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 79.5, "avg_ortg": 106.8, "hca_bonus": 2.5,
        "teams": {
            "London Lions": {"ORTG": 114.8, "DRTG": 101.2, "PACE": 80.2},
            "Leicester Riders": {"ORTG": 108.2, "DRTG": 106.5, "PACE": 79.1},
            "Cheshire Phoenix": {"ORTG": 111.5, "DRTG": 106.9, "PACE": 80.0}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.2, "avg_ortg": 111.2, "hca_bonus": 2.5,
        "teams": {
            "FC Bayern Munich": {"ORTG": 118.1, "DRTG": 105.9, "PACE": 77.4},
            "ALBA Berlin": {"ORTG": 112.4, "DRTG": 110.2, "PACE": 79.1},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 106.8, "PACE": 76.9}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.1, "avg_ortg": 111.8, "hca_bonus": 2.5,
        "teams": {
            "Virtus Segafredo Bologna": {"ORTG": 117.9, "DRTG": 108.4, "PACE": 76.1},
            "EA7 Emporio Armani Milano": {"ORTG": 116.5, "DRTG": 106.2, "PACE": 75.1},
            "Germani Brescia": {"ORTG": 115.2, "DRTG": 108.1, "PACE": 76.5}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 77.9, "avg_ortg": 107.5, "hca_bonus": 2.5,
        "teams": {
            "SL Benfica": {"ORTG": 114.2, "DRTG": 103.5, "PACE": 77.2},
            "Sporting CP": {"ORTG": 111.5, "DRTG": 106.9, "PACE": 78.4},
            "FC Porto": {"ORTG": 112.8, "DRTG": 105.1, "PACE": 78.1}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.2, "avg_ortg": 113.4, "hca_bonus": 2.5,
        "teams": {
            "Fenerbahce Beko": {"ORTG": 119.2, "DRTG": 106.9, "PACE": 76.4},
            "Anadolu Efes": {"ORTG": 119.8, "DRTG": 107.5, "PACE": 76.8},
            "Pinar Karsiyaka": {"ORTG": 115.2, "DRTG": 112.4, "PACE": 78.1}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.5, "avg_ortg": 113.2, "hca_bonus": 2.5,
        "teams": {
            "Capitanes de Arecibo": {"ORTG": 116.8, "DRTG": 113.4, "PACE": 82.9},
            "Mets de Guaynabo": {"ORTG": 113.9, "DRTG": 112.0, "PACE": 83.2},
            "Osos de Manatí": {"ORTG": 114.5, "DRTG": 116.8, "PACE": 85.0}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.1, "avg_ortg": 109.8, "hca_bonus": 2.5,
        "teams": {
            "Canterbury Rams": {"ORTG": 114.2, "DRTG": 106.5, "PACE": 83.8},
            "Auckland Tuatara": {"ORTG": 112.1, "DRTG": 108.2, "PACE": 84.5},
            "Wellington Saints": {"ORTG": 114.9, "DRTG": 111.0, "PACE": 85.2}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.2, "avg_ortg": 110.1, "hca_bonus": 2.5,
        "teams": {
            "Panathinaikos": {"ORTG": 120.4, "DRTG": 103.2, "PACE": 73.9},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 73.5},
            "Promitheas Patras": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 76.0}
        }
    },
    "Japan (B.League)": {
        "avg_pace": 73.5, "avg_ortg": 108.2, "hca_bonus": 3.0,
        "teams": {
            "Chiba Jets": {"ORTG": 114.1, "DRTG": 105.2, "PACE": 74.8},
            "Alvark Tokyo": {"ORTG": 115.5, "DRTG": 102.1, "PACE": 72.1},
            "Ryukyu Golden Kings": {"ORTG": 112.8, "DRTG": 106.4, "PACE": 73.9}
        }
    },
    "China (CBA)": {
        "avg_pace": 88.2, "avg_ortg": 110.4, "hca_bonus": 3.0,
        "teams": {
            "Liaoning Flying Leopards": {"ORTG": 115.2, "DRTG": 104.1, "PACE": 87.5},
            "Guangdong Southern Tigers": {"ORTG": 117.8, "DRTG": 109.2, "PACE": 89.9},
            "Xinjiang Flying Tigers": {"ORTG": 113.4, "DRTG": 106.1, "PACE": 88.1}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 82.8, "avg_ortg": 111.4, "hca_bonus": 2.5,
        "teams": {
            "Niagara River Lions": {"ORTG": 114.5, "DRTG": 109.2, "PACE": 82.1},
            "Vancouver Bandits": {"ORTG": 113.1, "DRTG": 110.8, "PACE": 83.5},
            "Winnipeg Sea Bears": {"ORTG": 113.8, "DRTG": 115.2, "PACE": 84.6}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.2, "avg_ortg": 105.4, "hca_bonus": 2.5,
        "teams": {
            "Flyers Wels": {"ORTG": 107.5, "DRTG": 104.9, "PACE": 76.5},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 75.9},
            "Swans Gmunden": {"ORTG": 110.2, "DRTG": 102.1, "PACE": 75.8}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 77.4, "avg_ortg": 108.1, "hca_bonus": 2.5,
        "teams": {
            "ERA Nymburk": {"ORTG": 116.5, "DRTG": 101.4, "PACE": 78.1},
            "Sluneta Usti nad Labem": {"ORTG": 110.2, "DRTG": 109.1, "PACE": 77.1},
            "BK Opava": {"ORTG": 109.4, "DRTG": 107.2, "PACE": 76.9}
        }
    },
    "Israel (Winner League)": {
        "avg_pace": 78.5, "avg_ortg": 112.4, "hca_bonus": 2.5,
        "teams": {
            "Maccabi Tel Aviv": {"ORTG": 119.5, "DRTG": 109.1, "PACE": 79.4},
            "Hapoel Tel Aviv": {"ORTG": 116.8, "DRTG": 108.5, "PACE": 79.1},
            "Hapoel Jerusalem": {"ORTG": 112.1, "DRTG": 106.2, "PACE": 77.2}
        }
    },
    "Belgium (BNXT League)": {
        "avg_pace": 75.9, "avg_ortg": 107.8, "hca_bonus": 2.5,
        "teams": {
            "Filou Oostende": {"ORTG": 114.2, "DRTG": 102.1, "PACE": 75.1},
            "Telenet Giants Antwerp": {"ORTG": 109.5, "DRTG": 106.4, "PACE": 76.2},
            "Limburg United": {"ORTG": 106.8, "DRTG": 105.9, "PACE": 74.8}
        }
    }
}

# =========================================================================
# COMPONENT CONTROL SELECTION (SIDEBAR)
# =========================================================================
selected_league_name = st.sidebar.selectbox("Active Competition", sorted(GLOBAL_LEAGUE_DATABASE.keys()))

LEAGUE_CONTEXT = GLOBAL_LEAGUE_DATABASE[selected_league_name]
LEAGUE_AVG_PACE = LEAGUE_CONTEXT["avg_pace"]
LEAGUE_AVG_ORTG = LEAGUE_CONTEXT["avg_ortg"]
HCA_BONUS = LEAGUE_CONTEXT["hca_bonus"]
TEAM_DATABASE = LEAGUE_CONTEXT["teams"]

st.sidebar.markdown("---")
st.sidebar.markdown("**Data Lineage tracking:**")
if selected_league_name in ["NBA", "WNBA"]:
    st.sidebar.caption(" Sourced via Basketball-Reference.com")
else:
    st.sidebar.caption(" Sourced via RealGM.com International Matrix")

# =========================================================================
# CLEAN MATCHUP INTERFACE
# =========================================================================
st.subheader(f" Matchup Design Engine: {selected_league_name}")

col1, col2 = st.columns(2)
with col1:
    home_team = st.selectbox("Select Home Team (🏡)", sorted(TEAM_DATABASE.keys()), index=0)
    h_ortg = float(TEAM_DATABASE[home_team]["ORTG"])
    h_drtg = float(TEAM_DATABASE[home_team]["DRTG"])
    h_pace = float(TEAM_DATABASE[home_team]["PACE"])

with col2:
    away_team = st.selectbox("Select Away Team (✈️)", sorted(TEAM_DATABASE.keys()), index=1 if len(TEAM_DATABASE) > 1 else 0)
    a_ortg = float(TEAM_DATABASE[away_team]["ORTG"])
    a_drtg = float(TEAM_DATABASE[away_team]["DRTG"])
    a_pace = float(TEAM_DATABASE[away_team]["PACE"])

st.markdown("---")

# Initialize session state variables to hold data when updating inputs
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
    st.session_state.p_home_ht = 0.0
    st.session_state.p_away_ht = 0.0
    st.session_state.p_home_ft = 0.0
    st.session_state.p_away_ft = 0.0
    st.session_state.m_spread = 0.0
    st.session_state.game_pace = 0.0
    st.session_state.last_matchup = ""

current_matchup_key = f"{selected_league_name}_{home_team}_{away_team}"

# Reset if matchup choices change
if st.session_state.last_matchup != current_matchup_key:
    st.session_state.calculated = False
    st.session_state.last_matchup = current_matchup_key

# Main Action Trigger
run_simulation = st.button("⚡ Run Predictive Simulation", type="primary", use_container_width=True)

if run_simulation:
    if home_team == away_team:
        st.warning("Please select two different teams to compute projections.")
        st.session_state.calculated = False
    else:
        # Expected pace formulation
        predicted_pace = (h_pace + a_pace) - LEAGUE_AVG_PACE
        st.session_state.game_pace = predicted_pace
        
        # Logistical efficiency formula mapping
        st.session_state.p_home_ft = ((h_ortg + a_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100) + HCA_BONUS
        st.session_state.p_away_ft = ((a_ortg + h_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100)
        
        # Splitting out half time and point margins
        st.session_state.p_home_ht = st.session_state.p_home_ft * 0.50
        st.session_state.p_away_ht = st.session_state.p_away_ft * 0.50
        st.session_state.m_spread = st.session_state.p_away_ft - st.session_state.p_home_ft
        st.session_state.calculated = True

st.markdown("---")

# =========================================================================
# DISPLAY LOGIC AREA
# =========================================================================
if st.session_state.calculated:
    # 1. WINNER IDENTIFICATION HEADLINER
    home_win = st.session_state.p_home_ft > st.session_state.p_away_ft
    winner_name = home_team if home_win else away_team
    icon = "🏡" if home_win else "✈️"
    
    st.markdown(f"### 🏆 Projected Winner: {icon} **{winner_name}**")
    st.caption(f"Calculated Game Pace: **{st.session_state.game_pace:.1f}** Possessions")
    st.markdown("---")

    # 2. HALF TIME SCORE PROJECTIONS BLOCK
    st.subheader("⏱️ Predicted Half-Time (HT) Scores")
    col_ht1, col_ht2 = st.columns(2)
    col_ht1.metric(f"🏡 {home_team} (HT)", f"{st.session_state.p_home_ht:.1f}")
    col_ht2.metric(f"✈️ {away_team} (HT)", f"{st.session_state.p_away_ht:.1f}")
    
    st.markdown("---")

    # 3. FINAL FULL TIME SCORE PROJECTIONS BLOCK
    st.subheader("🏁 Predicted Final (FT) Scores")
    col_ft1, col_ft2 = st.columns(2)
    col_ft1.metric(f"🏡 {home_team} (Final)", f"{st.session_state.p_home_ft:.1f}")
    col_ft2.metric(f"✈️ {away_team} (Final)", f"{st.session_state.p_away_ft:.1f}")

    st.markdown("---")
    
    # 4. POINT SPREAD PROJECTIONS
    st.subheader("📊 Point Spread Projections")
    sign = "" if st.session_state.m_spread < 0 else "+"
    st.metric(label=f"Model Spread Line (Relative to {home_team})", value=f"{st.session_state.m_spread:.1f}")
    st.caption(f"Interpretation: Your model favors **{home_team if st.session_state.m_spread < 0 else away_team}** by **{abs(st.session_state.m_spread):.1f}** points.")
    
    st.markdown("---")

    # 5. LIVE BOOKIE COMPARATOR MATRIX
    st.subheader("🎯 Step 5: Edge Finder Matrix")
    bookie_line = st.number_input(f"Sportsbook Market Line: {home_team} Spread", value=float(np.round(st.session_state.m_spread)), step=0.5)
    
    spread_differential = bookie_line - st.session_state.m_spread
    
    st.markdown("#### Optimal Play Recommendation:")
    if spread_differential > 1.0:
        st.success(f"🟢 **Bet {home_team} ({bookie_line})** | Bookie margin leaves an edge for the home unit.")
    elif spread_differential < -1.0:
        st.success(f"🟢 **Bet {away_team} (+{abs(bookie_line)})** | Valuation charts show variance favoring the away side.")
    else:
        st.info(f"❌ **Pass / Do Not Bet** | The bookie's line perfectly matches your model calculation.")
else:
    st.info("💡 Adjust your matchups above and click **Run Predictive Simulation** to calculate values.")
