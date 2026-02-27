import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v68.0", layout="wide")

# ADVANCED CUSTOM CSS FOR PROFESSIONAL FINISH
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    
    /* Overall Background */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* Sidebar Overhaul */
    section[data-testid="stSidebar"] { background-color: #010409 !important; border-right: 1px solid #30363d; min-width: 280px !important; }
    
    /* Refined Section Headers */
    .sidebar-label {
        font-size: 10px;
        font-weight: 700;
        color: #58a6ff;
        margin-top: 20px;
        margin-bottom: 8px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        opacity: 0.8;
    }

    /* Model Selection Buttons Fix */
    div.stButton > button {
        width: 100%;
        border-radius: 4px;
        height: 35px;
        font-size: 12px !important;
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #c9d1d9;
        margin-bottom: 0px;
    }
    div.stButton > button:hover { border-color: #58a6ff; color: #58a6ff; }
    div.stButton > button:active { background-color: #58a6ff; color: white; }

    /* Active Model Indicator Box */
    .active-box {
        background: rgba(88, 166, 255, 0.1);
        border: 1px solid #58a6ff;
        padding: 4px;
        border-radius: 4px;
        text-align: center;
        margin-top: 10px;
    }

    /* Dashboard Metric Styling */
    div[data-testid="stMetric"] {
        background-color: #161b22;
        border: 1px solid #30363d;
        padding: 15px !important;
        border-radius: 8px;
    }
    
    /* Remove unnecessary padding */
    .block-container { padding-top: 2rem !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (The Command Center) ---
with st.sidebar:
    # Branding
    st.markdown('<p style="font-size: 20px; font-weight: 700; color: white; margin-bottom:0;">Sayar Gyi\'s</p>', unsafe_allow_html=True)
    st.markdown('<p style="font-size: 12px; font-weight: 600; color: #58a6ff; letter-spacing: 2px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    # THE BRAIN
    st.markdown('<p class="sidebar-label">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        if st.button("Gemini"): st.session_state.model_choice = "Gemini"
    with m_col2:
        if st.button("GPT"): st.session_state.model_choice = "ChatGPT"
    with m_col3:
        if st.button("Claude"): st.session_state.model_choice = "Claude"
    
    st.markdown(f'<div class="active-box"><span style="color:#58a6ff; font-size:11px; font-weight:700;">Active: {st.session_state.model_choice}</span></div>', unsafe_allow_html=True)
    st.divider()

    # INTELLIGENCE
    st.markdown('<p class="sidebar-label">Intelligence</p>', unsafe_allow_html=True)
    if st.button("Open Intelligence Hub", use_container_width=True):
        st.session_state.menu = "Market Intelligence Hub"
    st.divider()

    # MENU
    st.markdown('<p class="sidebar-label">Menu</p>', unsafe_allow_html=True)
    nav_selected = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    # Logic to handle radio vs button override
    if st.session_state.menu not in ["Market Intelligence Hub", "Creator Mode"]:
        st.session_state.menu = nav_selected
    st.divider()

    # CREATOR MODE
    st.markdown('<p class="sidebar-label">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"
    st.divider()

    # SYSTEM STATUS
    st.markdown('<p class="sidebar-label">System Status</p>', unsafe_allow_html=True)
    st.markdown('<p style="color:#3fb950; font-size:12px; font-weight:600; margin:0;">● Core Engine: Online</p>', unsafe_allow_html=True)
    st.divider()

# --- 4. MAIN INTERFACE (Aligned with Screenshot 35) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="color: #58a6ff; font-size: 28px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # CONTENT CREATION STATUS (From Screenshot)
    st.markdown('<p style="font-size:11px; color:#8b949e; font-weight:700; letter-spacing:1px; text-transform:uppercase;">Content Creation Status</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12")
    c2.metric("Pending", "5")
    c3.metric("Scheduled", "18")
    c4.metric("Published", "145")
    
    st.write("") # Spacing
    
    # PLATFORM METRICS (From Screenshot)
    st.markdown('<p style="font-size:11px; color:#8b949e; font-weight:700; letter-spacing:1px; text-transform:uppercase;">Platform Metrics</p>', unsafe_allow_html=True)
    st.bar_chart(pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach']), color="#58a6ff")

elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 style="color: #58a6ff;">Intelligence Hub</h1>', unsafe_allow_html=True)
    st.tabs(["Industry News", "Market Research", "Spy Mode"])

else:
    st.markdown(f'<h1 style="color: #58a6ff;">{st.session_state.menu}</h1>', unsafe_allow_html=True)
    st.write("Section under management.")
