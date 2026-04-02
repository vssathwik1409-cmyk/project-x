import random
import time
from duckduckgo_search import DDGS

class MarketScout:
    """Enterprise-grade web scraping with anti-blocking protocols."""
    
    def __init__(self):
        self.stores = [
            "Amazon.in", "Flipkart", "Croma", "Reliance Digital", "Vijay Sales", 
            "Tata Cliq", "Poorvika", "Sangeetha Mobiles", "Moglix", "Jiomart"
        ]
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_2_1) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) Gecko/20100101 Firefox/122.0"
        ]

    def get_market_intelligence(self, product_name):
        """Orchestrates multi-node search and returns raw retail data."""
        results = []
        
        # FIX: Bulletproof string formatting to prevent SyntaxErrors
        store_string = " OR ".join(self.stores)
        query = f"{product_name} price India ({store_string}) buy official"
        
        try:
            # Random jitter to simulate human browsing
            time.sleep(random.uniform(1.2, 2.5))
            
            with DDGS(headers={"User-Agent": random.choice(self.user_agents)}) as ddgs:
                raw_data = list(ddgs.text(query, max_results=15))
                for item in raw_data:
                    results.append({
                        "source": item.get('href', 'Unknown'),
                        "snippet": item.get('body', ''),
                        "title": item.get('title', '')
                    })
            return results
        except Exception as e:
            return [{"error": f"Node Communication Failure: {str(e)}"}]
    
