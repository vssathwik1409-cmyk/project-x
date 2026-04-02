import google.generativeai as genai
import streamlit as st

class IntelligenceCore:
    """The AI Engine: Handles reasoning, behavior, and multi-lingual output."""
    
    def __init__(self):
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_consultation(self, user_query, market_data, language="English"):
        """Generates a high-value response with human-like empathy."""
        
        system_prompt = f"""
        ROLE: You are Project X, a elite commerce consultant. 
        USER: Sathwik (Founder) or his parents.
        BEHAVIOR: 
        1. Be warm, professional, and protective. 
        2. If data is missing for a store, explain why (e.g., 'Croma seems to be updating their stock').
        3. Provide a clear table of prices.
        4. Always suggest a 'Hidden Gem' (e.g., card offers or exchange bonuses).
        5. LANGUAGE: Respond in {language}.
        
        DATA: {market_data}
        """
        
        try:
            response = self.model.generate_content(system_prompt + user_query)
            return response.text
        except Exception:
            return "I'm currently recalibrating my data nodes. Give me a moment to re-sync."
          
