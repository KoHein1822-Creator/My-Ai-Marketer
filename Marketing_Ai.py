import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v69.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* Sidebar Overhaul for Spatial Balance */
    section[data-testid="stSidebar"] { 
        background-color: #010409 !important; 
        border-right: 1px solid #30363d; 
        min-width: 300px !important;
    }

    /* Section Headers - Elevated Typography */
    .sidebar-label {
        font-size: 13px;
        font-weight: 600;
        color: #58a6ff;
        margin-top: 30px;
        margin-bottom: 12px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Professional Button Styling */
    div.stButton > button {
        width: 100%;
        border-radius: 6px;
        height: 42px;
        font-size: 14px !important;
        font-weight: 500;
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #c9d1d9;
    }
    div.stButton > button:hover { border-color: #58a6ff; color: #58a6ff; background: #0d1117; }
    
    /* Active Model Box */
    .active-indicator {
        background: #0d1117;
        border-left: 3px solid #58a6ff;
        padding: 10px;
        margin-top: 5px;
        font-size: 13px;
    }

    /* Layout Spacing */
    .spacer { margin-bottom: 40px; }
    
    /* System Status at Bottom */
    .status-container {
        margin-top: 100px; /* Pushes to bottom area */
        padding: 15px;
        border-top: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Spatial Redesign) ---
with st.sidebar:
    # --- Branding ---
    st.markdown('<div style="padding: 10px 0;">', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 24px; font-weight: 700; color: white; margin-bottom:0;">Sayar Gyi\'s</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 14px; font-weight: 600; color: #58a6ff; letter-spacing: 3px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.divider()

    # --- THE BRAIN ---
    st.markdown('<p class="sidebar-label">The Brain</p>', unsafe_allow_html=True)
    # 2-column layout to ensure text fits comfortably
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini"): st.session_state.model_choice = "Gemini"
        if st.button("Claude"): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("ChatGPT"): st.session_state.model_choice = "ChatGPT"

    st.markdown(f'<div class="active-indicator">Running: <b style="color:#58a6ff;">{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # --- INTELLIGENCE ---
    st.markdown('<p class="sidebar-label">Intelligence</p>', unsafe_allow_html=True)
    if st.button("Market Intelligence Hub", use_container_width=True):
        st.session_state.menu = "Market Intelligence Hub"

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # --- NAVIGATION ---
    st.markdown('<p class="sidebar-label">System Menu</p>', unsafe_allow_html=True)
    # Using a list with larger font via radio or custom buttons
    nav_selected = st.radio("Select View", ["Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    # Internal Logic mapping
    menu_map = {"Dashboard": "Interactive Dashboard", "Brand DNA": "Brand DNA", "Project Archive": "Project Archive", "Asset Library": "Asset Library"}
    if st.session_state.menu not in ["Market Intelligence Hub", "Creator Mode"]:
        st.session_state.menu = menu_map[nav_selected]

    st.markdown('<div class="spacer"></div>', unsafe_allow_html=True)

    # --- CREATOR MODE ---
    st.markdown('<p class="sidebar-label">Execution</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"

    # --- SYSTEM STATUS (Bottom Aligned) ---
    st.markdown('<div class="status-container">', unsafe_allow_html=True)
    st.markdown('<p style="font-size:11px; color:#8b949e; margin-bottom:5px;">SYSTEM STATUS</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#3fb950; font-size:14px; font-weight:600;">● Core Engine: Online</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e; font-size:10px;">Version 69.0.2 Stable</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (V32.0 Restore & Polishing) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="color: #58a6ff; font-size: 32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # Row 1: Metrics
    st.markdown('<p class="sidebar-label" style="color:#8b949e;">Content Status</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12"); c2.metric("Pending", "5")
    c3.metric("Scheduled", "18"); c4.metric("Published", "145")
    
    st.divider()
    
    # Row 2: Analytics
    st.markdown('<p class="sidebar-label" style="color:#8b949e;">Performance Analytics</p>', unsafe_allow_html=True)
    chart_data = pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach'])
    st.bar_chart(chart_data, color="#58a6ff", use_container_width=True)

elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 style="color: #58a6ff;">Market Intelligence Hub</h1>', unsafe_allow_html=True)
    st.tabs(["Industry News", "Competitor Research", "Trend Analytics"])

else:
    st.markdown(f'<h1 style="color: #58a6ff;">{st.session_state.menu}</h1>', unsafe_allow_html=True)
