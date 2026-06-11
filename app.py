import streamlit as st
import pandas as pd

# Page Setup
st.set_page_config(page_title="Pro Hoops Predictor 2026", page_icon="🏀", layout="centered")
st.title("🏀 Pro Hoops 2026 Matrix Prediction Engine")
st.markdown("### Google Sheets Advanced Spreadsheet Math Pipeline (v2026.1)")
st.markdown("---")

# =========================================================================
# COMPREHENSIVE BASKETBALL REGISTRY DATABASE (UPDATED TO 2026 STATUS)
# Sourced from Basketball-Reference.com & RealGM.com 2026 Baselines
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
        "avg_pace": 81.6, "avg_ortg": 104.5, "source": "Basketball-Reference.com",
        "teams": {
            "Atlanta Dream": {"ORTG": 102.1, "DRTG": 102.5, "PACE": 80.6},
            "Chicago Sky": {"ORTG": 98.5, "DRTG": 104.4, "PACE": 81.5},
            "Connecticut Sun": {"ORTG": 102.8, "DRTG": 99.1, "PACE": 79.4},
            "Dallas Wings": {"ORTG": 105.4, "DRTG": 106.1, "PACE": 82.9},
            "Golden State Valkyries": {"ORTG": 104.2, "DRTG": 101.8, "PACE": 81.1},
            "Indiana Fever": {"ORTG": 106.2, "DRTG": 105.5, "PACE": 82.4},
            "Las Vegas Aces": {"ORTG": 109.1, "DRTG": 102.5, "PACE": 83.1},
            "Los Angeles Sparks": {"ORTG": 99.1, "DRTG": 107.1, "PACE": 81.3},
            "Minnesota Lynx": {"ORTG": 107.8, "DRTG": 100.1, "PACE": 80.9},
            "New York Liberty": {"ORTG": 108.5, "DRTG": 101.5, "PACE": 81.6},
            "Phoenix Mercury": {"ORTG": 103.1, "DRTG": 104.2, "PACE": 82.5},
            "Portland Fire": {"ORTG": 101.6, "DRTG": 103.9, "PACE": 82.0},
            "Seattle Storm": {"ORTG": 103.5, "DRTG": 102.4, "PACE": 81.4},
            "Toronto Tempo": {"ORTG": 102.9, "DRTG": 103.2, "PACE": 81.8},
            "Washington Mystics": {"ORTG": 101.2, "DRTG": 104.8, "PACE": 80.5}
        }
    },
    "Spain (Liga ACB)": {
        "avg_pace": 76.9, "avg_ortg": 111.8, "source": "RealGM.com",
        "teams": {
            "FC Barcelona": {"ORTG": 115.8, "DRTG": 107.5, "PACE": 77.2},
            "Baskonia": {"ORTG": 112.5, "DRTG": 111.4, "PACE": 76.8},
            "Girona": {"ORTG": 105.1, "DRTG": 109.9, "PACE": 76.1},
            "Manresa": {"ORTG": 109.2, "DRTG": 111.5, "PACE": 78.4},
            "Real Madrid": {"ORTG": 118.6, "DRTG": 106.5, "PACE": 76.3},
            "Unicaja Malaga": {"ORTG": 116.5, "DRTG": 107.2, "PACE": 77.1},
            "Valencia Basket": {"ORTG": 114.4, "DRTG": 109.8, "PACE": 78.0}
        }
    },
    "France (LNB Élite)": {
        "avg_pace": 75.8, "avg_ortg": 110.2, "source": "RealGM.com",
        "teams": {
            "AS Monaco": {"ORTG": 116.9, "DRTG": 104.1, "PACE": 74.5},
            "Dijon": {"ORTG": 108.8, "DRTG": 109.5, "PACE": 74.2},
            "JL Bourg": {"ORTG": 111.4, "DRTG": 107.9, "PACE": 75.1},
            "LDLC ASVEL": {"ORTG": 113.6, "DRTG": 109.4, "PACE": 75.4},
            "Paris Basketball": {"ORTG": 115.2, "DRTG": 107.5, "PACE": 77.1}
        }
    },
    "Germany (easyCredit BBL)": {
        "avg_pace": 78.6, "avg_ortg": 111.9, "source": "RealGM.com",
        "teams": {
            "ALBA Berlin": {"ORTG": 112.1, "DRTG": 110.9, "PACE": 79.3},
            "FC Bayern Munich": {"ORTG": 117.9, "DRTG": 106.5, "PACE": 77.9},
            "Niners Chemnitz": {"ORTG": 114.2, "DRTG": 107.4, "PACE": 77.1},
            "ratiopharm ulm": {"ORTG": 112.8, "DRTG": 112.1, "PACE": 78.5},
            "Telekom Baskets Bonn": {"ORTG": 113.5, "DRTG": 111.2, "PACE": 77.8}
        }
    },
    "Italy (Lega Basket Serie A)": {
        "avg_pace": 76.5, "avg_ortg": 112.4, "source": "RealGM.com",
        "teams": {
            "EA7 Emporio Armani Milano": {"ORTG": 116.2, "DRTG": 107.1, "PACE": 75.2},
            "Germani Brescia": {"ORTG": 115.1, "DRTG": 108.9, "PACE": 76.5},
            "Umana Reyer Venezia": {"ORTG": 111.2, "DRTG": 109.8, "PACE": 76.1},
            "Virtus Segafredo Bologna": {"ORTG": 117.6, "DRTG": 108.2, "PACE": 76.3}
        }
    },
    "Portugal (Liga Betclic)": {
        "avg_pace": 78.3, "avg_ortg": 107.1, "source": "RealGM.com",
        "teams": {
            "FC Porto": {"ORTG": 112.2, "DRTG": 105.1, "PACE": 78.5},
            "Ovarense": {"ORTG": 105.8, "DRTG": 108.2, "PACE": 77.8},
            "SL Benfica": {"ORTG": 113.9, "DRTG": 103.5, "PACE": 77.7},
            "Sporting CP": {"ORTG": 111.2, "DRTG": 106.5, "PACE": 78.9}
        }
    },
    "Türkiye (BSL)": {
        "avg_pace": 77.6, "avg_ortg": 113.5, "source": "RealGM.com",
        "teams": {
            "Anadolu Efes": {"ORTG": 119.2, "DRTG": 107.5, "PACE": 77.1},
            "Besiktas Emlakjet": {"ORTG": 112.1, "DRTG": 109.8, "PACE": 77.9},
            "Fenerbahce Beko": {"ORTG": 118.9, "DRTG": 106.8, "PACE": 76.8},
            "Galatasaray Ekmas": {"ORTG": 113.5, "DRTG": 113.1, "PACE": 77.5}
        }
    },
    "Puerto Rico (BSN)": {
        "avg_pace": 83.5, "avg_ortg": 113.1, "source": "RealGM.com",
        "teams": {
            "Cangrejeros de Santurce": {"ORTG": 112.4, "DRTG": 112.8, "PACE": 83.8},
            "Capitanes de Arecibo": {"ORTG": 116.5, "DRTG": 113.4, "PACE": 82.9},
            "Gigantes de Carolina": {"ORTG": 114.1, "DRTG": 112.5, "PACE": 84.1},
            "Mets de Guaynabo": {"ORTG": 113.8, "DRTG": 112.1, "PACE": 83.3}
        }
    },
    "New Zealand (NBL)": {
        "avg_pace": 84.8, "avg_ortg": 110.5, "source": "RealGM.com",
        "teams": {
            "Auckland Tuatara": {"ORTG": 112.8, "DRTG": 108.9, "PACE": 85.2},
            "Canterbury Rams": {"ORTG": 115.1, "DRTG": 106.4, "PACE": 84.4},
            "Taranaki Airs": {"ORTG": 114.2, "DRTG": 111.8, "PACE": 86.5},
            "Wellington Saints": {"ORTG": 115.5, "DRTG": 111.5, "PACE": 85.8}
        }
    },
    "Greece (GBL)": {
        "avg_pace": 74.8, "avg_ortg": 110.8, "source": "RealGM.com",
        "teams": {
            "AEK Athens": {"ORTG": 110.1, "DRTG": 112.4, "PACE": 75.6},
            "Aris Salonika": {"ORTG": 106.4, "DRTG": 105.8, "PACE": 74.3},
            "Olympiacos": {"ORTG": 119.8, "DRTG": 102.8, "PACE": 74.1},
            "Panathinaikos": {"ORTG": 120.5, "DRTG": 103.2, "PACE": 74.5}
        }
    },
    "Japan (B.League)": {
        "avg_pace": 75.7, "avg_ortg": 108.4, "source": "RealGM.com",
        "teams": {
            "Alvark Tokyo": {"ORTG": 114.2, "DRTG": 101.4, "PACE": 74.4},
            "Chiba Jets": {"ORTG": 112.8, "DRTG": 106.1, "PACE": 77.9},
            "Ryukyu Golden Kings": {"ORTG": 111.8, "DRTG": 105.4, "PACE": 75.3},
            "Utsunomiya Brex": {"ORTG": 113.5, "DRTG": 100.8, "PACE": 73.8}
        }
    },
    "China (CBA)": {
        "avg_pace": 88.5, "avg_ortg": 111.9, "source": "RealGM.com",
        "teams": {
            "Guangdong Southern Tigers": {"ORTG": 116.5, "DRTG": 109.1, "PACE": 91.1},
            "Liaoning Flying Leopards": {"ORTG": 115.1, "DRTG": 104.2, "PACE": 87.5},
            "Xinjiang Flying Tigers": {"ORTG": 112.8, "DRTG": 105.5, "PACE": 88.1},
            "Zhejiang Golden Bulls": {"ORTG": 117.1, "DRTG": 107.9, "PACE": 88.9}
        }
    },
    "Canada (CEBL)": {
        "avg_pace": 83.4, "avg_ortg": 112.1, "source": "RealGM.com",
        "teams": {
            "Edmonton Stingers": {"ORTG": 112.2, "DRTG": 110.8, "PACE": 83.7},
            "Niagara River Lions": {"ORTG": 115.1, "DRTG": 109.8, "PACE": 82.7},
            "Scarborough Shooting Stars": {"ORTG": 113.1, "DRTG": 112.8, "PACE": 83.5},
            "Vancouver Bandits": {"ORTG": 113.8, "DRTG": 111.5, "PACE": 84.1}
        }
    },
    "Austria (Superliga)": {
        "avg_pace": 76.8, "avg_ortg": 106.1, "source": "RealGM.com",
        "teams": {
            "Flyers Wels": {"ORTG": 107.4, "DRTG": 104.8, "PACE": 77.1},
            "Klosterneuburg Dukes": {"ORTG": 106.1, "DRTG": 105.8, "PACE": 76.5},
            "Swans Gmunden": {"ORTG": 110.1, "DRTG": 102.1, "PACE": 76.4},
            "UBSC Graz": {"ORTG": 105.4, "DRTG": 106.4, "PACE": 77.4}
        }
    },
    "Czech Republic (NBL)": {
        "avg_pace": 78.1, "avg_ortg": 108.8, "source": "RealGM.com",
        "teams": {
            "BK Decin": {"ORTG": 108.5, "DRTG": 109.2, "PACE": 78.3},
            "BK Opava": {"ORTG": 110.1, "DRTG": 107.9, "PACE": 77.6},
            "ERA Nymburk": {"ORTG": 117.2, "DRTG": 102.1, "PACE": 78.8},
            "Sluneta Usti nad Labem": {"ORTG": 110.9, "DRTG": 109.8, "PACE": 77.8}
        }
    },
    "Israel (Winner League)": {
        "avg_pace": 78.7, "avg_ortg": 113.2, "source": "RealGM.com",
        "teams": {
            "Hapoel Jerusalem": {"ORTG": 114.1, "DRTG": 108.9, "PACE": 77.6},
            "Hapoel Tel Aviv": {"ORTG": 117.5, "DRTG": 111.1, "PACE": 79.9},
            "Maccabi Tel Aviv": {"ORTG": 120.8, "DRTG": 110.2, "PACE": 79.2},
            "Hapoel Holon": {"ORTG": 111.2, "DRTG": 110.6, "PACE": 77.8}
        }
    },
    "Belgium (BNXT League)": {
        "avg_pace": 75.5, "avg_ortg": 106.8, "source": "RealGM.com",
        "teams": {
            "Filou Oostende": {"ORTG": 113.2, "DRTG": 102.1, "PACE": 74.8},
            "Telenet Giants Antwerp": {"ORTG": 109.8, "DRTG": 106.5, "PACE": 76.1},
            "Hubo Limburg United": {"ORTG": 106.5, "DRTG": 105.6, "PACE": 74.7},
            "Spirou Charleroi": {"ORTG": 104.9, "DRTG": 107.5, "PACE": 76.6}
        }
    },
    "England (Super League Basketball)": {
        "avg_pace": 80.1, "avg_ortg": 107.5, "source": "RealGM.com",
        "teams": {
            "Cheshire Phoenix": {"ORTG": 112.2, "DRTG": 107.6, "PACE": 80.6},
            "Leicester Riders": {"ORTG": 108.9, "DRTG": 107.2, "PACE": 79.7},
            "London Lions": {"ORTG": 115.5, "DRTG": 101.9, "PACE": 80.9},
            "Newcastle Eagles": {"ORTG": 108.6, "DRTG": 108.8, "PACE": 80.4}
        }
    }
}

# =========================================================================
# UI REGION: DESIGN INTERFACE
# =========================================================================
selected_db = st.sidebar.selectbox("🏀 Select Active Basketball League", list(BASKETBALL_MASTER_DB.keys()))
cfg = BASKETBALL_MASTER_DB[selected_db]

st.sidebar.caption(f"2026 Data Engine Sourced via: {cfg['source']}")

st.subheader(f"🏟️ Setup Matchup Projections: {selected_db}")
col_h, col_a = st.columns(2)
with col_h:
    home = st.selectbox("🏡 Select Home Team", sorted(cfg["teams"].keys()), index=0)
with col_a:
    away = st.selectbox("✈️ Select Away Team", sorted(cfg["teams"].keys()), index=1 if len(cfg["teams"]) > 1 else 0)

# Initiate Action Button
st.markdown(" ")
initiate_analysis = st.button("🚀 Initiate Advanced Matchup Simulation", type="primary", use_container_width=True)
st.markdown("---")

if initiate_analysis:
    if home == away:
        st.error("⚠️ System Mapping Error: Select two unique teams to initiate analysis.")
    else:
        # Load Operational Team Metrics
        h_data, a_data = cfg["teams"][home], cfg["teams"][away]
        
        # 1. Predict Game Pace: (Home Pace + Away Pace) - League Average Pace
        predicted_pace = (h_data["PACE"] + a_data["PACE"]) - cfg["avg_pace"]
        
        # 2. Predict Home Score (Includes +2.5 Spreadsheet Home Court Factor)
        projected_home_ft = ((h_data["ORTG"] + a_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100) + 2.5
        
        # 3. Predict Away Score
        projected_away_ft = ((a_data["ORTG"] + h_data["DRTG"]) - cfg["avg_ortg"]) * (predicted_pace / 100)
        
        # 4. Calculate Point Spread Model Value
        model_spread = projected_away_ft - projected_home_ft
        
        # Output Logic Targets
        winner_team = home if projected_home_ft > projected_away_ft else away
        winner_icon = "🏡" if winner_team == home else "✈️"

        # -------------------------------------------------------------------------
        # DISPLAY SECTION: SIMULATION RESULT GENERATIONS
        # -------------------------------------------------------------------------
        st.markdown("## 🏆 Model Consensus Selections")
        m1, m2 = st.columns(2)
        with m1:
            st.metric(label="Outright Winner", value=f"{winner_icon} {winner_team}")
        with m2:
            st.metric(label="Calculated Model Point Spread Line", value=f"{winner_team} {abs(model_spread):-.1f}")

        st.markdown(" ")
        st.subheader("📊 Performance Projections Summary Matrix Table")
        
        matrix_df = pd.DataFrame({
            "Team Segment": [f"🏡 {home} (Home Team)", f"✈️ {away} (Away Team)"],
            "Final Score Projections": [f"{projected_home_ft:.1f}", f"{projected_away_ft:.1f}"],
            "Model Point Spread Line": [f"{model_spread:+.1f}", f"{-model_spread:+.1f}"]
        })
        
        st.table(matrix_df)

        # -------------------------------------------------------------------------
        # ADVANCED SPREADSHEET CELL LOGGER AUDIT EXPANDER
        # -------------------------------------------------------------------------
        with st.expander("🔍 View 2026 Cell Variables & Sheet Calculation Logs"):
            st.markdown(f"#### League Infrastructure Baseline (2026 Season Parameters)")
            st.text(f"Cell B1 (League Average Pace): {cfg['avg_pace']} possessions")
            st.text(f"Cell B2 (League Average Offense Rating): {cfg['avg_ortg']}")
            
            st.markdown("---")
            st.markdown(f"#### Active Raw Advanced Metrics Dataset Breakdown")
            col_sh1, col_sh2 = st.columns(2)
            with col_sh1:
                st.markdown(f"**🏡 {home} (Column B Variables)**")
                st.text(f"Cell B6 (Offensive Rating): {h_data['ORTG']}")
                st.text(f"Cell B7 (Defensive Rating): {h_data['DRTG']}")
                st.text(f"Cell B8 (Team Total Pace): {h_data['PACE']}")
            with col_sh2:
                st.markdown(f"**✈️ {away} (Column C Variables)**")
                st.text(f"Cell C6 (Offensive Rating): {a_data['ORTG']}")
                st.text(f"Cell C7 (Defensive Rating): {a_data['DRTG']}")
                st.text(f"Cell C8 (Team Total Pace): {a_data['PACE']}")
                
            st.markdown("---")
            st.markdown("#### Formula Step Calculation Outputs")
            st.markdown(f"* Predicted Dynamic Game Pace (Cell B10 Output): `{predicted_pace:.2f}` possessions")
            st.markdown(f"* Raw Sheet Spread Target (Cell B14 Output): `{model_spread:+.1f}` points")
else:
    st.info("💡 System Ready. Configure teams and click the button above to execute calculations.")
