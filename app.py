import streamlit as st
import pandas as pd
import numpy as np

# 1. Setup Page configuration
st.set_page_config(page_title="MiHoops Dashboard", page_icon="🏀", layout="wide")
st.title("🏀MiHoops")
st.markdown("Automated predictive analysis using official global basketball standing hierarchies.")
st.markdown("---")

# 2. Hardcoded Solid Data Registry
def fetch_complete_league_data(league_selection):
    # ==================== NBA REGISTRY (30 TEAMS) ====================
    if league_selection == "NBA":
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
            "GP": [82]*30, "PTS": [120.6, 120.1, 114.9, 113.0, 117.9, 119.4, 112.8, 118.0, 117.8, 110.1, 114.6, 116.2, 123.3, 112.6, 110.5, 116.6, 115.1, 114.3, 112.3, 118.3, 110.4, 115.7, 112.4, 105.8, 112.1, 106.4, 106.6, 113.7, 109.9, 115.6],
            "Opp_PTS": [109.2, 111.0, 109.6, 106.5, 115.6, 116.4, 108.2, 117.4, 115.2, 108.4, 111.5, 113.2, 120.2, 110.2, 108.4, 114.8, 110.7, 113.2, 113.7, 120.5, 113.3, 120.5, 118.8, 112.8, 118.6, 115.4, 116.8, 123.0, 119.0, 112.3],
            "FGA": [89.2, 89.7, 89.4, 85.1, 89.8, 88.5, 86.2, 88.9, 91.2, 85.8, 86.8, 87.3, 92.6, 87.2, 85.0, 90.5, 88.2, 90.1, 89.3, 91.7, 88.1, 91.1, 89.9, 87.5, 91.4, 88.9, 88.6, 92.2, 89.5, 86.3],
            "FTA": [22.0, 21.6, 20.4, 22.8, 23.1, 24.1, 21.5, 24.2, 20.1, 22.4, 25.4, 23.9, 21.2, 21.0, 24.5, 21.1, 22.1, 23.2, 21.4, 23.0, 20.9, 22.1, 21.3, 21.9, 20.2, 22.3, 20.8, 22.2, 22.1, 22.9],
            "ORB": [10.2, 8.8, 10.9, 9.7, 9.5, 9.4, 12.7, 8.2, 12.3, 9.3, 10.0, 10.2, 10.1, 10.0, 10.6, 10.8, 10.4, 11.4, 11.2, 12.5, 11.3, 11.9, 11.5, 10.4, 10.2, 11.3, 10.3, 9.4, 11.1, 10.1],
            "TOV": [11.9, 12.4, 12.6, 14.2, 12.5, 12.9, 12.2, 14.0, 14.3, 12.7, 13.0, 14.9, 12.9, 13.6, 14.7, 13.2, 13.0, 12.7, 12.2, 13.3, 13.0, 15.6, 14.0, 15.1, 15.1, 15.2, 13.8, 14.0, 15.2, 13.1],
            "Opp_FGA": [91.3, 92.1, 89.9, 87.2, 90.5, 90.1, 85.9, 91.5, 89.5, 87.3, 86.9, 87.1, 88.9, 86.8, 86.6, 88.5, 87.6, 86.4, 86.2, 90.4, 88.6, 88.3, 90.2, 87.8, 92.1, 89.1, 89.5, 90.8, 88.7, 87.5],
            "Opp_FTA": [19.8, 23.0, 21.9, 21.2, 21.2, 21.8, 20.5, 19.5, 22.4, 20.1, 24.1, 22.5, 23.9, 21.5, 21.8, 23.1, 22.5, 24.3, 22.7, 22.8, 22.3, 22.9, 24.0, 21.1, 20.9, 23.5, 23.2, 24.9, 23.6, 21.4],
            "Opp_ORB": [10.0, 11.5, 9.8, 9.5, 10.4, 10.1, 9.3, 10.2, 10.5, 9.7, 10.5, 10.3, 10.2, 9.8, 10.1, 10.2, 9.8, 10.1, 9.6, 10.9, 11.1, 10.5, 11.3, 10.8, 11.2, 11.0, 11.1, 10.8, 10.4, 10.5],
            "Opp_TOV": [12.0, 15.2, 12.2, 13.0, 13.1, 11.8, 13.2, 13.1, 13.0, 13.5, 13.9, 13.1, 14.0, 13.6, 14.7, 13.8, 14.1, 13.7, 14.0, 11.8, 12.3, 13.1, 13.7, 15.0, 13.5, 13.2, 13.6, 14.2, 12.2, 13.0],
            "MIN": [48.0]*30
        })
        
    # ==================== WNBA REGISTRY ====================
    elif league_selection == "WNBA":
        return pd.DataFrame({
            "Team": [
                "Minnesota Lynx", "Las Vegas Aces", "Atlanta Dream", "Phoenix Mercury",
                "New York Liberty", "Indiana Fever", "Seattle Storm", "Golden State Valkyries",
                "Los Angeles Sparks", "Washington Mystics", "Connecticut Sun", "Chicago Sky", "Dallas Wings"
            ],
            "GP": [44]*13, 
            "PTS": [86.1, 83.6, 84.4, 82.8, 84.4, 84.9, 82.1, 77.7, 85.7, 77.1, 75.8, 75.8, 81.7],
            "Opp_PTS": [76.7, 80.7, 76.8, 80.1, 80.3, 81.5, 80.1, 76.3, 88.2, 81.6, 86.0, 85.8, 88.0],
            "FGA": [68.2, 69.1, 67.5, 66.2, 68.2, 68.8, 70.3, 67.5, 66.9, 66.0, 64.2, 69.0, 71.1],
            "FTA": [16.8, 19.5, 18.2, 18.0, 16.8, 17.5, 15.9, 17.0, 17.0, 15.9, 18.1, 16.5, 19.1],
            "ORB": [8.1, 6.9, 8.0, 6.5, 8.1, 7.5, 9.4, 8.0, 7.2, 7.0, 8.5, 10.1, 10.5],
            "TOV": [12.7, 11.2, 12.9, 13.5, 12.7, 14.4, 13.0, 13.1, 14.8, 14.1, 12.1, 13.9, 12.3],
            "Opp_FGA": [69.4, 69.8, 67.3, 69.1, 69.4, 71.2, 71.0, 68.0, 69.3, 66.5, 63.9, 68.4, 70.5],
            "Opp_FTA": [14.1, 15.5, 16.9, 18.2, 14.1, 17.0, 15.1, 16.1, 17.9, 18.0, 16.0, 17.2, 19.5],
            "Opp_ORB": [7.9, 8.6, 8.8, 8.2, 7.9, 8.5, 9.1, 8.5, 9.0, 8.0, 7.7, 9.5, 9.8],
            "Opp_TOV": [14.5, 12.6, 12.2, 12.6, 14.5, 11.9, 14.2, 12.9, 12.4, 14.5, 14.9, 13.1, 12.8],
            "MIN": [40.0]*13
        })

    # ==================== PUERTO RICO: BSN (12 TEAMS) ====================
    elif league_selection == "Puerto Rico: BSN":
        return pd.DataFrame({
            "Team": [
                "San German", "Capitanes de Arecibo", "Aguada Santeros", "Indios de Mayaguez",
                "Leones De Ponce", "Piratas de Quebradillas", "Criollos de Caguas", "Vaqueros de Bayamon",
                "Cangrejeros", "Gigantes de Carolina", "Mets de Guaynabo", "Osos de Manati"
            ],
            "GP": [36]*12,
            "PTS": [89.4, 92.5, 87.1, 86.8, 88.0, 85.3, 91.2, 87.5, 88.3, 89.1, 88.6, 91.0],
            "Opp_PTS": [84.2, 88.1, 89.4, 89.0, 92.4, 89.1, 88.5, 87.9, 86.5, 87.2, 89.3, 94.2],
            "FGA": [66.4]*12, "FTA": [19.5]*12, "ORB": [9.2]*12, "TOV": [13.1]*12,
            "Opp_FGA": [65.9]*12, "Opp_FTA": [18.8]*12, "Opp_ORB": [9.0]*12, "Opp_TOV": [12.8]*12,
            "MIN": [40.0]*12
        })

    # ==================== NEW ZEALAND: NBL (11 TEAMS) ====================
    elif league_selection == "New Zealand: NBL":
        return pd.DataFrame({
            "Team": [
                "Auckland Huskies", "Southland Sharks", "Canterbury Rams", "Wellington Saints",
                "Franklin Bulls", "Otago Nuggets", "Manawatu Jets", "Whai Tauranga",
                "Nelson Giants", "Taranaki Airs", "Bay Hawks"
            ],
            "GP": [20]*11,
            "PTS": [96.2, 92.4, 91.0, 95.8, 88.1, 89.5, 86.4, 85.2, 84.8, 86.0, 83.5],
            "Opp_PTS": [87.1, 86.5, 85.2, 89.0, 89.4, 89.1, 91.2, 87.0, 90.3, 91.5, 94.8],
            "FGA": [71.2]*11, "FTA": [17.4]*11, "ORB": [10.1]*11, "TOV": [12.5]*11,
            "Opp_FGA": [70.5]*11, "Opp_FTA": [17.0]*11, "Opp_ORB": [9.6]*11, "Opp_TOV": [13.1]*11,
            "MIN": [40.0]*11
        })

    # ==================== CANADA: CEBL (10 TEAMS) ====================
    elif league_selection == "Canada: CEBL":
        return pd.DataFrame({
            "Team": [
                "Brampton Honey Badgers", "Scarborough Shooting Stars", "Vancouver Bandits", 
                "Winnipeg Sea Bears", "Ottawa BlackJacks", "Niagara River Lions", 
                "Edmonton Stingers", "Montreal Alliance", "Saskatoon Mamba", "Calvary Surge"
            ],
            "GP": [20]*10,
            "PTS": [90.5, 92.1, 93.4, 91.8, 88.2, 87.5, 86.4, 84.3, 85.1, 82.0],
            "Opp_PTS": [84.2, 86.0, 87.0, 89.5, 89.0, 88.1, 88.5, 87.2, 91.4, 90.1],
            "FGA": [68.5]*10, "FTA": [19.1]*10, "ORB": [9.8]*10, "TOV": [13.4]*10,
            "Opp_FGA": [67.9]*10, "Opp_FTA": [18.5]*10, "Opp_ORB": [9.3]*10, "Opp_TOV": [12.9]*10,
            "MIN": [40.0]*10
        })

    # ==================== ITALY: LEGA BASKET SERIE A (15 TEAMS) ====================
    elif league_selection == "Italy: Lega Basket Serie A":
        return pd.DataFrame({
            "Team": [
                "Virtus Bologna", "Pallacanestro Brescia", "Olimpia Milano", "Reyer Venezia", "Derthona Basket",
                "Pallacanestro Reggiana", "Pallacanestro Trieste", "Aquila Basket Trento", "Pallacanestro Varese", "Napoli Basket",
                "Vanoli Cremona", "Universo Treviso Basket", "APU Udine", "Pallacanestro Cantù", "Dinamo Sassari"
            ],
            "GP": [28]*15,
            "PTS": [86.3, 89.0, 86.9, 90.0, 86.3, 83.8, 83.9, 84.9, 84.1, 84.5, 82.3, 83.6, 81.4, 84.6, 84.7],
            "Opp_PTS": [79.0, 83.9, 79.5, 85.0, 84.8, 80.1, 87.2, 84.6, 87.8, 86.5, 85.7, 89.0, 83.5, 88.7, 90.0],
            "FGA": [63.5]*15, "FTA": [18.1]*15, "ORB": [9.1]*15, "TOV": [12.2]*15,
            "Opp_FGA": [61.4]*15, "Opp_FTA": [16.3]*15, "Opp_ORB": [8.8]*15, "Opp_TOV": [12.9]*15,
            "MIN": [40.0]*15
        })

    # ==================== MEXICO: LNBP (14 TEAMS) ====================
    elif league_selection == "Mexico: LNBP":
        return pd.DataFrame({
            "Team": [
                "Astros de Jalisco", "Soles", "Fuerza Regia", "Diablos Rojos", "Mineros de Zacatecas",
                "Dorados de Chihuahua", "Halcones UV Xalapa", "Panteras de Aguascalientes", "El Calor de Cancun",
                "Correcaminos", "Gambusinos", "Santos de San Luis Potosi", "Abejas", "Freseros Irapuato"
            ],
            "GP": [28]*14,
            "PTS": [90.4, 88.9, 93.6, 92.4, 84.0, 84.4, 81.5, 87.3, 81.6, 84.5, 84.3, 79.2, 78.4, 74.6],
            "Opp_PTS": [77.6, 77.1, 82.2, 81.1, 82.0, 80.8, 81.6, 87.6, 83.6, 92.4, 88.3, 88.0, 90.8, 91.9],
            "FGA": [65.2]*14, "FTA": [18.5]*14, "ORB": [9.0]*14, "TOV": [12.8]*14,
            "Opp_FGA": [64.0]*14, "Opp_FTA": [17.9]*14, "Opp_ORB": [8.9]*14, "Opp_TOV": [12.4]*14,
            "MIN": [40.0]*14
        })

    # ==================== PORTUGAL: LPB (12 TEAMS) ====================
    elif league_selection == "Portugal: LPB":
        return pd.DataFrame({
            "Team": [
                "S.L. Benfica", "Sporting CP", "FC Porto", "Ovarense Basquetebol", "U.D. Oliveirense",
                "Imortal Basket Club", "Clube do Povo de Esgueira", "SC Braga", "Vitória S.C.",
                "C.A. Queluz", "SC Vasco da Gama", "Galitos Barreiro"
            ],
            "GP": [22]*12,
            "PTS": [98.0, 87.2, 89.2, 81.6, 85.3, 84.6, 85.1, 79.7, 83.2, 84.1, 83.1, 81.7],
            "Opp_PTS": [75.8, 76.9, 82.3, 78.5, 83.0, 84.5, 90.5, 82.6, 90.1, 87.4, 97.8, 93.5],
            "FGA": [64.1]*12, "FTA": [17.8]*12, "ORB": [9.3]*12, "TOV": [12.6]*12,
            "Opp_FGA": [63.2]*12, "Opp_FTA": [16.9]*12, "Opp_ORB": [8.8]*12, "Opp_TOV": [13.2]*12,
            "MIN": [40.0]*12
        })

    # ==================== CROATIA: PREMIJER LIGA (12 TEAMS) ====================
    else:
        return pd.DataFrame({
            "Team": [
                "KK Zadar", "KK Cibona", "KK Split", "KK Samobor", "KK Dubrovnik",
                "KK Zabok", "KK Furnir", "KK Kvarner 2010", "KK Alkar", "KK Cedevita Junior",
                "KK Dinamo Zagreb", "GKK Šibenka"
            ],
            "GP": [33]*12,
            "PTS": [87.0, 83.4, 90.6, 86.7, 79.1, 79.3, 81.7, 78.5, 70.9, 79.5, 83.1, 76.6],
            "Opp_PTS": [71.1, 74.7, 80.3, 85.1, 81.3, 80.3, 83.4, 82.7, 78.8, 82.6, 88.6, 87.6],
            "FGA": [62.4]*12, "FTA": [16.8]*12, "ORB": [8.7]*12, "TOV": [11.9]*12,
            "Opp_FGA": [61.1]*12, "Opp_FTA": [16.0]*12, "Opp_ORB": [8.5]*12, "Opp_TOV": [12.2]*12,
            "MIN": [40.0]*12
        })

# 3. Analytics Engine Execution
def calculate_advanced_stats(df, league):
    df["Possessions"] = df["FGA"] + (0.44 * df["FTA"]) - df["ORB"] + df["TOV"]
    df["Opp_Possessions"] = df["Opp_FGA"] + (0.44 * df["Opp_FTA"]) - df["Opp_ORB"] + df["Opp_TOV"]
    df["Avg_Poss"] = (df["Possessions"] + df["Opp_Possessions"]) / 2
    
    reg_min = 48.0 if league == "NBA" else 40.0
    floor_min_factor = df["MIN"]
    
    df["Pace"] = df["Avg_Poss"] / (floor_min_factor / reg_min)
    df["Offensive_Rating"] = (df["PTS"] / df["Possessions"]) * 100
    df["Defensive_Rating"] = (df["Opp_PTS"] / df["Opp_Possessions"]) * 100
    df["Net_Rating"] = df["Offensive_Rating"] - df["Defensive_Rating"]
    
    return df[["Team", "Pace", "Offensive_Rating", "Defensive_Rating", "Net_Rating"]]

# 4. Interactive User Interface View
selected_league = st.sidebar.selectbox(
    "Select League Registry", 
    [
        "NBA", "WNBA", "Puerto Rico: BSN", "New Zealand: NBL", "Canada: CEBL", 
        "Italy: Lega Basket Serie A", "Mexico: LNBP", "Portugal: LPB", "Croatia: Premijer Liga"
    ]
)

raw_data = fetch_complete_league_data(selected_league)
processed_stats = calculate_advanced_stats(raw_data, selected_league)

st.subheader(f"📊 League Standings & Analytics Dashboard: {selected_league}")
st.dataframe(processed_stats, use_container_width=True)

st.subheader("🔮 Matchup Engine")
col1, col2 = st.columns(2)
with col1: 
    team_a = st.selectbox("Team A (Home)", processed_stats["Team"].unique(), index=0)
with col2: 
    team_b = st.selectbox("Team B (Away)", processed_stats["Team"].unique(), index=1)

if team_a != team_b:
    if st.button("Run Simulation", type="primary"):
        sa = processed_stats[processed_stats["Team"] == team_a]
        sb = processed_stats[processed_stats["Team"] == team_b]
        
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
            
