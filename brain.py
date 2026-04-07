import json
from groq import Groq
from config import Config
from guard import Sentinel

class IntelligenceCore:
    def __init__(self):
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL

    @Sentinel.error_boundary
    def process_intelligence(self, query, raw_data):
        Sentinel.log_event(f"Analyzing market strategy for: {query}")
        
        if raw_data == "MARKET DATA INACCESSIBLE.":
            return {"error": "Connection failed.", "summary": "I couldn't reach the markets. Please try again."}

        # THE STRATEGIC ADVISOR PROMPT
        system_prompt = (
            "You are Project X, a high-end, friendly yet professional market intelligence advisor. "
            "Your goal is to analyze raw scraped data and provide a 'Buy or Wait' strategy. "
            "\n\nSTRICT RULES:"
            "1. Be conversational. If the user says 'I need a laptop', treat them like a VIP client."
            "2. Suggest whether to BUY NOW or WAIT based on price trends."
            "3. Identify which platform (e.g., Amazon, Croma) offers the best value or reliability."
            "4. Predict if prices will drop (e.g., upcoming sales or product cycles)."
            "5. You MUST return a STRICT JSON object with these keys: "
            "'lowest_price', 'best_platform', 'strategy' (Buy Now/Wait), 'market_trend', 'summary'."
        )

        user_prompt = f"USER REQUEST: {query}\n\nRAW DATA GATHERED:\n{raw_data}"

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3, # Slightly higher for better 'friendly' personality
            response_format={"type": "json_object"}
        )

        try:
            return json.loads(response.choices[0].message.content)
        except Exception:
            return {"error": "Synthesis failed."}
            
