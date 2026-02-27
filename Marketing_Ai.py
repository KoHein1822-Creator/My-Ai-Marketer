import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIGURATION FOR MAXIMUM CANVAS USE ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v82.0")

def apply_v82_styles():
    st.markdown("""
        <style>
        /* Screen Optimization */
        .block-container { padding-top: 1rem; max-width: 98%; }
        
        /* Metric Card - ပိုထွားပြီး ပိုကျယ်အောင် လုပ်ထားသည် */
        .metric-card-v82 {
            background: #161b22; border: 1px solid #30363d;
            padding: 25px; border-radius: 15px; margin-bottom: 25px;
            min-height: 250px; /* အောက်က Space ကို ယူရန် အရပ်ကို မြှင့်ထားသည် */
        }
        
        /* Headers Fix */
        .section-header {
            color: #58a6ff; font-size: 14px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 1.5px;
            margin-bottom: 20px; border-left: 4px solid #58a6ff; padding-left: 10px;
        }
        
        /* Pipeline Box */
        .status-box-v82 {
            background: #0d1117; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; text-align: center;
        }
        </style>
    """, unsafe_allow_html=True)

def render_v82_dashboard():
    apply_v82_styles()
    
    # --- TOP CONTROL BAR ---
    st.markdown('<h1 style="font-weight:900; margin-bottom:0px;">Strategic Dashboard v82.0</h1>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns([2, 0.5, 0.5])
    with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"], label_visibility="collapsed")
    with c3: chart_type = st.selectbox("Chart Style", ["Area Chart", "Bar Chart", "Line Chart"], label_visibility="collapsed")

    # --- 1. CONTENT CREATION STATUS (TOP BANNER) ---
    st.markdown('<p class="section-header">Content Creation Pipeline Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-v82"><div style="color:#8b949e; font-size:14px;">{label}</div><div style="font-size:35px; font-weight:900; color:#58a6ff;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- 2. MAIN INSIGHTS (EXPANDED GRID) ---
    st.markdown('<p class="section-header">Meta/Facebook Deep Performance Metrics</p>', unsafe_allow_html=True)

    def big_metric_block(label, value, delta):
        st.markdown('<div class="metric-card-v82">', unsafe_allow_html=True)
        # ထိပ်မှာ ဂဏန်းပြမယ်
        st.metric(label, value, delta)
        st.write("")
        # အောက်မှာ Chart ကို နေရာအပြည့်ယူခိုင်းမယ်
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_type == "Area Chart":
            st.area_chart(data, height=180, use_container_width=True)
        elif chart_type == "Bar Chart":
            st.bar_chart(data, height=180, use_container_width=True)
        else:
            st.line_chart(data, height=180, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # 3x2 Grid - တစ်ခုချင်းစီက နေရာပိုယူထားလို့ Desktop မှာ အားရစရာ ဖြစ်နေပါလိမ့်မယ်
    row1_c1, row1_c2, row1_c3 = st.columns(3)
    with row1_c1: big_metric_block("Views", "85.2K", "+12.5%")
    with row1_c2: big_metric_block("Interactions", "3.2K", "+8.2%")
    with row1_c3: big_metric_block("Followers", "12,402", "+1.2%")

    row2_c1, row2_c2, row2_c3 = st.columns(3)
    with row2_c1: big_metric_block("Page Visits", "4.5K", "+15.0%")
    with row2_c2: big_metric_block("Link Clicks", "920", "+22.4%")
    with row2_c3: big_metric_block("Conversations", "128", "+5.6%")

if __name__ == "__main__":
    render_v82_dashboard()
