# vision.py
import google.generativeai as genai
from config import ProjectConfig

class VisionIntelligence:
    """Handles Image-to-Text capabilities for Project X."""
    
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(ProjectConfig.MODEL_CORE)

    def identify_product(self, image_data):
        """
        Takes an uploaded image (Pillow object) and returns a specific 
        product query for the Scout engine.
        """
        prompt = """
        ROLE: Hardware Intelligence Analyzer.
        TASK: Look at this image and identify the electronic device or appliance.
        OUTPUT FORMAT: Only return the precise brand and model name, formatted as a search query. 
        Example: 'Sony PlayStation 5 Digital Edition' or 'Voltas 1.5 Ton Split AC'.
        If it is NOT an electronic device or appliance, reply with: 'INVALID_TARGET'.
        """
        
        try:
            # Gemini processes the text prompt and the image simultaneously
            response = self.model.generate_content([prompt, image_data])
            return response.text.strip()
        except Exception as e:
            return f"ERROR_VISION_SYNC: {str(e)}"
          
