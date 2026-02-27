import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v74.0", layout="wide")

# v72.0 SIDEBAR + MODERN DASHBOARD CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* v72.0 Sidebar Recovery */
    section[data-testid="stSidebar"] { background-color: #010409 !important; min-width: 320px !important; border-right: 1px solid #30363d; }
    .sidebar-header { font-size: 13px; font-weight: 700; color: #58a6ff; margin-top: 25px; margin-bottom: 12px; letter-spacing: 1.5px; text-transform: uppercase; }
    
    /* v72.0 Button Styles */
    div.stButton > button {
        height: 48px !important; font-size: 15px !important; font-weight: 600 !important;
        border-radius: 8px !important; background-color: #161b22 !important;
        border: 1px solid #30363d !important; color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Dashboard Metric Styling */
    div[data-testid="stMetric"] {
        background-color: #161b22; border: 1px solid #30363d;
        padding: 20px !important; border-radius: 12px;
    }
    
    /* System Status Panel (v72.0 Style) */
    .status-panel { background: #0d1117; border: 1px solid #30363d; padding: 18px; border-radius: 10px; margin-top: 10px; }
    .status-node-info { font-size: 10px; color: #8b949e; margin-top: 8px; border-top: 1px solid #21262d; padding-top: 8px; display: flex; justify-content: space-between; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v72.0 Design Restoration) ---
with st.sidebar:
    st.markdown('<h1 style="color:white; margin-bottom:0; font-size:28px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:12px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", key="gem", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", key="cla", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", key="gpt", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    
    st.markdown(f'<div style="background:rgba(88,166,255,0.1); border:1px solid rgba(88,166,255,0.3); padding:8px; border-radius:6px; text-align:center; margin-top:10px; font-size:12px; color:#58a6ff;">Active Core: <b>{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    st.divider()

    # System Status (Spatial Utilization from v72.0)
    st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
            <p style="color:#8b949e; font-size:11px; margin-top:2px;">Network: Stable (12ms)</p>
            <div class="status-node-info"><span>NODE: SG-AI-01</span><span>UPTIME: 99.9%</span></div>
            <p style="font-size:9px; color:#58a6ff; margin-top:5px; opacity:0.7;">🔒 Secure Protocol Active</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (V32.0 Precision + Upgrades) ---
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # Timeframe & Filter (V32.0 Layout)
    f_col1, f_col2 = st.columns([1, 1])
    with f_col1:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Timeframe</p>', unsafe_allow_html=True)
        st.segmented_control("T1", ["Weekly", "Monthly", "Yearly"], default="Monthly", label_visibility="collapsed")
    with f_col2:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Visual Filter</p>', unsafe_allow_html=True)
        st.selectbox("F1", ["Bar Chart", "Line Chart", "Trend Analysis"], label_visibility="collapsed")
    
    st.write("") 

    # Content Creation Status (Upgrade: Added Delta Trends)
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Content Creation Status</p>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Drafting", "12", "+2")
    m2.metric("Pending", "5", "-1")
    m3.metric("Scheduled", "18", "+5")
    m4.metric("Published", "145", "+12")
    
    st.divider()

    # Platform Metrics (Upgrade: Enhanced Visuals)
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Platform Performance</p>', unsafe_allow_html=True)
    p_tabs = st.tabs(["Facebook", "TikTok", "YouTube"])
    
    with p_tabs[0]: # Facebook
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K", "+15%")
        c2.metric("Engagement", "3.2K", "+8%")
        c3.metric("Followers", "12.4K", "+1.2K")
        
        # Rounded Blue Bar Chart (Upgraded Visuals)
        chart_data = pd.DataFrame({'Category': ['Convert', 'Engage', 'Reach'], 'Value': [25, 45, 32]})
        st.bar_chart(chart_data.set_index('Category'), color="#58a6ff", use_container_width=True)

# Placeholder for other menus
else:
    st.markdown(f"<h1>{st.session_state.menu}</h1>", unsafe_allow_html=True)
