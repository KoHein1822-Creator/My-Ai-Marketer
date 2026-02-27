import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (v32.0 Original) ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Interactive Dashboard"

# --- 2. PAGE CONFIG & v32.0 THEME ---
st.set_page_config(page_title="SAYAR GYI v32.0 Updated", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v32.0 Structure - Buttons Only Updated) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Main Menu</p>', unsafe_allow_html=True)
    if st.button("📊 Strategic Dashboard", use_container_width=True): st.session_state.menu = "Interactive Dashboard"
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): st.session_state.menu = "Market Intelligence Hub"
    if st.button("🎨 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    
    st.divider()
    st.markdown('<p class="nav-label">Management</p>', unsafe_allow_html=True)
    if st.button("📂 Project Archive", use_container_width=True): st.session_state.menu = "Project Archive"
    if st.button("📦 Asset Library", use_container_width=True): st.session_state.menu = "Asset Library"
    
    st.divider()
    st.success("v32.0 Stable Build + Hub Upgrade")

# --- 4. MAIN INTERFACE (v32.0 Components) ---

# A. INTERACTIVE DASHBOARD
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Engagement", "12.5k", "+12%")
    col2.metric("Efficiency", "98%", "+2%")
    col3.metric("Leads", "150", "Stable")

# B. PROJECT ARCHIVE (v32.0 Original)
elif st.session_state.menu == "Project Archive":
    st.markdown('<h1 class="header-blue">Project Archive</h1>', unsafe_allow_html=True)
    with st.expander("Add New Project"):
        st.text_input("Client Name"); st.date_input("Start Date"); st.button("Save")
    st.table(pd.DataFrame({"Project": ["Promotion A", "Brand DNA"], "Status": ["Finished", "Active"]}))

# C. ASSET LIBRARY (As requested - No Changes)
elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 class="header-blue">Asset Library</h1>', unsafe_allow_html=True)
    a_tab1, a_tab2, a_tab3 = st.tabs(["Media", "Copywriting", "Legal"])
    with a_tab1:
        st.table(pd.DataFrame({"File": ["Logo.png", "Promo.mp4"], "Type": ["Image", "Video"], "Platform": ["All", "TikTok"]}))
        st.file_uploader("Upload Assets")
    with a_tab2: st.write("Copywriting Templates Store")
    with a_tab3: st.write("Legal & Contract Templates")

# D. MARKET INTELLIGENCE HUB (Updated Industry News Feature)
elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 class="header-blue">🌐 Market Intelligence Hub</h1>', unsafe_allow_html=True)
    if st.button("Back"): st.session_state.menu = "Interactive Dashboard"
    
    # 3-in-1 Logic Integration
    i_tab1, i_tab2, i_tab3 = st.
