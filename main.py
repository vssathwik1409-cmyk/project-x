import streamlit as st
import google.generativeai as genai
from duckduckgo_search import DDGS
import requests

# 1. UI SETUP - "Project X: Stealth Mode"
st.set_page_config(page_title="Project X | Elite Scout", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;700&display=swap');
    html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; background-color: #000000; color: #ffffff; }
    .stTextInput>div>div>input { background-color: #0a0a0a; color: #00ff41; border: 1px solid #444; border-radius: 4px; font-size: 1.1rem; }
    .stButton>button { background: #ffffff; color: #000000; font-weight: 800; border-radius: 0px; height: 3em; width: 100%; border: none; }
    .stButton>button:hover { background: #00ff41; color: #000; }
    </style>
    """, unsafe_allow_html=True)

# 2. LOCATION INTELLIGENCE
def get_user_location():
    try:
        data = requests.get('https://ipapi.co/json/').json()
        return f"{data.get('city', 'Unknown')}, {data.get('region', 'India')}"
    except: return "India"

user_loc = get_user_location()

# 3. SIDEBAR (The Founder's Console)
with st.sidebar:
    st.title("🚀 PROJECT X")
    st.markdown("---")
    st.write(f"**ARCHITECT:** SATHWIK")
    st.write(f"**NODE:** {user_loc}")
    st.divider()
    st.caption("SCANNING: Amazon, Flipkart, Tata CLiQ, Moglix, Croma, Reliance, Vijay Sales")

# 4. SEARCH & REASONING ENGINE
st.title("System X: Electronics Intelligence")
# Fixed accessibility label here
query = st.text_input("Search Target", placeholder="Enter target device (e.g. Sony PS5, Macbook M3)...", label_visibility="collapsed")

if query:
    with st.status("Target Locked. Scouting Global Retailers...", expanded=True):
        # Configure Gemini
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # Standard model name for 2026
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Deep Search Logic
        search_query = f"{query} price India Amazon Flipkart TataCLiQ Moglix"
        
        # FIXED INDENTATION BLOCK BELOW
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(search_query, max_results=10)]
        
        analysis_prompt = f"""
        User Location: {user_loc}
        User Query: {query}
        Raw Data: {results}
        
        You are Project X Intelligence. Provide:
        1. A clean comparison table of prices found.
        2. Absolute Best Value recommendation.
        3. VERDICT: [PROCEED], [HOLD], or [ABORT].
        
        Tone: Cold, professional, and accurate.
        """
        response = model.generate_content(analysis_prompt)
    
    st.markdown("### 📊 Intelligence Brief")
    st.markdown(response.text)
else:
    st.info("Awaiting input for Project X.")
        
