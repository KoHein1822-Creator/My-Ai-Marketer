import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v73.0", layout="wide")

# V32.0 DASHBOARD LOOK & FEEL CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* Sidebar Scaling & Design */
    section[data-testid="stSidebar"] { background-color: #010409 !important; min-width: 300px !important; border-right: 1px solid #30363d; }
    .sidebar-header { font-size: 13px; font-weight: 700; color: #58a6ff; margin-top: 25px; margin-bottom: 12px; letter-spacing: 1.5px; text-transform: uppercase; }

    /* Metric Cards (V32.0 Style) */
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 20px !important;
        border-radius: 8px;
    }

    /* System Status Panel (As requested) */
    .status-panel {
        background: #0d1117;
        border: 1px solid #30363d;
        padding: 15px;
        border-radius: 8px;
        margin-top: 10px;
    }
    .status-node { font-size: 10px; color: #8b949e; display: flex; justify-content: space-between; border-top: 1px solid #21262d; padding-top: 8px; margin-top: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Synchronized with V72.0 Improvements) ---
with st.sidebar:
    st.markdown('<h1 style="color:white; margin-bottom:0; font-size:26px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:11px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", key="gem", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", key="cla", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", key="gpt", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    st.markdown(f'<p style="font-size:11px; color:#8b949e; text-align:center;">Active: <span style="color:#58a6ff;">{st.session_state.model_choice}</span></p>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    st.divider()

    st.markdown('<p class="sidebar-header" style="margin-top:5px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:14px; margin:0;">● Core Engine: Online</p>
            <div class="status-node">
                <span>NODE: SG-AI-MASTER</span>
                <span>STABLE</span>
            </div>
            <p style="font-size:9px; color:#58a6ff; margin-top:5px;">SESSION ID: {hex(id(st.session_state))[:10]}</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (V32.0 DASHBOARD REPLICATION) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # Timeframe & Filter Row
    f_col1, f_col2 = st.columns([1, 1])
    with f_col1:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Timeframe</p>', unsafe_allow_html=True)
        st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], selection_mode="single", default="Monthly", label_visibility="collapsed")
    with f_col2:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Visual Filter</p>', unsafe_allow_html=True)
        st.selectbox("Filter", ["Bar Chart", "Line Chart", "Area Chart"], label_visibility="collapsed")
    
    st.write("") # Spacer

    # Section 1: Content Creation Status
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Content Creation Status</p>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Drafting", "12")
    m2.metric("Pending", "5")
    m3.metric("Scheduled", "18")
    m4.metric("Published", "145")
    
    st.write("") # Spacer

    # Section 2: Platform Metrics
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Platform Metrics</p>', unsafe_allow_html=True)
    platform_tabs = st.tabs(["Facebook", "TikTok", "YouTube"])
    
    with platform_tabs[0]: # Facebook Example as per V32.0
        p1, p2, p3 = st.columns(3)
        p1.metric("Reach", "45.2K")
        p2.metric("Engagement", "3.2K")
        p3.metric("Followers", "12.4K")
        
        # Dashboard Chart (V32.0 Blue Theme)
        chart_data = pd.DataFrame({
            'Category': ['Convert', 'Engage', 'Reach'],
            'Value': [25, 45, 32]
        })
        st.bar_chart(chart_data.set_index('Category'), color="#87CEEB", use_container_width=True)

# Placeholder for other menus to keep the code clean
else:
    st.markdown(f"<h1>{st.session_state.menu}</h1>", unsafe_allow_html=True)
    st.info(f"{st.session_state.menu} view is synchronized and ready for data population.")
