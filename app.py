import streamlit as st
import time
from PIL import Image

# Project X Modules
from core_ui import ProjectXUI
from scout import MarketScout
from brain import IntelligenceCore
from config import ProjectConfig
from vision import VisionIntelligence

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    page_title="Project X | Enterprise Intelligence",
    page_icon="💠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. SESSION STATE (The App's Memory) ---
if "intelligence_log" not in st.session_state:
    st.session_state.intelligence_log = []
if "user_profile" not in st.session_state:
    st.session_state.user_profile = {"name": "Sathwik", "role": "Architect"}

# --- 3. COMPONENT INITIALIZATION ---
ui = ProjectXUI()
scout = MarketScout()
ai = IntelligenceCore()
api_key = ProjectConfig.get_api_key()

# --- 4. THE INTERFACE ---
ui.apply_custom_theme()

with st.sidebar:
    ui.render_header(node_name="VIZAG-01")
    st.markdown("---")
    
    # Advanced Controls for Parents
    st.subheader("🛠️ Control Console")
    language = st.selectbox("Interface Language", ["English", "Telugu", "Hindi"])
    search_depth = st.slider("Search Depth (Nodes)", 5, 20, 12)
    
    if st.button("🗑️ Clear Neural Link", use_container_width=True):
        st.session_state.intelligence_log = []
        st.rerun()

    st.markdown("---")
    
    # --- VISUAL SEARCH MODULE ---
    st.subheader("👁️ Visual Search")
    uploaded_image = st.file_uploader("Upload Appliance/Gadget Photo", type=["jpg", "png", "jpeg"])
    
    if uploaded_image:
        img = Image.open(uploaded_image)
        st.image(img, caption="Target Acquired", use_container_width=True)
        
        if st.button("Identify & Search", use_container_width=True):
            with st.spinner("Extracting product signatures..."):
                vision_engine = VisionIntelligence(api_key)
                identified_target = vision_engine.identify_product(img)
                
                if "INVALID_TARGET" in identified_target or "ERROR" in identified_target:
                    st.error(f"Scan Failed: {identified_target}. Please upload a clear photo of an electronic device.")
                else:
                    st.success(f"Target Identified: {identified_target}")
                    
                    # The Magic Hook: Inject the identified item directly into the chat flow!
                    auto_prompt = f"Find the best price for: {identified_target}"
                    st.session_state.intelligence_log.append({"role": "user", "content": auto_prompt})
                    st.rerun() # Forces the app to loop down and execute the Scout!

# --- 5. MAIN EXECUTION FLOW ---
st.write(f"### Welcome back, {st.session_state.user_profile['name']}.")

# Display the Chat History with Professional Bubbles
for entry in st.session_state.intelligence_log:
    with st.container():
        if entry["role"] == "user":
            st.markdown(f'<div class="chat-bubble user-bubble">{entry["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-bubble ai-bubble">{entry["content"]}</div>', unsafe_allow_html=True)

# --- 6. INPUT & REASONING ---
if prompt := st.chat_input("Query the market (e.g., 'Find the best 1.5 Ton Split AC')"):
    # Log User Input
    st.session_state.intelligence_log.append({"role": "user", "content": prompt})
    st.rerun()

# Check if the last message needs an AI response
if st.session_state.intelligence_log and st.session_state.intelligence_log[-1]["role"] == "user":
    last_query = st.session_state.intelligence_log[-1]["content"]
    
    with st.spinner("⚡ Initializing Multi-Node Reconnaissance..."):
        # Step A: The Scout goes to work
        market_data = scout.get_market_intelligence(last_query)
        
        # Step B: The Brain analyzes the data
        analysis = ai.generate_consultation(last_query, market_data, language=language)
        
        # Step C: Log the AI's professional advice
        st.session_state.intelligence_log.append({"role": "ai", "content": analysis})
        st.rerun()
