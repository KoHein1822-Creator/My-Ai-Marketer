import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Preserving v71.0) ---
if 'menu' not in st.session_state: st.session_state.menu = "Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v72.0", layout="wide")

# ADVANCED CSS FOR POLISHED FINISH
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; }
    
    section[data-testid="stSidebar"] { 
        background-color: #010409 !important; 
        min-width: 320px !important; 
    }

    .sidebar-header {
        font-size: 13px; font-weight: 700; color: #58a6ff;
        margin-top: 25px; margin-bottom: 12px;
        letter-spacing: 1.5px; text-transform: uppercase;
    }

    /* Professional Button Styling */
    div.stButton > button {
        height: 48px !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Active Core Indicator */
    .active-core-box {
        background: rgba(88, 166, 255, 0.1);
        border: 1px solid rgba(88, 166, 255, 0.3);
        padding: 8px;
        border-radius: 6px;
        text-align: center;
        margin-top: 10px;
        font-size: 12px;
        color: #58a6ff;
    }

    /* System Status Refinement */
    .status-panel {
        background: #0d1117;
        border: 1px solid #30363d;
        padding: 18px;
        border-radius: 10px;
        margin-top: 10px;
    }
    
    .status-node-info {
        font-size: 10px;
        color: #8b949e;
        margin-top: 8px;
        border-top: 1px solid #21262d;
        padding-top: 8px;
        display: flex;
        justify-content: space-between;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Revised Structure) ---
with st.sidebar:
    # Branding
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
    
    st.markdown(f'<div class="active-core-box">Active Core: <b>{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    st.divider()

    # SYSTEM MENU
    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    # SPECIAL FUNCTIONS
    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", key="intel", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", key="creat", use_container_width=True): st.session_state.menu = "Creator Mode"
    
    # ပြန်ထည့်ပေးလိုက်သော Section ခွဲတဲ့မျဉ်း
    st.divider()

    # SYSTEM STATUS (Redesigned with Spatial Utilization)
    st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
            <p style="color:#8b949e; font-size:11px; margin-top:2px;">Network: Stable (12ms)</p>
            <div class="status-node-info">
                <span>NODE: SG-AI-01</span>
                <span>UPTIME: 99.9%</span>
            </div>
            <p style="font-size:9px; color:#58a6ff; margin-top:5px; opacity:0.7;">🔒 End-to-End Encryption Active</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE ---
if st.session_state.menu == "Dashboard":
    st.markdown('<h1 style="color:#58a6ff; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    st.markdown("### Content Creation Status")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12"); c2.metric("Pending", "5")
    c3.metric("Scheduled", "18"); c4.metric("Published", "145")
    st.divider()
    st.markdown("### Platform Metrics")
    chart_data = pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach'])
    st.bar_chart(chart_data, color="#58a6ff")

elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 style="color:#58a6ff;">Asset Library</h1>', unsafe_allow_html=True)
    # v32.0 screenshot logic
    st.tabs(["Media", "Copywriting", "Legal"])

else:
    st.markdown(f'<h1 style="color:#58a6ff;">{st.session_state.menu}</h1>', unsafe_allow_html=True)
