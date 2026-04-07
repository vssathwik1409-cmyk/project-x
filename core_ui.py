import streamlit as st

class ProjectXUI:
    """The Design System for Project X: Minimalist, Dark, and Elite."""
    
    # --- BRAND CONSTANTS ---
    BG_PRIMARY = "#050505"
    ACCENT_BLUE = "#007AFF"
    TEXT_MAIN = "#FFFFFF"
    TEXT_DIM = "#888888"

    @staticmethod
    def apply_custom_theme():
        """Injects your elite CSS, protected with mobile-responsive fixes."""
        st.markdown(f"""
        <style>
            /* Global Reset & Typography */
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

            /* Hide Streamlit Clutter */
            header {{visibility: hidden;}}
            #MainMenu {{visibility: hidden;}}
            footer {{visibility: hidden;}}
            
            /* Sidebar Transformation */
            section[data-testid="stSidebar"] {{
                background-color: #000000 !important;
                border-right: 1px solid var(--border-color);
            }}

            /* --- FIXED VISIBLE SEARCH BAR --- */
            div[data-baseweb="input"] {{
                background-color: #1A1A1A !important;
                border: 1px solid #333333 !important;
                border-radius: 8px !important; /* Slightly rounded to match your bubbles */
            }}
            div[data-baseweb="input"]:focus-within {{
                border-color: var(--accent-blue) !important;
            }}
            input {{
                color: {ProjectXUI.TEXT_MAIN} !important;
                font-size: 1.1rem !important;
                padding: 12px !important;
                background-color: transparent !important;
                font-family: 'SF Pro Display', sans-serif;
            }}
            input::placeholder {{
                color: #555555 !important;
            }}
            
            /* Elite Execution Button */
            .stButton > button {{
                width: 100%;
                background-color: transparent;
                color: {ProjectXUI.TEXT_MAIN};
                border: 1px solid {ProjectXUI.TEXT_MAIN};
                border-radius: 8px;
                padding: 15px 30px;
                font-weight: 600;
                letter-spacing: 1.5px;
                transition: all 0.3s ease;
                margin-top: 10px;
            }}
            .stButton > button:hover {{
                background-color: var(--accent-blue);
                border-color: var(--accent-blue);
                color: {ProjectXUI.TEXT_MAIN};
            }}
            
            /* Data Metrics Cards */
            div[data-testid="stMetric"] {{
                background: var(--glass-bg);
                border: 1px solid var(--border-color);
                padding: 20px;
                border-radius: 12px;
                backdrop-filter: blur(10px);
            }}
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def render_header(node_name="ALPHA"):
        """Renders the Project X title using Flexbox for perfect mobile alignment."""
        header_html = f"""
        <div style="display: flex; align-items: center; gap: 15px; margin-bottom: 10px;">
            <div style="width: 45px; height: 45px; background: {ProjectXUI.ACCENT_BLUE}; border-radius: 8px; display: flex; justify-content: center; align-items: center; font-weight: 900; font-size: 24px; color: #fff;">
                X
            </div>
            <div style="line-height: 1.1;">
                <h1 style='margin:0; padding:0; font-weight:900; letter-spacing:-1px; font-size:2.2rem;'>
                    PROJECT <span style='color:{ProjectXUI.ACCENT_BLUE}'>X</span>
                </h1>
                <p style='color:{ProjectXUI.TEXT_DIM}; font-size:0.75rem; margin:0; font-weight:400; letter-spacing:1px; font-family:"JetBrains Mono", monospace;'>
                    NODE: {node_name} | STATUS: ACTIVE
                </p>
            </div>
        </div>
        """
        st.markdown(header_html, unsafe_allow_html=True)
        st.write("---")

    @staticmethod
    def display_results(data_dict):
        """Formats JSON output into your luxury UI components."""
        if "error" in data_dict:
            st.error(f"SYSTEM FAULT: {data_dict['error']}")
            return

        st.markdown(f"### MARKET SYNTHESIS")
        st.info(data_dict.get('summary', 'Analysis complete.'))
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("LOWEST PRICE", str(data_dict.get('lowest_price', 'N/A')))
        with col2:
            st.metric("AVERAGE MARKET", str(data_dict.get('average_price', 'N/A')))
        with col3:
            st.metric("TREND", str(data_dict.get('market_trend', 'N/A')))
        
