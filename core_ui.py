import streamlit as st

class ProjectXUI:
    """The Design System for Project X: Minimalist, Dark, and Elite."""
    
    # --- BRAND CONSTANTS ---
    BG_PRIMARY = "#050505"
    ACCENT_BLUE = "#007AFF"
    TEXT_MAIN = "#FFFFFF"
    TEXT_DIM = "#888888"
    ADVICE_GREEN = "#34C759"
    ADVICE_ORANGE = "#FF9500"

    @staticmethod
    def apply_custom_theme():
        """Injects your elite CSS, optimized for mobile visibility and SF Pro aesthetics."""
        st.markdown(f"""
        <style>
            /* Typography & Global Style */
            @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600;900&family=JetBrains+Mono&display=swap');
            
            :root {{
                --bg-primary: {ProjectXUI.BG_PRIMARY};
                --accent-blue: {ProjectXUI.ACCENT_BLUE};
                --glass-bg: rgba(255, 255, 255, 0.03);
                --border-color: rgba(255, 255, 255, 0.1);
            }}

            .stApp {{ 
                background-color: var(--bg-primary); 
                color: {ProjectXUI.TEXT_MAIN}; 
                font-family: 'SF Pro Display', sans-serif;
            }}

            /* Clean Dashboard: Hide Streamlit Default UI */
            header {{visibility: hidden;}}
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            [data-testid="stSidebar"] {{ background-color: #000000 !important; border-right: 1px solid var(--border-color); }}

            /* --- TARGET INPUT BOX (VISIBLE & ELITE) --- */
            div[data-baseweb="input"] {{
                background-color: #1A1A1A !important;
                border: 1px solid #333333 !important;
                border-radius: 8px !important;
                transition: border-color 0.3s ease;
            }}
            div[data-baseweb="input"]:focus-within {{
                border-color: var(--accent-blue) !important;
            }}
            input {{
                color: {ProjectXUI.TEXT_MAIN} !important;
                font-size: 1.1rem !important;
                padding: 12px !important;
                background-color: transparent !important;
            }}
            
            /* --- PROJECT X ACTION BUTTON --- */
            .stButton > button {{
                width: 100%;
                background-color: transparent;
                color: {ProjectXUI.TEXT_MAIN};
                border: 1px solid {ProjectXUI.TEXT_MAIN};
                border-radius: 8px;
                padding: 15px 30px;
                font-weight: 600;
                letter-spacing: 2px;
                text-transform: uppercase;
                transition: all 0.3s ease;
                margin-top: 10px;
            }}
            .stButton > button:hover {{
                background-color: var(--accent-blue);
                border-color: var(--accent-blue);
            }}
            
            /* --- INTELLIGENCE CARDS --- */
            div[data-testid="stMetric"] {{
                background: var(--glass-bg);
                border: 1px solid var(--border-color);
                padding: 20px;
                border-radius: 12px;
                backdrop-filter: blur(10px);
            }}
            
            /* Custom Info Box */
            .stAlert {{
                background: rgba(0, 122, 255, 0.05) !important;
                border: 1px solid var(--accent-blue) !important;
                color: white !important;
                border-radius: 12px !important;
            }}
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def render_header(node_name="ALPHA"):
        
