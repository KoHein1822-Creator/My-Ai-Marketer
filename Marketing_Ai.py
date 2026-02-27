import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (v64.0 Base preserved) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'brand_mode' not in st.session_state: st.session_state.brand_mode = "Intelligence Mode (AI Research)"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v65.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #010409; border-right: 1px solid #30363d; padding-top: 10px; }
    
    /* Highlighted Section Titles */
    .section-header { 
        font-size: 16px; 
        font-weight: 800; 
        color: #58a6ff; 
        margin-top: 15px; 
        margin-bottom: 10px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }
    .header-blue { color: #58a6ff; font-weight: 600; font-size: 24px; margin-bottom: 20px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 6px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Revised Structure) ---
with st.sidebar:
    # Title Section
    st.markdown("<h2 style='color:#58a6ff; margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; font-size:12px; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider() # မျဉ်းခွဲခြင်း

    # Marketing Intelligence Section
    st.markdown('<p class="section-header">🔍 Marketing Intelligence</p>', unsafe_allow_html=True)
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): 
        st.session_state.menu = "Market Intelligence Hub"
    st.divider()

    # Menu Section
    st.markdown('<p class="section-header">📋 Menu</p>', unsafe_allow_html=True)
    menu_options = ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"]
    # Radio buttons with default based on session state
    st.session_state.menu = st.radio("Navigation", menu_options, label_visibility="collapsed")
    st.divider()

    # My Agent Section
    st.markdown('<p class="section-header">👥 My Agents</p>', unsafe_allow_html=True)
    st.markdown("""
    - 🧘 **Agent 1:** Intel Researcher
    - 🎨 **Agent 2:** Creative Director
    - ⚖️ **Agent 3:** Performance Auditor
    """)
    st.divider()

    # Creator Mode Section
    st.markdown('<p class="section-header">🎬 Creator Mode</p>', unsafe_allow_html=True)
    if st.button("🔥 Switch to Creator Mode", use_container_width=True): 
        st.session_state.menu = "Creator Mode"
    st.divider()

    # System Status Section
    st.markdown('<p class="section-header">⚙️ System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")
    st.divider()

    # The Brain Section
    st.markdown('<p class="section-header">🧠 The Brain (AI Model)</p>', unsafe_allow_html=True)
    st.session_state.model_choice = st.selectbox("Choice Mode", ["Gemini", "ChatGPT", "Claude"], label_visibility="collapsed")
    st.divider()

# --- 4. MAIN INTERFACE (V64.0 Base Contents - NO CHANGES) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard 🔗</h1>', unsafe_allow_html=True)
    # ... (Metrics and charts from v64.0)
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Drafting", "12"); m_col2.metric("Pending", "5")
    m_col3.metric("Scheduled", "18"); m_col4.metric("Published", "145")
    st.bar_chart(pd.DataFrame({'Category': ['Convert', 'Engage', 'Reach'], 'Value': [25, 45, 32]}).set_index('Category'))

elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-blue">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    # ... (V64.0 logic preserved)
    st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)

elif st.session_state.menu == "Project Archive":
    st.markdown('<h1 class="header-blue">Project Archive Database</h1>', unsafe_allow_html=True)
    st.table(pd.DataFrame({"Client Name": ["Diamond Star"], "Status": ["Completed"], "Budget": ["$2,500"]}))

elif st.session_state.menu == "Asset Library":
    st.markdown('
