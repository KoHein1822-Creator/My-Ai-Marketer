import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v70.0", layout="wide")

# THE LUXURY UI ENGINE (Custom CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Background & Global Font */
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* Sidebar Overhaul */
    section[data-testid="stSidebar"] { 
        background-color: #010409 !important; 
        border-right: 1px solid #30363d; 
        min-width: 320px !important;
    }

    /* Professional Branding */
    .brand-box { padding: 20px 0; text-align: left; }
    .brand-main { font-size: 26px; font-weight: 700; color: #ffffff; margin-bottom: 0; }
    .brand-sub { font-size: 13px; font-weight: 600; color: #58a6ff; letter-spacing: 3px; margin-top: -5px; }

    /* Custom Header Styles */
    .nav-header {
        font-size: 12px;
        font-weight: 700;
        color: #58a6ff;
        margin-top: 35px;
        margin-bottom: 15px;
        letter-spacing: 2px;
        text-transform: uppercase;
        border-bottom: 1px solid #30363d;
        padding-bottom: 5px;
    }

    /* Luxury Navigation Buttons (Replacing Radio) */
    .stButton > button {
        width: 100% !important;
        background-color: transparent !important;
        border: 1px solid #30363d !important;
        color: #8b949e !important;
        text-align: left !important;
        padding: 10px 15px !important;
        font-size: 14px !important;
        font-weight: 500 !important;
        border-radius: 6px !important;
        margin-bottom: 8px !important;
        transition: 0.2s !important;
    }
    .stButton > button:hover {
        border-color: #58a6ff !important;
        color: #58a6ff !important;
        background: rgba(88, 166, 255, 0.05) !important;
    }
    
    /* Active State for Navigation */
    .active-nav button {
        border-color: #58a6ff !important;
        color: #ffffff !important;
        background: #161b22 !important;
        border-left: 4px solid #58a6ff !important;
    }

    /* Model Selection Grid */
    .model-grid { display: flex; gap: 8px; margin-bottom: 10px; }
    
    /* Status Section at the absolute bottom */
    .fixed-bottom {
        position: fixed;
        bottom: 20px;
        width: 280px;
        padding: 15px;
        background: #0d1117;
        border: 1px solid #30363d;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Luxury Reconstruction) ---
with st.sidebar:
    # Branding
    st.markdown('<div class="brand-box"><p class="brand-main">Sayar Gyi\'s</p><p class="brand-sub">COMMAND CENTER</p></div>', unsafe_allow_html=True)

    # --- THE BRAIN (3-Column Symmetrical Grid) ---
    st.markdown('<p class="nav-header">The Brain</p>', unsafe_allow_html=True)
    b_col1, b_col2, b_col3 = st.columns(3)
    with b_col1: 
        if st.button("Gemini", key="gem"): st.session_state.model_choice = "Gemini"
    with b_col2: 
        if st.button("GPT", key="gpt"): st.session_state.model_choice = "ChatGPT"
    with b_col3: 
        if st.button("Claude", key="cla"): st.session_state.model_choice = "Claude"
    
    st.markdown(f'<p style="font-size:12px; color:#8b949e; margin-top:5px; text-align:center;">Active Core: <span style="color:#58a6ff; font-weight:600;">{st.session_state.model_choice}</span></p>', unsafe_allow_html=True)

    # --- INTELLIGENCE ---
    st.markdown('<p class="nav-header">Intelligence</p>', unsafe_allow_html=True)
    if st.button("Market Intelligence Hub", key="intel_hub"):
        st.session_state.menu = "Intelligence Hub"

    # --- SYSTEM MENU (Replaced Radio with High-End Buttons) ---
    st.markdown('<p class="nav-header">System Menu</p>', unsafe_allow_html=True)
    
    # Custom Button Logic for Menu
    menus = ["Dashboard", "Brand DNA", "Project Archive", "Asset Library"]
    for m in menus:
        # Highlight active menu
        if st.session_state.menu == m:
            st.markdown(f'<div class="active-nav">', unsafe_allow_html=True)
            if st.button(m, key=f"btn_{m}"): st.session_state.menu = m
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            if st.button(m, key=f"btn_{m}"): st.session_state.menu = m

    # --- EXECUTION ---
    st.markdown('<p class="nav-header">Execution</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode", key="creator"):
        st.session_state.menu = "Creator Mode"

    # --- SYSTEM STATUS (Bottom Aligned & Readable) ---
    st.markdown('<div style="height: 100px;"></div>', unsafe_allow_html=True) # Spacer
    st.markdown("""
        <div style="border-top: 1px solid #30363d; padding-top: 20px;">
            <p style="font-size:12px; color:#8b949e; margin-bottom:8px; font-weight:600; letter-spacing:1px;">SYSTEM STATUS</p>
            <p style="color:#3fb950; font-size:15px; font-weight:700; margin:0;">● Core Engine: Online</p>
            <p style="color:#58a6ff; font-size:11px; margin-top:4px;">Secure Connection: Active</p>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE ---
if st.session_state.menu == "Dashboard":
    st.markdown('<h1 style="font-size: 32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    # Preservation of the content from V32.0 Screenshot
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12"); c2.metric("Pending", "5")
    c3.metric("Scheduled", "18"); c4.metric("Published", "145")
    st.bar_chart(pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach']), color="#58a6ff")

elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 style="font-size: 32px;">🧬 Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)

else:
    st.markdown(f'<h1>{st.session_state.menu}</h1>', unsafe_allow_html=True)
