import requests
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from fake_useragent import UserAgent
from config import Config
from guard import Sentinel

class ScoutEngine:
    """
    THE HYDRA PROTOCOL: 
    Multi-tier data acquisition framework. If Tier 1 falls, Tier 2 strikes.
    """
    def __init__(self):
        self.ua = UserAgent()
        
    def _generate_stealth_headers(self):
        """Generates a mathematically randomized browser fingerprint."""
        return {
            "User-Agent": self.ua.random,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
        }

    @Sentinel.error_boundary
    def _tier_1_ddgs(self, query):
        """PRIMARY ENGINE: DuckDuckGo Search API (High Speed)"""
        Sentinel.log_event(f"Engaging Tier 1 (DDGS) for target: {query}")
        results = []
        with DDGS() as ddgs:
            # We enforce the SCRAPE_LIMIT defined in config.py
            for r in ddgs.text(f"{query} price {' OR '.join(Config.TARGET_STORES)}", max_results=Config.SCRAPE_LIMIT):
                results.append(r['body'])
        
        if not results:
            raise ValueError("DDGS returned an empty payload. Possible shadow-ban.")
        return " | ".join(results)

    @Sentinel.error_boundary
    def _tier_2_direct_assault(self, query):
        """SECONDARY ENGINE: Direct HTML Parsing (The Sledgehammer)"""
        Sentinel.log_event("Tier 1 failed or blocked. Engaging Tier 2 Direct Assault.", "WARNING")
        
        url = f"https://html.duckduckgo.com/html/?q={query.replace(' ', '+')}+price"
        response = requests.get(url, headers=self._generate_stealth_headers(), timeout=Config.TIMEOUT)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            snippets = [a.text for a in soup.find_all('a', class_='result__snippet')]
            if not snippets:
                raise ValueError("HTML acquired but parsing failed to find target nodes.")
            return " | ".join(snippets)
        elif response.status_code == 429:
            Sentinel.handle_rate_limit(1)
            raise PermissionError("HTTP 429: Target actively rejecting connection.")
        else:
            raise ConnectionError(f"HTTP ERROR: {response.status_code}")

    def acquire_target_data(self, query):
        """
        The Execution Command.
        Attempts all tiers sequentially until data is secured.
        """
        Sentinel.log_event(f"SYSTEM INITIATING RECON: {query.upper()}")
        
        # Phase 1: Try the fast route
        for attempt in range(Config.MAX_RETRIES):
            data = self._tier_1_ddgs(query)
            if data:
                Sentinel.log_event("Target data secured via Tier 1.", "SUCCESS")
                return {"status": "SUCCESS", "source": "DDGS", "payload": data}
            Sentinel.handle_rate_limit(attempt)

        # Phase 2: If Phase 1 is totally burnt, bring the sledgehammer
        for attempt in range(Config.MAX_RETRIES):
            data = self._tier_2_direct_assault(query)
            if data:
                Sentinel.log_event("Target data secured via Tier 2.", "SUCCESS")
                return {"status": "SUCCESS", "source": "BS4_DIRECT", "payload": data}
            Sentinel.handle_rate_limit(attempt)

        # Phase 3: Total blackout
        Sentinel.log_event("CRITICAL FAILURE: ALL TIERS COMPROMISED.", "ERROR")
        return {"status": "FAILURE", "source": "NONE", "payload": "MARKET DATA INACCESSIBLE."}
    
