import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. CONFIG & STYLES (အုတ်မြစ် - လုံးဝမပြင်ပါနှင့်) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v151.0", page_icon="⚖️")

def apply_fixed_styles():
    st.markdown("""
        <style>
        /* Base Layout */
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Dashboard & Intelligence Cards */
        .main-header { color: #58a6ff; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; border-left: 5px solid #58a6ff; padding-left: 15px; margin-bottom: 15px; }
        .status-box-v88 { background: #161b22; border: 1px solid #30363d; padding: 30px 15px; border-radius: 12px; text-align: center; }
        .insight-card-v88 { background: #161b22; border: 1px solid #30363d; padding: 22px; border-radius: 15px; margin-bottom: 15px; }
        .perspective-card { background: #0d1117; border: 1px solid #30363d; border-radius: 12px; padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff; }
        
        /* Values & Deltas */
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        .header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 15px; }
        
        /* Sidebar Buttons (Screenshot 26 Style) */
        div.stButton > button {
            background-color: #161b22; color: #adbac7; border: 1px solid #30363d;
            text-align: left; padding: 10px 15px; width: 100%; border-radius: 8px; margin-bottom: -10px;
        }
        div.stButton > button:hover { border-color: #58a6ff; color: white; background-color: #21262d; }
        
        /* Weekly Report Paper */
        .report-paper { background: #ffffff; color: #1e293b; padding: 50px; border-radius: 4px; box-shadow: 0 15px 35px rgba(0,0,0,0.4); line-height: 1.8; font-family: sans-serif; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR LOGIC (SCREENSHOT 26) ---
def render_sidebar():
    if 'page' not in st.session_state:
        st.session_state.page = "Dashboard"

    with st.sidebar:
        st.markdown('<h2 style="color:white; margin-bottom:0;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("### SAYAR GYI'S INTELLIGENCE")
        if st.button("🧠 Deep Strategy & Reports"):
            st.session_state.page = "Intelligence"
        
        st.divider()
        st.markdown("### MENU")
        if st.button("📊 Interactive Dashboard"): st.session_state.page = "Dashboard"
        if st.button("🧬 Brand DNA"): st.session_state.page = "Brand DNA"
        if st.button("📂 Project Archive"): st.session_state.page = "Archive"
        if st.button("🎨 Asset Library"): st.session_state.page = "Library"
        
        st.divider()
        st.markdown("### MY AGENTS")
        st.button("🔥 Switch to Creator Mode")
        st.write("")
        st.success("Core Engine: Online")
        st.radio("Engine", ["Gemini 1.5 Pro", "GPT-4o"], horizontal=True, label_visibility="collapsed")

# --- 3. PAGE: DASHBOARD (V143 LOGIC) ---
def show_dashboard():
    h_col, f_col = st.columns([1.5, 1])
    with h_col: st.markdown('<h1 style="font-weight:900; font-size:38px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with f_col:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    # Content Pipeline
    st.markdown('<p class="main-header" style="margin-top:20px;">Content Creation Status</p>', unsafe_allow_html=True)
    p_cols = st.columns(4)
    status = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(status):
        with p_cols[i]:
            st.markdown(f'<div class="status-box-v88"><div style="color:#8b949e; font-size:12px;">{label}</div>'
                        f'<div style="font-size:40px; font-weight:900; color:#58a6ff;">{val}</div></div>', unsafe_allow_html=True)

    # Metrics
    st.write("")
    st.markdown(f'<p class="main-header">{platform} Trends</p>', unsafe_allow_html=True)
    m_cols = st.columns(3)
    for i in range(3):
        with m_cols[i]:
            st.markdown(f'<div class="insight-card-v88"><div class="header-flex"><div><small style="color:#8b949e;">METRIC {i+1}</small><div class="m-value-v88">{20+i}.5K</div></div><span class="m-delta-v88">↑12%</span></div>', unsafe_allow_html=True)
            st.line_chart(np.random.randn(15, 1), height=150)
            st.markdown('</div>', unsafe_allow_html=True)

# --- 4. PAGE: INTELLIGENCE (TAB 4 ခု) ---
def show_intelligence():
    st.markdown('<h1 style="font-weight:900; font-size:38px;">Intelligence Suite</h1>', unsafe_allow_html=True)
    t1, t2, t3, t4 = st.tabs(["🌐 Global Pulse", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])
    
    with t1:
        st.info("Global Marketing & AI Trends Loading...")
        st.table(pd.DataFrame({"Trend": ["AEO", "Agentic Ads"], "Impact": ["High", "Critical"]}))
    
    with t2:
        st.warning("Myanmar Digital Ecosystem: Telegram & VPN usage rising.")

    with t3:
        st.markdown("""<div class="perspective-card"><h3>🖋️ Content: SEO to AEO</h3><p>AI Answer Engines တွေအတွက် အသင့်ဖြစ်ဖို့ Structured Data နဲ့ Case Studies တွေ အားဖြည့်ပါ။</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="perspective-card" style="border-left-color: #f85149;"><h3>🎯 Media Buying: Creative-Led</h3><p>AI Targeting ကို စိတ်မချပါနဲ့။ Creative Variation များများနဲ့ AI ကို လမ်းပြပါ။</p></div>""", unsafe_allow_html=True)

    with t4:
        if st.button("Generate Executive Report"):
            report_date = datetime.now().strftime("%d %B %Y")
            st.markdown(f'<div class="report-paper"><h2>EXECUTIVE REPORT</h2><p>Date: {report_date}</p><hr><p><b>Summary:</b> ယခုအပတ်တွင် Content Engagement 12% တက်လာသော်လည်း Reach မှာ ပုံမှန်သာ ရှိပါသည်။</p><p><b>Action:</b> Short-form Video Hook များကို ပြန်လည်စစ်ဆေးရန်။</p></div>', unsafe_allow_html=True)

# --- 5. EXECUTION (အဓိက မောင်းနှင်ချက်) ---
apply_fixed_styles()
render_sidebar()

if st.session_state.page == "Dashboard":
    show_dashboard()
elif st.session_state.page == "Intelligence":
    show_intelligence()
else:
    st.markdown(f"<h1>{st.session_state.page}</h1>", unsafe_allow_html=True)
    st.info("Module Syncing in progress...")
