import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Marketer Pro | Workspace", layout="wide", page_icon="💎")

# --- ULTIMATE SAAS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    section[data-testid="stSidebar"] { background-color: #111827 !important; border-right: 1px solid #1f2937; }
    .workspace-card {
        background: #111827; padding: 25px; border-radius: 12px;
        border: 1px solid #1f2937; margin-bottom: 20px;
    }
    .matrix-box {
        background: #1f2937; padding: 20px; border-radius: 8px;
        border-top: 4px solid #6366f1; margin-bottom: 20px;
    }
    .main-title { font-size: 32px; font-weight: 800; color: #ffffff; }
    .section-tag { font-size: 12px; font-weight: 700; color: #818cf8; text-transform: uppercase; letter-spacing: 1.2px; margin-bottom: 10px; }
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        border: none !important; color: white !important; font-weight: 700 !important;
        width: 100%; border-radius: 8px !important; height: 50px; text-transform: uppercase;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BRAND VAULT ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#6366f1;'>Pro</span></h2>", unsafe_allow_html=True)
    st.caption("Strategic Intelligence Suite v2.5")
    st.divider()
    
    st.markdown('<p class="section-tag">Workspace Settings</p>', unsafe_allow_html=True)
    brand = st.selectbox("Current Project", ["Jewelry Client A", "Tech Startup X"], label_visibility="collapsed")
    
    with st.expander("🧬 Brand DNA Insights", expanded=True):
        st.write("**Niche:** Luxury Jewelry")
        st.write("**Tone:** Elegant, Trustworthy")
        st.button("Update Brand DNA", use_container_width=True)

    st.markdown("---")
    st.markdown('<p class="section-tag">Status</p>', unsafe_allow_html=True)
    st.info("Elite Plan: 45 Days Remaining")

# --- MAIN DASHBOARD ---
st.markdown('<p class="main-title">Campaign Command Center</p>', unsafe_allow_html=True)
st.caption(f"Deploying Marketing Intelligence for **{brand}**")

col_input, col_matrix = st.columns([1, 2], gap="large")

with col_input:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-tag">Configuration</p>', unsafe_allow_html=True)
    
    mode = st.radio("System Engine Mode", ["Smart Mode", "Architect Mode"], horizontal=True)
    
    topic = st.text_input("Marketing Topic", placeholder="e.g. New Spring Collection Launch")
    
    if mode == "Smart Mode":
        st.info("⚡ AI will auto-select multi-angle strategies based on Brand DNA.")
        objective = st.selectbox("Campaign Objective", ["Sales Conversion", "Brand Awareness", "Direct Engagement"])
    else:
        st.warning("🛠️ Manual Expert Mode Enabled.")
        frameworks = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB", "4Ps"], default=["AIDA", "PAS"])
        st.slider("Creativity Depth (Temp)", 0.0, 1.0, 0.7)
    
    if st.button("EXECUTE STRATEGY MATRIX"):
        st.session_state['run'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_matrix:
    if st.session_state.get('run'):
        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-tag">Generated Strategic Content Matrix</p>', unsafe_allow_html=True)
        
        tab_copy, tab_prod, tab_analytics = st.tabs(["📄 AD COPY DECK", "🎬 PRODUCTION", "📊 ANALYTICS"])
        
        with tab_copy:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="matrix-box">', unsafe_allow_html=True)
                st.write("**[AIDA] Sales Angle**")
                st.caption("Focus on Desire and Urgency.")
                st.text_area("AIDA Output", "AI is writing your high-converting copy...", height=180, key="aida")
                st.markdown('</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="matrix-box">', unsafe_allow_html=True)
                st.write("**[PAS] Problem Angle**")
                st.caption("Deep emotional resonance with pain points.")
                st.text_area("PAS Output", "AI is highlighting the problem and solution...", height=180, key="pas")
                st.markdown('</div>', unsafe_allow_html=True)
            st.button("🔄 Regenerate All Angles", use_container_width=False)
                
        with tab_prod:
            st.write("### Content Production Brief")
            st.text_area("Video Script (Reels/TikTok)", "Hook: [0-3s]\nValue: [4-15s]\nCTA: [16-20s]", height=150)
            st.code("/imagine prompt: Macro shot of diamond necklace, minimalist background, luxury lighting, 8k --ar 9:16")
            
        with tab_analytics:
            st.write("### Targeted Metadata")
            st.write("`#LuxuryLife` `#JewelryAddict` `#Elegance` `#BrandLaunch`")
            st.button("Export to Ads Manager")
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Placeholder for Professional Feel
        st.markdown('<div style="border: 2px dashed #1f2937; padding: 80px; text-align: center; border-radius: 12px; margin-top:10px;">', unsafe_allow_html=True)
        st.markdown('<p style="color: #4b5563; font-size: 16px;">Configuration အား ဖြည့်စွက်ပြီး Execute ကိုနှိပ်ပါ။ <br> သင့်အတွက် Campaign Ecosystem တစ်ခုလုံးကို AI မှ တွက်ချက်ပေးပါမည်။</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
