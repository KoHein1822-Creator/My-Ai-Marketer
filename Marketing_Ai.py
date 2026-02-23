import streamlit as st
import google.generativeai as genai

# --- 1. SETTINGS & AI CONNECTION ---
st.set_page_config(page_title="AI Marketer Pro v4.0", layout="wide", page_icon="💎")

# Secrets ထဲက Key ကို လှမ်းဖတ်ခြင်း
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.warning("⚠️ Please configure GEMINI_API_KEY in Streamlit Secrets.")

# --- 2. CSS FOR HIGH-END UI ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .workspace-card {
        background: #161b22; padding: 25px; border-radius: 12px;
        border: 1px solid #30363d; margin-bottom: 20px;
    }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; }
    .main-header { font-size: 32px; font-weight: 800; color: #ffffff; }
    .stButton>button {
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important;
        border: none !important; color: white !important; font-weight: 700 !important;
        width: 100%; border-radius: 8px !important; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: BRAND VAULT ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="section-label">Brand Identity</p>', unsafe_allow_html=True)
    brand = st.selectbox("Current Project", ["Jewelry Client A", "Tech Startup X"], label_visibility="collapsed")
    
    with st.expander("🧬 Brand DNA Insights", expanded=True):
        st.write("**Niche:** Luxury")
        st.write("**Tone:** Professional & Elegant")
    
    st.markdown("---")
    st.markdown("<p style='color:#3fb950;'>● Elite Access Active</p>", unsafe_allow_html=True)

# --- 4. COMMAND CENTER ---
st.markdown('<p class="main-header">Strategic Command Center</p>', unsafe_allow_html=True)
st.caption(f"Executing Market Intelligence for **{brand}**")

col_config, col_output = st.columns([1, 2], gap="large")

with col_config:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Setup</p>', unsafe_allow_html=True)
    
    topic = st.text_input("Marketing Topic", placeholder="e.g. 18k White Gold Necklace")
    goal = st.selectbox("Objective", ["High Conversion", "Brand Awareness", "Viral Engagement"])
    
    if st.button("GENERATE STRATEGY MATRIX"):
        if topic:
            st.session_state['run'] = True
        else:
            st.error("Please enter a topic first.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_output:
    if st.session_state.get('run'):
        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Strategic Result Matrix</p>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📄 Content Deck", "🎬 Media Brief", "🎨 Visual Prompts"])
        
        with tab1:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**[AIDA] Sales Angle**")
                st.text_area("Output", "AI Generating AIDA...", height=200)
            with c2:
                st.markdown("**[PAS] Problem Angle**")
                st.text_area("Output", "AI Generating PAS...", height=200)
        
        with tab2:
            st.markdown("**Video Script Narrative**")
            st.text_area("Script", "Hook: ... \nBody: ...", height=150)
            
        with tab3:
            st.markdown("**AI Visual Direction**")
            st.code("/imagine prompt: high-end jewelry, macro shot, 8k")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="border: 2px dashed #30363d; padding: 100px; text-align: center; border-radius: 12px; background: #161b22;">', unsafe_allow_html=True)
        st.write("Configuration အားဖြည့်စွက်ပြီး Execute ကိုနှိပ်ပါ။")
        st.markdown('</div>', unsafe_allow_html=True)
