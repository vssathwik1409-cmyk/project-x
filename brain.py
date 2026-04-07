import json
from groq import Groq
from config import Config
from guard import Sentinel

class IntelligenceCore:
    """
    THE BRAIN: 
    Powered by Groq's LPU. Parses raw scraped data into structured market intelligence.
    """
    def __init__(self):
        # Initializes the client using the key verified by the Config module
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL

    @Sentinel.error_boundary
    def process_intelligence(self, query, raw_data):
        """
        Feeds raw data to Llama-3.3-70b-versatile and forces a strict JSON output.
        """
        Sentinel.log_event(f"Transmitting raw payload to Groq LPU for target: {query}")
        
        # If the Hydra Scraper failed completely, we don't waste Groq tokens.
        if raw_data == "MARKET DATA INACCESSIBLE.":
            Sentinel.log_event("Aborting LPU transmission: No raw data.", "WARNING")
            return {"error": "Scraping failed.", "lowest_price": "N/A", "trend": "Unknown"}

        # The System Prompt: This programs the AI's behavior and strictness.
        system_prompt = (
            "You are Sentri.ai, an elite, uncompromising market intelligence engine. "
            "Analyze the provided scraped data for the target product. "
            "Extract the following: 'lowest_price' (number or string), 'average_price' (number or string), "
            "'market_trend' (e.g., 'Volatile', 'Stable', 'Dropping'), and a 'summary' (1 sharp sentence). "
            "You must output STRICTLY in JSON format with these exact keys. "
            "Do not include any markdown formatting or extra text."
        )

        user_prompt = f"TARGET: {query}\n\nRAW SCRAPED DATA:\n{raw_data}"

        # Execute the Groq LPU
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.1, # Extremely low temperature to prevent hallucination
            max_tokens=Config.MAX_OUTPUT_TOKENS,
            response_format={"type": "json_object"} # Forces perfect JSON
        )

        # Validate and Parse the JSON response
        try:
            result = json.loads(response.choices[0].message.content)
            Sentinel.log_event("Groq synthesis complete. JSON payload structured.", "SUCCESS")
            return result
        except json.JSONDecodeError as e:
            Sentinel.log_event(f"Groq returned malformed JSON: {e}", "CRITICAL")
            return {"error": "LPU output parsing failed.", "raw_output": response.choices[0].message.content}
        
