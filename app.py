import streamlit as st
import pandas as pd
import numpy as np

# Page Configuration
st.set_page_config(page_title="MiHoops Global Analytics Engine", page_icon="🏀", layout="centered")
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
        "avg_pace": 81.5, "avg_ortg": 103.2, "hca_bonus": 2.5,
        "teams": {
            "Atlanta Dream": {"ORTG": 98.7, "DRTG": 100.2, "PACE": 80.1},
            "Chicago Sky": {"ORTG": 97.5, "DRTG": 101.4, "PACE": 81.2},
            "Connecticut Sun": {"ORTG": 102.1, "DRTG": 95.6, "PACE": 79.4},
            "Dallas Wings": {"ORTG": 101.4, "DRTG": 104.2, "PACE": 82.5},
            "Golden State Valkyries": {"ORTG": 102.8, "DRTG": 101.1, "PACE": 81.8},
            "Indiana Fever": {"ORTG": 104.2, "DRTG": 105.0, "PACE": 83.1},
            "Las Vegas Aces": {"ORTG": 108.5, "DRTG": 100.3, "PACE": 82.9},
            "Los Angeles Sparks": {"ORTG": 98.1, "DRTG": 103.2, "PACE": 80.6},
            "Minnesota Lynx": {"ORTG": 106.2, "DRTG": 98.1, "PACE": 81.3},
            "New York Liberty": {"ORTG": 107.9, "DRTG": 97.5, "PACE": 80.9},
            "Phoenix Mercury": {"ORTG": 101.2, "DRTG": 102.8, "PACE": 82.4},
            "Portland Fire": {"ORTG": 99.4, "DRTG": 102.5, "PACE": 81.1},
            "Seattle Storm": {"ORTG": 103.0, "DRTG": 99.2, "PACE": 81.7},
            "Toronto Tempo": {"ORTG": 100.5, "DRTG": 101.8, "PACE": 80.8},
            "Washington Mystics": {"ORTG": 98.9, "DRTG": 102.1, "PACE": 80.5}
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
            "Real Madrid": {"ORTG": 119.5, "DRTG": 105.2, "PACE": 75.8},
            "Unicaja Malaga": {"ORTG": 115.8, "DRTG": 107.2, "PACE": 76.5},
            "Valencia Basket": {"ORTG": 113.4, "DRTG": 110.1, "PACE": 78.0},
            "Zaragoza": {"ORTG": 107.9, "DRTG": 112.1, "PACE": 76.6}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.5, "hca_bonus": 2.5,
        "teams": {
            "AS Monaco": {"ORTG": 117.2, "DRTG": 104.1, "PACE": 74.9},
            "Cholet": {"ORTG": 111.5, "DRTG": 110.2, "PACE": 76.5},
            "Dijon": {"ORTG": 109.1, "DRTG": 109.8, "PACE": 74.2},
            "JL Bourg": {"ORTG": 110.2, "DRTG": 108.1, "PACE": 74.5},
            "Le Mans": {"ORTG": 112.0, "DRTG": 110.8, "PACE": 75.9},
            "LDLC ASVEL": {"ORTG": 112.1, "DRTG": 109.4, "PACE": 75.3},
            "Nanterre 92": {"ORTG": 113.1, "DRTG": 108.4, "PACE": 76.0},
            "Paris Basketball": {"ORTG": 115.4, "DRTG": 107.9, "PACE": 77.2},
            "SIG Strasbourg": {"ORTG": 109.5, "DRTG": 109.5, "PACE": 75.8}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.2, "avg_ortg": 111.2, "hca_bonus": 2.5,
        "teams": {
            "ALBA Berlin": {"ORTG": 112.4, "DRTG": 110.2, "PACE": 79.1},
            "Bamberg Baskets": {"ORTG": 113.5, "DRTG": 111.4, "PACE": 78.8},
            "FC Bayern Munich": {"ORTG": 118.1, "DRTG": 105.9, "PACE": 77.4},
            "MHP Riesen Ludwigsburg": {"ORTG": 111.8, "DRTG": 109.4, "PACE": 77.0},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 106.8, "PACE": 76.9},
            "ratiopharm ulm": {"ORTG": 113.0, "DRTG": 111.1, "PACE": 78.5},
            "Telekom Baskets Bonn": {"ORTG": 112.9, "DRTG": 111.0, "PACE": 77.9},
            "Wuerzburg Baskets": {"ORTG": 113.6, "DRTG": 107.9, "PACE": 76.4}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.1, "avg_ortg": 111.8, "hca_bonus": 2.5,
        "teams": {
            "Bertram Derthona Tortona": {"ORTG": 109.8, "DRTG": 111.1, "PACE": 75.9},
            "EA7 Emporio Armani Milano": {"ORTG": 116.5, "DRTG": 106.2, "PACE": 75.1},
            "Germani Brescia": {"ORTG": 115.2, "DRTG": 108.1, "PACE": 76.5},
            "Openjobmetis Varese": {"ORTG": 110.8, "DRTG": 116.2, "PACE": 80.5},
            "Umana Reyer Venezia": {"ORTG": 111.4, "DRTG": 109.2, "PACE": 76.2},
            "UNAHOTELS Reggio Emilia": {"ORTG": 111.9, "DRTG": 111.2, "PACE": 75.6},
            "Virtus Segafredo Bologna": {"ORTG": 117.9, "DRTG": 108.4, "PACE": 76.1}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.2, "avg_ortg": 113.4, "hca_bonus": 2.5,
        "teams": {
            "Anadolu Efes": {"ORTG": 119.8, "DRTG": 107.5, "PACE": 76.8},
            "Bahcesehir Koleji": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 76.5},
            "Besiktas Emlakjet": {"ORTG": 112.5, "DRTG": 110.1, "PACE": 77.9},
            "Fenerbahce Beko": {"ORTG": 119.2, "DRTG": 106.9, "PACE": 76.4},
            "Galatasaray Ekmas": {"ORTG": 113.8, "DRTG": 113.2, "PACE": 77.5},
            "Pinar Karsiyaka": {"ORTG": 115.2, "DRTG": 112.4, "PACE": 78.1},
            "Tofas Bursa": {"ORTG": 113.1, "DRTG": 114.2, "PACE": 77.0},
            "Turk Telekom": {"ORTG": 110.4, "DRTG": 109.8, "PACE": 75.6}
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
            "Newcastle Eagles": {"ORTG": 107.9, "DRTG": 108.1, "PACE": 79.7}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 77.9, "avg_ortg": 107.5, "hca_bonus": 2.5,
        "teams": {
            "FC Porto": {"ORTG": 112.8, "DRTG": 105.1, "PACE": 78.1},
            "Ovarense": {"ORTG": 106.1, "DRTG": 108.5, "PACE": 77.6},
            "SL Benfica": {"ORTG": 114.2, "DRTG": 103.5, "PACE": 77.2},
            "Sporting CP": {"ORTG": 111.5, "DRTG": 106.9, "PACE": 78.4},
            "UD Oliveirense": {"ORTG": 107.4, "DRTG": 107.2, "PACE": 77.3}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.5, "avg_ortg": 113.2, "hca_bonus": 2.5,
        "teams": {
            "Cangrejeros de Santurce": {"ORTG": 112.5, "DRTG": 112.9, "PACE": 83.7},
            "Capitanes de Arecibo": {"ORTG": 116.8, "DRTG": 113.4, "PACE": 82.9},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.0},
            "Mets de Guaynabo": {"ORTG": 113.9, "DRTG": 112.0, "PACE": 83.2},
            "Piratas de Quebradillas": {"ORTG": 113.0, "DRTG": 111.4, "PACE": 82.6},
            "Vaqueros de Bayamón": {"ORTG": 111.2, "DRTG": 111.0, "PACE": 83.1}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.1, "avg_ortg": 109.8, "hca_bonus": 2.5,
        "teams": {
            "Auckland Tuatara": {"ORTG": 112.1, "DRTG": 108.2, "PACE": 84.5},
            "Canterbury Rams": {"ORTG": 114.2, "DRTG": 106.5, "PACE": 83.8},
            "Franklin Bulls": {"ORTG": 110.1, "DRTG": 109.5, "PACE": 84.0},
            "Taranaki Airs": {"ORTG": 113.5, "DRTG": 111.0, "PACE": 85.8},
            "Wellington Saints": {"ORTG": 114.9, "DRTG": 111.0, "PACE": 85.2}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.2, "avg_ortg": 110.1, "hca_bonus": 2.5,
        "teams": {
            "AEK Athens": {"ORTG": 110.2, "DRTG": 112.5, "PACE": 75.1},
            "Aris Salonika": {"ORTG": 106.5, "DRTG": 105.9, "PACE": 73.8},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 73.5},
            "Panathinaikos": {"ORTG": 120.4, "DRTG": 103.2, "PACE": 73.9},
            "Peristeri": {"ORTG": 108.5, "DRTG": 110.4, "PACE": 74.8},
            "Promitheas Patras": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 76.0}
        }
    },
    "Japan (B.League)": {
        "avg_pace": 75.1, "avg_ortg": 108.4, "hca_bonus": 2.0,
        "teams": {
            "Alvark Tokyo": {"ORTG": 114.2, "DRTG": 101.5, "PACE": 73.9},
            "Chiba Jets": {"ORTG": 112.8, "DRTG": 106.2, "PACE": 77.4},
            "Ryukyu Golden Kings": {"ORTG": 111.9, "DRTG": 105.4, "PACE": 74.8},
            "Utsunomiya Brex": {"ORTG": 113.5, "DRTG": 100.8, "PACE": 73.2},
            "Nagoya Diamond Dolphins": {"ORTG": 110.4, "DRTG": 107.1, "PACE": 76.5}
        }
    },
    "China (CBA)": {
        "avg_pace": 88.5, "avg_ortg": 111.2, "hca_bonus": 3.0,
        "teams": {
            "Guangdong Southern Tigers": {"ORTG": 116.4, "DRTG": 109.1, "PACE": 91.2},
            "Liaoning Flying Leopards": {"ORTG": 115.1, "DRTG": 104.2, "PACE": 87.5},
            "Xinjiang Flying Tigers": {"ORTG": 112.8, "DRTG": 105.6, "PACE": 88.1},
            "Zhejiang Golden Bulls": {"ORTG": 117.0, "DRTG": 107.8, "PACE": 89.0}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 82.8, "avg_ortg": 111.4, "hca_bonus": 2.5,
        "teams": {
            "Edmonton Stingers": {"ORTG": 111.5, "DRTG": 110.2, "PACE": 83.0},
            "Niagara River Lions": {"ORTG": 114.5, "DRTG": 109.2, "PACE": 82.1},
            "Scarborough Shooting Stars": {"ORTG": 112.4, "DRTG": 112.0, "PACE": 82.9},
            "Vancouver Bandits": {"ORTG": 113.1, "DRTG": 110.8, "PACE": 83.5},
            "Winnipeg Sea Bears": {"ORTG": 113.8, "DRTG": 115.2, "PACE": 84.6}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.2, "avg_ortg": 105.4, "hca_bonus": 2.5,
        "teams": {
            "Flyers Wels": {"ORTG": 107.5, "DRTG": 104.9, "PACE": 76.5},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 75.9},
            "Swans Gmunden": {"ORTG": 110.2, "DRTG": 102.1, "PACE": 75.8},
            "UBSC Graz": {"ORTG": 105.4, "DRTG": 106.4, "PACE": 76.8}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 77.4, "avg_ortg": 108.1, "hca_bonus": 2.5,
        "teams": {
            "BK Decin": {"ORTG": 107.8, "DRTG": 108.5, "PACE": 77.6},
            "BK Opava": {"ORTG": 109.4, "DRTG": 107.2, "PACE": 76.9},
            "ERA Nymburk": {"ORTG": 116.5, "DRTG": 101.4, "PACE": 78.1},
            "Sluneta Usti nad Labem": {"ORTG": 110.2, "DRTG": 109.1, "PACE": 77.1}
        }
    },
    "Israel (Winner League)": {
        "avg_pace": 78.0, "avg_ortg": 112.5, "hca_bonus": 2.5,
        "teams": {
            "Hapoel Jerusalem": {"ORTG": 113.4, "DRTG": 108.2, "PACE": 76.9},
            "Hapoel Tel Aviv": {"ORTG": 116.8, "DRTG": 110.4, "PACE": 79.2},
            "Maccabi Tel Aviv": {"ORTG": 120.1, "DRTG": 109.5, "PACE": 78.5},
            "Hapoel Holon": {"ORTG": 110.5, "DRTG": 109.9, "PACE": 77.1}
        }
    },
    "Belgium (BNXT League)": {
        "avg_pace": 74.9, "avg_ortg": 106.2, "hca_bonus": 2.5,
        "teams": {
            "Filou Oostende": {"ORTG": 112.5, "DRTG": 101.4, "PACE": 74.1},
            "Telenet Giants Antwerp": {"ORTG": 109.1, "DRTG": 105.8, "PACE": 75.4},
            "Hubo Limburg United": {"ORTG": 105.8, "DRTG": 104.9, "PACE": 74.0},
            "Spirou Charleroi": {"ORTG": 104.2, "DRTG": 106.8, "PACE": 75.9}
        }
    }
}

# =========================================================================
# CONTROL SIDEBAR UI
# =========================================================================
selected_league_name = st.sidebar.selectbox("Active Competition Matrix", sorted(GLOBAL_LEAGUE_DATABASE.keys()))

LEAGUE_CONTEXT = GLOBAL_LEAGUE_DATABASE[selected_league_name]
LEAGUE_AVG_PACE = LEAGUE_CONTEXT["avg_pace"]
LEAGUE_AVG_ORTG = LEAGUE_CONTEXT["avg_ortg"]
HCA_BONUS = LEAGUE_CONTEXT["hca_bonus"]
TEAM_DATABASE = LEAGUE_CONTEXT["teams"]

st.sidebar.markdown("---")
st.sidebar.markdown("**Advanced Data Lineage:**")
if selected_league_name in ["NBA", "WNBA"]:
    st.sidebar.caption("📊 Sourced via Basketball-Reference.com")
else:
    st.sidebar.caption("🌍 Sourced via RealGM.com International Matrix")

# =========================================================================
# MAIN INTERFACE MATCHUP SELECTION
# =========================================================================
st.subheader(f"🏟️ Competition Setup: {selected_league_name}")

col1, col2 = st.columns(2)
with col1:
    home_team = st.selectbox("🏡 Select Home Team Unit", sorted(TEAM_DATABASE.keys()), index=0)
    h_ortg = float(TEAM_DATABASE[home_team]["ORTG"])
    h_drtg = float(TEAM_DATABASE[home_team]["DRTG"])
    h_pace = float(TEAM_DATABASE[home_team]["PACE"])

with col2:
    away_team = st.selectbox("✈️ Select Away Team Unit", sorted(TEAM_DATABASE.keys()), index=1 if len(TEAM_DATABASE) > 1 else 0)
    a_ortg = float(TEAM_DATABASE[away_team]["ORTG"])
    a_drtg = float(TEAM_DATABASE[away_team]["DRTG"])
    a_pace = float(TEAM_DATABASE[away_team]["PACE"])

st.markdown("---")

# Initialize persistent session state properties
if 'calculated' not in st.session_state:
    st.session_state.calculated = False
    st.session_state.summary_df = None
    st.session_state.winner_verdict = ""
    st.session_state.last_matchup_signature = ""

current_signature = f"{selected_league_name}_{home_team}_{away_team}"

# Reset view logic safely if teams change
if st.session_state.last_matchup_signature != current_signature:
    st.session_state.calculated = False
    st.session_state.last_matchup_signature = current_signature

# Main Execution Switch
execute_simulation = st.button("⚡ Run Predictive Analysis", type="primary", use_container_width=True)

if execute_simulation:
    if home_team == away_team:
        st.warning("Please verify selections. A team cannot play an identical matchup variant against itself.")
        st.session_state.calculated = False
    else:
        # Step 1: Compute custom expected game pace factor
        predicted_pace = (h_pace + a_pace) - LEAGUE_AVG_PACE
        
        # Step 2: Calculate Projected Full-Time Points per 100 Possessions
        p_home_ft = ((h_ortg + a_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100) + HCA_BONUS
        p_away_ft = ((a_ortg + h_drtg) - LEAGUE_AVG_ORTG) * (predicted_pace / 100)
        
        # Step 3: Derive Half-Time Allocations
        p_home_ht = p_home_ft * 0.50
        p_away_ht = p_away_ft * 0.50
        
        # Step 4: Map Final Output Values & Assign Correct Outright Winners
        final_spread = p_away_ft - p_home_ft
        sign_string = "+" if final_spread > 0 else ""
        
        if p_home_ft > p_away_ft:
            st.session_state.winner_verdict = f"🏡 {home_team} (Home Winner Outright)"
        else:
            st.session_state.winner_verdict = f"✈️ {away_team} (Away Winner Outright)"
            
        # Step 5: Package into clean analytical summary Table DataFrame
        data_matrix = {
            "Team Segment": [f"🏡 {home_team} (Home)", f"✈️ {away_team} (Away)"],
            "Half Time (HT) Score": [f"{p_home_ht:.1f}", f"{p_away_ht:.1f}"],
            "Final Score (FT)": [f"{p_home_ft:.1f}", f"{p_away_ft:.1f}"],
            "Model Point Spread Line": [f"{final_spread:+.1f}", f"{-final_spread:+.1f}"]
        }
        
        st.session_state.summary_df = pd.DataFrame(data_matrix)
        st.session_state.calculated = True

# =========================================================================
# RENDER OUTPUT MATRIX TABLE VIEW WITH EXPLICIT WINNER UI
# =========================================================================
if st.session_state.calculated:
    st.subheader("📊 Model Projections Summary Matrix")
    
    # Explicit Winner Section Added directly to the UI
    st.markdown("### 🏆 Predicted Winner Matrix")
    st.info(f"**Direct Moneyline Outright Winner Projection:** {st.session_state.winner_verdict}")
    
    # Render table view format
    st.table(st.session_state.summary_df)
    
    # Extra Advanced Context block for review
    with st.expander("🔍 View Raw Advanced Analytical Variables Used"):
        st.markdown(f"**Expected Matchup Total Pace Line:** `{ (h_pace + a_pace) - LEAGUE_AVG_PACE :.2f}` possessions")
        st.markdown(f"**Baseline Competition Environment Average Pace:** `{LEAGUE_AVG_PACE}`")
        st.markdown(f"**Baseline Environment Average Offensive Rating:** `{LEAGUE_AVG_ORTG}`")
        st.markdown(f"**Applied Home Field/Court Advantage Value:** `+{HCA_BONUS}` points")
else:
    st.info("💡 Confirm assignments above and select **'Run Predictive Analysis'** to construct the dynamic data table.")
