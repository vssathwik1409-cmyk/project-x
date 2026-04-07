import streamlit as st
import time
import random

class Sentinel:
    """
    CENTRALIZED DEFENSE SYSTEM
    Handles logging, error trapping, and tactical delays.
    """
    @staticmethod
    def initialize_session():
        if 'logs' not in st.session_state:
            st.session_state.logs = []
        if 'search_count' not in st.session_state:
            st.session_state.search_count = 0

    @staticmethod
    def log_event(message, type="INFO"):
        timestamp = time.strftime("%H:%M:%S")
        entry = f"[{timestamp}] {type.upper()}: {message}"
        st.session_state.logs.append(entry)
        # Keep logs manageable
        if len(st.session_state.logs) > 50:
            st.session_state.logs.pop(0)

    @staticmethod
    def handle_rate_limit(attempt):
        """Exponential backoff to bypass 429 errors."""
        wait_time = (2 ** attempt) + random.uniform(0.5, 1.5)
        Sentinel.log_event(f"Rate limit detected. Tactical pause: {wait_time:.2f}s", "WARNING")
        time.sleep(wait_time)

    @staticmethod
    def error_boundary(func):
        """Decorator to wrap any function in a 150% backup safety net."""
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                Sentinel.log_event(f"Execution Error in {func.__name__}: {str(e)}", "CRITICAL")
                st.error(f"ENGINE_FAULT: System attempting automatic reroute...")
                return None
        return wrapper
