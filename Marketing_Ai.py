import streamlit as st
import pandas as pd
import numpy as np

# --- CUSTOM CSS FOR HORIZONTAL CARDS ---
def apply_v80_styles():
    st.markdown("""
        <style>
        .metric-card-horizontal {
            background: #161b22; border: 1px solid #30363d;
            padding: 15px; border-radius: 12px; margin-bottom: 20px;
        }
        .status-box {
            background: #0d1117; border: 1px solid #30363d;
            padding: 10px; border-radius: 8px; text-align: center;
        }
        /* Custom Table/Grid for Charts */
        .chart-grid { display: flex; flex-wrap: wrap; gap: 15px; }
        </style>
    """, unsafe_allow_html=True)

def render_v80_dashboard():
    apply_v80_styles()
    
    # --- HEADER: CONTROL AREA ---
    col_title, col_ctrl = st.columns([1.5, 1])
    with col_title:
        st.markdown('<h1 style="font-size:28px; font-weight:700;">Strategic Dashboard v80.0</h1>', unsafe_allow_html=True)
    with col_ctrl:
        # Integrated Filter Controls
        sub_c1, sub_c2 = st.columns(2)
        with sub_c1:
            timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly", "Custom"], label_visibility="collapsed")
        with sub_c2:
            chart_type = st.selectbox("Chart Style", ["Line Chart", "Bar Chart", "Area Chart"], label_visibility="collapsed")

    # --- 1. PIPELINE STATUS (HORIZONTAL) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#8b949e; text-transform:uppercase;">Content Creation Pipeline</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box"><div style="color:#8b949e; font-size:11px;">{label}</div><div style="font-size:22px; font-weight:700; color:#58a6ff;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- 2. DEEP METRICS WITH DYNAMIC CHARTS (HORIZONTAL GRID) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; text-transform:uppercase;">Meta/Facebook Insight Auditor</p>', unsafe_allow_html=True)

    # Function to render Horizontal Metric with Dynamic Chart
    def horizontal_metric_block(label, value, delta, key):
        st.markdown('<div class="metric-card-horizontal">', unsafe_allow_html=True)
        c_left, c_right = st.columns([1, 2.5])
        
        with c_left:
            st.metric(label, value, delta)
        
        with c_right:
            # Generate Dummy Data for Trend
            data = pd.DataFrame(np.random.randn(15, 1), columns=['Trend'])
            if chart_type == "Line Chart":
                st.line_chart(data, height=80, use_container_width=True)
            elif chart_type == "Bar Chart":
                st.bar_chart(data, height=80, use_container_width=True)
            else:
                st.area_chart(data, height=80, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Row 1: Views, Interactions, Followers
    r1_c1, r1_c2, r1_c3 = st.columns(3)
    with r1_c1: horizontal_metric_block("Views", "85.2K", "+12.5%", "v1")
    with r1_c2: horizontal_metric_block("Interactions", "3.2K", "+8.2%", "i1")
    with r1_c3: horizontal_metric_block("Followers", "12,402", "+1.2%", "f1")

    # Row 2: Visits, Link Clicks, Conversations
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1: horizontal_metric_block("Page Visits", "4.5K", "+15.0%", "pv1")
    with r2_c2: horizontal_metric_block("Link Clicks", "920", "+22.4%", "lc1")
    with r2_c3: horizontal_metric_block("Conversations", "128", "+5.6%", "cv1")

if __name__ == "__main__":
    render_v80_dashboard()
