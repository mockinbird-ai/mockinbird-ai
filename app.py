import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Pro Hoops Predictor", page_icon="🏀", layout="centered")
st.title("🏀 Pro Hoops Efficiency Prediction Engine")
st.markdown("### Google Sheets Advanced Spreadsheet Math Model Pipeline")
st.markdown("---")

# =========================================================================
# COMPREHENSIVE BASKETBALL REGISTRY DATABASE 
# Sourced from Basketball-Reference.com & RealGM.com Advanced Datasets
# =========================================================================
BASKETBALL_MASTER_DB = {
    "NBA": {
        "avg_pace": 99.2, "avg_ortg": 115.6, "source": "Basketball-Reference.com",
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
        "avg_pace": 81.4, "avg_ortg": 104.2, "source": "Basketball-Reference.com",
        "teams": {
            "Atlanta Dream": {"ORTG": 101.5, "DRTG": 102.8, "PACE": 80.4},
            "Chicago Sky": {"ORTG": 99.2, "DRTG": 104.1, "PACE": 81.8},
            "Connecticut Sun": {"ORTG": 103.4, "DRTG": 98.5, "PACE": 79.1},
            "Dallas Wings": {"ORTG": 105.1, "DRTG": 106.4, "PACE": 83.2},
            "Indiana Fever": {"ORTG": 106.8, "DRTG": 105.9, "PACE": 82.7},
            "Las Vegas Aces": {"ORTG": 109.4, "DRTG": 102.1, "PACE": 83.5},
            "Los Angeles Sparks": {"ORTG": 98.7, "DRTG": 107.5, "PACE": 81.0},
            "Minnesota Lynx": {"ORTG": 107.2, "DRTG": 100.4, "PACE": 80.6},
            "New York Liberty": {"ORTG": 108.9, "DRTG": 101.2, "PACE": 81.3},
            "Phoenix Mercury": {"ORTG": 102.6, "DRTG": 104.8, "PACE": 82.1},
            "Seattle Storm": {"ORTG": 104.0, "DRTG": 101.9, "PACE": 81.9},
            "Washington Mystics": {"ORTG": 100.8, "DRTG": 105.2, "PACE": 80.2}
        }
    },
    "Spain (Liga ACB)": {
        "avg_pace": 76.8, "avg_ortg": 111.4, "source": "RealGM.com",
        "teams": {
            "FC Barcelona": {"ORTG": 115.4, "DRTG": 107.2, "PACE": 77.5},
            "Baskonia": {"ORTG": 112.1, "DRTG": 111.0, "PACE": 76.4},
            "Girona": {"ORTG": 104.8, "DRTG": 109.5, "PACE": 75.9},
            "Manresa": {"ORTG": 108.9, "DRTG": 111.2, "PACE": 78.1},
            "Real Madrid": {"ORTG": 118.2, "DRTG": 106.1, "PACE": 76.0},
            "Unicaja Malaga": {"ORTG": 116.1, "DRTG": 106.8, "PACE": 76.9},
            "Valencia Basket": {"ORTG": 114.0, "DRTG": 109.4, "PACE": 77.8}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.5, "avg_ortg": 109.8, "source": "RealGM.com",
        "teams": {
            "AS Monaco": {"ORTG": 116.5, "DRTG": 103.8, "PACE": 74.2},
            "Dijon": {"ORTG": 108.4, "DRTG": 109.1, "PACE": 73.9},
            "JL Bourg": {"ORTG": 111.0, "DRTG": 107.5, "PACE": 74.8},
            "LDLC ASVEL": {"ORTG": 113.2, "DRTG": 109.0, "PACE": 75.1},
            "Paris Basketball": {"ORTG": 114.9, "DRTG": 107.2, "PACE": 76.8}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.4, "avg_ortg": 111.5, "source": "RealGM.com",
        "teams": {
            "ALBA Berlin": {"ORTG": 111.8, "DRTG": 110.5, "PACE": 79.0},
            "FC Bayern Munich": {"ORTG": 117.5, "DRTG": 106.2, "PACE": 77.6},
            "Niners Chemnitz": {"ORTG": 113.9, "DRTG": 107.1, "PACE": 76.8},
            "ratiopharm ulm": {"ORTG": 112.4, "DRTG": 111.8, "PACE": 78.2},
            "Telekom Baskets Bonn": {"ORTG": 113.1, "DRTG": 110.9, "PACE": 77.5}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.2, "avg_ortg": 112.0, "source": "RealGM.com",
        "teams": {
            "EA7 Emporio Armani Milano": {"ORTG": 115.9, "DRTG": 106.8, "PACE": 74.9},
            "Germani Brescia": {"ORTG": 114.8, "DRTG": 108.5, "PACE": 76.2},
            "Umana Reyer Venezia": {"ORTG": 110.9, "DRTG": 109.4, "PACE": 75.8},
            "Virtus Segafredo Bologna": {"ORTG": 117.2, "DRTG": 107.9, "PACE": 76.0}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 78.0, "avg_ortg": 106.8, "source": "RealGM.com",
        "teams": {
            "FC Porto": {"ORTG": 111.9, "DRTG": 104.8, "PACE": 78.2},
            "Ovarense": {"ORTG": 105.4, "DRTG": 107.9, "PACE": 77.5},
            "SL Benfica": {"ORTG": 113.5, "DRTG": 103.1, "PACE": 77.4},
            "Sporting CP": {"ORTG": 110.8, "DRTG": 106.2, "PACE": 78.6}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.4, "avg_ortg": 113.1, "source": "RealGM.com",
        "teams": {
            "Anadolu Efes": {"ORTG": 118.9, "DRTG": 107.2, "PACE": 76.9},
            "Besiktas Emlakjet": {"ORTG": 111.8, "DRTG": 109.5, "PACE": 77.6},
            "Fenerbahce Beko": {"ORTG": 118.5, "DRTG": 106.4, "PACE": 76.5},
            "Galatasaray Ekmas": {"ORTG": 113.2, "DRTG": 112.8, "PACE": 77.2}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.2, "avg_ortg": 112.8, "source": "RealGM.com",
        "teams": {
            "Cangrejeros de Santurce": {"ORTG": 112.1, "DRTG": 112.4, "PACE": 83.5},
            "Capitanes de Arecibo": {"ORTG": 116.2, "DRTG": 113.0, "PACE": 82.6},
            "Gigantes de Carolina": {"ORTG": 113.8, "DRTG": 112.1, "PACE": 83.8},
            "Mets de Guaynabo": {"ORTG": 113.5, "DRTG": 111.8, "PACE": 83.0}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.5, "avg_ortg": 110.2, "source": "RealGM.com",
        "teams": {
            "Auckland Tuatara": {"ORTG": 112.5, "DRTG": 108.6, "PACE": 84.9},
            "Canterbury Rams": {"ORTG": 114.8, "DRTG": 106.1, "PACE": 84.1},
            "Taranaki Airs": {"ORTG": 113.9, "DRTG": 111.4, "PACE": 86.2},
            "Wellington Saints": {"ORTG": 115.2, "DRTG": 111.2, "PACE": 85.5}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.5, "avg_ortg": 110.5, "source": "RealGM.com",
        "teams": {
            "AEK Athens": {"ORTG": 109.8, "DRTG": 112.1, "PACE": 75.3},
            "Aris Salonika": {"ORTG": 106.1, "DRTG": 105.4, "PACE": 74.0},
            "Olympiacos": {"ORTG": 119.5, "DRTG": 102.5, "PACE": 73.8},
            "Panathinaikos": {"ORTG": 120.1, "DRTG": 102.9, "PACE": 74.2}
        }
    },
    "Japan (B.League)": {
        "avg_pace": 75.4, "avg_ortg": 108.1, "source": "RealGM.com",
        "teams": {
            "Alvark Tokyo": {"ORTG": 113.9, "DRTG": 101.1, "PACE": 74.1},
            "Chiba Jets": {"ORTG": 112.4, "DRTG": 105.8, "PACE": 77.6},
            "Ryukyu Golden Kings": {"ORTG": 111.5, "DRTG": 105.0, "PACE": 75.0},
            "Utsunomiya Brex": {"ORTG": 113.1, "DRTG": 100.4, "PACE": 73.5}
        }
    },
    "China (CBA)": {
        "avg_pace": 88.2, "avg_ortg": 111.5, "source": "RealGM.com",
        "teams": {
            "Guangdong Southern Tigers": {"ORTG": 116.1, "DRTG": 108.8, "PACE": 90.8},
            "Liaoning Flying Leopards": {"ORTG": 114.8, "DRTG": 103.9, "PACE": 87.2},
            "Xinjiang Flying Tigers": {"ORTG": 112.5, "DRTG": 105.2, "PACE": 87.8},
            "Zhejiang Golden Bulls": {"ORTG": 116.8, "DRTG": 107.5, "PACE": 88.6}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 83.1, "avg_ortg": 111.8, "source": "RealGM.com",
        "teams": {
            "Edmonton Stingers": {"ORTG": 111.9, "DRTG": 110.5, "PACE": 83.4},
            "Niagara River Lions": {"ORTG": 114.8, "DRTG": 109.5, "PACE": 82.4},
            "Scarborough Shooting Stars": {"ORTG": 112.8, "DRTG": 112.4, "PACE": 83.2},
            "Vancouver Bandits": {"ORTG": 113.5, "DRTG": 111.2, "PACE": 83.8}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.5, "avg_ortg": 105.8, "source": "RealGM.com",
        "teams": {
            "Flyers Wels": {"ORTG": 107.1, "DRTG": 104.5, "PACE": 76.8},
            "Klosterneuburg Dukes": {"ORTG": 105.8, "DRTG": 105.4, "PACE": 76.2},
            "Swans Gmunden": {"ORTG": 109.8, "DRTG": 101.8, "PACE": 76.1},
            "UBSC Graz": {"ORTG": 105.0, "DRTG": 106.0, "PACE": 77.1}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 77.8, "avg_ortg": 108.5, "source": "RealGM.com",
        "teams": {
            "BK Decin": {"ORTG": 108.2, "DRTG": 108.9, "PACE": 78.0},
            "BK Opava": {"ORTG": 109.8, "DRTG": 107.6, "PACE": 77.3},
            "ERA Nymburk": {"ORTG": 116.9, "DRTG": 101.8, "PACE": 78.5},
            "Sluneta Usti nad Labem": {"ORTG": 110.6, "DRTG": 109.5, "PACE": 77.5}
        }
    },
    "Israel (Winner League)": {
        "avg_pace": 78.4, "avg_ortg": 112.9, "source": "RealGM.com",
        "teams": {
            "Hapoel Jerusalem": {"ORTG": 113.8, "DRTG": 108.6, "PACE": 77.3},
            "Hapoel Tel Aviv": {"ORTG": 117.2, "DRTG": 110.8, "PACE": 79.6},
            "Maccabi Tel Aviv": {"ORTG": 120.5, "DRTG": 109.9, "PACE": 78.9},
            "Hapoel Holon": {"ORTG": 110.9, "DRTG": 110.3, "PACE": 77.5}
        }
    },
    "Belgium (BNXT League)": {
        "avg_pace": 75.2, "avg_ortg": 106.5, "source": "RealGM.com",
        "teams": {
            "Filou Oostende": {"ORTG": 112.9, "DRTG": 101.8, "PACE": 74.5},
            "Telenet Giants Antwerp": {"ORTG": 109.5, "DRTG": 106.2, "PACE": 75.8},
            "Hubo Limburg United": {"ORTG": 106.2, "DRTG": 105.3, "PACE": 74.4},
            "Spirou Charleroi": {"ORTG": 104.6, "DRTG": 107.2, "PACE": 76.3}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 79.8, "avg_ortg": 107.2, "source": "RealGM.com",
        "teams": {
            "Cheshire Phoenix": {"ORTG": 111.9, "DRTG": 107.3, "PACE": 80.3},
            "Leicester Riders": {"ORTG": 108.6, "DRTG": 106.9, "PACE": 79.4},
            "London Lions": {"ORTG": 115.2, "DRTG": 101.6, "PACE": 80.6},
            "Newcastle Eagles": {"ORTG": 108.3, "DRTG": 108.5, "PACE": 80.1}
        }
    }
}

# =========================================================================
# UI REGION: LEAGUE SELECTION & TEAM CONFIGURATIONS
# =========================================================================
selected_db = st.sidebar.selectbox("🏀 Select Active Basketball League", list(BASKETBALL_MASTER_DB.keys()))
cfg = BASKETBALL_MASTER_DB[selected_db]

st.sidebar.caption(f"Data Lineage Pipeline: {cfg['source']}")

st.subheader(f"🏟️ Setup Matchup Matrix Summary: {selected_db}")
col_h, col_a = st.columns(2)
with col_h:
    home = st.selectbox("🏡 Select Home Team Unit", sorted(cfg["teams"].keys()), index=0)
with col_a:
    away = st.selectbox("✈️ Select Away Team Unit", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

if home == away:
    st.error("⚠️ Select two unique matching teams to generate score lines.")
else:
    # -------------------------------------------------------------------------
    # EMBEDDED SPREADSHEET FORMULA MATH ENGINE
    # -------------------------------------------------------------------------
    h_data, a_data = cfg["teams"][home], cfg["teams"][away]
    
    # 1. Predict the Game Pace: =(B8 + C8) - B1
    predicted_pace = (h_data["PACE"] + a_data["PACE"]) - cfg["avg_pace"]
    
    # 2. Predict the Home Score (With custom +2.5 HCA): =((B6 + C7) - B2) * (B10 / 100) + 2.5
    projected_home_ft = ((h_data["ORTG"] + a_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100) + 2.5
    
    # 3. Predict the Away Score: =((C6 + B7) - B2) * (B10 / 100)
    projected_away_ft = ((a_data["ORTG"] + h_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100)
    
    # 4. Calculate Model Spread Line: =C12 - B12
    model_spread = projected_away_ft - projected_home_ft
    
    # Consensus Outputs
    winner_team = home if projected_home_ft > projected_away_ft else away
    winner_icon = "🏡" if winner_team == home else "✈️"

    # -------------------------------------------------------------------------
    # UI OUTRIGHT SELECTION CONTAINER DISPLAY
    # -------------------------------------------------------------------------
    st.markdown("## 🏆 Model Consensus Selection")
    with st.container():
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="Outright Moneyline Winner", value=f"{winner_icon} {winner_team}")
        with m2:
            st.metric(label="Model Calculated Line Spread", value=f"{winner_team} {abs(model_spread):-.1f}")

    st.markdown("---")

    # -------------------------------------------------------------------------
    # UI SUMMARY MATRIX TABLE DISPLAY
    # -------------------------------------------------------------------------
    st.subheader("📊 Performance Projections Summary Matrix Table")
    
    matrix_df = pd.DataFrame({
        "Team Segment": [f"🏡 {home} (Home)", f"✈️ {away} (Away)"],
        "Final Projected Score": [f"{projected_home_ft:.1f}", f"{projected_away_ft:.1f}"],
        "Spread Line Derivative": [f"{model_spread:+.1f}", f"{-model_spread:+.1f}"]
    })
    
    st.table(matrix_df)

    # -------------------------------------------------------------------------
    # SPREADSHEET AUDIT EXPANDER
    # -------------------------------------------------------------------------
    with st.expander("🔍 View Cell Variables & Sheet Calculation Logs"):
        st.markdown(f"#### League Baseline Matrix Assumptions")
        st.text(f"Cell B1 (League Average Pace): {cfg['avg_pace']}")
        st.text(f"Cell B2 (League Average Offense): {cfg['avg_ortg']}")
        
        st.markdown("---")
        st.markdown(f"#### Active Raw Advanced Metrics Dataset Breakdown")
        col_sh1, col_sh2 = st.columns(2)
        with col_sh1:
            st.markdown(f"**🏡 {home} (Column B Variables)**")
            st.text(f"Cell B6 (Offensive Rating): {h_data['ORTG']}")
            st.text(f"Cell B7 (Defensive Rating): {h_data['DRTG']}")
            st.text(f"Cell B8 (Pace): {h_data['PACE']}")
        with col_sh2:
            st.markdown(f"**✈️ {away} (Column C Variables)**")
            st.text(f"Cell C6 (Offensive Rating): {a_data['ORTG']}")
            st.text(f"Cell C7 (Defensive Rating): {a_data['DRTG']}")
            st.text(f"Cell C8 (Pace): {a_data['PACE']}")
            
        st.markdown("---")
        st.markdown("#### Formula Step Calculation Outputs")
        st.markdown(f"* Predicted Dynamic Game Pace: `{predicted_pace:.1f}` possessions")
        st.markdown(f"* Pure Spread Output: `{model_spread:+.1f}` points")
