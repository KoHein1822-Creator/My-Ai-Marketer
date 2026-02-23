import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Marketer Suite Pro", layout="wide", page_icon="🚀")

# --- CUSTOM CSS (Glassmorphism & Modern UI) ---
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #f8fafc; }
    
    /* Glassmorphism Card */
    .command-card {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 15px;
        padding: 20px;
        border: 1px solid rgba(226, 232, 240, 1);
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    
    /* Custom Toggle Style */
    .stRadio > div { flex-direction: row; gap: 20px; }
    
    /* Matrix Tab Styling */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #f1f5f9;
        border-radius: 8px 8px 0px 0px;
        padding: 10px 20px;
    }
    
    /* Professional Button */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3.5em;
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%);
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: ASSET & BRAND VAULT ---
with st.sidebar:
    st.title("💎 AI Marketer")
    st.markdown("---")
    
    st.subheader("📁 Brand Vault")
    selected_brand = st.selectbox("Select Brand/Project", ["Personal Brand", "Jewelry Client A", "Tech Startup X", "+ Add New Brand"])
    
    with st.expander("🧬 Style DNA Settings"):
        st.info("အမှတ်တံဆိပ်၏ လေသံနှင့် ရေးဟန်ကို ဤနေရာတွင် စီမံပါ။")
        st.text_area("Master Copy (DNA)", height=150, placeholder="သင့်ရဲ့ အကောင်းဆုံး Post နမူနာများ...")
        
    st.divider()
    st.subheader("💳 Subscription")
    st.success("Plan: Elite Agency (3 Months)")
    st.caption("Expiry: 25 May 2026")

# --- MAIN LAYOUT ---
# Header Area
col_title, col_mode = st.columns([2, 1])
with col_title:
    st.title("Command Center")
    st.caption(f"Currently Managing: **{selected_brand}**")

with col_mode:
    # THE PSYCHOLOGY TOGGLE: SMART VS ARCHITECT
    app_mode = st.radio("System Engine", ["⚡ Smart Mode", "🛠️ Architect Mode"], help="Smart: One-click fast generation | Architect: Manual Expert control")

st.divider()

# --- INPUT & OUTPUT AREA ---
col_input, col_output = st.columns([1, 1.4], gap="large")

with col_input:
    st.markdown('<div class="command-card">', unsafe_allow_html=True)
    st.subheader("🎯 Campaign Input")
    
    topic = st.text_input("What are we marketing today?", placeholder="e.g. ရွှေဖြူဆွဲကြိုး လက်ရာသစ်")
    
    # Smart Mode Logic
    if "Smart" in app_mode:
        st.info("💡 **Smart Tip:** Promo Price သို့မဟုတ် Discount ထည့်ပေးလျှင် AI က ပိုမိုထိရောက်သော Angle များ ထုတ်ပေးနိုင်ပါသည်။")
        goal = st.selectbox("Campaign Goal", ["Instant Sales", "Brand Storytelling", "Educational Awareness"])
        st.caption("System will auto-select Frameworks & Roles based on Brand DNA.")
    
    # Architect Mode Logic (The IKEA Effect)
    else:
        st.warning("🛠️ **Expert Control Enabled**")
        niche = st.selectbox("Niche", ["Jewelry", "Cosmetics", "Tech", "Real Estate"])
        role = st.selectbox("AI Persona Role", ["Senior Copywriter", "Direct Response Closer", "Luxury Brand Expert"])
        frameworks = st.multiselect("Select Frameworks", ["AIDA", "PAS", "BAB", "4Ps"], default=["AIDA", "PAS"])
        creativity = st.slider("Creativity Level (Temperature)", 0.0, 1.0, 0.7)
        tone_intensity = st.select_slider("Tone Intensity", ["Soft", "Medium", "Aggressive"])

    if st.button("EXECUTE CAMPAIGN ✨"):
        st.toast("AI Marketer is thinking...")
        # (Generation Logic would go here)
        st.session_state['generated'] = True
    
    st.markdown('</div>', unsafe_allow_html=True)

with col_output:
    st.subheader("🚀 Content Matrix")
    
    if 'generated' in st.session_state:
        # THE CONTENT MATRIX TABS
        tab_copy, tab_script, tab_visual = st.tabs(["📝 Ad Copies", "🎬 Video Scripts", "🎨 Visual Assets"])
        
        with tab_copy:
            st.markdown("### Framework-Based Variations")
            col_a, col_p = st.columns(2)
            with col_a:
                st.markdown("**AIDA Style**")
                st.text_area("Copy 1", "Attention: [Hook]...\nInterest: ...\nDesire: ...\nAction: ...", height=250, key="aida")
            with col_p:
                st.markdown("**PAS Style**")
                st.text_area("Copy 2", "Problem: [Pain Point]...\nAgitation: ...\nSolution: ...", height=250, key="pas")
        
        with tab_script:
            st.markdown("### Short-Form Video Scripts (Reels/TikTok)")
            st.text_area("Viral Script", "Hook: 0-3 sec\nValue: 3-15 sec\nCTA: 15-20 sec", height=200)
            st.button("🔄 Regenerate with Different Hook")
            
        with tab_visual:
            st.markdown("### AI Image Prompts (Midjourney/DALL-E)")
            st.code("/imagine prompt: Luxury white gold necklace on a velvet neck stand, soft cinematic lighting, 8k resolution --ar 4:5", language="bash")
            st.caption("ဒီ Prompt ကိုကူးပြီး AI Image Generator တွေမှာ ပုံထုတ်နိုင်ပါတယ်။")
            
        # Global Action Bar
        st.markdown("---")
        c1, c2, c3 = st.columns(3)
        c1.button("📋 Copy All Assets")
        c2.button("📥 Export to PDF")
        c3.button("🔄 Bulk Refine")

    else:
        st.info("Input များဖြည့်သွင်းပြီး Execute နှိပ်ပါက Content Matrix ပေါ်လာပါလိမ့်မည်။")

# --- FOOTER ---
st.markdown("---")
st.caption("Powered by Gemini 1.5 Pro | Designed for Digital Nomads & AI Marketers")
