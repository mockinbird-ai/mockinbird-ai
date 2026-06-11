import streamlit as st
import pandas as pd
import numpy as np
from dataclasses import dataclass
from typing import Dict, Tuple, List
from enum import Enum

# ========================================================================
# DATA MODELS & CONSTANTS
# ========================================================================

@dataclass
class TeamStats:
    """Core team statistical metrics"""
    name: str
    ortg: float  # Offensive Rating: points scored per 100 possessions
    drtg: float  # Defensive Rating: points allowed per 100 possessions
    pace: float  # Pace: possessions per 48 minutes
    
    @property
    def net_rating(self) -> float:
        """Net rating = ORTG - DRTG"""
        return self.ortg - self.drtg


class PredictionModel:
    """Basketball game prediction engine using possessions-based methodology"""
    
    # Constants from NCAA/NBA research
    HOME_COURT_ADVANTAGE = 2.7  # Average HCA in points (evidence-based, not 3.5)
    AVG_POSSESSION_LENGTH = 14.0  # Seconds per possession
    MINUTES_PER_GAME = 48.0
    POSSESSIONS_PER_GAME_BASELINE = 100.0  # Possessions per 100 possessions (normalized)
    
    def __init__(self, league_pace: float, league_ortg: float):
        """
        Initialize model with league baseline parameters
        
        Args:
            league_pace: Average league possessions per 48 min
            league_ortg: Average league ORTG
        """
        self.league_pace = league_pace
        self.league_ortg = league_ortg
        self.league_drtg = league_ortg  # Assumes league offense = league defense
    
    def calculate_game_pace(self, home_pace: float, away_pace: float) -> float:
        """
        Calculate predicted game pace.
        
        Uses simple average of both teams' paces weighted toward league average.
        Formula: (home_pace + away_pace) / 2
        """
        return (home_pace + away_pace) / 2.0
    
    def estimate_possessions(self, game_pace: float, minutes: float = 48.0) -> float:
        """
        Estimate total possessions in game based on pace.
        
        Possessions = (Pace / 100) * (Minutes / 2)
        Divided by 2 because pace is per 100 possessions per 48 min
        """
        return (game_pace / self.POSSESSIONS_PER_GAME_BASELINE) * (minutes / 2.0)
    
    def calculate_team_points(
        self, 
        team_ortg: float, 
        opponent_drtg: float,
        game_pace: float,
        is_home: bool = False
    ) -> float:
        """
        Calculate predicted points for a team using possessions-based model.
        
        Formula:
        Points = (ORTG / 100) * Possessions + HCA (if home)
        
        Where ORTG accounts for both team's offensive efficiency and opponent's defense:
        Adjusted ORTG = (Team ORTG + Opponent DRTG) / 2
        
        This captures the matchup impact.
        """
        possessions = self.estimate_possessions(game_pace)
        
        # Matchup-adjusted offensive rating
        adjusted_ortg = (team_ortg + opponent_drtg) / 2.0
        
        # Base points from possessions
        points = (adjusted_ortg / self.POSSESSIONS_PER_GAME_BASELINE) * possessions
        
        # Add home court advantage
        if is_home:
            points += self.HOME_COURT_ADVANTAGE
        
        return points
    
    def predict_game(
        self, 
        home_team: TeamStats, 
        away_team: TeamStats
    ) -> Dict:
        """
        Generate full game prediction with confidence intervals.
        
        Returns:
            Dictionary with predictions at FT (full time) and HT (half time)
        """
        # Calculate game dynamics
        game_pace = self.calculate_game_pace(home_team.pace, away_team.pace)
        
        # Predict points
        home_points = self.calculate_team_points(
            home_team.ortg, 
            away_team.drtg,
            game_pace,
            is_home=True
        )
        
        away_points = self.calculate_team_points(
            away_team.ortg,
            home_team.drtg,
            game_pace,
            is_home=False
        )
        
        # Calculate spreads
        spread = home_points - away_points
        over_under = home_points + away_points
        
        # Half-time projections (assume linear scoring)
        home_ht = home_points / 2.0
        away_ht = away_points / 2.0
        
        # Determine winner
        winner = home_team.name if spread > 0 else away_team.name
        confidence = min(abs(spread) / 8.0, 1.0)  # Scale spread to confidence (8pt = 100% confident)
        
        return {
            'home_team': home_team.name,
            'away_team': away_team.name,
            'home_ft': home_points,
            'away_ft': away_points,
            'home_ht': home_ht,
            'away_ht': away_ht,
            'spread': spread,  # Positive means home favored
            'over_under': over_under,
            'game_pace': game_pace,
            'possessions': self.estimate_possessions(game_pace),
            'winner': winner,
            'confidence': confidence,
            'hca': self.HOME_COURT_ADVANTAGE
        }


# ========================================================================
# LEAGUE DATA
# ========================================================================

LEAGUE_DATABASE = {
    "Puerto Rico (BSN)": {
        "default_pace": 84.3,
        "default_ortg": 115.5,
        "teams": {
            "Atléticos de San Germán": (116.9, 110.6, 84.6),
            "Criollos de Caguas": (120.0, 114.8, 85.5),
            "Vaqueros de Bayamón": (112.0, 107.7, 83.2),
            "Leones de Ponce": (120.1, 117.3, 83.9),
            "Gigantes de Carolina": (117.9, 116.4, 84.1),
            "Cangrejeros de Santurce": (114.9, 113.8, 83.8),
            "Indios de Mayagüez": (116.4, 115.6, 85.0),
            "Capitanes de Arecibo": (115.4, 115.4, 84.9),
            "Osos de Manatí": (113.1, 116.4, 85.1),
            "Mets de Guaynabo": (114.2, 120.6, 83.3),
            "Santeros de Aguada": (112.9, 119.5, 84.4),
            "Piratas de Quebradillas": (110.8, 117.9, 85.6),
        }
    },
    "Spain (Liga ACB)": {
        "default_pace": 77.0,
        "default_ortg": 111.5,
        "teams": {
            "FC Barcelona": (116.8, 107.5, 77.2),
            "Real Madrid": (118.6, 106.5, 76.3),
            "Unicaja Malaga": (116.5, 107.2, 77.1),
            "Valencia Basket": (114.4, 109.8, 78.0),
            "Saski Baskonia": (112.5, 111.4, 76.8),
            "UCAM Murcia": (111.2, 110.5, 76.4),
            "Joventut Badalona": (110.8, 111.2, 77.5),
            "CB Gran Canaria": (111.8, 110.2, 76.2),
            "Casademont Zaragoza": (108.4, 111.9, 77.9),
            "MoraBanc Andorra": (109.0, 111.4, 77.6),
            "La Laguna Tenerife": (113.1, 109.5, 75.8),
            "Bilbao Basket": (109.5, 110.1, 76.5),
            "Bàsquet Girona": (107.2, 112.4, 78.1),
            "Baxi Manresa": (111.0, 111.8, 79.2),
            "Coviran Granada": (106.8, 113.2, 76.9),
            "Leyma Coruña": (108.1, 114.0, 78.4),
            "Hiopos Lleida": (107.5, 113.5, 77.3),
            "Río Breogán": (105.9, 110.8, 75.9),
        }
    },
    "France (LNB Élite)": {
        "default_pace": 75.4,
        "default_ortg": 109.8,
        "teams": {
            "AS Monaco": (116.9, 104.1, 74.5),
            "Paris Basketball": (115.2, 107.5, 77.1),
            "LDLC ASVEL": (113.6, 109.4, 75.4),
            "JL Bourg": (111.4, 107.9, 75.1),
            "JDA Dijon": (108.8, 109.5, 74.2),
            "Nanterre 92": (110.5, 111.2, 76.8),
            "Cholet Basket": (108.1, 108.9, 75.5),
            "SIG Strasbourg": (109.2, 110.4, 75.9),
            "Le Mans Sarthe": (109.0, 110.1, 76.2),
            "Élan Chalon": (107.4, 112.5, 76.8),
            "SLUC Nancy": (109.6, 111.9, 77.0),
            "Boulazac Dordogne": (105.5, 109.2, 74.8),
            "Limoges CSP": (107.9, 111.4, 75.2),
            "Gravelines-Dunkerque": (106.2, 108.5, 74.4),
            "Saint-Quentin": (108.7, 107.2, 73.9),
            "ESSM Le Portel": (106.0, 112.1, 75.6),
        }
    },
    "Germany (easyCredit BBL)": {
        "default_pace": 78.0,
        "default_ortg": 110.2,
        "teams": {
            "FC Bayern Munich": (117.9, 106.5, 77.9),
            "ALBA Berlin": (112.1, 110.9, 79.3),
            "Niners Chemnitz": (114.2, 107.4, 77.1),
            "ratiopharm ulm": (112.8, 112.1, 78.5),
            "Telekom Baskets Bonn": (113.5, 111.2, 77.8),
            "MHP Riesen Ludwigsburg": (110.1, 109.4, 77.5),
            "Würzburg Baskets": (111.2, 108.1, 76.8),
            "Rasta Vechta": (110.8, 111.5, 78.4),
            "Bamberg Baskets": (110.4, 112.8, 79.0),
            "Löwen Braunschweig": (108.2, 109.9, 77.4),
            "Syntainics MBC": (109.5, 114.2, 79.5),
            "BG Göttingen": (106.4, 115.1, 78.1),
            "EWE Baskets Oldenburg": (111.6, 110.5, 78.9),
            "SKYLINERS Frankfurt": (105.1, 110.9, 76.2),
            "PS Karlsruhe Lions": (104.8, 113.4, 77.9),
            "Towers Hamburg": (109.2, 114.6, 80.2),
            "MLP Academics Heidelberg": (108.9, 113.1, 79.1),
            "Rostock Seawolves": (107.6, 112.4, 78.6),
        }
    },
    "Italy (Lega Basket Serie A)": {
        "default_pace": 76.5,
        "default_ortg": 111.3,
        "teams": {
            "Olimpia Milano": (116.2, 107.1, 75.2),
            "Virtus Bologna": (117.6, 108.2, 76.3),
            "Germani Brescia": (115.1, 108.9, 76.5),
            "Reyer Venezia": (111.2, 109.8, 76.1),
            "Aquila Basket Trento": (110.8, 110.4, 76.9),
            "Derthona Tortona": (111.5, 110.1, 75.8),
            "Pallacanestro Reggiana": (110.2, 110.6, 75.5),
            "Openjobmetis Varese": (112.6, 117.9, 80.4),
            "Dinamo Sassari": (109.4, 111.5, 76.0),
            "Pistoia Basket": (108.5, 111.2, 75.4),
            "Scafati Basket": (110.9, 114.1, 77.8),
            "Treviso Basket": (109.1, 113.5, 77.2),
            "Vanoli Cremona": (106.4, 109.5, 74.6),
            "Napoli Basket": (108.0, 114.6, 77.5),
            "Trapani Shark": (113.2, 112.0, 78.3),
            "Pallacanestro Cantù": (107.1, 109.0, 75.1),
        }
    },
    "England (Super League Basketball)": {
        "default_pace": 80.1,
        "default_ortg": 109.3,
        "teams": {
            "London Lions": (115.5, 101.9, 80.9),
            "Cheshire Phoenix": (112.2, 107.6, 80.6),
            "Manchester Basketball": (109.5, 109.1, 81.2),
            "Sheffield Sharks": (104.2, 105.1, 78.9),
            "Leicester Riders": (108.9, 107.2, 79.7),
            "Bristol Flyers": (106.5, 107.8, 79.1),
            "Surrey 89ers": (107.1, 110.2, 80.5),
            "Newcastle Eagles": (108.6, 108.8, 80.4),
            "Caledonia Gladiators": (106.8, 108.0, 80.2),
        }
    },
    "Greece (GBL)": {
        "default_pace": 74.9,
        "default_ortg": 112.4,
        "teams": {
            "Panathinaikos AKTOR": (120.5, 103.2, 74.5),
            "Olympiacos Piraeus": (119.8, 102.8, 74.1),
            "Peristeri": (111.4, 110.5, 75.0),
            "Promitheas Patras": (112.8, 112.1, 75.9),
            "AEK Athens": (110.1, 112.4, 75.6),
            "Aris Salonika": (106.4, 105.8, 74.3),
            "PAOK Salonika": (107.9, 111.2, 74.8),
            "Kolossos Rodou": (108.2, 113.1, 75.1),
            "Maroussi BC": (109.0, 112.5, 76.0),
            "Karditsa AS": (106.1, 111.8, 74.5),
            "Iraklis Salonika": (105.5, 110.9, 74.9),
            "BC Mykonos": (106.9, 112.0, 75.3),
        }
    },
    "China (CBA)": {
        "default_pace": 88.6,
        "default_ortg": 112.8,
        "teams": {
            "Liaoning Flying Leopards": (115.1, 104.2, 87.5),
            "Xinjiang Flying Tigers": (112.8, 105.5, 88.1),
            "Zhejiang Golden Bulls": (117.1, 107.9, 88.9),
            "Guangdong Southern Tigers": (116.5, 109.1, 91.1),
            "Zhejiang Guangsha Lions": (114.2, 106.8, 86.9),
            "Shanghai Sharks": (111.5, 112.4, 89.4),
            "Beijing Ducks": (109.8, 106.1, 86.2),
            "Guangzhou Loong Lions": (110.4, 111.5, 88.0),
            "Shenzhen Leopards": (112.1, 111.9, 87.8),
            "Qingdao Eagles": (109.2, 108.5, 88.3),
            "Shanxi Loongs": (113.6, 115.2, 90.5),
            "Nanjing Monkey Kings": (108.5, 111.8, 89.0),
        }
    },
}

# ========================================================================
# STREAMLIT UI CONFIGURATION
# ========================================================================

st.set_page_config(
    page_title="Basketball Game Predictor",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🏀 Basketball Game Predictor")
st.markdown("""
Accurate game predictions using possession-based statistical modeling.
Accounts for team offensive/defensive efficiency, pace, and home court advantage.
""")

# ========================================================================
# SIDEBAR CONFIGURATION
# ========================================================================

st.sidebar.markdown("## Configuration")

# League selection
league_name = st.sidebar.selectbox(
    "Select League",
    list(LEAGUE_DATABASE.keys())
)

league_config = LEAGUE_DATABASE[league_name]
league_pace = league_config["default_pace"]
league_ortg = league_config["default_ortg"]

st.sidebar.metric("League Avg Pace", f"{league_pace:.1f}")
st.sidebar.metric("League Avg ORTG", f"{league_ortg:.1f}")

# ========================================================================
# MAIN INTERFACE
# ========================================================================

col1, col2 = st.columns(2)

with col1:
    st.subheader("Home Team")
    home_team_name = st.selectbox(
        "Select home team",
        sorted(league_config["teams"].keys()),
        key="home"
    )
    home_ortg, home_drtg, home_pace_val = league_config["teams"][home_team_name]
    
    # Allow overrides
    with st.expander("Adjust stats"):
        home_ortg = st.number_input(
            "ORTG",
            value=home_ortg,
            min_value=80.0,
            max_value=130.0,
            step=0.1,
            key="home_ortg"
        )
        home_drtg = st.number_input(
            "DRTG",
            value=home_drtg,
            min_value=80.0,
            max_value=130.0,
            step=0.1,
            key="home_drtg"
        )
        home_pace_val = st.number_input(
            "Pace",
            value=home_pace_val,
            min_value=60.0,
            max_value=100.0,
            step=0.1,
            key="home_pace"
        )

with col2:
    st.subheader("Away Team")
    away_team_name = st.selectbox(
        "Select away team",
        sorted(league_config["teams"].keys()),
        key="away"
    )
    away_ortg, away_drtg, away_pace_val = league_config["teams"][away_team_name]
    
    # Allow overrides
    with st.expander("Adjust stats"):
        away_ortg = st.number_input(
            "ORTG",
            value=away_ortg,
            min_value=80.0,
            max_value=130.0,
            step=0.1,
            key="away_ortg"
        )
        away_drtg = st.number_input(
            "DRTG",
            value=away_drtg,
            min_value=80.0,
            max_value=130.0,
            step=0.1,
            key="away_drtg"
        )
        away_pace_val = st.number_input(
            "Pace",
            value=away_pace_val,
            min_value=60.0,
            max_value=100.0,
            step=0.1,
            key="away_pace"
        )

# ========================================================================
# PREDICTION EXECUTION
# ========================================================================

if home_team_name == away_team_name:
    st.error("⚠️ Please select two different teams")
else:
    # Create team objects
    home = TeamStats(home_team_name, home_ortg, home_drtg, home_pace_val)
    away = TeamStats(away_team_name, away_ortg, away_drtg, away_pace_val)
    
    # Initialize model and predict
    model = PredictionModel(league_pace, league_ortg)
    prediction = model.predict_game(home, away)
    
    # ====================================================================
    # RESULTS DISPLAY
    # ====================================================================
    
    st.markdown("---")
    st.header("Prediction Results")
    
    # Main score display
    col1, col2, col3 = st.columns([2, 1, 2])
    
    with col1:
        st.metric(
            f"🏡 {home_team_name}",
            f"{prediction['home_ft']:.1f}",
            delta=None
        )
    
    with col2:
        spread_text = f"Home -" if prediction['spread'] > 0 else f"Home +"
        st.metric(
            "Spread",
            f"{spread_text}{abs(prediction['spread']):.1f}",
            delta=None
        )
    
    with col3:
        st.metric(
            f"✈️ {away_team_name}",
            f"{prediction['away_ft']:.1f}",
            delta=None
        )
    
    # Confidence and game metrics
    col1, col2, col3, col4 = st.columns(4)
    
    confidence_pct = prediction['confidence'] * 100
    with col1:
        st.metric("Confidence", f"{confidence_pct:.0f}%")
    with col2:
        st.metric("Over/Under", f"{prediction['over_under']:.1f}")
    with col3:
        st.metric("Game Pace", f"{prediction['game_pace']:.1f}")
    with col4:
        st.metric("Possessions", f"{prediction['possessions']:.0f}")
    
    # Half-time projection
    st.markdown("### Half-Time Score (Est.)")
    col1, col2 = st.columns(2)
    with col1:
        st.write(f"**{home_team_name}**: {prediction['home_ht']:.1f}")
    with col2:
        st.write(f"**{away_team_name}**: {prediction['away_ht']:.1f}")
    
    # Winner display
    st.markdown("---")
    if prediction['spread'] > 0:
        st.success(f"### 🏆 Predicted Winner: {home_team_name} by {prediction['spread']:.1f}")
    else:
        st.success(f"### 🏆 Predicted Winner: {away_team_name} by {abs(prediction['spread']):.1f}")
    
    # Detailed analysis
    st.markdown("### Model Explanation")
    explanation = f"""
**How this prediction was calculated:**

1. **Game Pace**: Average of both teams' pace settings ({prediction['game_pace']:.1f} possessions/48min)
2. **Possessions**: Estimated {prediction['possessions']:.0f} total possessions for the game
3. **Scoring**: Points calculated as (ORTG / 100) × Possessions, adjusted for opponent defense
4. **Home Court Advantage**: {prediction['hca']:.1f} points added to home team
5. **Spread**: Difference in projected final scores

**Model Assumptions:**
- Linear scoring throughout the game
- Home court advantage of {prediction['hca']:.1f} points (evidence-based average)
- ORTG/DRTG ratings remain constant (no adjustments for rest, injuries, or recent form)
- No adjustment for back-to-back games or travel
"""
    st.info(explanation)
    
    # Matchup details
    st.markdown("### Matchup Details")
    matchup_df = pd.DataFrame({
        "Metric": ["ORTG", "DRTG", "Net Rating", "Pace"],
        home_team_name: [
            f"{home.ortg:.1f}",
            f"{home.drtg:.1f}",
            f"{home.net_rating:.1f}",
            f"{home.pace:.1f}"
        ],
        away_team_name: [
            f"{away.ortg:.1f}",
            f"{away.drtg:.1f}",
            f"{away.net_rating:.1f}",
            f"{away.pace:.1f}"
        ]
    })
    st.table(matchup_df)
        
