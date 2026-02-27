import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Ensuring no data loss) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v76.0", layout="wide")

# v72.0 SIDEBAR + v32.0 DASHBOARD + BRAND DNA CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* v72.0 Sidebar Exact Restoration */
    section[data-testid="stSidebar"] { background-color: #010409 !important; min-width: 320px !important; border-right: 1px solid #30363d; }
    .sidebar-header { font-size: 13px; font-weight: 700; color: #58a6ff; margin-top: 25px; margin-bottom: 12px; letter-spacing: 1.5px; text-transform: uppercase; }
    
    /* The Brain Buttons Grid */
    div.stButton > button {
        height: 48px !important; font-size: 15px !important; font-weight: 600 !important;
        border-radius: 8px !important; background-color: #161b22 !important;
        border: 1px solid #30363d !important; color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Dashboard Metric Card Style */
    div[data-testid="stMetric"] {
        background-color: #161b22; border: 1px solid #30363d;
        padding: 20px !important; border-radius: 12px;
    }

    /* Status Panel Restoration */
    .status-panel { background: #0d1117; border: 1px solid #30363d; padding: 18px; border-radius: 10px; margin-top: 10px; }
    .status-node-info { font-size: 10px; color: #8b949e; margin-top: 8px; border-top: 1px solid #21262d; padding-top: 8px; display: flex; justify-content: space-between; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v72.0 Engine) ---
with st.sidebar:
    st.markdown('<h1 style="color:white; margin-bottom:0; font-size:28px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:12px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    # THE BRAIN
    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", key="gem", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", key="cla", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", key="gpt", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    st.markdown(f'<div style="background:rgba(88,166,255,0.1); border:1px solid rgba(88,166,255,0.3); padding:8px; border-radius:6px; text-align:center; margin-top:10px; font-size:12px; color:#58a6ff;">Active Core: <b>{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    st.divider()

    # MENU NAVIGATION
    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    # SPECIAL FUNCTIONS
    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    st.divider()

    # SYSTEM STATUS
    st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
            <div class="status-node-info"><span>NODE: SG-MASTER-01</span><span>UPTIME: 99.9%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE LOGIC (RESTORING ALL VIEWS) ---

# --- A. INTERACTIVE DASHBOARD (v32.0 Exact Recovery) ---
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    f_col1, f_col2 = st.columns([1, 1])
    with f_col1:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Timeframe</p>', unsafe_allow_html=True)
        st.segmented_control("T1", ["Weekly", "Monthly", "Yearly"], default="Monthly", label_visibility="collapsed")
    with f_col2:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Visual Filter</p>', unsafe_allow_html=True)
        st.selectbox("F1", ["Bar Chart", "Line Chart", "Trend Analysis"], label_visibility="collapsed")
    
    st.write("")
