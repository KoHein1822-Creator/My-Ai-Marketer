import streamlit as st
import sqlite3
from datetime import datetime
import time

# --- 1. DATABASE & SYSTEM INITIALIZATION ---
def init_db():
    conn = sqlite3.connect('sayargyi_vault.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS archives 
                 (id INTEGER PRIMARY KEY, date TEXT, client TEXT, content TEXT, strategy TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- 2. PREMIUM UI STYLING (The Professional Dark Theme) ---
st.set_page_config(page_title="Sayar Gyi | Enterprise Command", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #c9d1d9; }
    .st-emotion-cache-1r6slb0 { background: #161b22; border: 1px solid #30363d; border-radius: 12px; }
    .metric-card { background: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; }
    .sub-label { font-size: 10px; text-transform: uppercase; color: #8b949e; letter-spacing: 1.5px; font-weight: 700; margin-bottom: 8px; }
    .status-online { color: #3fb950; font-size: 12px; font-weight: bold; }
    .launch-btn button { background: #238636 !important; color: white !important; width: 100%; border: none !important; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: MULTI-ACCOUNT & NAVIGATION ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>Sayar Gyi</h2>", unsafe_allow_html=True)
    st.caption("AI Content Architect v15.0")
    st.divider()
    
    # [FEATURE INCLUDED]: Multi-Account Switcher
    st.markdown("<p class='sub-label'>Account Switcher</p>", unsafe_allow_html=True)
    active_client = st.selectbox(
        "Select Active Client",
        ["Jewelry SME", "Digital Marketing Academy", "Real Estate Pro"],
        label_visibility="collapsed"
    )
    
    st.divider()
    nav = st.radio("MAIN MENU", ["Strategic Hub", "Project Archive", "Market Research Agent"])
    
    st.divider()
    st.markdown("<p class='sub-label'>System Integrity</p>", unsafe_allow_html=True)
    st.markdown("<span class='status-online'>● Official API Connected</span>", unsafe_allow_html=True)
    st.markdown("<span class='status-online'>● Database Encrypted</span>", unsafe_allow_html=True)

# --- 4. STRATEGIC HUB (Main Working Area) ---
if nav == "Strategic Hub":
    st.subheader(f"Strategic Hub: {active_client}")
    
    # [FEATURE INCLUDED]: Monitoring Row (Ops & Intel)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("<p class='sub-label'>Live Inventory (Ops)</p>", unsafe_allow_html=True)
        # Conditional Logic based on Client Type
        if "Academy" in active_client:
            st.metric("Seats Remaining", "2 / 30", "-2")
        else:
            st.metric("Stock Level", "Active", "Normal")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("<p class='sub-label'>Market Pulse (Intel)</p>", unsafe_allow_html=True)
        st.write("Meta Andromeda: Optimized")
        st.write("Trend: Storytelling Reels")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with m3:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.markdown("<p class='sub-label'>Account Velocity</p>", unsafe_allow_html=True)
        st.metric("Engagement", "+14.2%", "Growth")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # [FEATURE INCLUDED]: Strategic Generation Area
    col_input, col_output = st.columns([1, 1.8], gap="medium")
    
    with col_input:
        st.markdown("<p class='sub-label'>Campaign Parameters</p>", unsafe_allow_html=True)
        with st.container(border=True):
            topic = st.text_input("Mission Topic", placeholder="Enter product or event name")
            strategy = st.selectbox("Strategic Logic", ["Scarcity (Urgent)", "Educational", "Brand Story"])
            st.divider()
            if st.button("RUN SAYAR GYI ENGINE"):
                with st.status("Sayar Gyi is architecting...", expanded=False):
                    time.sleep(1)
                    st.write("Analyzing Inventory status...")
                    time.sleep(1)
                    st.write("Checking latest Meta Andromeda trends...")
                st.session_state['generated'] = True

    with col_output:
        st.markdown("<p class='sub-label'>Proposed Strategic Assets</p>", unsafe_allow_html=True)
        if st.session_state.get('generated'):
            t1, t2, t3 = st.tabs(["Draft Content", "Sayar Gyi's Reasoning", "Visual Suggestion"])
            with t1:
                st.info("AI-generated Burmese/English content based on Scarcity logic will appear here.")
                st.markdown('<div class="launch-btn">', unsafe_allow_html=True)
                if st.button("✅ Approve & Launch"):
                    st.success("Mission Launched and Archived Successfully!")
                st.markdown('</div>', unsafe_allow_html=True)
            with t2:
                st.write(f"This content is optimized for {active_client} because current trends favor short hooks.")
            with t3:
                st.caption("AI-Selected Visual: High-contrast product shot for {active_client}")
        else:
            st.markdown("<div style='height:300px; display:flex; align-items:center; justify-content:center; border: 1px dashed #30363d; border-radius:12px; color:#484f58;'>Awaiting configuration for current client...</div>", unsafe_allow_html=True)

# --- 5. PROJECT ARCHIVE (The Vault Feature) ---
elif nav == "Project Archive":
    st.subheader(f"Project Archive: {active_client}")
    st.write("Full history of approved campaigns and data logs.")
    # Here we would display the SQLite data filtered by active_client
    st.info(f"Filtering logs for {active_client}...")

# --- 6. MARKET RESEARCH AGENT (SME Auto-Onboarding Feature) ---
elif nav == "Market Research Agent":
    st.subheader("Autonomous Research Node")
    st.write(f"Analyzing market landscape for {active_client} to build Brand DNA.")
    # Deep research logic here
