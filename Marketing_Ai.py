import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v150.0",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS (V143 Dashboard + Professional Sidebar) ---
def apply_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Dashboard Styling */
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 15px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }
        .status-box-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 30px 15px; border-radius: 12px; text-align: center;
        }
        .insight-card-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 22px; border-radius: 15px; margin-bottom: 15px;
        }
        .m-label-v88 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        .header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }

        /* Intelligence & Report Styling */
        .perspective-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .report-paper {
            background: #ffffff; color: #1e293b; padding: 50px; border-radius: 4px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4); line-height: 1.8; font-family: sans-serif;
        }
        
        /* Sidebar Button Fix */
        div.stButton > button {
            background-color: #161b22; color: #adbac7; border: 1px solid #30363d;
            text-align: left; padding: 10px 15px; width: 100%; border-radius: 8px;
        }
        div.stButton > button:hover { border-color: #58a6ff; color: white; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'page' not in st.session_state:
    st.session_state.page = "📊 Dashboard"

# --- 4. SIDEBAR (IMAGE 26 / SCREENSHOT 20 STYLE) ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="color:white; margin-bottom:0;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase;">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("### SAYAR GYI'S INTELLIGENCE")
        if st.button("🧠 Deep Strategy & Reports"):
            st.session_state.page = "Intelligence"
        
        st.divider()
        st.markdown("### MENU")
        if st.button("📊 Interactive Dashboard"): st.session_state.page = "📊 Dashboard"
        if st.button("🧬 Brand DNA"): st.session_state.page = "Brand DNA"
        if st.button("📂 Project Archive"): st.session_state.page = "Archive"
        if st.button("🎨 Asset Library"): st.session_state.page = "Library"
        
        st.divider()
        st.markdown("### MY AGENTS")
        st.button("🔥 Switch to Creator Mode")
        st.write("")
        st.success("Core Engine: Online")

# --- 5. DASHBOARD (V143 EXACT CODE) ---
def render_dashboard():
    h_col, f_col = st.columns([1.5, 1])
    with h_col: st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with f_col:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    st.markdown('<p class="main-header" style="margin-top:20px;">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-v88"><div class="m-label-v88">{label}</div>'
                        f'<div style="font-size:42px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_card(label, value, delta):
        st.markdown(f'<div class="insight-card-v88"><div class="m-label-v88">{label}</div><div class="header-flex"><span class="m-value-v88">{value}</span><span class="m-delta-v88">{delta}</span></div>', unsafe_allow_html=True)
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=170)
        elif chart_style == "Area Chart": st.area_chart(data, height=170)
        else: st.bar_chart(data, height=170)
        st.markdown('</div>', unsafe_allow_html=True)

    m = {"Facebook": [("Views", "85.2K", "↑12%"), ("Interactions", "3.2K", "↑8%"), ("Followers", "12.4K", "↑1%")],
         "TikTok": [("Video Views", "1.2M", "↑45%"), ("Shares", "12K", "↑30%"), ("Saves", "4.5K", "↑18%")],
         "YouTube": [("Impressions", "2.5M", "↑5%"), ("Watch Time", "14K h", "↑12%"), ("Subscribers", "420", "↑2%")]}
    
    cols = st.columns(3)
    for i in range(3):
        with cols[i]: render_card(m[platform][i][0], m[platform][i][1], m[platform][i][2])

# --- 6. INTELLIGENCE HUB (THE 4 TABS) ---
def render_intelligence():
    st.markdown('<h1 style="font-weight:900; font-size:38px;">Sayar Gyi\'s Intelligence</h1>', unsafe_allow_html=True)
    t1, t2, t3, t4 = st.tabs(["🌐 Global Pulse", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])
    
    with t3:
        st.markdown("""<div class="perspective-card"><h3>🖋️ Content: SEO to AEO</h3><p>AI Answer Engines တွေက နေရာယူလာပါပြီ။ Case Studies တွေကို အားဖြည့်ပါ။</p></div>""", unsafe_allow_html=True)
        st.markdown("""<div class="perspective-card" style="border-left-color: #f85149;"><h3>🎯 Media Buying: Creative-Led</h3><p>Creative Quality ကသာ အဓိက Targeting ဖြစ်လာပါပြီ။</p></div>""", unsafe_allow_html=True)

    with t4:
        if st.button("Generate Executive Report"):
            st.markdown(f'<div class="report-paper"><h3>SAYAR GYI WEEKLY REPORT</h3><p>ထုတ်ပြန်သည့်ရက်စွဲ - {datetime.now().strftime("%d-%m-%Y")}</p><hr><p>၁။ AI အသုံးပြုမှု မြင့်တက်လာပြီး Local Content မှာ Authentic ဖြစ်ဖို့ လိုအပ်ပါသည်။</p></div>', unsafe_allow_html=True)

# --- 7. MAIN ROUTING ---
apply_styles()
render_sidebar()

if st.session_state.page == "📊 Dashboard":
    render_dashboard()
elif st.session_state.page == "Intelligence":
    render_intelligence()
else:
    st.title(st.session_state.page)
    st.info(f"{st.session_state.page} section is coming soon...")
