from google import genai
from config import ProjectConfig

class IntelligenceCore:
    def __init__(self):
        self.client = genai.Client(api_key=ProjectConfig.get_api_key())

    def generate_consultation(self, user_query, market_data, language="English"):
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
            response = self.client.models.generate_content(
                model=ProjectConfig.MODEL_CORE,
                contents=f"{system_prompt}\n\nUSER QUERY: {user_query}"
            )
            return response.text
        except Exception as e:
            return f"System Error: {str(e)}"
            
