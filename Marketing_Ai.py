import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION (SPACE FIX) ---
# ဒါက Desktop screen တစ်ခုလုံးကို ပြန့်သွားစေမယ့် အဓိက Magic line ပါ
st.set_page_config(layout="wide", page_title="SAYAR GYI v81.0")

def apply_v81_styles():
    st.markdown("""
        <style>
        /* Screen width optimize */
        .block-container { padding-top: 2rem; padding-bottom: 2rem; max-width: 95%; }
        
        /* Metric Card Horizontal Design */
        .metric-card-full {
            background: #161b22; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; margin-bottom: 15px;
            display: flex; align-items: center; justify-content: space-between;
        }
        .status-box-wide {
            background: #0d1117; border: 1px solid #30363d;
            padding: 15px; border-radius: 10px; text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_v81_dashboard():
    apply_v81_styles()
    
    # --- HEADER: CONTROL AREA ---
    col_t, col_s = st.columns([2, 1])
    with col_t:
        st.markdown('<h1 style="font-weight:800; color:white;">Strategic Dashboard v81.0</h1>', unsafe_allow_html=True)
    with col_s:
        # Dynamic Controls
        sc1, sc2 = st.columns(2)
        with sc1: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"], label_visibility="collapsed")
        with sc2: chart_style = st.selectbox("Chart Type", ["Line Chart", "Area Chart", "Bar Chart"], label_visibility="collapsed")

    # --- 2. PIPELINE STATUS (WIDE) ---
    st.write("")
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-wide"><div style="color:#8b949e; font-size:13px;">{label}</div><div style="font-size:30px; font-weight:800; color:#58a6ff;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- 3. HORIZONTAL METRICS WITH DYNAMIC GRAPHS ---
    # Desktop မျက်နှာပြင်ကျယ်မှာ 3 Column စီထားခြင်းက အကောင်းဆုံးပါ
    st.markdown('<p style="font-size:12px; font-weight:700; color:#58a6ff; text-transform:uppercase; letter-spacing:1px;">Meta/Facebook Insight Auditor</p>', unsafe_allow_html=True)

    def render_wide_metric(label, value, delta, key):
        with st.container():
            # Card UI
            st.markdown('<div class="metric-card-full">', unsafe_allow_html=True)
            m_left, m_right = st.columns([1, 2.5])
            
            with m_left:
                st.metric(label, value, delta)
            
            with m_right:
                # CEO စိတ်ကြိုက် Chart ပြောင်းလဲနိုင်သော Logic
                data = pd.DataFrame(np.random.randn(20, 1), columns=['Val'])
                if chart_style == "Line Chart":
                    st.line_chart(data, height=100, use_container_width=True)
                elif chart_style == "Area Chart":
                    st.area_chart(data, height=100, use_container_width=True)
                else:
                    st.bar_chart(data, height=100, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Grid Layout (3x2)
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    with row1_c1: render_wide_metric("Views", "85.2K", "+12.5%", "v")
    with row1_c2: render_wide_metric("Interactions", "3.2K", "+8.2%", "i")
    with row1_c3: render_wide_metric("Followers", "12,402", "+1.2%", "f")

    row2_c1, row2_c2, row2_c3 = st.columns(3)
    with row2_c1: render_wide_metric("Page Visits", "4.5K", "+15.0%", "pv")
    with row2_c2: render_wide_metric("Link Clicks", "920", "+22.4%", "lc")
    with row2_c3: render_wide_metric("Conversations", "128", "+5.6%", "cv")

if __name__ == "__main__":
    render_v81_dashboard()
