from google import genai
from config import ProjectConfig

class VisionIntelligence:
    def __init__(self, api_key):
        self.client = genai.Client(api_key=api_key)

    def identify_product(self, image_data):
        prompt = """
        ROLE: Hardware Intelligence Analyzer.
        TASK: Look at this image and identify the electronic device or appliance.
        OUTPUT FORMAT: Only return the precise brand and model name.
        If it is NOT an electronic device or appliance, reply with: 'INVALID_TARGET'.
        """
        try:
            response = self.client.models.generate_content(
                model=ProjectConfig.MODEL_CORE,
                contents=[prompt, image_data]
            )
            return response.text.strip()
        except Exception as e:
            return f"ERROR_VISION_SYNC: {str(e)}"
            
