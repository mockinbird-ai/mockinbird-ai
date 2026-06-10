import streamlit as st
import pandas as pd
import numpy as np

# 1. Setup Minimalist Page UI Config
st.set_page_config(page_title="MiHoops Deep Analytics Engine", page_icon="🏀", layout="centered")
st.title("MiHoops🏀")
st.markdown("High-fidelity predictive matchup platform operating on updated multi-league structural efficiency models.")
st.markdown("---")

# 2. Comprehensive Global Database Registry
def fetch_complete_league_data(league_selection):
    """
    Complete, authenticated team hierarchies structured natively 
    for algorithmic efficiency extraction.
    """
    # SPAIN: LIGA ACB
    if league_selection == "Spain: Liga ACB":
        return pd.DataFrame({
            "Team": ["Real Madrid", "Valencia Basket", "Saski Baskonia", "UCAM Murcia", "FC Barcelona", "Joventut Badalona", "Bilbao Basket", "Canarias (Tenerife)", "Unicaja Málaga", "Bàsquet Manresa", "CB Breogán", "Bàsquet Girona", "San Pablo Burgos", "Força Lleida", "Basket Zaragoza", "MoraBanc Andorra", "Gran Canaria", "Fundación CB Granada"],
            "GP": [34]*18, "PTS": [92.9, 94.6, 93.4, 91.5, 89.5, 85.4, 84.8, 89.4, 87.5, 86.2, 91.0, 85.6, 89.6, 84.0, 87.1, 87.5, 81.2, 83.7],
            "Opp_PTS": [85.4, 83.2, 86.7, 84.5, 82.7, 81.3, 86.0, 86.4, 86.9, 90.5, 93.2, 88.9, 92.7, 91.0, 93.4, 93.2, 86.2, 92.7],
            "FGA": [65.4, 66.1, 65.8, 64.9, 64.0, 62.8, 63.2, 63.9, 62.5, 63.8, 65.0, 62.9, 64.2, 62.4, 63.5, 64.0, 61.2, 63.0],
            "FTA": [18.2, 19.5, 18.0, 18.8, 17.5, 16.9, 17.1, 18.5, 17.9, 17.2, 18.5, 16.8, 18.0, 17.1, 17.8, 17.4, 16.5, 16.9],
            "ORB": [9.8, 9.5, 9.2, 9.6, 8.9, 8.5, 9.0, 8.7, 9.1, 9.3, 9.6, 8.8, 9.2, 8.6, 9.1, 9.0, 8.4, 8.7],
            "TOV": [11.2, 12.1, 11.5, 12.4, 12.2, 12.0, 12.6, 11.8, 12.1, 12.8, 12.5, 13.2, 12.9, 13.5, 13.1, 12.7, 13.3, 13.8],
            "Opp_FGA": [66.1, 63.8, 65.0, 64.1, 63.0, 61.8, 63.9, 63.2, 61.9, 64.5, 65.4, 63.5, 65.0, 63.2, 64.1, 64.9, 62.1, 64.0],
            "Opp_FTA": [15.2, 16.1, 15.8, 16.5, 15.8, 16.5, 16.9, 16.8, 16.1, 17.1, 18.2, 17.5, 18.2, 17.9, 18.0, 18.5, 16.9, 18.1],
            "Opp_ORB": [9.2, 8.7, 9.1, 9.0, 9.1, 9.0, 9.4, 8.9, 8.7, 9.3, 9.5, 9.1, 9.4, 9.2, 9.3, 9.5, 8.9, 9.2],
            "Opp_TOV": [12.8, 12.9, 12.5, 13.2, 12.7, 12.1, 12.3, 12.5, 12.9, 12.1, 12.4, 12.1, 12.5, 12.0, 12.2, 12.6, 12.1, 11.9]
        })
        
    # FRANCE: LNB ÉLITE
    elif league_selection == "France: LNB Élite":
        return pd.DataFrame({
            "Team": ["AS Monaco", "Paris Basketball", "Nanterre 92", "LDLC ASVEL", "Cholet Basket", "Le Mans Sarthe", "JL Bourg", "SIG Strasbourg", "Élan Chalon", "SLUC Nancy", "JDA Dijon", "Boulazac", "Limoges CSP", "Gravelines-Dunkerque", "Saint-Quentin", "ESSM Le Portel"],
            "GP": [30]*16, "PTS": [97.5, 99.1, 86.6, 87.5, 87.7, 90.1, 87.4, 86.5, 86.5, 85.7, 90.1, 82.4, 83.5, 82.6, 80.8, 74.9],
            "Opp_PTS": [90.4, 85.9, 81.0, 79.9, 83.8, 85.5, 83.8, 86.5, 85.1, 86.9, 90.7, 84.1, 88.3, 90.3, 86.5, 100.9],
            "FGA": [66.2, 67.4, 63.5, 63.9, 63.8, 64.8, 63.1, 63.2, 63.0, 62.8, 64.1, 61.5, 62.0, 61.2, 61.0, 59.0],
            "FTA": [19.2, 19.8, 17.5, 18.0, 18.2, 18.8, 17.9, 17.1, 17.3, 16.9, 18.4, 16.8, 17.2, 17.3, 16.8, 15.2],
            "ORB": [10.2, 9.8, 8.8, 9.1, 9.0, 9.5, 8.9, 8.7, 8.9, 8.5, 9.4, 8.5, 8.6, 8.3, 8.5, 8.0],
            "TOV": [11.5, 11.0, 12.0, 11.9, 12.4, 12.1, 11.8, 12.2, 12.1, 12.5, 11.8, 12.6, 12.4, 13.1, 13.2, 14.8],
            "Opp_FGA": [64.5, 63.0, 62.1, 62.5, 63.0, 63.8, 61.9, 63.0, 61.7, 62.1, 63.8, 62.1, 63.5, 63.8, 62.5, 64.1],
            "Opp_FTA": [16.5, 15.8, 15.4, 16.0, 16.9, 17.4, 16.2, 15.8, 16.9, 17.1, 17.0, 16.5, 17.5, 18.2, 17.1, 18.9],
            "Opp_ORB": [9.1, 8.9, 8.6, 8.9, 9.1, 9.3, 8.8, 9.1, 8.9, 9.0, 9.3, 9.0, 9.2, 9.5, 9.1, 10.1],
            "Opp_TOV": [12.8, 12.4, 12.9, 12.7, 12.2, 12.9, 12.5, 12.1, 12.6, 12.1, 12.2, 12.1, 12.3, 12.4, 12.5, 11.5]
        })

    # GREECE: HEBA A1
    elif league_selection == "Greece: GBL A1":
        return pd.DataFrame({
            "Team": ["Panathinaikos BC", "Olympiacos BC", "Peristeri B.C.", "Promitheas Patras", "Aris Thessaloniki", "AEK Athens", "PAOK Thessaloniki", "Maroussi B.C.", "Karditsas", "Lavrio B.C.", "Kolossos Rodou", "Apollon Patras"],
            "GP": [22]*12, "PTS": [88.5, 87.2, 80.4, 82.1, 77.2, 83.4, 78.9, 79.5, 75.1, 76.9, 77.8, 72.3],
            "Opp_PTS": [73.1, 71.4, 76.5, 80.2, 75.4, 84.1, 80.1, 82.3, 81.0, 83.4, 82.1, 84.5],
            "FGA": [61.1, 60.5, 59.8, 61.2, 58.5, 62.4, 60.1, 61.0, 58.9, 59.4, 59.0, 58.1],
            "FTA": [19.5, 18.9, 17.2, 18.5, 17.9, 19.1, 17.5, 17.2, 16.8, 17.4, 17.1, 16.1],
            "ORB": [9.1, 9.4, 8.5, 8.2, 8.9, 8.8, 8.4, 8.6, 8.1, 8.3, 8.2, 7.9],
            "TOV": [11.8, 11.2, 12.5, 13.1, 13.4, 12.9, 12.6, 12.8, 13.2, 13.0, 12.7, 13.9],
            "Opp_FGA": [59.5, 58.4, 60.2, 62.1, 59.0, 61.8, 61.1, 61.5, 60.4, 61.2, 60.9, 61.4],
            "Opp_FTA": [15.2, 14.8, 16.5, 17.8, 16.9, 18.2, 17.1, 17.5, 17.9, 18.1, 17.4, 18.5],
            "Opp_ORB": [8.2, 8.0, 8.9, 9.1, 9.0, 9.2, 8.9, 9.1, 9.3, 9.0, 9.1, 9.5],
            "Opp_TOV": [13.4, 14.1, 12.8, 12.4, 13.1, 12.5, 12.1, 12.3, 12.0, 12.2, 12.1, 11.8]
        })

    # TURKIYE: BASKETBOL SÜPER LİGİ
    elif league_selection == "Turkiye: BSL":
        return pd.DataFrame({
            "Team": ["Fenerbahçe Beko", "Beşiktaş Icrypex", "Bahçeşehir Koleji", "Anadolu Efes", "Türk Telekom", "Trabzonspor", "Galatasaray", "Esenler Erokspor", "Tofaş SC", "Merkezefendi Denizli", "Manisa BB", "Bursaspor", "Mersin BSB", "Pınar Karşıyaka", "Socar Petkimspor", "Buyukcekmece Basket"],
            "GP": [30]*16, "PTS": [88.1, 86.7, 83.2, 88.3, 87.0, 86.2, 85.9, 81.3, 83.9, 81.6, 81.9, 81.4, 84.6, 80.3, 80.0, 80.7],
            "Opp_PTS": [79.8, 76.8, 78.3, 81.5, 81.2, 82.0, 83.8, 78.3, 85.3, 86.4, 86.0, 88.4, 88.3, 87.6, 87.1, 90.3],
            "FGA": [63.2, 62.5, 61.9, 64.0, 62.8, 63.5, 63.1, 61.2, 62.9, 61.5, 62.0, 61.8, 63.4, 60.9, 61.1, 62.0],
            "FTA": [18.4, 18.1, 17.5, 19.2, 18.0, 17.9, 17.6, 16.9, 18.2, 17.4, 17.1, 17.3, 18.5, 16.8, 16.5, 17.1],
            "ORB": [9.5, 9.1, 8.8, 9.0, 9.3, 9.2, 8.9, 8.4, 9.1, 8.5, 8.7, 8.6, 9.2, 8.3, 8.4, 8.6],
            "TOV": [12.0, 11.5, 12.2, 11.8, 12.4, 12.1, 12.5, 12.8, 12.3, 13.0, 12.7, 12.9, 13.2, 13.4, 13.1, 13.8],
            "Opp_FGA": [61.8, 60.9, 61.2, 62.5, 61.9, 62.7, 62.9, 60.5, 63.4, 62.8, 63.0, 63.5, 64.1, 62.4, 62.7, 63.9],
            "Opp_FTA": [15.6, 15.1, 16.0, 16.8, 16.2, 16.5, 17.1, 15.9, 17.5, 17.9, 17.3, 18.2, 18.0, 18.4, 18.1, 18.9],
            "Opp_ORB": [8.7, 8.4, 8.6, 8.9, 9.0, 9.1, 9.2, 8.5, 9.3, 9.4, 9.2, 9.5, 9.6, 9.3, 9.4, 9.7],
            "Opp_TOV": [13.1, 12.8, 12.5, 12.7, 12.4, 12.6, 12.2, 12.0, 12.1, 11.9, 12.3, 11.8, 12.0, 11.7, 11.9, 11.5]
        })

    # GERMANY: BASKETBALL BUNDESLIGA
    elif league_selection == "Germany: easyCredit BBL":
        return pd.DataFrame({
            "Team": ["FC Bayern Munich", "Alba Berlin", "Brose Bamberg", "Telekom Baskets Bonn", "Würzburg Baskets", "Ratiopharm Ulm", "SC Rasta Vechta", "Gladiators Trier", "Rostock Seawolves", "MHP Riesen Ludwigsburg", "Baskets Oldenburg", "Niners Chemnitz", "Mitteldeutscher BC", "Hamburg Towers", "Fraport Skyliners", "Science City Jena", "Löwen Braunschweig", "MLP Academics Heidelberg"],
            "GP": [34]*18, "PTS": [2980/34, 2918/34, 3055/34, 2853/34, 2780/34, 2817/34, 3064/34, 3073/34, 2849/34, 2801/34, 2826/34, 2839/34, 2874/34, 2881/34, 2750/34, 2756/34, 2821/34, 2676/34],
            "Opp_PTS": [2530/34, 2648/34, 2777/34, 2731/34, 2727/34, 2665/34, 3009/34, 3171/34, 2796/34, 2847/34, 2866/34, 2913/34, 2965/34, 3004/34, 2928/34, 3023/34, 3070/34, 2943/34],
            "FGA":
            
