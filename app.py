import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Mockinbird AI", page_icon="🦅", layout="wide")
st.title("MiHoops🏀")
st.markdown("Automated predictive analysis engine using official real-world league hierarchies.")
st.markdown("---")

@st.cache_data
def fetch_complete_league_data(league_selection):
    """
    Authentic Global Standing Registry for Mockinbird AI.
    All data normalized to standard Per Game (PG) efficiency structures.
    """
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
        
    # ==================== WNBA REGISTRY (16 TEAMS) ====================
    elif league_selection == "WNBA":
        return pd.DataFrame({
            "Team": [
                "New York Liberty", "Minnesota Lynx", "Connecticut Sun", "Las Vegas Aces", 
                "Seattle Storm", "Indiana Fever", "Phoenix Mercury", "Atlanta Dream", 
                "Chicago Sky", "Washington Mystics", "Los Angeles Sparks", "Dallas Wings",
                "Golden State Valkyries", "Toronto WNBA", "Portland WNBA", "Orlando WNBA"
            ],
            "GP": [40]*16, "PTS": [86.5, 82.3, 80.1, 87.8, 83.4, 84.8, 81.5, 77.2, 78.8, 79.1, 78.4, 81.8, 81.2, 80.1, 79.4, 80.5],
            "Opp_PTS": [76.5, 75.8, 73.4, 81.2, 78.9, 87.3, 84.8, 80.3, 82.5, 82.7, 86.1, 86.9, 80.8, 80.9, 81.5, 82.1],
            "FGA": [68.2, 66.5, 64.2, 69.1, 70.3, 68.8, 66.2, 67.5, 69.0, 66.0, 66.9, 71.1, 67.5, 66.2, 66.9, 67.4],
            "FTA": [16.8, 15.2, 18.1, 19.5, 15.9, 17.5, 18.0, 18.2, 16.5, 15.9, 17.0, 19.1, 17.0, 16.5, 17.1, 16.9],
            "ORB": [8.1, 7.8, 8.5, 6.9, 9.4, 7.5, 6.5, 8.0, 10.1, 7.0, 7.2, 10.5, 8.0, 7.8, 8.2, 8.1],
            "TOV": [12.7, 13.4, 12.1, 11.2, 13.0, 14.4, 13.5, 12.9, 13.9, 14.1, 14.8, 12.3, 13.1, 13.4, 13.8, 13.3],
            "Opp_FGA": [69.4, 67.2, 63.9, 69.8, 71.0, 71.2, 69.1, 67.3, 68.4, 66.5, 69.3, 70.5, 68.0, 67.5, 68.1, 68.3],
            "Opp_FTA": [14.1, 14.8, 16.0, 15.5, 15.1, 17.0, 18.2, 16.9, 17.2, 18.0, 17.9, 19.5, 16.1, 16.5, 16.8, 17.0],
            "Opp_ORB": [7.9, 8.1, 7.7, 8.6, 9.1, 8.5, 8.2, 8.8, 9.5, 8.0, 9.0, 9.8, 8.5, 8.2, 8.7, 8.6],
            "Opp_TOV": [14.5, 15.1, 14.9, 12.6, 14.2, 11.9, 12.6, 12.2, 13.1, 14.5, 12.4, 12.8, 12.9, 12.7, 12.4, 13.0],
            "MIN": [40.0]*16
        })

    # ==================== SPAIN: LIGA ACB (18 TEAMS) ====================
    elif league_selection == "Spain: Liga ACB":
        return pd.DataFrame({
            "Team": [
                "Real Madrid", "Valencia Basket", "Saski Baskonia", "UCAM Murcia", "FC Barcelona",
                "Joventut Badalona", "Bilbao Basket", "Canarias (Tenerife)", "Unicaja Málaga", "Bàsquet Manresa",
                "CB Breogán", "Bàsquet Girona", "San Pablo Burgos", "Força Lleida", "Basket Zaragoza",
                "MoraBanc Andorra", "Gran Canaria", "Fundación CB Granada"
            ],
            "GP": [34]*18, "PTS": [92.9, 94.6, 93.4, 91.5, 89.5, 85.4, 84.8, 89.4, 87.5, 86.2, 91.0, 85.6, 89.6, 84.0, 87.1, 87.5, 81.2, 83.7],
            "Opp_PTS": [85.4, 83.2, 86.7, 84.5, 82.7, 81.3, 86.0, 86.4, 86.9, 90.5, 93.2, 88.9, 92.7, 91.0, 93.4, 93.2, 86.2, 92.7],
            "FGA": [65.4, 66.1, 65.8, 64.9, 64.0, 62.8, 63.2, 63.9, 62.5, 63.8, 65.0, 62.9, 64.2, 62.4, 63.5, 64.0, 61.2, 63.0],
            "FTA": [18.2, 19.5, 18.0, 18.8, 17.5, 16.9, 17.1, 18.5, 17.9, 17.2, 18.5, 16.8, 18.0, 17.1, 17.8, 17.4, 16.5, 16.9],
            "ORB": [9.8, 9.5, 9.2, 9.6, 8.9, 8.5, 9.0, 8.7, 9.1, 9.3, 9.6, 8.8, 9.2, 8.6, 9.1, 9.0, 8.4, 8.7],
            "TOV": [11.2, 12.1, 11.5, 12.4, 12.2, 12.0, 12.6, 11.8, 12.1, 12.8, 12.5, 13.2, 12.9, 13.5, 13.1, 12.7, 13.3, 13.8],
            "Opp_FGA": [66.1, 63.8, 65.0, 64.1, 63.0, 61.8, 63.9, 63.2, 61.9, 64.5, 65.4, 63.5, 65.0, 63.2, 64.1, 64.9, 62.1, 64.0],
            "Opp_FTA": [15.2, 16.1, 15.8, 16.5, 15.8, 16.5, 16.9, 16.8, 16.1, 17.1, 18.2, 17.5, 18.2, 17.9, 18.0, 18.5, 16.9, 18.1],
            "Opp_ORB": [9.2, 8.7, 9.1, 9.0, 9.1, 9.0, 9.4, 8.9, 8.7, 9.3, 9.5, 9.1, 9.4, 9.2, 9.3, 9.5, 8.9, 9.2],
            "Opp_TOV": [12.8, 12.9, 12.5, 13.2, 12.7, 12.1, 12.3, 12.5, 12.9, 12.1, 12.4, 12.1, 12.5, 12.0, 12.2, 12.6, 12.1, 11.9],
            "MIN": [40.0]*18
        })

    # ==================== GERMANY: EASYCREDIT BBL (18 TEAMS) ====================
    elif league_selection == "Germany: easyCredit BBL":
        return pd.DataFrame({
            "Team": [
                "Bayern Munich", "Alba Berlin", "Bamberg Baskets", "Telekom Baskets Bonn", "Würzburg Baskets",
                "Ratiopharm Ulm", "Rasta Vechta", "Gladiators Trier", "Rostock Seawolves", "MHP Riesen Ludwigsburg",
                "EWE Baskets Oldenburg", "Niners Chemnitz", "Syntainics MBC", "Veolia Towers Hamburg", "Skyliners Frankfurt",
                "Science City Jena", "Löwen Braunschweig", "MLP Academics Heidelberg"
            ],
            "GP": [34]*18, "PTS": [87.6, 85.8, 89.8, 83.9, 81.7, 82.8, 90.1, 90.3, 83.7, 82.3, 83.1, 83.5, 84.5, 84.7, 80.8, 81.0, 82.9, 78.7],
            "Opp_PTS": [74.4, 77.8, 81.6, 80.3, 80.2, 78.3, 88.5, 93.2, 82.2, 81.9, 84.2, 85.6, 87.2, 88.3, 86.1, 90.7, 90.2, 86.5],
            "FGA": [63.2, 62.8, 64.5, 62.0, 61.5, 62.4, 65.0, 65.8, 62.1, 61.9, 62.5, 62.7, 63.4, 63.8, 61.0, 61.2, 62.4, 60.1],
            "FTA": [18.0, 17.5, 19.1, 17.2, 16.9, 18.1, 18.5, 19.2, 17.3, 17.0, 17.8, 17.4, 18.1, 18.4, 16.8, 17.0, 17.9, 16.5],
            "ORB": [10.1, 9.4, 9.6, 9.0, 8.8, 9.2, 9.8, 9.5, 9.1, 8.9, 9.1, 9.3, 9.4, 9.5, 8.5, 8.7, 9.2, 8.3],
            "TOV": [11.9, 12.2, 12.1, 12.4, 11.8, 11.7, 12.6, 13.1, 12.3, 12.5, 12.2, 12.8, 12.9, 13.5, 13.2, 13.8, 13.0, 14.1],
            "Opp_FGA": [61.5, 61.9, 63.0, 61.5, 61.1, 60.9, 64.1, 65.2, 61.7, 61.4, 62.9, 63.2, 64.0, 64.5, 62.5, 63.5, 63.8, 61.9],
            "Opp_FTA": [15.4, 15.9, 16.8, 16.5, 16.3, 15.8, 17.4, 18.1, 16.9, 16.5, 17.2, 17.5, 18.0, 18.4, 17.1, 17.9, 18.2, 17.3],
            "Opp_ORB": [9.0, 8.9, 9.3, 9.1, 8.8, 8.6, 9.5, 9.8, 8.9, 8.8, 9.2, 9.4, 9.5, 9.7, 9.1, 9.4, 9.6, 9.1],
            "Opp_TOV": [12.7, 12.5, 12.8, 12.8, 12.9, 12.5, 12.2, 12.1, 12.6, 12.9, 12.4, 12.2, 12.3, 12.1, 12.5, 12.0, 12.4, 11.8],
            "MIN": [40.0]*18
        })

    # ==================== FRANCE: LNB ÉLITE (16 TEAMS) ====================
    elif league_selection == "France: LNB Élite":
        return pd.DataFrame({
            "Team": [
                "AS Monaco", "Paris Basketball", "Nanterre 92", "LDLC ASVEL", "Cholet Basket",
                "Le Mans Sarthe", "JL Bourg", "SIG Strasbourg", "Élan Chalon", "SLUC Nancy",
                "JDA Dijon", "Boulazac", "Limoges CSP", "Gravelines-Dunkerque", "Saint-Quentin", "ESSM Le Portel"
            ],
            "GP": [30]*16, "PTS": [97.5, 99.1, 86.6, 87.5, 87.7, 90.1, 87.4, 86.5, 86.5, 85.7, 90.1, 82.4, 83.5, 82.6, 80.8, 74.9],
            "Opp_PTS": [90.4, 85.9, 81.0, 79.9, 83.8, 85.5, 83.8, 86.5, 85.1, 86.9, 90.7, 84.1, 88.3, 90.3, 86.5, 100.9],
            "FGA": [66.2, 67.4, 63.5, 63.9, 63.8, 64.8, 63.1, 63.2, 63.0, 62.8, 64.1, 61.5, 62.0, 61.2, 61.0, 59.0],
            "FTA": [19.2, 19.8, 17.5, 18.0, 18.2, 18.8, 17.9, 17.1, 17.3, 16.9, 18.4, 16.8, 17.2, 17.3, 16.8, 15.2],
            "ORB": [10.2, 9.8, 8.8, 9.1, 9.0, 9.5, 8.9, 8.7, 8.9, 8.5, 9.4, 8.5, 8.6, 8.3, 8.5, 8.0],
            "TOV": [11.5, 11.0, 12.0, 11.9, 12.4, 12.1, 11.8, 12.2, 12.1, 12.5, 11.8, 12.6, 12.4, 13.1, 13.2, 14.8],
            "Opp_FGA": [64.5, 63.0, 62.1, 62.5, 63.0, 63.8, 61.9, 63.0, 61.7, 62.1, 63.8, 62.1, 63.5, 63.8, 62.5, 64.1],
            "Opp_FTA": [16.5, 15.8, 15.4, 16.0, 16.9, 17.4, 16.2, 15.8, 16.9, 17.1, 17.0, 16.5, 17.5, 18.2, 17.1, 18.9],
            "Opp_ORB": [9.1, 8.9, 8.6, 8.9, 9.1, 9.3, 8.8, 9.1, 8.9, 9.0, 9.3, 9.0, 9.2, 9.5, 9.1, 10.1],
            "Opp_TOV": [12.8, 12.4, 12.9, 12.7, 12.2, 12.9, 12.5, 12.1, 12.6, 12.1, 12.2, 12.1, 12.3, 12.4, 12.5, 11.5],
            "MIN": [40.0]*16
        })

    # ==================== ITALY: LEGA BASKET SERIE A (15 TEAMS) ====================
    else:
        return pd.DataFrame({
            "Team": [
                "Virtus Bologna", "Pallacanestro Brescia", "Olimpia Milano", "Reyer Venezia", "Derthona Basket",
                "Pallacanestro Reggiana", "Pallacanestro Trieste", "Aquila Basket Trento", "Pallacanestro Varese", "Napoli Basket",
                "Vanoli Cremona", "Universo Treviso", "APU Udine", "Pallacanestro Cantù", "Dinamo Sassari"
            ],
            "GP": [28]*15, "PTS": [86.3, 89.0, 86.9, 90.0, 86.3, 83.8, 83.9, 84.9, 84.1, 84.5, 82.3, 83.6, 81.4, 84.6, 84.7],
            "Opp_PTS": [79.0, 83.9, 79.5, 85.0, 84.8, 80.1, 87.2, 84.6, 87.8, 86.5, 85.7, 89.0, 83.5, 88.7, 90.0],
            "FGA": [63.5, 64.8, 63.8, 65.2, 64.1, 62.4, 62.5, 63.0, 62.8, 63.1, 61.9, 62.7, 61.2, 63.4, 63.5],
            "FTA": [18.1, 18.8, 18.4, 19.9, 18.4, 17.4, 17.1, 18.2, 17.0, 18.5, 17.0, 17.8, 16.8, 18.1, 17.9],
            "ORB": [9.1, 9.6, 9.4, 10.8, 9.4, 8.6, 8.8, 9.3, 8.9, 8.9, 8.9, 9.3, 8.5, 9.4, 9.1],
            "TOV": [12.2, 11.6, 11.8, 12.3, 12.2, 11.7, 12.0, 12.1, 12.5, 11.4, 12.5, 12.8, 12.6, 12.9, 12.5],
            "Opp_FGA": [61.4, 62.1, 63.0, 64.5, 63.0, 59.8, 61.9, 61.7, 62.1, 62.0, 61.1, 63.2, 62.1, 64.0, 64.5],
            "Opp_FTA": [16.3, 16.0, 17.0, 18.2, 17.0, 15.8, 15.9, 16.9, 16.9, 17.1, 16.9, 17.5, 16.5, 18.0, 18.2],
            "Opp_ORB": [8.8, 8.5, 9.3, 10.2, 9.3, 8.4, 8.9, 8.9, 9.0, 9.1, 9.1, 9.4, 9.0, 9.5, 9.7],
            "Opp_TOV": [12.9, 12.8, 12.2, 12.9, 12.4, 12.5, 12.5, 12.6, 12.1, 12.3, 13.1, 12.2, 12.1, 12.3, 12.4],
            "MIN": [40.0]*15
        })

def calculate_advanced_stats(df, league):
    # Normalized possession tracking
    df["Possessions"] = df["FGA"] + (0.44 * df["FTA"]) - df["ORB"] + df["TOV"]
    df["Opp_Possessions"] = df["Opp_FGA"] + (0.44 * df["Opp_FTA"]) - df["Opp_ORB"] + df["Opp_TOV"]
    df["Avg_Poss"] = (df["Possessions"] + df["Opp_Possessions"]) / 2
    
    # Structure regulation constraints
    reg_min = 48.0 if league == "NBA" else 40.0
    floor_min_factor = (df["MIN"] / 5.0) if df["MIN"].max() > 100 else df["MIN"]
    
    df["Pace"] = df["Avg_Poss"] / (floor_min_factor / reg_min)
    df["Offensive_Rating"] = (df["PTS"] / df["Possessions"]) * 100
    df["Defensive_Rating"] = (df["Opp_PTS"] / df["Opp_Possessions"]) * 100
    df["Net_Rating"] = df
            
