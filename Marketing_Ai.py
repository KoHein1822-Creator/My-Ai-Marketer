import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Stable Core) ---
if 'menu' not in st.session_state: st.session_state.menu = "Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v71.0", layout="wide")

# CLEAN & POWERFUL CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; }
    
    /* Sidebar Scaling */
    section[data-testid="stSidebar"] { 
        background-color: #010409 !important; 
        min-width: 320px !important; 
    }

    /* Section Headers */
    .sidebar-header {
        font-size: 13px; font-weight: 700; color: #58a6ff;
        margin-top: 25px; margin-bottom: 10px;
        letter-spacing: 1.5px; text-transform: uppercase;
    }

    /* Big & Bold Model Buttons */
    div.stButton > button {
        height: 50px !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        border-radius: 8px !important;
        background-color: #161b22 !important;
        border: 1px solid #30363d !important;
        color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Dashboard Metric Styling (Ensuring visibility) */
    div[data-testid="stMetric"] {
        background: #161b22;
        border: 1px solid #30363d;
        padding: 20px !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Symmetrical & Spaced) ---
with st.sidebar:
    # Branding
    st.markdown('<h1 style="color:white; margin-bottom:0;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:2px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    # THE BRAIN (Big, easy-to-click buttons)
    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    
    st.info(f"Active Core: {st.session_state.model_choice}")
    st.divider()

    # NAVIGATION
    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Select View", ["Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    # INTELLIGENCE & EXECUTION
    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    
    # SYSTEM STATUS (Solid & Grounded)
    st.markdown('<div style="margin-top: 50px; padding: 15px; background: #0d1117; border: 1px solid #30363d; border-radius: 8px;">', unsafe_allow_html=True)
    st.markdown('<p style="color:#3fb950; font-weight:bold; margin-bottom:0;">● Core Engine: Online</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#8b949e; font-size:11px;">Latency: 12ms | Stable</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (Restoring Full V32.0 Content) ---

if st.session_state.menu == "Dashboard":
    st.markdown('<h1 style="color:#58a6ff;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # Restoring Metrics (From screenshot 32.0)
    st.markdown("### Content Creation Status")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12")
    c2.metric("Pending", "5")
    c3.metric("Scheduled", "18")
    c4.metric("Published", "145")
    
    st.divider()
    
    # Restoring Performance Chart
    st.markdown("### Platform Metrics")
    chart_data = pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach'])
    st.bar_chart(chart_data, color="#58a6ff")

elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 style="color:#58a6ff;">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)

elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 style="color:#58a6ff;">Asset Library</h1>', unsafe_allow_html=True)
    st.tabs(["Media", "Copywriting", "Legal"])

else:
    st.markdown(f'<h1 style="color:#58a6ff;">{st.session_state.menu}</h1>', unsafe_allow_html=True)
    st.info("System is ready for your command.")
