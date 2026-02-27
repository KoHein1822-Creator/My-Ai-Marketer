import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v67.0", layout="wide")

# Custom CSS for high-end professional look
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { 
        background-color: #010409; 
        border-right: 1px solid #30363d; 
    }
    
    /* Section Headers - More subtle and professional */
    .sidebar-header {
        font-size: 11px;
        font-weight: 700;
        color: #8b949e;
        margin-top: 25px;
        margin-bottom: 10px;
        letter-spacing: 1.2px;
        text-transform: uppercase;
    }

    /* Branding Style */
    .brand-title { color: #ffffff; font-weight: 700; font-size: 20px; margin-bottom: 0px; }
    .brand-sub { color: #58a6ff; font-size: 12px; font-weight: 600; letter-spacing: 1.5px; margin-top: -5px; margin-bottom: 20px; }

    /* Custom Button Look for Model Selection */
    div.stButton > button {
        width: 100%;
        background-color: #161b22;
        border: 1px solid #30363d;
        color: #c9d1d9;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        border-color: #58a6ff;
        color: #58a6ff;
    }
    
    /* Status Indicator */
    .status-text { color: #3fb950; font-size: 12px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Refined Structural Design) ---
with st.sidebar:
    # Branding Area
    st.markdown('<p class="brand-title">Sayar Gyi\'s</p>', unsafe_allow_html=True)
    st.markdown('<p class="brand-sub">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    # THE BRAIN - Model Selection with Clean Grid
    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        if st.button("Gemini"): st.session_state.model_choice = "Gemini"
    with m_col2:
        if st.button("GPT"): st.session_state.model_choice = "ChatGPT"
    with m_col3:
        if st.button("Claude"): st.session_state.model_choice = "Claude"
    
    # Active Model Display
    st.markdown(f"""
        <div style="background: #0d1117; border: 1px solid #30363d; padding: 5px 10px; border-radius: 4px; text-align: center;">
            <span style="color: #8b949e; font-size: 11px;">Active:</span> 
            <span style="color: #58a6ff; font-size: 11px; font-weight: 700;">{st.session_state.model_choice}</span>
        </div>
    """, unsafe_allow_html=True)
    st.divider()

    # MARKETING INTELLIGENCE - Single Focus Action
    st.markdown('<p class="sidebar-header">Intelligence</p>', unsafe_allow_html=True)
    if st.button("Open Intelligence Hub", use_container_width=True):
        st.session_state.menu = "Market Intelligence Hub"
    st.divider()

    # MENU - Standard Navigation
    st.markdown('<p class="sidebar-header">Menu</p>', unsafe_allow_html=True)
    nav_options = ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"]
    selected_nav = st.radio("Nav", nav_options, label_visibility="collapsed")
    
    # Logic to handle radio vs button menu state
    if st.session_state.menu not in ["Market Intelligence Hub", "Creator Mode"]:
        st.session_state.menu = selected_nav
    elif selected_nav != st.session_state.menu and st.session_state.menu in ["Market Intelligence Hub", "Creator Mode"]:
        # If user clicks radio while in Hub/Creator, switch back to radio selection
        st.session_state.menu = selected_nav

    st.divider()

    # CREATOR MODE - Special Action
    st.markdown('<p class="sidebar-header">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"
    st.divider()

    # SYSTEM STATUS - Minimalist
    st.markdown('<p class="sidebar-header">System Status</p>', unsafe_allow_html=True)
    st.markdown('<span class="status-text">● Core Engine: Online</span>', unsafe_allow_html=True)
    st.divider()

# --- 4. MAIN INTERFACE (Maintaining V32.0 DNA from Screenshots) ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="color: #58a6ff;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    # Re-mimicking the visual from Dashboard Screenshot
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Drafting", "12")
    c2.metric("Pending", "5")
    c3.metric("Scheduled", "18")
    c4.metric("Published", "145")
    st.bar_chart(pd.DataFrame({'Value': [25, 45, 32]}, index=['Convert', 'Engage', 'Reach']), color="#58a6ff")

elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 style="color: #58a6ff;">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)

elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 style="color: #58a6ff;">Intelligence Hub</h1>', unsafe_allow_html=True)
    st.tabs(["Industry News", "Market Research", "Spy Mode"])

elif st.session_state.menu == "Creator Mode":
    st.markdown('<h1 style="color: #58a6ff;">Creator Mode</h1>', unsafe_allow_html=True)
    st.info("AI Creative Engine is ready.")

else:
    st.markdown(f'<h1 style="color: #58a6ff;">{st.session_state.menu}</h1>', unsafe_allow_html=True)
