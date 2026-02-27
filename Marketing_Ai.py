import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIG & SIDEBAR ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v83.0")

def render_sidebar():
    with st.sidebar:
        st.title("SAYAR GYI'S")
        st.caption("AI Marketing Agency")
        st.divider()
        st.markdown("### MENU")
        st.radio("Navigate", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
        st.divider()
        st.success("Core Engine: Online")
        st.info("Node: SG-AI-MASTER")

def apply_v83_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        /* Black Box Fix - Empty Space ဖယ်ထုတ်ခြင်း */
        .metric-container-v83 {
            background: #161b22; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; margin-bottom: 20px;
        }
        .section-label {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; border-left: 3px solid #58a6ff;
            padding-left: 10px; margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_v83_dashboard():
    render_sidebar()
    apply_v83_styles()
    
    # --- TOP CONTROLS (PLATFORM FILTER) ---
    col_head, col_opt = st.columns([1.5, 1])
    with col_head:
        st.markdown('<h1 style="font-weight:800; margin:0;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with col_opt:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Area Chart", "Bar Chart", "Line Chart"])

    # --- 1. PIPELINE STATUS ---
    st.write("")
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div style="background:#0d1117; border:1px solid #30363d; padding:15px; border-radius:10px; text-align:center;">'
                        f'<div style="color:#8b949e; font-size:12px;">{label}</div>'
                        f'<div style="font-size:28px; font-weight:800; color:#58a6ff;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.markdown(f'<p class="section-label">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    # --- 2. DYNAMIC METRIC GRID (FIXED EMPTY SPACE) ---
    def metric_engine(label, value, delta):
        st.markdown('<div class="metric-container-v83">', unsafe_allow_html=True)
        # Metric ကို ထိပ်ဆုံးမှာ တင်လိုက်ခြင်းဖြင့် အမဲရောင်အကွက်ကြီး ပျောက်သွားမည်
        st.metric(label, value, delta)
        
        # Generate Data
        data = pd.DataFrame(np.random.randn(20, 1), columns=['Val'])
        if chart_style == "Area Chart": st.area_chart(data, height=150, use_container_width=True)
        elif chart_style == "Bar Chart": st.bar_chart(data, height=150, use_container_width=True)
        else: st.line_chart(data, height=150, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Platform အလိုက် Metrics များ ပြောင်းလဲပေးခြင်း
    if platform == "Facebook":
        m_list = [("Views", "85.2K", "+12%"), ("Interactions", "3.2K", "+8%"), ("Followers", "12.4K", "+1%"),
                  ("Page Visits", "4.5K", "+15%"), ("Link Clicks", "920", "+22%"), ("Conversations", "128", "+5%")]
    elif platform == "TikTok":
        m_list = [("Video Views", "1.2M", "+45%"), ("Shares", "12K", "+30%"), ("Saves", "4.5K", "+18%"),
                  ("Profile Visits", "25K", "+10%"), ("Bio Clicks", "1.5K", "+25%"), ("Completion Rate", "65%", "+5%")]
    else: # YouTube
        m_list = [("Impressions", "2.5M", "+5%"), ("Watch Time", "14K hrs", "+12%"), ("Subscribers", "420", "+2%"),
                  ("Avg View Duration", "4:32", "+0:45"), ("CTR", "8.5%", "+1.2%"), ("Comments", "850", "+15%")]

    # Render Grid
    r1_cols = st.columns(3)
    for i in range(3):
        with r1_cols[i]: metric_engine(m_list[i][0], m_list[i][1], m_list[i][2])
    
    r2_cols = st.columns(3)
    for i in range(3, 6):
        with r2_cols[i-3]: metric_engine(m_list[i][0], m_list[i][1], m_list[i][2])

if __name__ == "__main__":
    render_v83_dashboard()
