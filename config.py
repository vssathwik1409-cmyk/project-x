import streamlit as st

class Config:
    """
    SENTRI.AI ENTERPRISE CONFIGURATION
    Pulls directly from Streamlit's built-in Secrets management.
    """
    # --- INTELLIGENCE ACCESS ---
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except KeyError:
        st.error("CRITICAL: GROQ_API_KEY not found in Streamlit Secrets.")
        st.stop()

    GROQ_MODEL = "llama-3.3-70b-versatile"
    
    # --- HYDRA PROTOCOL TARGETS (10 STORES) ---
    TARGET_STORES = [
        "Amazon", "Flipkart", "Reliance Digital", "Croma", "Vijay Sales",
        "Newegg", "Best Buy", "B&H Photo", "Walmart", "eBay"
    ]
    
    # --- SYSTEM THRESHOLDS ---
    TIMEOUT = 12
    MAX_RETRIES = 3
    SCRAPE_LIMIT = 10 # 10 Stores per search
