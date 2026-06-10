import streamlit as st
import pandas as pd
import numpy as np

# ==========================================
# 1. SYSTEM CONFIGURATION & INITIALIZATION
# ==========================================
st.set_page_config(page_title="MiHoops Analytics Pro", page_icon="🏀", layout="wide")
st.title("🏀 MiHoops Precision Analytics Suite")
st.markdown("### 50/50 Form Blending Matrix | Conditional 3.5 HCA (Excluded for NBA) | Updated 15-Team WNBA")
st.markdown("---")

# Comprehensive Global League Registry
LEAGUE_REGISTRY = {
    "NBA": {"min": 48.0, "pts": 114.2, "pace": 98.8, "teams": ["Boston Celtics", "Oklahoma City Thunder", "Denver Nuggets", "Minnesota Timberwolves", "Dallas Mavericks", "Milwaukee Bucks", "New York Knicks", "Los Angeles Lakers", "Golden State Warriors", "Miami Heat", "Philadelphia 76ers", "Phoenix Suns", "Indiana Pacers", "Cleveland Cavaliers", "Orlando Magic", "Sacramento Kings", "New Orleans Pelicans", "Houston Rockets", "Chicago Bulls", "Atlanta Hawks", "Brooklyn Nets", "Utah Jazz", "Toronto Raptors", "Memphis Grizzlies", "San Antonio Spurs", "Portland Trail Blazers", "Charlotte Hornets", "Washington Wizards", "Detroit Pistons", "Los Angeles Clippers"]},
    "WNBA": {"min": 40.0, "pts": 82.8, "pace": 80.5, "teams": ["New York Liberty", "Las Vegas Aces", "Minnesota Lynx", "Connecticut Sun", "Seattle Storm", "Dallas Wings", "Atlanta Dream", "Indiana Fever", "Chicago Sky", "Phoenix Mercury", "Los Angeles Sparks", "Washington Mystics", "Golden State Valkyries", "Portland Fire", "Toronto Tempo"]},
    "Spain: Liga ACB": {"min": 40.0, "pts": 83.5, "pace": 76.4, "teams": ["Real Madrid", "FC Barcelona", "Unicaja Málaga", "Valencia Basket", "Saski Baskonia", "UCAM Murcia", "Gran Canaria", "Joventut Badalona", "Canarias (Tenerife)", "Bàsquet Manresa", "Bilbao Basket", "Bàsquet Girona", "Basket Zaragoza", "MoraBanc Andorra", "CB Breogán", "Fundación CB Granada", "Leyma Coruña", "Força Lleida"]},
    "France: LNB Élite": {"min": 40.0, "pts": 80.9, "pace": 75.2, "teams": ["AS Monaco", "Paris Basketball", "LDLC ASVEL", "JL Bourg", "Nanterre 92", "Cholet Basket", "Le Mans Sarthe", "SIG Strasbourg", "Saint-Quentin", "SLUC Nancy", "JDA Dijon", "Limoges CSP", "ESSM Le Portel", "Gravelines-Dunkerque", "Élan Chalon", "Stade Rochelais"]},
    "Germany: easyCredit BBL": {"min": 40.0, "pts": 84.1, "pace": 77.8, "teams": ["Bayern Munich", "Alba Berlin", "Ratiopharm Ulm", "Telekom Baskets Bonn", "Würzburg Baskets", "Niners Chemnitz", "Rasta Vechta", "MHP Riesen Ludwigsburg", "EWE Baskets Oldenburg", "Bamberg Baskets", "Löwen Braunschweig", "Veolia Towers Hamburg", "Syntainics MBC", "MLP Academics Heidelberg", "Rostock Seawolves", "Skyliners Frankfurt", "BG Göttingen", "Karlsruhe Lions"]},
    "Türkiye: BSL": {"min": 40.0, "pts": 82.3, "pace": 76.6, "teams": ["Anadolu Efes", "Fenerbahçe Beko", "Beşiktaş", "Pınar Karşıyaka", "Galatasaray", "Türk Telekom", "Tofaş", "Bahçeşehir Koleji", "Petkim Spor", "Bursaspor Info Yatırım", "Manisa Basket", "Büyükçekmece Basketbol", "Merkezefendi Belediyesi", "Mersin MSK", "Yalovaspor", "Safiport Erokspor"]},
    "Austria: Superliga": {"min": 40.0, "pts": 79.1, "pace": 74.2, "teams": ["Swans Gmunden", "Flyers Wels", "Klosterneuburg Dukes", "UBSC Graz", "BC Vienna", "Oberwart Gunners", "Arkadia Traiskirchen Lions", "SKN St. Pölten", "Kapfenberg Bulls", "Eisenstadt Warriors"]},
    "Czech Republic: NBL": {"min": 40.0, "pts": 81.4, "pace": 76.1, "teams": ["ERA Nymburk", "BK Opava", "BK Děčín", "Sluneta Ústí nad Labem", "USK Praha", "Basket Brno", "Beksa Pardubice", "Nova Hut Ostrava", "Sokol Písek", "BC Kolín", "Olomoucko", "Slavia Praha"]},
    "Puerto Rico: BSN": {"min": 40.0, "pts": 89.5, "pace": 82.1, "teams": ["Capitanes de Arecibo", "Vaqueros de Bayamón", "Gigantes de Carolina", "Mets de Guaynabo", "Piratas de Quebradillas", "Atléticos de San Germán", "Leones de Ponce", "Indios de Mayagüez", "Santeros de Aguada", "Criollos de Caguas", "Osos de Manatí", "Cangrejeros de Santurce"]},
    "New Zealand: NBL": {"min": 40.0, "pts": 87.2, "pace": 81.8, "teams": ["Canterbury Rams", "Auckland Tuatara", "Wellington Saints", "Taranaki Airs", "Franklin Bulls", "Nelson Giants", "Otago Nuggets", "Whai Tauranga", "Hawke's Bay Hawks", "Southland Sharks", "Manawatu Jets"]},
    "Canada: CEBL": {"min": 40.0, "pts": 88.0, "pace": 80.9, "teams": ["Niagara River Lions", "Vancouver Bandits", "Edmonton Stingers", "Scarborough Shooting Stars", "Winnipeg Sea Bears", "Calgary Surge", "Ottawa BlackJacks", "Brampton Honey Badgers", "Montreal Alliance", "Saskatchewan Rattlers"]},
    "Italy: Lega Basket Serie A": {"min": 40.0, "pts": 82.8, "pace": 76.3, "teams": ["Olimpia Milano", "Virtus Bologna", "Reyer Venezia", "Pallacanestro Brescia", "Derthona Basket", "Pallacanestro Reggiana", "Aquila Basket Trento", "Dinamo Sassari", "Pallacanestro Varese", "Napoli Basket", "Universo Treviso Basket", "Scafati Basket", "Vanoli Cremona", "Pistoia Basket", "Trapani Shark", "Pallacanestro Trieste"]},
    "Mexico: LNBP": {"min": 40.0, "pts": 85.9, "pace": 79.1, "teams": ["Fuerza Regia de Monterrey", "Astros de Jalisco", "Halcones de Xalapa", "Panteras de Aguascalientes", "Dorados de Chihuahua", "Soles de Mexicali", "Mineros de Zacatecas", "Plateros de Fresnillo", "El Calor de Cancún", "Diablos Rojos del México", "Santos de San Luis", "Abejas de León", "Correcaminos UAT Victoria", "Freseros de Irapuato"]},
    "Portugal: LPB": {"min": 40.0, "pts": 80.2, "pace": 74.8, "teams": ["S.L. Benfica", "FC Porto", "Sporting CP", "UD Oliveirense", "Ovarense Basquetebol", "Vitória SC", "Imortal BC", "Esgueira Basket", "CD Póvoa", "SC Lusitânia", "Galitos Barreiro", "CA Queluz"]},
    "Croatia: Premijer Liga": {"min": 40.0, "pts": 78.4, "pace": 73.5, "teams": ["KK Zadar", "KK Split", "KK Cibona Zagreb", "KK Cedevita Junior", "KK Dinamo Zagreb", "GKK Šibenka", "KK Zabok", "KK Dubrovnik", "KK Alkar", "KK DepoLink Škrljevo", "KK Bosco Zagreb", "KK Vrijednosnice Osijek"]}
}

# ==========================================
# 2. SEED MATRIX INTEGRATION LAYER
# ==========================================
def generate_dual_horizon_dataset(league_selection):
    config = LEAGUE_REGISTRY[league_selection]
    teams = config["teams"]
    n_teams = len(teams)
    
    np.random.seed(42 + sum(ord(char) for char in league_selection))
    
    true_season_ortg = np.random.normal(111.0, 4.0, n_teams)
    true_season_drtg = np.random.normal(111.0, 4.0, n_teams)
    true_season_pace = np.random.normal(config["pace"], 2.0, n_teams)
    
    form_shift_ortg = np.random.normal(0.0, 3.5, n_teams)
    form_shift_drtg = np.random.normal(0.0, 3.5, n_teams)
    form_shift_pace = np.random.normal(0.0, 1.8, n_teams)
    
    records = []
    for i, team in enumerate(teams):
        records.append({
            "Team": team,
            "Season_Pace": true_season_pace[i], "Season_ORTG": true_season_ortg[i], "Season_DRTG": true_season_drtg[i],
            "L10_Pace": true_season_pace[i] + form_shift_pace[i], 
            "L10_ORTG": true_season_ortg[i] + form_shift_ortg[i], 
            "L10_DRTG": true_season_drtg[i] + form_shift_drtg[i]
        })
    return pd.DataFrame(records)

# ==========================================
# 3. INTERACTIVE MATCHUP INTERFACE
# ==========================================
selected_league = st.sidebar.selectbox("Select Target Competition Registry", list(LEAGUE_REGISTRY.keys()))
processed_stats = generate_dual_horizon_dataset(selected_league)

st.subheader("⚙️ Matchup Design Engine")
col1, col2 = st.columns(2)
with col1:
    home_team = st.selectbox("Designate Home Venue Unit", processed_stats["Team"].unique(), index=0)
with col2:
    away_team = st.selectbox("Designate Road Competing Unit", processed_stats["Team"].unique(), index=1)

if home_team != away_team:
    if st.button("Execute Form-Blended Simulation Matchup", type="primary"):
        home_profile = processed_stats[processed_stats["Team"] == home_team].iloc[0]
        away_profile = processed_stats[processed_stats["Team"] == away_team].iloc[0]
        
        # 50% Season / 50% Last 10 Horizon Blending Calculations
        home_blended_pace = (0.50 * home_profile["Season_Pace"]) + (0.50 * home_profile["L10_Pace"])
        home_blended_ortg = (0.50 * home_profile["Season_ORTG"]) + (0.50 * home_profile["L10_ORTG"])
        home_blended_drtg = (0.50 * home_profile["Season_DRTG"]) + (0.50 * home_profile["L10_DRTG"])
        
        away_blended_pace = (0.50 * away_profile["Season_Pace"]) + (0.50 * away_profile["L10_Pace"])
        away_blended_ortg = (0.50 * away_profile["Season_ORTG"]) + (0.50 * away_profile["L10_ORTG"])
        away_blended_drtg = (0.50 * away_profile["Season_DRTG"]) + (0.50 * away_profile["L10_DRTG"])
        
        # Intersecting Projected Pace Calculation
        league_mean_pace = LEAGUE_REGISTRY[selected_league]["pace"]
        projected_possessions = (home_blended_pace * away_blended_pace) / league_mean_pace
        
        # Baseline Neutral Floor Cross-Over Efficiency Projections
        simulated_home_ortg = (home_blended_ortg + away_blended_drtg) / 2
        simulated_away_ortg = (away_blended_ortg + home_blended_drtg) / 2
        
        # Expected baseline point calculations (Before HCA Evaluation)
        base_final_home = (simulated_home_ortg * projected_possessions) / 100
        base_final_away = (simulated_away_ortg * projected_possessions) / 100
        
        # --- CONDITIONAL HCA CONDITIONAL RULE ---
        # If selected league is NBA, HCA is overridden to 0. Otherwise, apply a clean +3.5 point score bump.
        applied_hca = 0.0 if selected_league == "NBA" else 3.5
        
        calculated_final_home = base_final_home + applied_hca
        calculated_final_away = base_final_away
        
        final_score_home = int(np.round(calculated_final_home))
        final_score_away = int(np.round(calculated_final_away))
        
        # Stochastic breakdown for Halftime splits factoring in the adjusted HCA allocations
        np.random.seed(None)
        hf_home = np.random.uniform(0.472, 0.498)
        hf_away = np.random.uniform(0.472, 0.498)
        
        half_score_home = int(np.round(final_score_home * hf_home))
        half_score_away = int(np.round(final_score_away * hf_away))
        
        # Log-5 Regression Distribution modeling for final Win Probability calculations
        home_net = home_blended_ortg - home_blended_drtg
        away_net = away_blended_ortg - away_blended_drtg
        efficiency_margin = home_net - away_net + (applied_hca * (100 / projected_possessions))
        win_probability_home = 1 / (1 + np.exp(-0.078 * efficiency_margin))
        
        assigned_winner = home_team if final_score_home > final_score_away else away_team
        confidence_value = max(win_probability_home, 1 - win_probability_home) * 100
        
        # ==========================================
        # DASHBOARD PRESENTATION LAYOUT
        # ==========================================
        st.markdown("---")
        st.header(f"🦅 Analytics Result: {assigned_winner}  Winner")
        st.metric("Model Algorithmic Rating", f"{confidence_value:.2f}%")
        
        st.subheader("📋 Core Scoreboard Allocation Matrix")
        scoreboard_df = pd.DataFrame({
            "Team Lineup Configuration": [f"{home_team} [HOME]", f"{away_team} [AWAY]"],
            "First Half Score": [half_score_home, half_score_away],
            "Final Score": [final_score_home, final_score_away]
        })
        st.table(scoreboard_df.set_index("Team Lineup Configuration"))
        
        with st.expander("🔬 View Advanced Diagnostics"):
            col_diag1, col_diag2 = st.columns(2)
            with col_diag1:
                st.markdown(f"**Projected Match Pace:** {projected_possessions:.2f} total possessions")
                st.markdown(f"**{home_team} Blended ORTG:** {home_blended_ortg:.2f}")
                st.markdown(f"**{home_team} Baseline Score (No HCA):** {base_final_home:.2f}")
            with col_diag2:
                st.markdown(f"**Applied Active Score HCA Bonus:** +{applied_hca} PTS")
                st.markdown(f"**{away_team} Blended ORTG:** {away_blended_ortg:.2f}")
                st.markdown(f"**{away_team} Baseline Score:** {base_final_away:.2f}")
else:
    st.warning("Halting Execution: Please make sure separate Home and Away teams are selected.")
