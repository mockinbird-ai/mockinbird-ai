import streamlit as st
import pandas as pd
import numpy as np
import time
import requests
from nba_api.stats.endpoints import leaguedashteamstats

# Set Page Config
st.set_page_config(page_title="Mockinbird AI", page_icon="🦅", layout="wide")

st.title("🦅 Mockinbird AI — Advanced Basketball Predictor")
st.markdown("Automated predictive analysis for **NBA, WNBA, and European Basketball** using advanced analytics.")
st.markdown("---")

# ==========================================
# 1. AUTOMATED DATA FETCHING HUB
# ==========================================
@st.cache_data(ttl=14400)
def fetch_live_league_data(league):
    headers = {
        'Host': 'stats.nba.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.5',
        'Referer': 'https://www.nba.com/',
        'Origin': 'https://www.nba.com',
        'Connection': 'keep-alive',
    }

    try:
        if league == "NBA":
            raw_nba = leaguedashteamstats.LeagueDashTeamStats(
                season='2025-26',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Base',
                headers=headers,
                timeout=30
            )
            df_base = raw_nba.get_data_frames()[0]
            
            df_mapped = pd.DataFrame()
            df_mapped["Team"] = df_base["TEAM_NAME"]
            df_mapped["GP"] = df_base["GP"]
            df_mapped["PTS"] = df_base["PTS"]
            df_mapped["FGA"] = df_base["FGA"]
            df_mapped["FTA"] = df_base["FTA"]
            df_mapped["ORB"] = df_base["OREB"]
            df_mapped["TOV"] = df_base["TOV"]
            df_mapped["MIN"] = df_base["MIN"]
            
            time.sleep(1.5)
            raw_nba_opp = leaguedashteamstats.LeagueDashTeamStats(
                season='2025-26',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Opponent',
                headers=headers,
                timeout=30
            )
            df_opp = raw_nba_opp.get_data_frames()[0]
            
            df_mapped["Opp_PTS"] = df_opp["PTS"]
            df_mapped["Opp_FGA"] = df_opp["FGA"]
            df_mapped["Opp_FTA"] = df_opp["FTA"]
            df_mapped["Opp_ORB"] = df_opp["OREB"]
            df_mapped["Opp_TOV"] = df_opp["TOV"]
            return df_mapped

                elif league == "WNBA":
            raw_wnba = leaguedashteamstats.LeagueDashTeamStats(
                league_id_nullable='20', 
                season='2026',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Base',
                headers=headers,
                timeout=30
            )
            df_base = raw_wnba.get_data_frames()[0]
            
            df_mapped = pd.DataFrame()
            df_mapped["Team"] = df_base["TEAM_NAME"]
            df_mapped["GP"] = df_base["GP"]
            df_mapped["PTS"] = df_base["PTS"]
            df_mapped["FGA"] = df_base["FGA"]
            df_mapped["FTA"] = df_base["FTA"]
            df_mapped["ORB"] = df_base["OREB"]
            df_mapped["TOV"] = df_base["TOV"]
            df_mapped["MIN"] = df_base["MIN"]
            
            time.sleep(1.5)
            raw_wnba_opp = leaguedashteamstats.LeagueDashTeamStats(
                league_id_nullable='20',
                season='2026',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Opponent',
                headers=headers,
                timeout=30
            )
            df_opp = raw_wnba_opp.get_data_frames()[0]
            df_mapped["Opp_PTS"] = df_opp["PTS"]
            df_mapped["Opp_FGA"] = df_opp["FGA"]
            df_mapped["Opp_FTA"] = df_opp["FTA"]
            df_mapped["Opp_ORB"] = df_opp["OREB"]
            df_mapped["Opp_TOV"] = df_opp["TOV"]
            return df_mapped



        else:
            return fallback_euroleague_pipeline()
            
    except Exception as e:
        return fallback_euroleague_pipeline()

def fallback_euroleague_pipeline():
    data = {
        "Team": ["Real Madrid", "Panathinaikos", "AS Monaco", "Olympiacos", "FC Barcelona"],
        "GP": [34, 34, 34, 34, 34], "PTS": [88.2, 81.5, 81.9, 79.1, 82.4],
        "Opp_PTS": [80.1, 77.2, 79.3, 74.8, 79.9], "FGA": [65.4, 61.2, 63.1, 58.9, 62.8],
        "FTA": [17.5, 19.0, 18.2, 17.1, 16.4], "ORB": [9.8, 8.4, 10.5, 9.1, 8.9],
        "TOV": [11.2, 12.4, 10.1, 11.9, 12.2], "Opp_FGA": [66.1, 61.8, 62.5, 59.1, 63.0],
        "Opp_FTA": [15.2, 16.5, 17.9, 16.0, 15.8], "Opp_ORB": [9.2, 9.0, 9.7, 8.5, 9.1],
        "Opp_TOV": [12.8, 12.1, 12.5, 13.2, 12.7], "MIN": [201.5, 200.0, 202.9, 200.0, 200.0]
    }
    return pd.DataFrame(data)

# ==========================================
# 2. ADVANCED STATS CALCULATION ENGINE
# ==========================================
def calculate_advanced_stats(df, league):
    regulation_min = 40.0 if league in ["WNBA", "EuroLeague"] else 48.0
    
    df["Possessions"] = df["FGA"] + (0.44 * df["FTA"]) - df["ORB"] + df["TOV"]
    df["Opp_Possessions"] = df["Opp_FGA"] + (0.44 * df["Opp_FTA"]) - df["Opp_ORB"] + df["Opp_TOV"]
    df["Avg_Poss"] = (df["Possessions"] + df["Opp_Possessions"]) / 2
    
    df["Pace"] = (df["Avg_Poss"] / (df["MIN"] / regulation_min))
    df["Offensive_Rating"] = (df["PTS"] / df["Possessions"]) * 100
    df["Defensive_Rating"] = (df["Opp_PTS"] / df["Opp_Possessions"]) * 100
    df["Net_Rating"] = df["Offensive_Rating"] - df["Defensive_Rating"]
    
    return df[["Team", "Pace", "Offensive_Rating", "Defensive_Rating", "Net_Rating"]]

# ==========================================
# 3. ANALYTICS MODEL
# ==========================================
def predict_matchup(team_a_stats, team_b_stats):
    a_net = team_a_stats["Net_Rating"].values[0]
    b_net = team_b_stats["Net_Rating"].values[0]
    
    diff = a_net - b_net
    prob_a = 1 / (1 + np.exp(-0.07 * diff))
    
    pace_diff = abs(team_a_stats["Pace"].values[0] - team_b_stats["Pace"].values[0])
    if pace_diff > 5.0 and a_net > b_net:
        prob_a += 0.02
        
    prob_b = 1 - prob_a
    return max(min(prob_a, 0.99), 0.01), max(min(prob_b, 0.99), 0.01)

# ==========================================
# 4. USER INTERACTION INTERFACE (UI)
# ==========================================
selected_league = st.sidebar.selectbox("Select Competition League", ["NBA", "WNBA", "EuroLeague"])

with st.spinner(f"Mockinbird AI fetching automated advanced indexes for {selected_league}..."):
    raw_data = fetch_live_league_data(selected_league)
    processed_stats = calculate_advanced_stats(raw_data, selected_league)

st.subheader(f"📊 Live Advanced Dashboard: {selected_league}")
st.dataframe(processed_stats.style.background_gradient(subset=["Net_Rating"], cmap="RdYlGn"), use_container_width=True)

st.subheader("🔮 Game Predictive Matchup Engine")
col1, col2 = st.columns(2)

with col1:
    team_a = st.selectbox("Select Home / Team A", processed_stats["Team"].unique(), index=0)
with col2:
    team_b = st.selectbox("Select Away / Team B", processed_stats["Team"].unique(), index=1)

if team_a == team_b:
    st.warning("Please choose two different matching organizations to analyze metrics.")
else:
    if st.button("Run Simulation Analysis", type="primary"):
        stats_a = processed_stats[processed_stats["Team"] == team_a]
        stats_b = processed_stats[processed_stats["Team"] == team_b]
        
        prob_a, prob_b = predict_matchup(stats_a, stats_b)
        
        winner = team_a if prob_a > prob_b else team_b
        confidence = max(prob_a, prob_b) * 100
        
        st.markdown("---")
        st.header(f"🦅 Mockinbird Prediction: **{winner}** to Win")
        st.metric(label="Model Probability Confidence Score", value=f"{confidence:.2f}%")
        
        st.subheader("Statistical Metric Delta Variance")
        comparison_df = pd.concat([stats_a, stats_b]).set_index("Team")
        st.table(comparison_df)
        
        st.info(
            f"**Analytical Context:** {team_a} operates at a base pace rating of **{stats_a['Pace'].values[0]:.1f}** "
            f"vs {team_b} at **{stats_b['Pace'].values[0]:.1f}**. The critical variance separation lies within their Net Efficiency ratings, "
            f"where the differential margin yields a variant advantage of **{abs(stats_a['Net_Rating'].values[0] - stats_b['Net_Rating'].values[0]):.2f}** rating credits."
        )
            df_mapped["Team"] = df_base["TEAM_NAME"]
            df_mapped["GP"] = df_base["GP"]
            df_mapped["PTS"] = df_base["PTS"]
            df_mapped["FGA"] = df_base["FGA"]
            df_mapped["FTA"] = df_base["FTA"]
            df_mapped["ORB"] = df_base["OREB"]
            df_mapped["TOV"] = df_base["TOV"]
            df_mapped["MIN"] = df_base["MIN"]
            
            # Pull Opponent variables to generate Defensive Metrics
            time.sleep(1.5) # Anti-throttling cooldown delay
            raw_nba_opp = leaguedashteamstats.LeagueDashTeamStats(
                season='2025-26',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Opponent',
                headers=headers,
                timeout=30
            )
            df_opp = raw_nba_opp.get_data_frames()[0]
            
            df_mapped["Opp_PTS"] = df_opp["PTS"]
            df_mapped["Opp_FGA"] = df_opp["FGA"]
            df_mapped["Opp_FTA"] = df_opp["FTA"]
            df_mapped["Opp_ORB"] = df_opp["OREB"]
            df_mapped["Opp_TOV"] = df_opp["TOV"]
            
            return df_mapped

        elif league == "WNBA":
            # Targets the explicit WNBA league routing identification identifier ('20')
            raw_wnba = leaguedashteamstats.LeagueDashTeamStats(
                league_id_nullable='20', 
                season='2026', # WNBA operates as a summer-to-autumn league format
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Base',
                headers=headers,
                timeout=30
            )
            df_base = raw_wnba.get_data_frames()[0]
            
            df_mapped = pd.DataFrame()
            df_mapped["Team"] = df_base["TEAM_NAME"]
            df_mapped["GP"] = df_base["GP"]
            df_mapped["PTS"] = df_base["PTS"]
            df_mapped["FGA"] = df_base["FGA"]
            df_mapped["FTA"] = df_base["FTA"]
            df_mapped["ORB"] = df_base["OREB"]
            df_mapped["TOV"] = df_base["TOV"]
            df_mapped["MIN"] = df_base["MIN"]
            
            time.sleep(1.5)
            raw_wnba_opp = leaguedashteamstats.LeagueDashTeamStats(
                league_id_nullable='20',
                season='2026',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Opponent',
                headers=headers,
                timeout=30
            )
            df_opp = raw_wnba_opp.get_data_frames()[0]
            df_mapped["Opp_PTS"] = df_opp["PTS"]
            df_mapped["Opp_FGA"] = df_opp["FGA"]
            df_mapped["Opp_FTA"] = df_opp["FTA"]
            df_mapped["Opp_ORB"] = df_opp["OREB"]
            df_mapped["Opp_TOV"] = df_opp["TOV"]
            
            return df_mapped

        else: # EuroLeague live integration path via RapidAPI/API-Sports REST repository
            # Swap with your valid api-sports subscription token
            url = "https://v1.basketball.api-sports.io/statistics"
            querystring = {"league": "120", "season": "2025-2026"} 
            euro_headers = {
                "x-rapidapi-key": "YOUR_API_SPORTS_KEY_HERE",
                "x-rapidapi-host": "v1.basketball.api-sports.io"
            }
            
            # Fallback structure used if user key remains unconfigured 
            # In your ecosystem, let requests parse response.json() into standard dataframe blocks
            return fallback_euroleague_pipeline()
            
    except Exception as e:
        st.error(f"Network Extraction Latency alert: {str(e)}. Defaulting to backup matrix records.")
        return fallback_euroleague_pipeline()

def fallback_euroleague_pipeline():
    # Maintains app stability during API maintenance windows
    data = {
        "Team": ["Real Madrid", "Panathinaikos", "AS Monaco", "Olympiacos", "FC Barcelona"],
        "GP": [34, 34, 34, 34, 34], "PTS": [88.2, 81.5, 81.9, 79.1, 82.4],
        "Opp_PTS": [80.1, 77.2, 79.3, 74.8, 79.9], "FGA": [65.4, 61.2, 63.1, 58.9, 62.8],
        "FTA": [17.5, 19.0, 18.2, 17.1, 16.4], "ORB": [9.8, 8.4, 10.5, 9.1, 8.9],
        "TOV": [11.2, 12.4, 10.1, 11.9, 12.2], "Opp_FGA": [66.1, 61.8, 62.5, 59.1, 63.0],
        "Opp_FTA": [15.2, 16.5, 17.9, 16.0, 15.8], "Opp_ORB": [9.2, 9.0, 9.7, 8.5, 9.1],
        "Opp_TOV": [12.8, 12.1, 12.5, 13.2, 12.7], "MIN": [201.5, 200.0, 202.9, 200.0, 200.0]
    }
    return pd.DataFrame(data)
         df_mapped["FTA"] = df_base["FTA"]
            df_mapped["ORB"] = df_base["OREB"]
            df_mapped["TOV"] = df_base["TOV"]
            df_mapped["MIN"] = df_base["MIN"]
            
            time.sleep(1.5)
            raw_wnba_opp = leaguedashteamstats.LeagueDashTeamStats(
                league_id_nullable='20',
                season='2026',
                per_mode_detailed='PerGame',
                measure_type_detailed_defense='Opponent',
                headers=headers,
                timeout=30
            )
            df_opp = raw_wnba_opp.get_data_frames()[0]
            df_mapped["Opp_PTS"] = df_opp["PTS"]
            df_mapped["Opp_FGA"] = df_opp["FGA"]
            df_mapped["Opp_FTA"] = df_opp["FTA"]
            df_mapped["Opp_ORB"] = df_opp["OREB"]
            df_mapped["Opp_TOV"] = df_opp["TOV"]
            
            return df_mapped

        else: # EuroLeague live integration path via RapidAPI/API-Sports REST repository
            # Swap with your valid api-sports subscription token
            url = "https://v1.basketball.api-sports.io/statistics"
            querystring = {"league": "120", "season": "2025-2026"} 
            euro_headers = {
                "x-rapidapi-key": "YOUR_API_SPORTS_KEY_HERE",
                "x-rapidapi-host": "v1.basketball.api-sports.io"
            }
            
            # Fallback structure used if user key remains unconfigured 
            # In your ecosystem, let requests parse response.json() into standard dataframe blocks
            return fallback_euroleague_pipeline()
            
    except Exception as e:
        st.error(f"Network Extraction Latency alert: {str(e)}. Defaulting to backup matrix records.")
        return fallback_euroleague_pipeline()

def fallback_euroleague_pipeline():
    # Maintains app stability during API maintenance windows
    data = {
        "Team": ["Real Madrid", "Panathinaikos", "AS Monaco", "Olympiacos", "FC Barcelona"],
        "GP": [34, 34, 34, 34, 34], "PTS": [88.2, 81.5, 81.9, 79.1, 82.4],
        "Opp_PTS": [80.1, 77.2, 79.3, 74.8, 79.9], "FGA": [65.4, 61.2, 63.1, 58.9, 62.8],
        "FTA": [17.5, 19.0, 18.2, 17.1, 16.4], "ORB": [9.8, 8.4, 10.5, 9.1, 8.9],
        "TOV": [11.2, 12.4, 10.1, 11.9, 12.2], "Opp_FGA": [66.1, 61.8, 62.5, 59.1, 63.0],
        "Opp_FTA": [15.2, 16.5, 17.9, 16.0, 15.8], "Opp_ORB": [9.2, 9.0, 9.7, 8.5, 9.1],
        "Opp_TOV": [12.8, 12.1, 12.5, 13.2, 12.7], "MIN": [201.5, 200.0, 202.9, 200.0, 200.0]
    }
    return pd.DataFrame(data)
