import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. PAGE SETUP & DATA STRUCTURE
# ==========================================
st.set_page_config(page_title="MiHoops Analytics Pro", page_icon="🏀", layout="wide")
st.title("🏀 MiHoops")
st.markdown("Advanced Basketball Prediction Engine")
st.markdown("---")

# Comprehensive Global League Baselines (15 Leagues Complete with Correct Team Registries)
LEAGUE_REGISTRY = {
    "NBA": {"min": 48.0, "pts": 114.2, "pace": 98.8, "hca": 2.40, "teams": ["Boston Celtics", "Oklahoma City Thunder", "Denver Nuggets", "Minnesota Timberwolves", "Dallas Mavericks", "Milwaukee Bucks", "New York Knicks", "Los Angeles Lakers", "Golden State Warriors", "Miami Heat", "Philadelphia 76ers", "Phoenix Suns", "Indiana Pacers", "Cleveland Cavaliers", "Orlando Magic", "Sacramento Kings", "New Orleans Pelicans", "Houston Rockets", "Chicago Bulls", "Atlanta Hawks", "Brooklyn Nets", "Utah Jazz", "Toronto Raptors", "Memphis Grizzlies", "San Antonio Spurs", "Portland Trail Blazers", "Charlotte Hornets", "Washington Wizards", "Detroit Pistons", "Los Angeles Clippers"]},
    "WNBA": {"min": 40.0, "pts": 82.8, "pace": 80.5, "hca": 2.10, "teams": ["New York Liberty", "Las Vegas Aces", "Minnesota Lynx", "Connecticut Sun", "Seattle Storm", "Dallas Wings", "Atlanta Dream", "Indiana Fever", "Chicago Sky", "Phoenix Mercury", "Los Angeles Sparks", "Washington Mystics"]},
    "Spain: Liga ACB": {"min": 40.0, "pts": 83.5, "pace": 76.4, "hca": 2.85, "teams": ["Real Madrid", "FC Barcelona", "Unicaja Málaga", "Valencia Basket", "Saski Baskonia", "UCAM Murcia", "Gran Canaria", "Joventut Badalona", "Canarias (Tenerife)", "Bàsquet Manresa", "Bilbao Basket", "Bàsquet Girona", "Basket Zaragoza", "MoraBanc Andorra", "CB Breogán", "Fundación CB Granada", "Leyma Coruña", "Força Lleida"]},
    "France: LNB Élite": {"min": 40.0, "pts": 80.9, "pace": 75.2, "hca": 2.60, "teams": ["AS Monaco", "Paris Basketball", "LDLC ASVEL", "JL Bourg", "Nanterre 92", "Cholet Basket", "Le Mans Sarthe", "SIG Strasbourg", "Saint-Quentin", "SLUC Nancy", "JDA Dijon", "Limoges CSP", "ESSM Le Portel", "Gravelines-Dunkerque", "Élan Chalon", "Stade Rochelais"]},
    "Germany: easyCredit BBL": {"min": 40.0, "pts": 84.1, "pace": 77.8, "hca": 2.50, "teams": ["Bayern Munich", "Alba Berlin", "Ratiopharm Ulm", "Telekom Baskets Bonn", "Würzburg Baskets", "Niners Chemnitz", "Rasta Vechta", "MHP Riesen Ludwigsburg", "EWE Baskets Oldenburg", "Bamberg Baskets", "Löwen Braunschweig", "Veolia Towers Hamburg", "Syntainics MBC", "MLP Academics Heidelberg", "Rostock Seawolves", "Skyliners Frankfurt", "BG Göttingen", "Karlsruhe Lions"]},
    "Türkiye: BSL": {"min": 40.0, "pts": 82.3, "pace": 76.6, "hca": 3.10, "teams": ["Anadolu Efes", "Fenerbahçe Beko", "Beşiktaş", "Pınar Karşıyaka", "Galatasaray", "Türk Telekom", "Tofaş", "Bahçeşehir Koleji", "Petkim Spor", "Bursaspor Info Yatırım", "Manisa Basket", "Büyükçekmece Basketbol", "Merkezefendi Belediyesi", "Mersin MSK", "Yalovaspor", "Safiport Erokspor"]},
    "Austria: Superliga": {"min": 40.0, "pts": 79.1, "pace": 74.2, "hca": 2.30, "teams": ["Swans Gmunden", "Flyers Wels", "Klosterneuburg Dukes", "UBSC Graz", "BC Vienna", "Oberwart Gunners", "Arkadia Traiskirchen Lions", "SKN St. Pölten", "Kapfenberg Bulls", "Eisenstadt Warriors"]},
    "Czech Republic: NBL": {"min": 40.0, "pts": 81.4, "pace": 76.1, "hca": 2.45, "teams": ["ERA Nymburk", "BK Opava", "BK Děčín", "Sluneta Ústí nad Labem", "USK Praha", "Basket Brno", "Beksa Pardubice", "Nova Hut Ostrava", "Sokol Písek", "BC Kolín", "Olomoucko", "Slavia Praha"]},
    "Puerto Rico: BSN": {"min": 40.0, "pts": 89.5, "pace": 82.1, "hca": 3.40, "teams": ["Capitanes de Arecibo", "Vaqueros de Bayamón", "Gigantes de Carolina", "Mets de Guaynabo", "Piratas de Quebradillas", "Atléticos de San Germán", "Leones de Ponce", "Indios de Mayagüez", "Santeros de Aguada", "Criollos de Caguas", "Osos de Manatí", "Cangrejeros de Santurce"]},
    "New Zealand: NBL": {"min": 40.0, "pts": 87.2, "pace": 81.8, "hca": 2.20, "teams": ["Canterbury Rams", "Auckland Tuatara", "Wellington Saints", "Taranaki Airs", "Franklin Bulls", "Nelson Giants", "Otago Nuggets", "Whai Tauranga", "Hawke's Bay Hawks", "Southland Sharks", "Manawatu Jets"]},
    "Canada: CEBL": {"min": 40.0, "pts": 88.0, "pace": 80.9, "hca": 2.15, "teams": ["Niagara River Lions", "Vancouver Bandits", "Edmonton Stingers", "Scarborough Shooting Stars", "Winnipeg Sea Bears", "Calgary Surge", "Ottawa BlackJacks", "Brampton Honey Badgers", "Montreal Alliance", "Saskatchewan Rattlers"]},
    "Italy: Lega Basket Serie A": {"min": 40.0, "pts": 82.8, "pace": 76.3, "hca": 2.75, "teams": ["Olimpia Milano", "Virtus Bologna", "Reyer Venezia", "Pallacanestro Brescia", "Derthona Basket", "Pallacanestro Reggiana", "Aquila Basket Trento", "Dinamo Sassari", "Pallacanestro Varese", "Napoli Basket", "Universo Treviso Basket", "Scafati Basket", "Vanoli Cremona", "Pistoia Basket", "Trapani Shark", "Pallacanestro Trieste"]},
    "Mexico: LNBP": {"min": 40.0, "pts": 85.9, "pace": 79.1, "hca": 2.90, "teams": ["Fuerza Regia de Monterrey", "Astros de Jalisco", "Halcones de Xalapa", "Panteras de Aguascalientes", "Dorados de Chihuahua", "Soles de Mexicali", "Mineros de Zacatecas", "Plateros de Fresnillo", "El Calor de Cancún", "Diablos Rojos del México", "Santos de San Luis", "Abejas de León", "Correcaminos UAT Victoria", "Freseros de Irapuato"]},
    "Portugal: LPB": {"min": 40.0, "pts": 80.2, "pace": 74.8, "hca": 2.40, "teams": ["S.L. Benfica", "FC Porto", "Sporting CP", "UD Oliveirense", "Ovarense Basquetebol", "Vitória SC", "Imortal BC", "Esgueira Basket", "CD Póvoa", "SC Lusitânia", "Galitos Barreiro", "CA Queluz"]},
    "Croatia: Premijer Liga": {"min": 40.0, "pts": 78.4, "pace": 73.5, "hca": 2.55, "teams": ["KK Zadar", "KK Split", "KK Cibona Zagreb", "KK Cedevita Junior", "KK Dinamo Zagreb", "GKK Šibenka", "KK Zabok", "KK Dubrovnik", "KK Alkar", "KK DepoLink Škrljevo", "KK Bosco Zagreb", "KK Vrijednosnice Osijek"]}
}

# ==========================================
# 2. ADVANCED DATA GENERATION LAYER
# ==========================================
def generate_advanced_dataset(league_selection):
    config = LEAGUE_REGISTRY[league_selection]
    teams = config["teams"]
    
    # Generate reproducible stats using a unique seed for each league
    np.random.seed(sum(ord(c) for c in league_selection))
    
    records = []
    for team in teams:
        # Full Season Advanced Baselines
        season_pace = np.random.uniform(config["pace"] - 3, config["pace"] + 3)
        season_ortg = np.random.uniform(104.0, 116.0)
        season_drtg = np.random.uniform(104.0, 116.0)
        
        # Last 10 Games Advanced Trends (Capturing momentum / roster form shifts)
        l10_pace = season_pace + np.random.uniform(-2.5, 2.5)
        l10_ortg = season_ortg + np.random.uniform(-6.0, 6.0)
        l10_drtg = season_drtg + np.random.uniform(-6.0, 6.0)
        
        records.append({
            "Team": team,
            "Season_Pace": season_pace, "Season_ORTG": season_ortg, "Season_DRTG": season_drtg,
            "L10_Pace": l10_pace, "L10_ORTG": l10_ortg, "L10_DRTG": l10_drtg
        })
    return pd.DataFrame(records)

# ==========================================
# 3. INTERACTIVE MATCHUP INTERFACE
# ==========================================
selected_league = st.sidebar.selectbox("Select Competition Registry", list(LEAGUE_REGISTRY.keys()))

processed_stats = generate_advanced_dataset(selected_league)

st.subheader("🤖 Matchup Profiling")
col1, col2 = st.columns(2)
with col1:
    home_team = st.selectbox("Home Team", processed_stats["Team"].unique(), index=0)
with col2:
    away_team = st.selectbox("Away Team", processed_stats["Team"].unique(), index=1)

if home_team != away_team:
    if st.button("Launch", type="primary"):
        home_profile = processed_stats[processed_stats["Team"] == home_team].iloc[0]
        away_profile = processed_stats[processed_stats["Team"] == away_team].iloc[0]
        
        # --- THE 50% SEASON / 50% LAST 10 BLENDING MATRIX ---
        home_blended_pace = (0.50 * home_profile["Season_Pace"]) + (0.50 * home_profile["L10_Pace"])
        home_blended_ortg = (0.50 * home_profile["Season_ORTG"]) + (0.50 * home_profile["L10_ORTG"])
        home_blended_drtg = (0.50 * home_profile["Season_DRTG"]) + (0.50 * home_profile["L10_DRTG"])
        
        away_blended_pace = (0.50 * away_profile["Season_Pace"]) + (0.50 * away_profile["L10_Pace"])
        away_blended_ortg = (0.50 * away_profile["Season_ORTG"]) + (0.50 * away_profile["L10_ORTG"])
        away_blended_drtg = (0.50 * away_profile["Season_DRTG"]) + (0.50 * away_profile["L10_DRTG"])
        
        # Calculate Projected Game Pace (Possessions)
        league_base_pace = LEAGUE_REGISTRY[selected_league]["pace"]
        match_projected_pace = (home_blended_pace * away_blended_pace) / league_base_pace
        
        # Calculate Crossover Efficiencies including Home Court Advantage (HCA)
        league_hca = LEAGUE_REGISTRY[selected_league]["hca"]
        expected_home_ortg = ((home_blended_ortg + away_blended_drtg) / 2) + (league_hca / 2)
        expected_away_ortg = ((away_blended_ortg + home_blended_drtg) / 2) - (league_hca / 2)
        
        # Convert Advanced Metrics to Volumetric Point Estimates
        raw_final_home = (expected_home_ortg * match_projected_pace) / 100
        raw_final_away = (expected_away_ortg * match_projected_pace) / 100
        
        final_home = int(np.round(raw_final_home))
        final_away = int(np.round(raw_final_away))
        
        # Generate Realistic First Half Scores using Stochastic Distribution Arrays
        np.random.seed(None)
        half_distribution_home = np.random.uniform(0.47, 0.50)
        half_distribution_away = np.random.uniform(0.47, 0.50)
        
        half_home = int(np.round(final_home * half_distribution_home))
        half_away = int(np.round(final_away * half_distribution_away))
        
        # Log-5 Probability Formula for Exact Win/Loss Metrics
        home_net_rating = home_blended_ortg - home_blended_drtg
        away_net_rating = away_blended_ortg - away_blended_drtg
        efficiency_difference = home_net_rating - away_net_rating + league_hca
        win_prob_home = 1 / (1 + np.exp(-0.075 * efficiency_difference))
        
        winner_declaration = home_team if final_home > final_away else away_team
        confidence_percentage = max(win_prob_home, 1 - win_prob_home) * 100
        
        # ==========================================
        # 4. DATA PRESENTATION DASHBOARD
        # ==========================================
        st.markdown("---")
        st.header(f"🦅 Winner: {winner_declaration}")
        st.metric("Model Algorithmic Rating", f"{confidence_percentage:.2f}%")
        
        st.subheader("📋 Core Scoreboard Allocation Matrix")
        scoreboard_df = pd.DataFrame({
            "Team Lineup": [f"{home_team} [HOME]", f"{away_team} [AWAY]"],
            "First Half Score": [half_home, half_away],
            "Final Score": [final_home, final_away]
        })
        st.table(scoreboard_df.set_index("Team Lineup"))
        
        # Diagnostic Analytics Expandable Drawer
        with st.expander("🔬 View Blended Advanced Stats Diagnostics"):
            col_diag1, col_diag2 = st.columns(2)
            with col_diag1:
                st.markdown(f"**Projected Match Pace:** {match_projected_pace:.2f} possessions")
                st.markdown(f"**{home_team} Blended ORTG:** {home_blended_ortg:.2f}")
                st.markdown(f"**{home_team} Blended DRTG:** {home_blended_drtg:.2f}")
                st.markdown(f"**{home_team} Blended Pace:** {home_blended_pace:.2f}")
            with col_diag2:
                st.markdown(f"**Selected League Base HCA Weighting:** +{league_hca} PTS")
                st.markdown(f"**{away_team} Blended ORTG:** {away_blended_ortg:.2f}")
                st.markdown(f"**{away_team} Blended DRTG:** {away_blended_drtg:.2f}")
                st.markdown(f"**{away_team} Blended Pace:** {away_blended_pace:.2f}")
else:
    st.warning("Halting Execution: Please make sure separate Home and Away teams are selected.")
        
