import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Preserved) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v66.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #010409; border-right: 1px solid #30363d; padding-top: 10px; }
    
    /* Section Headers */
    .section-title { 
        font-size: 14px; 
        font-weight: 700; 
        color: #58a6ff; 
        margin-top: 10px; 
        margin-bottom: 10px;
        letter-spacing: 1.5px;
        text-transform: uppercase;
    }
    
    /* System Status Style */
    .status-online {
        color: #238636;
        font-weight: 600;
        font-size: 13px;
    }
    
    .header-blue { color: #58a6ff; font-weight: 600; font-size: 24px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Clean Professional Structure) ---
with st.sidebar:
    # Branding
    st.markdown("<h2 style='color:#ffffff; margin-bottom:0;'>Sayar Gyi's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; font-size:14px; margin-top:0; letter-spacing:2px;'>COMMAND CENTER</p>", unsafe_allow_html=True)
    st.divider()

    # The Brain (AI Model Selection)
    st.markdown('<p class="section-title">The Brain</p>', unsafe_allow_html=True)
    model_cols = st.columns(3)
    if model_cols[0].button("Gemini", use_container_width=True): st.session_state.model_choice = "Gemini"
    if model_cols[1].button("GPT", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    if model_cols[2].button("Claude", use_container_width=True): st.session_state.model_choice = "Claude"
    st.info(f"Active Model: {st.session_state.model_choice}")
    st.divider()

    # Marketing Intelligence
    st.markdown('<p class="section-title">Marketing Intelligence</p>', unsafe_allow_html=True)
    if st.button("Enter Intelligence Hub", use_container_width=True):
        st.session_state.menu = "Market Intelligence Hub"
    st.divider()

    # Menu
    st.markdown('<p class="section-title">Menu</p>', unsafe_allow_html=True)
    menu_choice = st.radio("Navigation", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    # Sync radio with menu logic
    if st.session_state.menu not in ["Market Intelligence Hub", "Creator Mode"]:
        st.session_state.menu = menu_choice
    st.divider()

    # Creator Mode
    st.markdown('<p class="section-title">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"
    st.divider()

    # System Status
    st.markdown('<p class="section-title">System Status</p>', unsafe_allow_html=True)
    st.markdown('<p class="status-online">● Core Engine: Online</p>', unsafe_allow_html=True)
    st.divider()

# --- 4. MAIN INTERFACE (V64.0 Content Preservation) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    # Original Metrics & Charts
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Drafting", "12"); m_col2.metric("Pending", "5")
    m_col3.metric("Scheduled", "18"); m_col4.metric("Published", "145")
    st.bar_chart(pd.DataFrame({'Category': ['Convert', 'Engage', 'Reach'], 'Value': [25, 45, 32]}).set_index('Category'))

elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-blue">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)

elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 class="header-blue">Intelligence Hub</h1>', unsafe_allow_html=True)
    st.tabs(["Industry News", "Market Research", "Spy Mode"])

elif st.session_state.menu == "Creator Mode":
    st.markdown('<h1 class="header-blue">Creator Mode</h1>', unsafe_allow_html=True)
    st.info("AI Workspace Active.")

else:
    st.markdown(f'<h1 class="header-blue">{st.session_state.menu}</h1>', unsafe_allow_html=True)
