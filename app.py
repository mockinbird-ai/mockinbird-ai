import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mockinbird AI", page_icon="🦅", layout="wide")
st.title("Mockinbird AI🏀")
st.markdown("Automated advanced analytics engine for global basketball matchups.")
st.markdown("---")

@st.cache_data
def fetch_complete_league_data(league):
    """
    Unblockable Global Registry Database for Mockinbird AI
    Contains full box-score matrices for every single franchise across all three leagues.
    """
    if league == "NBA":
        # Full 30-Team Advanced Performance Matrix
        return pd.DataFrame({
            "Team": [
                "Boston Celtics", "Oklahoma City Thunder", "Denver Nuggets", "Minnesota Timberwolves", 
                "Dallas Mavericks", "Milwaukee Bucks", "New York Knicks", "Los Angeles Lakers", 
                "Golden State Warriors", "Miami Heat", "Philadelphia 76ers", "Phoenix Suns", 
                "Indiana Pacers", "Cleveland Cavaliers", "Orlando Magic", "Sacramento Kings", 
                "New Orleans Pelicans", "Houston Rockets", "Chicago Bulls", "Atlanta Hawks", 
                "Brooklyn Nets", "Utah Jazz", "Toronto Raptors", "Memphis Grizzlies", 
                "San Antonio Spurs", "Portland Trail Blazers", "Charlotte Hornets", 
                "Washington Wizards", "Detroit Pistons", "Los Angeles Clippers"
            ],
            "GP": [82]*30,
            "PTS": [120.6, 120.1, 114.9, 113.0, 117.9, 119.4, 112.8, 118.0, 117.8, 110.1, 114.6, 116.2, 123.3, 112.6, 110.5, 116.6, 115.1, 114.3, 112.3, 118.3, 110.4, 115.7, 112.4, 105.8, 112.1, 106.4, 106.6, 113.7, 109.9, 115.6],
            "Opp_PTS": [109.2, 111.0, 109.6, 106.5, 115.6, 116.4, 108.2, 117.4, 115.2, 108.4, 111.5, 113.2, 120.2, 110.2, 108.4, 114.8, 110.7, 113.2, 113.7, 120.5, 113.3, 120.5, 118.8, 112.8, 118.6, 115.4, 116.8, 123.0, 119.0, 112.3],
            "FGA": [89.2, 89.7, 89.4, 85.1, 89.8, 88.5, 86.2, 88.9, 91.2, 85.8, 86.8, 87.3, 92.6, 87.2, 85.0, 90.5, 88.2, 90.1, 89.3, 91.7, 88.1, 91.1, 89.9, 87.5, 91.4, 88.9, 88.6, 92.2, 89.5, 86.3],
            "FTA": [22.0, 21.6, 20.4, 22.8, 23.1, 24.1, 21.5, 24.2, 20.1, 22.4, 25.4, 23.9, 21.2, 21.0, 24.5, 21.1, 22.1, 23.2, 21.4, 23.0, 20.9, 22.1, 21.3, 21.9, 20.2, 22.3, 20.8, 22.2, 22.1, 22.9],
            "ORB": [10.2, 8.8, 10.9, 9.7, 9.5, 9.4, 12.7, 8.2, 12.3, 9.3, 10.0, 10.2, 10.1, 10.0, 10.6, 10.8, 10.4, 11.4, 11.2, 12.5, 11.3, 11.9, 11.5, 10.4, 10.2, 11.3, 10.3, 9.4, 11.1, 10.1],
            "TOV": [11.9, 12.4, 12.6, 14.2, 12.5, 12.9, 12.2, 14.0, 14.3, 12.7, 13.0, 14.9, 12.9, 13.6, 14.7, 13.2, 13.0, 12.7, 12.2, 13.3, 13.0, 15.6, 14.0, 15.1, 15.1, 15.2, 13.8, 14.0, 15.2, 13.1],
            "Opp_FGA": [91.3, 92.1, 89.9, 87.2, 90.5, 90.1, 85.9, 91.5, 89.5, 87.3, 86.9, 87.1, 88.9, 86.8, 86.6, 88.5, 87.6, 86.4, 86.2, 90.4, 88.6, 88.3, 90.2, 87.8, 92.1, 89.1, 89.5, 90.8, 88.7, 87.5],
            "Opp_FTA": [19.8, 23.0, 21.9, 21.2, 21.2, 21.8, 20.5, 19.5, 22.4, 20.1, 24.1, 22.5, 23.9, 21.5, 21.8, 23.1, 22.5, 24.3, 22.7, 22.8, 22.3, 22.9, 24.0, 21.1, 20.9, 23.5, 23.2, 24.9, 23.6, 21.4],
            "Opp_ORB": [10.0, 11.5, 9.8, 9.5, 10.4, 10.1, 9.3, 10.2, 10.5, 9.7, 10.5, 10.3, 10.2, 9.8, 10.1, 10.2, 9.8, 10.1, 9.6, 10.9, 11.1, 10.5, 11.3, 10.8, 11.2, 11.0, 11.1, 10.8, 10.4, 10.5],
            "Opp_TOV": [12.0, 15.2, 12.2, 13.0, 13.1, 11.8, 13.2, 13.1, 13.0, 13.5, 13.9, 13.1, 14.0, 13.6, 14.9, 13.8, 14.1, 13.7, 14.0, 11.8, 12.3, 13.1, 13.7, 15.0, 13.5, 13.2, 13.6, 14.2, 12.2, 13.0],
            "MIN": [48.0]*30
        })
        
    elif league == "WNBA":
        # Full 12-Team Advanced Performance Matrix
        return pd.DataFrame({
            "Team": [
                "New York Liberty", "Las Vegas Aces", "Minnesota Lynx", "Connecticut Sun", 
                "Seattle Storm", "Indiana Fever", "Phoenix Mercury", "Atlanta Dream", 
                "Chicago Sky", "Washington Mystics", "Los Angeles Sparks", "Dallas Wings"
            ],
            "GP": [40]*12,
            "PTS": [86.5, 87.8, 82.3, 80.1, 83.4, 84.8, 81.5, 77.2, 78.8, 79.1, 78.4, 81.8],
            "Opp_PTS": [76.5, 81.2, 75.8, 73.4, 78.9, 87.3, 84.8, 80.3, 82.5, 82.7, 86.1, 86.9],
            "FGA": [68.2, 69.1, 66.5, 64.2, 70.3, 68.8, 66.2, 67.5, 69.0, 66.0, 66.9, 71.1],
            "FTA": [16.8, 19.5, 15.2, 18.1, 15.9, 17.5, 18.0, 18.2, 16.5, 15.9, 17.0, 19.1],
            "ORB": [8.1, 6.9, 7.8, 8.5, 9.4, 7.5, 6.5, 8.0, 10.1, 7.0, 7.2, 10.5],
            "TOV": [12.7, 11.2, 13.4, 12.1, 13.0, 14.4, 13.5, 12.9, 13.9, 14.1, 14.8, 12.3],
            "Opp_FGA": [69.4, 69.8, 67.2, 63.9, 71.0, 71.2, 69.1, 67.3, 68.4, 66.5, 69.3, 70.5],
            "Opp_FTA": [14.1, 15.5, 14.8, 16.0, 15.1, 17.0, 18.2, 16.9, 17.2, 18.0, 17.9, 19.5],
            "Opp_ORB": [7.9, 8.6, 8.1, 7.7, 9.1, 8.5, 8.2, 8.8, 9.5, 8.0, 9.0, 9.8],
            "Opp_TOV": [14.5, 12.6, 15.1, 14.9, 14.2, 11.9, 12.6, 12.2, 13.1, 14.5, 12.4, 12.8],
            "MIN": [40.0]*12
        })
        
    else:
        # EuroLeague: Full 18-Team Advanced Performance Matrix
        return pd.DataFrame({
            "Team": [
                "Real Madrid", "Panathinaikos", "AS Monaco", "Olympiacos", "FC Barcelona", 
                "Maccabi Tel Aviv", "Fenerbahce", "Efes Istanbul", "Virtus Bologna", 
                "Baskonia", "Partizan Belgrade", "Milano", "Valencia", "Zalgiris Kaunas", 
                "Bayern Munich", "Red Star Belgrade", "ASVEL Villeurbanne", "ALBA Berlin"
            ],
            "GP": [34]*18,
            "PTS": [88.2, 81.5, 81.9, 79.1, 82.4, 87.1, 84.6, 83.9, 80.2, 84.2, 81.9, 77.4, 76.9, 79.2, 77.7, 80.5, 77.3, 75.3],
            "Opp_PTS": [80.1, 77.2, 79.3, 74.8, 79.9, 86.3, 80.5, 82.1, 81.4, 84.5, 82.4, 77.1, 78.4, 79.8, 79.4, 80.9, 83.5, 86.2],
            "FGA": [65.4, 61.2, 63.1, 58.9, 62.8, 64.5, 62.1, 63.0, 60.1, 63.8, 59.8, 58.5, 59.2, 59.7, 59.9, 61.2, 59.4, 60.5],
            "FTA": [17.5, 19.0, 18.2, 17.1, 16.4, 19.8, 17.3, 18.1, 17.8, 16.9, 19.2, 16.0, 17.4, 16.8, 17.1, 16.5, 17.9, 15.2],
            "ORB": [9.8, 8.4, 10.5, 9.1, 8.9, 11.2, 9.4, 8.3, 8.1, 9.2, 8.5, 8.3, 9.4, 8.7, 9.5, 9.1, 8.9, 8.2],
            "TOV": [11.2, 12.4, 10.1, 11.9, 12.2, 11.5, 11.8, 11.0, 13.1, 12.1, 12.6, 12.0, 13.3, 12.5, 12.8, 12.3, 13.2, 14.5],
            "Opp_FGA": [66.1, 61.8, 62.5, 59.1, 63.0, 65.2, 60.9, 62.4, 61.5, 63.1, 59.1, 57.9, 58.3, 60.1, 60.4, 61.0, 60.2, 63.1],
            "Opp_FTA": [15.2, 16.5, 17.9, 16.0, 15.8, 16.9, 15.4, 16.7, 17.2, 18.1, 18.5, 16.2, 18.0, 17.1, 17.5, 17.9, 19.1, 17.4],
            "Opp_ORB": [9.2, 9.0, 9.7, 8.5, 9.1, 10.1, 8.8, 9.2, 9.5, 9.8, 9.2, 8.7, 9.1, 9.4, 9.8, 9.6, 9.9, 10.5],
            "Opp_TOV": [12.8, 12.1, 12.5, 13.2, 12.7, 12.0, 12.3, 11.9, 12.5, 12.1, 13.2, 12.4, 13.0, 12.1, 11.9, 13.5, 12.2, 11.8],
            "MIN": [40.0]*18
        })

def calculate_advanced_stats(df, league):
    # Normalized possession equations
    df["Possessions"] = df["FGA"] + (0.44 * df["FTA"]) - df["ORB"] + df["TOV"]
    df["Opp_Possessions"] = df["Opp_FGA"] + (0.44 * df["Opp_FTA"]) - df["Opp_ORB"] + df["Opp_TOV"]
    df["Avg_Poss"] = (df["Possessions"] + df["Opp_Possessions"]) / 2
    
    reg_min = 40.0 if league in ["WNBA", "EuroLeague"] else 48.0
    floor_min_factor = (df["MIN"] / 5.0) if df["MIN"].max() > 100 else df["MIN"]
    
    df["Pace"] = df["Avg_Poss"] / (floor_min_factor / reg_min)
    df["Offensive_Rating"] = (df["PTS"] / df["Possessions"]) * 100
    df["Defensive_Rating"] = (df["Opp_PTS"] / df["Opp_Possessions"]) * 100
    df["Net_Rating"] = df["Offensive_Rating"] - df["Defensive_Rating"]
    return df[["Team", "Pace", "Offensive_Rating", "Defensive_Rating", "Net_Rating"]]

# Sidebar Configuration Control Panel (Tap '>' on Mobile)
selected_league = st.sidebar.selectbox("Select Competition League", ["NBA", "WNBA", "EuroLeague"])

with st.spinner("Mockinbird AI compiling advanced analytics metrics..."):
    raw_data = fetch_complete_league_data(selected_league)
    processed_stats = calculate_advanced_stats(raw_data, selected_league)

st.subheader(f"📊 Dashboard: {selected_league}")
st.dataframe(processed_stats, use_container_width=True)

st.subheader("🔮 Predictive Matchup Engine")
col1, col2 = st.columns(2)
with col1: team_a = st.selectbox("Team A (Home)", processed_stats["Team"].unique(), index=0)
with col2: team_b = st.selectbox("Team B (Away)", processed_stats["Team"].unique(), index=1)

if team_a != team_b:
    if st.button("Run Simulation", type="primary"):
        sa, sb = processed_stats[processed_stats["Team"] == team_a], processed_stats[processed_stats["Team"] == team_b]
        diff = sa["Net_Rating"].values[0] - sb["Net_Rating"].values[0]
        prob_a = 1 / (1 + np.exp(-0.07 * diff))
        
        winner = team_a if prob_a > 0.5 else team_b
        conf = max(prob_a, 1 - prob_a) * 100
        
        st.markdown("---")
        st.header(f"🦅 Prediction: {winner} Wins")
        st.metric("Confidence Score", f"{conf:.2f}%")
        st.table(pd.concat([sa, sb]).set_index("Team"))
else:
    st.warning("Please pick two different teams.")
                    
