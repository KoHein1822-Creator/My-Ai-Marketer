import streamlit as st

# --- SIDE PANEL CONFIGURATION ---
def render_sidebar():
    # v72.0 Core Styling
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
        
        /* Sidebar Sizing & Background */
        section[data-testid="stSidebar"] { 
            background-color: #010409 !important; 
            min-width: 320px !important; 
            border-right: 1px solid #30363d; 
        }

        /* Section Headers */
        .sidebar-header {
            font-size: 13px; font-weight: 700; color: #58a6ff;
            margin-top: 25px; margin-bottom: 12px;
            letter-spacing: 1.5px; text-transform: uppercase;
        }

        /* The Brain Buttons Style */
        div.stButton > button {
            height: 48px !important; font-size: 15px !important; font-weight: 600 !important;
            border-radius: 8px !important; background-color: #161b22 !important;
            border: 1px solid #30363d !important; color: #ffffff !important;
        }
        div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

        /* Status Panel Logic */
        .status-panel { 
            background: #0d1117; border: 1px solid #30363d; 
            padding: 18px; border-radius: 10px; margin-top: 10px; 
        }
        .status-node-info { 
            font-size: 10px; color: #8b949e; margin-top: 8px; 
            border-top: 1px solid #21262d; padding-top: 8px; 
            display: flex; justify-content: space-between; 
        }
        </style>
        """, unsafe_allow_html=True)

    with st.sidebar:
        # 1. Branding
        st.markdown('<h1 style="color:white; margin-bottom:0; font-size:28px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:12px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
        st.divider()

        # 2. The Brain
        st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
        m_col1, m_col2 = st.columns(2)
        with m_col1:
            if st.button("Gemini 💎", key="gem_side", use_container_width=True): st.session_state.model_choice = "Gemini"
            if st.button("Claude 🧠", key="cla_side", use_container_width=True): st.session_state.model_choice = "Claude"
        with m_col2:
            if st.button("GPT 🤖", key="gpt_side", use_container_width=True): st.session_state.model_choice = "ChatGPT"
        
        # Choice Display
        current_model = st.session_state.get('model_choice', 'Gemini')
        st.markdown(f'<div style="background:rgba(88,166,255,0.1); border:1px solid rgba(88,166,255,0.3); padding:8px; border-radius:6px; text-align:center; margin-top:10px; font-size:12px; color:#58a6ff;">Active Core: <b>{current_model}</b></div>', unsafe_allow_html=True)
        st.divider()

        # 3. System Menu
        st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
        nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
        st.session_state.menu = nav_choice
        st.divider()

        # 4. Special Functions
        st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
        if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
        if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
        st.divider()

        # 5. System Status
        st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
        st.markdown(f"""
            <div class="status-panel">
                <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
                <div class="status-node-info"><span>NODE: SG-MASTER-01</span><span>UPTIME: 99.9%</span></div>
            </div>
        """, unsafe_allow_html=True)

# Calling Sidebar for Testing
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
render_sidebar()

# Test Placeholder for Main Content
st.write(f"Active Menu: {st.session_state.menu}")
