import streamlit as st
import pandas as pd

# --- 1. SESSION STATE ---
if 'menu' not in st.session_state: st.session_state.menu = "Brand DNA"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v75.0", layout="wide")

# v72.0 SIDEBAR RECOVERY + BRAND DNA CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* v72.0 Sidebar Exact Restoration */
    section[data-testid="stSidebar"] { background-color: #010409 !important; min-width: 320px !important; border-right: 1px solid #30363d; }
    .sidebar-header { font-size: 13px; font-weight: 700; color: #58a6ff; margin-top: 25px; margin-bottom: 12px; letter-spacing: 1.5px; text-transform: uppercase; }
    
    /* The Brain Buttons v72.0 Grid */
    div.stButton > button {
        height: 48px !important; font-size: 15px !important; font-weight: 600 !important;
        border-radius: 8px !important; background-color: #161b22 !important;
        border: 1px solid #30363d !important; color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Status Panel v72.0 Exact */
    .status-panel { background: #0d1117; border: 1px solid #30363d; padding: 18px; border-radius: 10px; margin-top: 10px; }
    .status-node-info { font-size: 10px; color: #8b949e; margin-top: 8px; border-top: 1px solid #21262d; padding-top: 8px; display: flex; justify-content: space-between; }
    
    /* Brand DNA UI Enhancements */
    .dna-card { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 12px; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v72.0 RESTORED) ---
with st.sidebar:
    st.markdown('<h1 style="color:white; margin-bottom:0; font-size:28px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:12px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", key="gem", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", key="cla", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", key="gpt", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    
    st.markdown(f'<div style="background:rgba(88,166,255,0.1); border:1px solid rgba(88,166,255,0.3); padding:8px; border-radius:6px; text-align:center; margin-top:10px; font-size:12px; color:#58a6ff;">Active Core: <b>{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          index=1, label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    st.divider()

    # System Status v72.0 Spatial Optimization
    st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
            <p style="color:#8b949e; font-size:11px; margin-top:2px;">Network: Stable (12ms)</p>
            <div class="status-node-info"><span>NODE: SG-AI-01</span><span>UPTIME: 99.9%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (Brand DNA Intelligence) ---
if st.session_state.menu == "Brand DNA":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    
    # Mode Selection (Intelligence vs Manual)
    mode = st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)
    st.divider()

    if "Intelligence Mode" in mode:
        st.markdown('<div class="dna-card">', unsafe_allow_html=True)
        st.subheader("AI Intelligence Researcher")
        st.write("လုပ်ငန်းအမျိုးအစား ရွေးချယ်ပါ သို့မဟုတ် အသစ်ထည့်ပါ")
        
        # Industry Choices for Myanmar Market
        industries = [
            "Jewelry & Gold (ကျောက်မျက်ရတနာနှင့် ရွှေဆိုင်)",
            "Fashion & Clothing (အထည်အလိပ်နှင့် ဖက်ရှင်)",
            "Real Estate (အိမ်ခြံမြေ ဝန်ဆောင်မှု)",
            "F&B / Restaurant (စားသောက်ဆိုင်နှင့် မုန့်တိုက်)",
            "Cosmetics & Beauty (အလှကုန်နှင့် အလှအပရေးရာ)",
            "Education Services (ပညာရေးဝန်ဆောင်မှု)",
            "Tech & Gadgets (နည်းပညာနှင့် ဖုန်း/ကွန်ပျူတာ)",
            "Others (စာရင်းထဲတွင်မပါပါ)"
        ]
        
        choice = st.selectbox("Industry Type", industries, label_visibility="collapsed")
        
        # Custom Input Feature
        if choice == "Others (စာရင်းထဲတွင်မပါပါ)":
            custom_industry = st.text_input("သင့်လုပ်ငန်းအမျိုးအစားကို အသေးစိတ်ရေးပေးပါ", placeholder="ဥပမာ- စိုက်ပျိုးရေးသွင်းအားစု အရောင်းဆိုင်")
        
        st.button("Generate Strategy")
        st.markdown('</div>', unsafe_allow_html=True)

    else: # Manual Mode
        st.markdown('<div class="dna-card">', unsafe_allow_html=True)
        st.subheader("Manual Brand Configuration")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Brand Name")
            st.text_area("Brand Mission")
        with col2:
            st.text_input("Target Audience")
            st.text_area("Unique Selling Point (USP)")
        st.button("Save Brand DNA")
        st.markdown('</div>', unsafe_allow_html=True)

# Preserve other layouts for consistency
elif st.session_state.menu == "Interactive Dashboard":
    st.info("Interactive Dashboard is active. All metrics from v32.0 are preserved.")
