import streamlit as st
import plotly.graph_objects as go

class UI_Engine:
    """
    THE VISUAL CORE:
    Handles all CSS overrides, custom SVG rendering, and Plotly data visualizations.
    """
    
    # --- BRAND CONSTANTS ---
    BG_COLOR = "#050505"
    TEXT_MAIN = "#FFFFFF"
    TEXT_DIM = "#888888"
    ACCENT_RED = "#D32F2F"

    @staticmethod
    def inject_premium_css():
        """Overrides Streamlit's default styling for a borderless, luxury feel."""
        st.markdown(f"""
            <style>
                /* Import high-end fonts */
                @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;700;900&display=swap');
                
                /* Global Background and Text */
                .stApp {{
                    background-color: {UI_Engine.BG_COLOR};
                    color: {UI_Engine.TEXT_MAIN};
                    font-family: 'Inter', sans-serif;
                }}
                
                /* Hide Streamlit Clutter */
                header {{visibility: hidden;}}
                #MainMenu {{visibility: hidden;}}
                footer {{visibility: hidden;}}
                [data-testid="stSidebar"] {{display: none;}}
                
                /* Luxury Input Field */
                .stTextInput input {{
                    background-color: transparent !important;
                    border: none !important;
                    border-bottom: 2px solid {UI_Engine.TEXT_DIM} !important;
                    color: {UI_Engine.TEXT_MAIN} !important;
                    border-radius: 0px !important;
                    font-size: 1.2rem !important;
                    padding: 10px 0px !important;
                    transition: border-color 0.3s ease;
                }}
                .stTextInput input:focus {{
                    border-bottom: 2px solid {UI_Engine.ACCENT_RED} !important;
                    box-shadow: none !important;
                }}
                
                /* Ferrari-Style Execution Button */
                .stButton > button {{
                    width: 100%;
                    background-color: transparent;
                    color: {UI_Engine.TEXT_MAIN};
                    border: 1px solid {UI_Engine.TEXT_MAIN};
                    border-radius: 0px;
                    padding: 15px 30px;
                    font-weight: 700;
                    letter-spacing: 2px;
                    text-transform: uppercase;
                    transition: all 0.3s ease;
                }}
                .stButton > button:hover {{
                    background-color: {UI_Engine.ACCENT_RED};
                    border-color: {UI_Engine.ACCENT_RED};
                    color: {UI_Engine.TEXT_MAIN};
                }}
                
                /* Data Metrics Cards */
                div[data-testid="stMetric"] {{
                    background-color: rgba(255,255,255,0.03);
                    border: 1px solid rgba(255,255,255,0.1);
                    padding: 20px;
                    border-radius: 5px;
                }}
            </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def render_header():
        """Renders the custom SVG logo and minimalist title."""
        # Sharp, geometric 'S' symbol
        custom_svg = f"""
        <svg width="50" height="50" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path d="M10 30L90 30L50 50L90 70L10 70L50 50L10 30Z" stroke="{UI_Engine.ACCENT_RED}" stroke-width="4" fill="none"/>
        </svg>
        """
        col1, col2 = st.columns([1, 10])
        with col1:
            st.markdown(custom_svg, unsafe_allow_html=True)
        with col2:
            st.markdown(
                f"<h1 style='margin:0; padding:0; font-weight:900; letter-spacing:-2px; font-size:2.5rem;'>"
                f"SENTRI<span style='color:{UI_Engine.ACCENT_RED}'>.AI</span></h1>", 
                unsafe_allow_html=True
            )
            st.markdown(
                f"<p style='color:{UI_Engine.TEXT_DIM}; font-size:0.9rem; margin-top:-5px; font-weight:300; letter-spacing:1px;'>"
                f"AUTONOMOUS MARKET INTELLIGENCE // GROQ LPU</p>", 
                unsafe_allow_html=True
            )
        st.write("---")

    @staticmethod
    def display_results(data_dict):
        """
        Takes the JSON output from brain.py and formats it into luxury UI components.
        """
        if "error" in data_dict:
            st.error(f"SYSTEM FAULT: {data_dict['error']}")
            return

        st.markdown(f"### MARKET SYNTHESIS")
        st.info(data_dict.get('summary', 'Analysis complete.'))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("LOWEST DETECTED PRICE", str(data_dict.get('lowest_price', 'N/A')))
        with col2:
            st.metric("AVERAGE MARKET PRICE", str(data_dict.get('average_price', 'N/A')))
        with col3:
            st.metric("MARKET TREND", str(data_dict.get('market_trend', 'N/A')))
        
