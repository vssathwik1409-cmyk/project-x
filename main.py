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
        return f"{data.get('city')}, {data.get('region')}"
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
query = st.text_input("", placeholder="Enter target device (e.g. Sony PS5, Macbook M3, Moglix tools)...")

if query:
    with st.status("Target Locked. Scouting Global Retailers...", expanded=True):
        # Configure Gemini
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        model = genai.GenerativeModel('models/gemini-1.5-flash')
        
        # Deep Search Query covering TataCLiQ and Moglix
        search_query = f"'{query}' price India site:amazon.in OR site:flipkart.com OR site:tatacliq.com OR site:moglix.com OR site:croma.com OR site:reliancedigital.in OR site:vijaysales.com"
        
        with DDGS() as ddgs:
    # Adding 'India' inside the search string helps the US server find local results
    results = [r for r in ddgs.text(f"{query} price in INR India", max_results=10)]
    
        
        
        analysis_prompt = f"""
        User Location: {user_loc}
        User Query: {query}
        Raw Data: {results}
        
        You are Project X Intelligence. Provide:
        1. A clean comparison table of all variants and prices found.
        2. Absolute Best Value recommendation for someone in {user_loc}.
        3. TECH ADVICE: Is this the right time to buy? Any model refreshes coming?
        4. VERDICT: [PROCEED], [HOLD], or [ABORT].
        
        Tone: Cold, professional, and accurate.
        """
        response = model.generate_content(analysis_prompt)
    
    st.markdown("### 📊 Intelligence Brief")
    st.markdown(response.text)
else:
    st.info("Awaiting input for Project X.")
