import streamlit as st

# --- PAGE SETTINGS ---
st.set_page_config(page_title="AI Marketer Pro", layout="wide", page_icon="📈")

# --- PROFESSIONAL CSS (No more st.overline errors) ---
st.markdown("""
    <style>
    .stApp { background-color: #0f172a; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #1e293b !important; border-right: 1px solid #334155; }
    
    /* Professional Subheader Style */
    .section-label {
        font-size: 0.75rem;
        font-weight: 700;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 5px;
        margin-top: 15px;
    }

    .main-header {
        font-size: 2.2rem;
        font-weight: 800;
        background: -webkit-linear-gradient(#e2e8f0, #94a3b8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .pro-card {
        background: #1e293b;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #334155;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }

    .stButton > button {
        width: 100%;
        background-color: #6366f1 !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 0.6rem !important;
        font-weight: 600 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#6366f1;'>Pro</span></h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    # st.overline အစား Custom HTML သုံးထားပါတယ်
    st.markdown('<p class="section-label">CURRENT PROJECT</p>', unsafe_allow_html=True)
    project = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X"], label_visibility="collapsed")
    
    st.markdown('<p class="section-label">SUBSCRIPTION</p>', unsafe_allow_html=True)
    st.markdown("""
        <div style='background: #334155; padding: 10px; border-radius: 8px; border: 1px solid #475569;'>
            <p style='margin:0; font-weight: bold; color: #818cf8;'>Elite Agency (Active)</p>
        </div>
    """, unsafe_allow_html=True)

# --- MAIN DASHBOARD ---
st.markdown('<p class="main-header">Command Center</p>', unsafe_allow_html=True)
st.markdown(f"<p style='color: #94a3b8;'>Strategic Intelligence for <b>{project}</b></p>", unsafe_allow_html=True)

col_config, col_results = st.columns([1, 1.8], gap="large")

with col_config:
    st.markdown('<div class="pro-card">', unsafe_allow_html=True)
    st.subheader("Campaign Config")
    
    # Engine Mode ကို Radio Button အနေနဲ့ ပိုရှင်းအောင် ထားပါတယ်
    engine_mode = st.radio("System Engine Mode", ["Smart Mode", "Architect Mode"], horizontal=True)
    
    topic = st.text_input("Marketing Topic", placeholder="Enter core subject...")
    
    if engine_mode == "Smart Mode":
        goal = st.selectbox("Objective", ["Conversion", "Engagement", "Awareness"])
    else:
        framework = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB"], default="AIDA")
        creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)

    if st.button("EXECUTE STRATEGY"):
        st.session_state['processed'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_results:
    if st.session_state.get('processed'):
        st.markdown('<div class="pro-card">', unsafe_allow_html=True)
        st.subheader("Strategy Matrix")
        tabs = st.tabs(["Copywriting", "Video Scripts", "Visual Prompts"])
        
        with tabs[0]:
            st.text_area("Master Copy (AI Generated)", "Result will appear here...", height=200)
        with tabs[1]:
            st.text_area("Video Narrative", "Script details...", height=200)
        with tabs[2]:
            st.code("/imagine prompt: high-end commercial photography...")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("အချက်အလက်များဖြည့်သွင်းပြီး Execute ကိုနှိပ်ပါ။ AI မှ သင့်အတွက် Strategy များကို တွက်ချက်ပေးပါမည်။")
