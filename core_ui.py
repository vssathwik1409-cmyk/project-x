import streamlit as st

class ProjectXUI:
    """The Design System for Project X: Minimalist, Dark, and Elite."""
    
    @staticmethod
    def apply_custom_theme():
        st.markdown("""
        <style>
            /* Global Reset & Typography */
            @import url('https://fonts.googleapis.com/css2?family=SF+Pro+Display:wght@300;400;600&family=JetBrains+Mono&display=swap');
            
            :root {
                --bg-primary: #050505;
                --accent-blue: #007AFF;
                --glass-bg: rgba(255, 255, 255, 0.03);
                --border-color: rgba(255, 255, 255, 0.1);
            }

            .stApp { background-color: var(--bg-primary); color: #ffffff; }

            /* Professional Glassmorphism Bubbles */
            .chat-bubble {
                padding: 24px;
                border-radius: 18px;
                margin-bottom: 20px;
                border: 1px solid var(--border-color);
                backdrop-filter: blur(10px);
                transition: transform 0.2s ease;
            }
            .user-bubble { background: var(--glass-bg); align-self: flex-end; border-left: 4px solid var(--accent-blue); }
            .ai-bubble { background: rgba(0, 122, 255, 0.05); border-left: 4px solid #34C759; }

            /* Sidebar Transformation */
            section[data-testid="stSidebar"] {
                background-color: #000000 !important;
                border-right: 1px solid var(--border-color);
            }

            /* Custom Loader Animation */
            .loader {
                border: 2px solid #f3f3f3;
                border-top: 2px solid var(--accent-blue);
                border-radius: 50%;
                width: 20px;
                height: 20px;
                animation: spin 2s linear infinite;
            }
            @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
        </style>
        """, unsafe_allow_html=True)

    @staticmethod
    def render_header(node_name):
        st.title("💠 PROJECT X")
        st.caption(f"CONNECTED TO INTELLIGENCE NODE: {node_name} | STATUS: ACTIVE")
                    
