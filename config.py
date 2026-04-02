import streamlit as st

class ProjectConfig:
    VERSION = "2.0-ENTERPRISE"
    TARGET_MARKET = "India"
    
    # The modern 2026 engine
    MODEL_CORE = 'gemini-2.0-flash' 
    
    STORES = [
        "Amazon.in", "Flipkart", "Croma", "Reliance Digital", 
        "Vijay Sales", "Tata Cliq", "Poorvika", "Sangeetha Mobiles", 
        "Moglix", "Jiomart", "Bajaj Electronics"
    ]
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/122.0"
    ]
    
    @staticmethod
    def get_api_key():
        try:
            return st.secrets["GEMINI_API_KEY"]
        except Exception:
            return None
            
