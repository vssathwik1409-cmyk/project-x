from google import genai
import streamlit as st
from config import ProjectConfig

class IntelligenceCore:
    """The AI Engine: Handles reasoning, behavior, and multi-lingual output."""
    
    def __init__(self):
        # The new 2026 Enterprise Client!
        self.client = genai.Client(api_key=ProjectConfig.get_api_key())

    def generate_consultation(self, user_query, market_data, language="English"):
        """Generates a high-value response with human-like empathy."""
        
        system_prompt = f"""
        ROLE: You are Project X, an elite commerce consultant. 
        USER: Sathwik (Founder) or his parents.
        BEHAVIOR: 
        1. Be warm, professional, and protective. 
        2. Provide a clear table of prices.
        3. Always suggest a 'Hidden Gem' (e.g., card offers or exchange bonuses).
        4. LANGUAGE: Respond in {language}.
        
        DATA: {market_data}
        """
        
        try:
            response = self.client.models.generate_content(
                model=ProjectConfig.MODEL_CORE,
                contents=f"{system_prompt}\n\nUSER QUERY: {user_query}"
            )
            return response.text
        except Exception as e:
            return f"I'm currently recalibrating my data nodes. Error: {str(e)}"
            
