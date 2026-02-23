import streamlit as st

# --- PAGE SETTINGS ---
st.set_page_config(page_title="AI Marketer Pro", layout="wide", page_icon="📈")

# --- PROFESSIONAL CSS INJECTION ---
st.markdown("""
    <style>
    /* Main Layout Background */
    .stApp {
        background-color: #0f172a; /* Deep Slate Blue */
        color: #f8fafc;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }

    /* Header Styling */
    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#e2e8f0, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }

    /* Professional Card Component */
    .pro-card {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }

    /* Button Styling */
    .stButton > button {
        width: 100%;
        background-color: #6366f1 !important; /* Indigo */
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.6rem !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: #4f46e5 !important;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.4);
    }

    /* Tab Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        color: #94a3b8 !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: #6366f1;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ASSET MANAGEMENT ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#6366f1;'>Pro</span></h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.overline("CURRENT PROJECT")
    project = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X"], label_visibility="collapsed")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.overline("SUBSCRIPTION")
    st.markdown("""
        <div style='background: #334155; padding: 10px; border-radius: 8px; border: 1px solid #475569;'>
            <p style='margin:0; font-size: 0.8rem; color: #94a3b8;'>Current Plan</p>
            <p style='margin:0; font-weight: bold; color: #818cf8;'>Elite Agency (Active)</p>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
st.markdown('<p class="main-header">Command Center</p>', unsafe_allow_html=True)
st.markdown(f"<p style='color: #94a3b8;'>Strategic Intelligence for <b>{project}</b></p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- LAYOUT: CONFIGURATION & OUTPUT ---
col_config, col_results = st.columns([1, 1.8], gap="large")

with col_config:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.subheader("Campaign Config")
    
    engine_mode = st.segmented_control(
        "System Engine", 
        ["Smart Mode", "Architect Mode"], 
        default="Smart Mode"
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
    topic = st.text_input("Marketing Topic", placeholder="Enter core subject...")
    
    if engine_mode == "Smart Mode":
        st.caption("AI will auto-select the best frameworks for your niche.")
        goal = st.selectbox("Objective", ["Conversion", "Engagement", "Brand Awareness"])
    else:
        st.caption("Manual expert overrides enabled.")
        framework = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB", "4Ps"], default="AIDA")
        creativity = st.slider("Creativity Depth", 0.0, 1.0, 0.7)

    if st.button("EXECUTE STRATEGY"):
        st.session_state['processed'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_results:
    if st.session_state.get('processed'):
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        st.subheader("Strategy Matrix")
        
        tab_copy, tab_script, tab_visual = st.tabs(["Copywriting", "Video Scripts", "Visual Prompts"])
        
        with tab_copy:
            st.markdown("#### Direct Response Variations")
            st.text_area("Master Copy (AIDA)", "System is generating high-converting copy...", height=200)
            st.button("Refine Copy", key="refine_1")
            
        with tab_script:
            st.markdown("#### Short-Form Narrative")
            st.text_area("Reels/TikTok Script", "Hook: ... \nBody: ...", height=200)
            
        with tab_visual:
            st.markdown("#### AI Art Direction")
            st.code("/imagine prompt: high-end commercial photography, minimalist, 8k --ar 16:9")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("Configuration အားဖြည့်စွက်ပြီး Execute ကိုနှိပ်ပါ။ AI မှ သင့်အတွက် Marketing Ecosystem တစ်ခုလုံးကို တည်ဆောက်ပေးပါမည်။")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-size: 0.8rem;'>© 2026 AI Marketer Pro. Optimized for Strategic Growth.</p>", unsafe_allow_html=True)
