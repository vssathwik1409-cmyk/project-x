import streamlit as st

# --- IMPORT ENTERPRISE MODULES ---
from config import Config
from guard import Sentinel
from vault import MemoryVault
from scout import ScoutEngine
from brain import IntelligenceCore
from core_ui import UI_Engine

# --- 1. SYSTEM INITIALIZATION ---
st.set_page_config(
    page_title="SENTRI.AI | COMMAND",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Initialize Defense and Memory
Sentinel.initialize_session()
MemoryVault.initialize()

# Inject Luxury Option 2 Styling (Ferrari/Minimalist Vibe)
UI_Engine.inject_premium_css()

# --- 2. THE DASHBOARD ---
UI_Engine.render_header()

# Execution Input
query = st.text_input("ENTER TARGET ASSET", placeholder="e.g., RTX 5090, PS5 Pro, or Ferrari 812")

if st.button("INITIATE RECON"):
    if not query:
        st.warning("SYSTEM STANDBY: TARGET DESIGNATION REQUIRED.")
    else:
        # Step 1: Query The Vault (Check Memory)
        cached_result = MemoryVault.retrieve_data(query)
        
        if cached_result:
            st.success("DATA RETRIEVED FROM VAULT (LATENCY: 0.01s)")
            UI_Engine.display_results(cached_result)
        
        else:
            # Step 2: Engage The Engine (Scrape & Process)
            with st.status(f"EXECUTING HYDRA PROTOCOL: {query.upper()}...", expanded=True) as status:
                
                # Instantiate Engines
                scout = ScoutEngine()
                brain = IntelligenceCore()
                
                # Phase A: Data Acquisition
                st.write("Deploying stealth scrapers...")
                recon_data = scout.acquire_target_data(query)
                
                if recon_data["status"] == "FAILURE":
                    status.update(label="RECON FAILED", state="error")
                    st.error("MARKET DATA INACCESSIBLE. ALL SCRAPING TIERS BLOCKED.")
                else:
                    # Phase B: Data Synthesis via Groq LPU
                    st.write("Synthesizing raw data via Groq LPU...")
                    final_intel = brain.process_intelligence(query, recon_data["payload"])
                    
                    if "error" not in final_intel:
                        # Phase C: Lock Intel in Vault
                        MemoryVault.store_data(query, final_intel)
                    
                    status.update(label="INTELLIGENCE SECURED", state="complete")
            
            # Step 3: Render Results to UI
            UI_Engine.display_results(final_intel)

# --- 3. SYSTEM LOGS (THE GOGGINS MONITOR) ---
st.write("---")
with st.expander("TERMINAL / SYSTEM LOGS"):
    for log in reversed(st.session_state.logs):
        if "CRITICAL" in log or "ERROR" in log:
            st.markdown(f"<span style='color:{UI_Engine.ACCENT_RED};'>{log}</span>", unsafe_allow_html=True)
        elif "SUCCESS" in log:
            st.markdown(f"<span style='color:#00C853;'>{log}</span>", unsafe_allow_html=True)
        else:
            st.markdown(f"<span style='color:{UI_Engine.TEXT_DIM};'>{log}</span>", unsafe_allow_html=True)
                    
