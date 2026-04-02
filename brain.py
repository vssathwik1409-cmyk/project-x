import google.generativeai as genai
from config import ProjectConfig

class IntelligenceCore:
    """The AI Engine: Handles reasoning, behavior, and multi-lingual output."""
    
    def __init__(self):
        genai.configure(api_key=ProjectConfig.get_api_key())
        self.model = genai.GenerativeModel(ProjectConfig.MODEL_CORE)

    def generate_consultation(self, user_query, market_data, language="English"):
        """Generates a high-value response with human-like empathy."""
        
        system_prompt = f"""
        ROLE: You are Project X, an elite commerce consultant. 
        BEHAVIOR: 
        1. Be warm, professional, and protective of the user's wallet. 
        2. Provide a clear, easy-to-read comparison of the prices found.
        3. Always suggest a 'Hidden Gem' (e.g., card offers, exchange bonuses, or waiting for a sale).
        4. LANGUAGE: Respond strictly in {language}.
        
        DATA: {market_data}
        """
        
        try:
            response = self.model.generate_content(f"{system_prompt}\n\nUSER QUERY: {user_query}")
            return response.text
        except Exception as e:
            return f"System Error: {str(e)}"
            
