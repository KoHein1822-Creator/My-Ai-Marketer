import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIG & ORIGINAL v27.0 THEME ---
st.set_page_config(page_title="SAYAR GYI v55.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    
    /* Original Sidebar Style */
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    
    /* Core Layout Elements */
    .header-blue { color: #58a6ff; font-weight: 600; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    .trend-alert { border-left: 4px solid #ff6b6b; background: #1c1c1c; padding: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. ORIGINAL SIDE PANEL (v27.0 Framework) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    # Smart Features (New additions but kept in Original Format)
    st.markdown('<p class="nav-label">Intelligence Control</p>', unsafe_allow_html=True)
    if st.button("🧠 Strategy & Guard Dog", use_container_width=True): st.session_state.menu = "Strategy"
    if st.button("🚨 Monitoring & Spy Center", use_container_width=True): st.session_state.menu = "Monitoring"
    if st.button("📊 Executive Report AI", use_container_width=True): st.session_state.menu = "Executive Report"

    st.divider()
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content Production"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"
    if st.button("👥 Ethical Lead CRM", use_container_width=True): st.session_state.menu = "Leads"

    st.divider()
    # Original Navigation Links
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    
    st.divider()
    st.success("Core Engine: Online")
    brain_choice = st.segmented_control("Model", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE (Refining sections while keeping UI consistency) ---

# A. STRATEGY & GUARD DOG (New v55.0 Logic)
if st.session_state.menu == "Strategy":
    st.markdown('<h1 class="header-blue">🧠 AI Strategy & Guard Dog</h1>', unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="trend-alert"><b>Trend Jacking:</b> Transition Videos are Viral.</div>', unsafe_allow_html=True)
        st.button("Update Monthly Plan with Trend")
    with c2:
        st.error("Crisis Watch: 1 Negative Comment detected.")
        st.button("Authorize AI Defense Response")

# B. CONTENT PRODUCTION (The Monthly Autopilot Engine)
elif st.session_state.menu == "Content Production":
    st.markdown('<h1 style="color:#d3b6ff;">🎬 Content Factory</h1>', unsafe_allow_html=True)
    t1, t2 = st.tabs(["Monthly Calendar", "Bulk Generator"])
    with t2:
        st.button("🚀 Generate (1) Month Content (Video/Script/Images)")
    with t1:
        st.info("Batch Approval Required for 30 Posts.")

# C. INTERACTIVE DASHBOARD (Original v27.0 Layout)
elif st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Engagement", "12.5k", "+12%")
    s2.metric("Leads", "150", "+5%")
    s3.metric("Response Rate", "100%", "Perfect")
    s4.metric("Autonomy", "98%", "Stable")
    st.divider()
    st.tabs(["Facebook", "TikTok", "YouTube"])

# D. LEADS (CRM)
elif st.session_state.menu == "Leads":
    st.markdown('<h1 style="color:#aff5b4;">👥 Ethical Lead CRM</h1>', unsafe_allow_html=True)
    st.write("Captured Leads from Inbox-Only Strategy:")
    st.table(pd.DataFrame({"Name": ["Ma Thandar"], "Phone": ["09-450XXX"], "Interest": ["Gold"]}))

else:
    st.title(st.session_state.menu)
