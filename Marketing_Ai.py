import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Data Persistence) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"

# --- 2. PAGE CONFIG & v32.0 ORIGINAL UI THEME ---
st.set_page_config(page_title="SAYAR GYI v60.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .intel-card { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    .status-tag { background: #238636; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v32.0 Structure with Re-organized Buttons) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    # --- INTELLIGENCE SECTION (The New Combined Hub) ---
    st.markdown('<p class="nav-label">Intelligence Center</p>', unsafe_allow_html=True)
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): 
        st.session_state.menu = "Intel Hub"

    st.divider()
    # --- EXECUTION SECTION ---
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"

    st.divider()
    # --- NAVIGATION (v32.0 Original Radio) ---
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    if nav_choice in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"] and st.session_state.menu not in ["Intel Hub", "Content", "Engagement"]:
        st.session_state.menu = nav_choice

    st.
