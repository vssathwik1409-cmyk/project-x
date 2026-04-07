import streamlit as st
import time
from config import Config
from guard import Sentinel

class MemoryVault:
    """
    THE VAULT:
    High-speed caching engine. Intercepts redundant queries 
    to protect Groq API limits and drop latency to zero.
    """
    @staticmethod
    def initialize():
        """Secures the memory sector in the session state."""
        if 'vault_cache' not in st.session_state:
            st.session_state.vault_cache = {}

    @staticmethod
    def store_data(query, data_dict):
        """Locks the scraped and processed JSON into The Vault."""
        MemoryVault.initialize()
        st.session_state.vault_cache[query.lower()] = {
            "timestamp": time.time(),
            "payload": data_dict
        }
        Sentinel.log_event(f"Intelligence for '{query}' locked in The Vault.", "CACHE")

    @staticmethod
    def retrieve_data(query):
        """Checks if we have fresh intel before waking up the scrapers."""
        MemoryVault.initialize()
        query_key = query.lower()
        
        if query_key in st.session_state.vault_cache:
            cached_item = st.session_state.vault_cache[query_key]
            age = time.time() - cached_item["timestamp"]
            
            # Check if the data is still within the Time-To-Live (TTL) window
            if age < Config.CACHE_TIME:
                Sentinel.log_event(f"Vault hit for '{query}'. Bypassing network. (Age: {int(age)}s)", "SUCCESS")
                return cached_item["payload"]
            else:
                Sentinel.log_event(f"Intel for '{query}' expired. Purging cache.", "WARNING")
                del st.session_state.vault_cache[query_key]
        
        return None
      
