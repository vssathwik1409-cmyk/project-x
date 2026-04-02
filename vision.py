from google import genai
from config import ProjectConfig

class VisionIntelligence:
    """Handles Image-to-Text capabilities for Project X."""
    
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def identify_product(self, image_data):
        """Identifies the uploaded image for the Scout engine."""
        prompt = """
        ROLE: Hardware Intelligence Analyzer.
        TASK: Identify the electronic device or appliance.
        OUTPUT FORMAT: Only return the precise brand and model name.
        If it is NOT an electronic device, reply with: 'INVALID_TARGET'.
        """
        
        try:
            response = self.client.models.generate_content(
                model=ProjectConfig.MODEL_CORE,
                contents=[prompt, image_data]
            )
            return response.text.strip()
        except Exception as e:
            return f"ERROR_VISION_SYNC: {str(e)}"
        
