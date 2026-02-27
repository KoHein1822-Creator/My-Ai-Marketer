import streamlit as st
import pandas as pd
import numpy as np

# --- CUSTOM UI STYLING ---
def apply_premium_styles():
    st.markdown("""
        <style>
        .metric-container {
            background: #161b22; border: 1px solid #30363d;
            padding: 15px; border-radius: 10px; margin-bottom: 10px;
        }
        .status-card {
            background: #0d1117; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; text-align: center;
        }
        .status-value { color: #58a6ff; font-size: 24px; font-weight: 700; }
        </style>
    """, unsafe_allow_html=True)

def render_v79_dashboard():
    apply_premium_styles()
    
    # --- HEADER SECTION ---
    st.markdown('<h2 style="font-weight:700;">Strategic Dashboard v79.0</h2>', unsafe_allow_html=True)
    
    col_f1, col_f2 = st.columns([1, 1])
    with col_f1:
        timeframe = st.radio("Timeframe", ["Weekly", "Monthly", "Yearly", "Custom"], horizontal=True, label_visibility="collapsed")
    with col_f2:
        v_filter = st.selectbox("Global View Type", ["Bar Chart", "Area Chart"], label_visibility="collapsed")

    st.write("")

    # --- 1. CONTENT CREATION STATUS ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#8b949e; text-transform:uppercase;">Creation Pipeline</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    status_data = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(status_data):
        with [s1, s2, s3, s4][i]:
            st.markdown(f'<div class="status-card"><div style="color:#8b949e; font-size:12px;">{label}</div><div class="status-value">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- 2. DEEP PLATFORM METRICS (WITH MINI CHARTS) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; text-transform:uppercase;">Meta/Facebook Insight Auditor</p>', unsafe_allow_html=True)
    
    # Function to create a metric with a sparkline
    def spark_metric(label, value, delta, data_seed):
        with st.container():
            st.markdown('<div class="metric-container">', unsafe_allow_html=True)
            st.metric(label, value, delta)
            # Generate dummy trend data for sparkline
            chart_data = pd.DataFrame(np.random.randn(10, 1), columns=['trend'])
            st.line_chart(chart_data, height=60, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # Metric Grid: Row 1
    m1, m2, m3 = st.columns(3)
    with m1: spark_metric("Views", "85.2K", "+12.5%", 1)
    with m2: spark_metric("Interactions", "3.2K", "+8.2%", 2)
    with m3: spark_metric("Followers", "12,402", "+1.2%", 3)

    # Metric Grid: Row 2
    m4, m5, m6 = st.columns(3)
    with m4: spark_metric("Page Visits", "4.5K", "+15.0%", 4)
    with m5: spark_metric("Link Clicks", "920", "+22.4%", 5)
    with m6: spark_metric("Conversations", "128", "+5.6%", 6)

    st.write("")

    # --- 3. MAIN PERFORMANCE ANALYTICS ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#8b949e; text-transform:uppercase;">Funnel Efficiency Overview</p>', unsafe_allow_html=True)
    main_chart_data = pd.DataFrame({
        'Stage': ['Convert', 'Engage', 'Reach'],
        'Performance': [25, 45, 32]
    }).set_index('Stage')
    
    if v_filter == "Bar Chart":
        st.bar_chart(main_chart_data, color="#58a6ff", height=300)
    else:
        st.area_chart(main_chart_data, color="#58a6ff", height=300)

if __name__ == "__main__":
    render_v79_dashboard()
