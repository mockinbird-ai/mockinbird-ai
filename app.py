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
            "Girona": {"ORTG": 105.4, "DRTG": 110.2, "PACE": 76.1},
            "Granada": {"ORTG": 106.8, "DRTG": 111.9, "PACE": 75.8},
            "Gran Canaria": {"ORTG": 110.5, "DRTG": 108.2, "PACE": 74.9},
            "Joventut Badalona": {"ORTG": 110.8, "DRTG": 109.1, "PACE": 76.2},
            "Lenovo Tenerife": {"ORTG": 112.1, "DRTG": 110.5, "PACE": 75.2},
            "Manresa": {"ORTG": 109.2, "DRTG": 110.8, "PACE": 78.4},
            "Palencia": {"ORTG": 103.1, "DRTG": 114.5, "PACE": 76.0},
            "Real Madrid": {"ORTG": 119.5, "DRTG": 105.2, "PACE": 75.8},
            "Breogan": {"ORTG": 102.5, "DRTG": 106.9, "PACE": 74.8},
            "Surne Bilbao": {"ORTG": 109.4, "DRTG": 111.2, "PACE": 76.0},
            "UCAM Murcia": {"ORTG": 112.5, "DRTG": 109.8, "PACE": 75.5},
            "Unicaja Malaga": {"ORTG": 115.8, "DRTG": 107.2, "PACE": 76.5},
            "Valencia Basket": {"ORTG": 113.4, "DRTG": 110.1, "PACE": 78.0},
            "Zaragoza": {"ORTG": 107.9, "DRTG": 112.1, "PACE": 76.6}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.5, "hca_bonus": 2.5,
        "teams": {
            "AS Monaco": {"ORTG": 117.2, "DRTG": 104.1, "PACE": 74.9},
            "Blois": {"ORTG": 104.5, "DRTG": 112.1, "PACE": 76.2},
            "Chalon/Saone": {"ORTG": 106.9, "DRTG": 111.0, "PACE": 75.1},
            "Cholet": {"ORTG": 111.5, "DRTG": 110.2, "PACE": 76.5},
            "Dijon": {"ORTG": 109.1, "DRTG": 109.8, "PACE": 74.2},
            "Gravelines-Dunkerque": {"ORTG": 103.8, "DRTG": 108.5, "PACE": 74.0},
            "JL Bourg": {"ORTG": 110.2, "DRTG": 108.1, "PACE": 74.5},
            "Le Mans": {"ORTG": 112.0, "DRTG": 110.8, "PACE": 75.9},
            "Le Portel": {"ORTG": 107.2, "DRTG": 113.4, "PACE": 76.8},
            "Limoges": {"ORTG": 106.1, "DRTG": 109.5, "PACE": 74.6},
            "LDLC ASVEL": {"ORTG": 112.1, "DRTG": 109.4, "PACE": 75.3},
            "Metropolitans 92": {"ORTG": 101.2, "DRTG": 116.4, "PACE": 77.0},
            "Nanterre 92": {"ORTG": 113.1, "DRTG": 108.4, "PACE": 76.0},
            "Paris Basketball": {"ORTG": 115.4, "DRTG": 107.9, "PACE": 77.2},
            "Roanne": {"ORTG": 108.9, "DRTG": 115.1, "PACE": 78.1},
            "Saint-Quentin": {"ORTG": 106.5, "DRTG": 104.9, "PACE": 73.5},
            "SIG Strasbourg": {"ORTG": 109.5, "DRTG": 109.5, "PACE": 75.8}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.2, "avg_ortg": 111.2, "hca_bonus": 2.5,
        "teams": {
            "ALBA Berlin": {"ORTG": 112.4, "DRTG": 110.2, "PACE": 79.1},
            "Bamberg Baskets": {"ORTG": 113.5, "DRTG": 111.4, "PACE": 78.8},
            "BG Goettingen": {"ORTG": 108.1, "DRTG": 114.2, "PACE": 79.5},
            "Crailsheim Merlins": {"ORTG": 106.2, "DRTG": 116.9, "PACE": 79.0},
            "EWE Baskets Oldenburg": {"ORTG": 110.4, "DRTG": 111.5, "PACE": 78.1},
            "FC Bayern Munich": {"ORTG": 118.1, "DRTG": 105.9, "PACE": 77.4},
            "MHP Riesen Ludwigsburg": {"ORTG": 111.8, "DRTG": 109.4, "PACE": 77.0},
            "MLP Academics Heidelberg": {"ORTG": 107.5, "DRTG": 115.8, "PACE": 80.2},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 106.8, "PACE": 76.9},
            "Rasta Vechta": {"ORTG": 112.8, "DRTG": 110.1, "PACE": 78.3},
            "ratiopharm ulm": {"ORTG": 113.0, "DRTG": 111.1, "PACE": 78.5},
            "ROSTOCK SEAWOLVES": {"ORTG": 109.9, "DRTG": 113.8, "PACE": 79.8},
            "SYNTAINICS MBC": {"ORTG": 108.5, "DRTG": 114.7, "PACE": 78.6},
            "Telekom Baskets Bonn": {"ORTG": 112.9, "DRTG": 111.0, "PACE": 77.9},
            "Tigers Tuebingen": {"ORTG": 105.1, "DRTG": 117.2, "PACE": 79.2},
            "Veolia Towers Hamburg": {"ORTG": 108.9, "DRTG": 114.1, "PACE": 79.4},
            "Wuerzburg Baskets": {"ORTG": 113.6, "DRTG": 107.9, "PACE": 76.4}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.1, "avg_ortg": 111.8, "hca_bonus": 2.5,
        "teams": {
            "Banco di Sardegna Sassari": {"ORTG": 109.2, "DRTG": 112.4, "PACE": 76.8},
            "Bertram Derthona Tortona": {"ORTG": 109.8, "DRTG": 111.1, "PACE": 75.9},
            "Carpegna Prosciutto Pesaro": {"ORTG": 106.5, "DRTG": 114.8, "PACE": 77.2},
            "Dolomiti Energia Trentino": {"ORTG": 110.1, "DRTG": 112.5, "PACE": 77.0},
            "EA7 Emporio Armani Milano": {"ORTG": 116.5, "DRTG": 106.2, "PACE": 75.1},
            "Estra Pistoia": {"ORTG": 108.4, "DRTG": 110.9, "PACE": 75.4},
            "Germani Brescia": {"ORTG": 115.2, "DRTG": 108.1, "PACE": 76.5},
            "Givova Scafati": {"ORTG": 111.0, "DRTG": 114.1, "PACE": 77.9},
            "Happy Casa Brindisi": {"ORTG": 105.2, "DRTG": 111.8, "PACE": 75.8},
            "NutriBullet Treviso": {"ORTG": 109.5, "DRTG": 112.9, "PACE": 76.3},
            "Openjobmetis Varese": {"ORTG": 110.8, "DRTG": 116.2, "PACE": 80.5},
            "Umana Reyer Venezia": {"ORTG": 111.4, "DRTG": 109.2, "PACE": 76.2},
            "UNAHOTELS Reggio Emilia": {"ORTG": 111.9, "DRTG": 111.2, "PACE": 75.6},
            "Vanoli Cremona": {"ORTG": 107.8, "DRTG": 108.9, "PACE": 74.8},
            "Virtus Segafredo Bologna": {"ORTG": 117.9, "DRTG": 108.4, "PACE": 76.1}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.5, "avg_ortg": 113.2, "hca_bonus": 2.5,
        "teams": {
            "Atléticos de San Germán": {"ORTG": 110.8, "DRTG": 112.5, "PACE": 83.0},
            "Cangrejeros de Santurce": {"ORTG": 112.5, "DRTG": 112.9, "PACE": 83.7},
            "Capitanes de Arecibo": {"ORTG": 116.8, "DRTG": 113.4, "PACE": 82.9},
            "Criollos de Caguas": {"ORTG": 111.2, "DRTG": 112.1, "PACE": 83.4},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.0},
            "Indios de Mayagüez": {"ORTG": 109.5, "DRTG": 111.8, "PACE": 82.8},
            "Leones de Ponce": {"ORTG": 112.0, "DRTG": 114.2, "PACE": 84.1},
            "Mets de Guaynabo": {"ORTG": 113.9, "DRTG": 112.0, "PACE": 83.2},
            "Osos de Manatí": {"ORTG": 114.5, "DRTG": 116.8, "PACE": 85.0},
            "Piratas de Quebradillas": {"ORTG": 113.0, "DRTG": 111.4, "PACE": 82.6},
            "Santeros de Aguada": {"ORTG": 110.1, "DRTG": 110.9, "PACE": 82.5},
            "Vaqueros de Bayamón": {"ORTG": 111.2, "DRTG": 111.0, "PACE": 83.1}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.1, "avg_ortg": 109.8, "hca_bonus": 2.5,
        "teams": {
            "Auckland Tuatara": {"ORTG": 112.1, "DRTG": 108.2, "PACE": 84.5},
            "Canterbury Rams": {"ORTG": 114.2, "DRTG": 106.5, "PACE": 83.8},
            "Franklin Bulls": {"ORTG": 110.1, "DRTG": 109.5, "PACE": 84.0},
            "Hawke's Bay Hawks": {"ORTG": 108.2, "DRTG": 113.1, "PACE": 84.9},
            "Manawatu Jets": {"ORTG": 101.5, "DRTG": 115.4, "PACE": 85.2},
            "Nelson Giants": {"ORTG": 107.9, "DRTG": 109.2, "PACE": 82.9},
            "Otago Nuggets": {"ORTG": 108.5, "DRTG": 111.4, "PACE": 83.6},
            "Southland Sharks": {"ORTG": 103.4, "DRTG": 112.8, "PACE": 84.3},
            "Taranaki Airs": {"ORTG": 113.5, "DRTG": 111.0, "PACE": 85.8},
            "Wellington Saints": {"ORTG": 114.9, "DRTG": 111.0, "PACE": 85.2},
            "Whai": {"ORTG": 105.1, "DRTG": 108.7, "PACE": 82.2}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.2, "avg_ortg": 110.1, "hca_bonus": 2.5,
        "teams": {
            "AEK Athens": {"ORTG": 110.2, "DRTG": 112.5, "PACE": 75.1},
            "Aris Salonika": {"ORTG": 106.5, "DRTG": 105.9, "PACE": 73.8},
            "Karditsa": {"ORTG": 105.1, "DRTG": 111.4, "PACE": 74.5},
            "Kolossos Rhodes": {"ORTG": 109.4, "DRTG": 113.2, "PACE": 74.2},
            "Lavrio": {"ORTG": 106.8, "DRTG": 114.9, "PACE": 75.6},
            "Maroussi": {"ORTG": 109.9, "DRTG": 114.0, "PACE": 75.3},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 73.5},
            "Panathinaikos": {"ORTG": 120.4, "DRTG": 103.2, "PACE": 73.9},
            "PAOK Salonika": {"ORTG": 107.9, "DRTG": 111.0, "PACE": 74.0},
            "Peristeri": {"ORTG": 108.5, "DRTG": 110.4, "PACE": 74.8},
            "Promitheas Patras": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 76.0},
            "Apollon Patras": {"ORTG": 101.8, "DRTG": 113.5, "PACE": 73.9}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 77.9, "avg_ortg": 107.5, "hca_bonus": 2.5,
        "teams": {
            "AD Galomar": {"ORTG": 101.2, "DRTG": 109.5, "PACE": 77.1},
            "CD Povoa": {"ORTG": 104.5, "DRTG": 108.1, "PACE": 77.4},
            "Esgueira": {"ORTG": 102.1, "DRTG": 110.8, "PACE": 78.0},
            "FC Porto": {"ORTG": 112.8, "DRTG": 105.1, "PACE": 78.1},
            "Imortal": {"ORTG": 105.4, "DRTG": 110.2, "PACE": 77.8},
            "Lusitania": {"ORTG": 99.5, "DRTG": 114.2, "PACE": 78.5},
            "Ovarense": {"ORTG": 106.1, "DRTG": 108.5, "PACE": 77.6},
            "Portimonense": {"ORTG": 103.0, "DRTG": 109.9, "PACE": 77.2},
            "SL Benfica": {"ORTG": 114.2, "DRTG": 103.5, "PACE": 77.2},
            "Sporting CP": {"ORTG": 111.5, "DRTG": 106.9, "PACE": 78.4},
            "UD Oliveirense": {"ORTG": 107.4, "DRTG": 107.2, "PACE": 77.3},
            "Vitoria SC": {"ORTG": 105.9, "DRTG": 108.8, "PACE": 78.2}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 82.8, "avg_ortg": 111.4, "hca_bonus": 2.5,
        "teams": {
            "Brampton Honey Badgers": {"ORTG": 108.9, "DRTG": 112.4, "PACE": 83.1},
            "Calgary Surge": {"ORTG": 109.8, "DRTG": 111.1, "PACE": 82.4},
            "Edmonton Stingers": {"ORTG": 111.5, "DRTG": 110.2, "PACE": 83.0},
            "Montreal Alliance": {"ORTG": 106.4, "DRTG": 111.8, "PACE": 81.9},
            "Niagara River Lions": {"ORTG": 114.5, "DRTG": 109.2, "PACE": 82.1},
            "Ottawa BlackJacks": {"ORTG": 110.1, "DRTG": 113.5, "PACE": 83.6},
            "Saskatchewan Rattlers": {"ORTG": 109.2, "DRTG": 112.9, "PACE": 84.1},
            "Scarborough Shooting Stars": {"ORTG": 112.4, "DRTG": 112.0, "PACE": 82.9},
            "Vancouver Bandits": {"ORTG": 113.1, "DRTG": 110.8, "PACE": 83.5},
            "Winnipeg Sea Bears": {"ORTG": 113.8, "DRTG": 115.2, "PACE": 84.6}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 79.5, "avg_ortg": 106.8, "hca_bonus": 2.5,
        "teams": {
            "Bristol Flyers": {"ORTG": 104.2, "DRTG": 106.1, "PACE": 78.9},
            "Caledonia Gladiators": {"ORTG": 106.1, "DRTG": 107.4, "PACE": 78.8},
            "Cheshire Phoenix": {"ORTG": 111.5, "DRTG": 106.9, "PACE": 80.0},
            "Leicester Riders": {"ORTG": 108.2, "DRTG": 106.5, "PACE": 79.1},
            "London Lions": {"ORTG": 114.8, "DRTG": 101.2, "PACE": 80.2},
            "Manchester Giants": {"ORTG": 102.5, "DRTG": 111.4, "PACE": 79.9},
            "Newcastle Eagles": {"ORTG": 107.9, "DRTG": 108.1, "PACE": 79.7},
            "Sheffield Sharks": {"ORTG": 104.8, "DRTG": 103.9, "PACE": 77.8},
            "Surrey Scorchers": {"ORTG": 105.1, "DRTG": 111.0, "PACE": 80.4},
            "Plymouth City Patriots": {"ORTG": 100.9, "DRTG": 112.8, "PACE": 79.2}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.2, "avg_ortg": 105.4, "hca_bonus": 2.5,
        "teams": {
            "Arkadia Traiskirchen Lions": {"ORTG": 104.8, "DRTG": 103.1, "PACE": 75.4},
            "BK IMMO聯合 Klostern.": {"ORTG": 101.2, "DRTG": 105.0, "PACE": 75.0},
            "BSC Raiffeisen Furstenfeld": {"ORTG": 96.5, "DRTG": 112.8, "PACE": 77.1},
            "C देवेंद्र OCS Capital Bulls": {"ORTG": 103.5, "DRTG": 106.2, "PACE": 76.3},
            "Eisenstadt Coldamaris": {"ORTG": 99.1, "DRTG": 109.4, "PACE": 75.9},
            "Flyers Wels": {"ORTG": 107.5, "DRTG": 104.9, "PACE": 76.5},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 75.9},
            "Oberwart Gunners": {"ORTG": 101.9, "DRTG": 102.5, "PACE": 74.8},
            "SKN St. Poelten": {"ORTG": 102.9, "DRTG": 107.2, "PACE": 76.0},
            "Swans Gmunden": {"ORTG": 110.2, "DRTG": 102.1, "PACE": 75.8},
            "UBSC Graz": {"ORTG": 105.4, "DRTG": 106.4, "PACE": 76.8},
            "Vienna D. Timberwolves": {"ORTG": 97.2, "DRTG": 110.5, "PACE": 76.1}
        }
    },
    "Croatia (Premijer Liga)": {
        "avg_pace": 75.5, "avg_ortg": 107.2, "hca_bonus": 2.5,
        "teams": {
            "Alkar": {"ORTG": 101.2, "DRTG": 109.5, "PACE": 75.1},
            "Bosco": {"ORTG": 94.8, "DRTG": 119.2, "PACE": 77.0},
            "Cedevita Junior": {"ORTG": 108.5, "DRTG": 108.0, "PACE": 75.5},
            "Cibona Zagreb": {"ORTG": 109.8, "DRTG": 109.1, "PACE": 76.1},
            "DepoLink Skrljevo": {"ORTG": 103.4, "DRTG": 113.8, "PACE": 76.4},
            "Dinamo Zagreb": {"ORTG": 105.1, "DRTG": 108.4, "PACE": 75.2},
            "Dubrava": {"ORTG": 104.2, "DRTG": 109.9, "PACE": 75.0},
            "KK Split": {"ORTG": 111.2, "DRTG": 106.4, "PACE": 75.9},
            "KK Zadar": {"ORTG": 115.4, "DRTG": 103.1, "PACE": 74.8},
            "Sibenka": {"ORTG": 103.9, "DRTG": 110.5, "PACE": 74.9},
            "Zabok": {"ORTG": 105.8, "DRTG": 111.2, "PACE": 75.6},
            "Vrijednosnice Osijek": {"ORTG": 102.1, "DRTG": 108.9, "PACE": 74.7}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 77.4, "avg_ortg": 108.1, "hca_bonus": 2.5,
        "teams": {
            "BK Decin": {"ORTG": 107.8, "DRTG": 108.5, "PACE": 77.6},
            "BK Kvis Pardubice": {"ORTG": 105.4, "DRTG": 108.2, "PACE": 76.5},
            "BK Nova Hut Ostrava": {"ORTG": 104.1, "DRTG": 109.5, "PACE": 76.9},
            "BK Opava": {"ORTG": 109.4, "DRTG": 107.2, "PACE": 76.9},
            "BK Redstone Olomoucko": {"ORTG": 105.9, "DRTG": 112.4, "PACE": 78.0},
            "ERA Nymburk": {"ORTG": 116.5, "DRTG": 101.4, "PACE": 78.1},
            "GEOSAN Kolin": {"ORTG": 106.8, "DRTG": 111.0, "PACE": 77.4},
            "Kralovsti Sokoli": {"ORTG": 101.5, "DRTG": 113.8, "PACE": 76.8},
            "Sluneta Usti nad Labem": {"ORTG": 110.2, "DRTG": 109.1, "PACE": 77.1},
            "SRSNI Pisek": {"ORTG": 108.5, "DRTG": 111.9, "PACE": 79.2},
            "USK Praha": {"ORTG": 104.5, "DRTG": 106.8, "PACE": 76.8},
            "Slavia Praha": {"ORTG": 102.8, "DRTG": 110.4, "PACE": 76.4}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.2, "avg_ortg": 113.4, "hca_bonus": 2.5,
        "teams": {
            "Anadolu Efes": {"ORTG": 119.8, "DRTG": 107.5, "PACE": 76.8},
            "Bahcesehir Koleji": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 76.5},
            "Besiktas Emlakjet": {"ORTG": 112.5, "DRTG": 110.1, "PACE": 77.9},
            "Darussafaka Lassa": {"ORTG": 111.0, "DRTG": 114.5, "PACE": 77.8},
            "Fenerbahce Beko": {"ORTG": 119.2, "DRTG": 106.9, "PACE": 76.4},
            "Frutti Extra Bursaspor": {"ORTG": 110.5, "DRTG": 113.9, "PACE": 77.2},
            "Galatasaray Ekmas": {"ORTG": 113.8, "DRTG": 113.2, "PACE": 77.5},
            "Manisa BBSK": {"ORTG": 111.9, "DRTG": 112.8, "PACE": 76.9},
            "Onvo Buyukcekmece": {"ORTG": 109.8, "DRTG": 111.5, "PACE": 76.1},
            "Petkim Spor": {"ORTG": 112.1, "DRTG": 111.2, "PACE": 76.6},
            "Pinar Karsiyaka": {"ORTG": 115.2, "DRTG": 112.4, "PACE": 78.1},
            "Reeder Samsunspor": {"ORTG": 102.1, "DRTG": 118.4, "PACE": 76.0},
            "Tofas Bursa": {"ORTG": 113.1, "DRTG": 114.2, "PACE": 77.0},
            "Turk Telekom": {"ORTG": 110.4, "DRTG": 109.8, "PACE": 75.6},
            "Yukatel Merkezefendi": {"ORTG": 108.9, "DRTG": 113.5, "PACE": 76.8},
            "Cagdas Bodrum": {"ORTG": 107.5, "DRTG": 112.9, "PACE": 76.4}
        }
    },
    "Brazil (NBB)": {
        "avg_pace": 76.8, "avg_ortg": 109.5, "hca_bon
