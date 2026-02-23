import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Marketer Pro | Workspace", layout="wide", page_icon="💎")

# --- HIGH-END SAAS CSS ---
st.markdown("""
    <style>
    /* Global Background */
    .stApp { background-color: #0b0f19; color: #e2e8f0; }
    
    /* Sidebar */
    section[data-testid="stSidebar"] { background-color: #111827 !important; border-right: 1px solid #1f2937; }
    
    /* Workspace Card Style */
    .workspace-card {
        background: #111827;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #1f2937;
        margin-bottom: 20px;
    }
    
    /* Typography */
    .main-title { font-size: 28px; font-weight: 800; color: #ffffff; letter-spacing: -0.5px; }
    .section-tag { font-size: 11px; font-weight: 700; color: #6366f1; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 8px; }
    
    /* Custom Matrix Box */
    .matrix-box {
        background: #1f2937;
        padding: 15px;
        border-radius: 8px;
        border-left: 4px solid #6366f1;
        margin-bottom: 15px;
    }
    
    /* Input & Buttons */
    .stButton>button {
        background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%) !important;
        border: none !important; color: white !important; font-weight: 600 !important;
        width: 100%; border-radius: 8px !important; height: 45px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: BRAND ASSETS ---
with st.sidebar:
    st.markdown("<h2 style='color:white; margin-bottom:0;'>AI Marketer <span style='color:#6366f1;'>Pro</span></h2>", unsafe_allow_html=True)
    st.caption("Strategic Intelligence Suite v2.5")
    st.markdown("---")
    
    st.markdown('<p class="section-tag">Workspace</p>', unsafe_allow_html=True)
    brand = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X"], label_visibility="collapsed")
    
    with st.expander("🧬 Brand DNA Insights", expanded=False):
        st.write("**Tone:** Luxury & Elegant")
        st.write("**Audience:** Women (25-45)")
        st.write("**Keywords:** Heritage, Glow, Forever")
        st.button("Edit DNA")

    st.markdown("---")
    st.markdown('<p class="section-tag">Plan Status</p>', unsafe_allow_html=True)
    st.info("Elite Agency - 45 Days Left")

# --- MAIN WORKSPACE ---
col_head, col_action = st.columns([2, 1])
with col_head:
    st.markdown('<p class="main-title">Campaign Command Center</p>', unsafe_allow_html=True)
    st.caption(f"Strategy Deployment for **{brand}**")

# --- LAYOUT: INPUT vs ANALYSIS ---
col_input, col_matrix = st.columns([1, 1.8], gap="medium")

with col_input:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-tag">Configuration</p>', unsafe_allow_html=True)
    
    mode = st.radio("System Engine Mode", ["Smart Mode", "Architect Mode"], horizontal=True)
    
    topic = st.text_input("Marketing Topic", placeholder="Enter core subject (e.g. New Necklace Collection)")
    
    if mode == "Smart Mode":
        st.caption("AI will auto-generate multi-angle strategies.")
        goal = st.selectbox("Objective", ["Sales Conversion", "Brand Awareness", "Educational Awareness"])
    else:
        st.caption("Manual framework & role injection.")
        frameworks = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB", "4Ps"], default=["AIDA", "PAS"])
        st.slider("Creativity Depth", 0.0, 1.0, 0.7)
    
    if st.button("EXECUTE STRATEGY MATRIX"):
        st.session_state['run'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_matrix:
    if st.session_state.get('run'):
        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-tag">Generated Strategy Matrix</p>', unsafe_allow_html=True)
        
        tab_copy, tab_visual, tab_meta = st.tabs(["📄 Ad Copy Deck", "🎬 Production Scripts", "📈 Campaign Metadata"])
        
        with tab_copy:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown('<div class="matrix-box">', unsafe_allow_html=True)
                st.write("**Angle A: AIDA (Sales Focus)**")
                st.caption("Attention-grabbing copy for high conversion.")
                st.text_area("Copy Output", "AI is writing your AIDA copy...", height=150, key="aida_out")
                st.markdown('</div>', unsafe_allow_html=True)
            with c2:
                st.markdown('<div class="matrix-box">', unsafe_allow_html=True)
                st.write("**Angle B: PAS (Problem/Solution)**")
                st.caption("Deep emotional resonance with customer pain points.")
                st.text_area("Copy Output", "AI is writing your PAS copy...", height=150, key="pas_out")
                st.markdown('</div>', unsafe_allow_html=True)
                
        with tab_visual:
            st.write("### Content Production Brief")
            st.info("Visual Direction: Minimalist luxury, high-contrast lighting.")
            st.text_area("Video Script (Reels/TikTok)", "Hook: [0-3s]\nValue: [4-15s]\nCTA: [16-20s]", height=150)
            st.code("/imagine prompt: Macro shot of diamond necklace, bokeh background, 8k resolution --ar 4:5")

        with tab_meta:
            st.write("### SEO & Target Tags")
            st.write("`#LuxuryJewelry` `#GoldCollection` `#Elegance` `#BrandStory`")
            st.button("Push to Facebook Ads Manager")

        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Placeholder for Professional Feel
        st.markdown('<div style="border: 2px dashed #1f2937; padding: 60px; text-align: center; border-radius: 12px;">', unsafe_allow_html=True)
        st.markdown('<p style="color: #4b5563;">Configuration အား ဖြည့်စွက်ပြီး Execute ကိုနှိပ်ပါ။ <br> သင့်အတွက် Campaign Ecosystem တစ်ခုလုံးကို AI မှ တွက်ချက်ပေးပါမည်။</p>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<p style='text-align: center; color: #4b5563; font-size: 12px; margin-top: 50px;'>AI Marketer Pro v2.5 | Enterprise Strategic Workspace</p>", unsafe_allow_html=True)
