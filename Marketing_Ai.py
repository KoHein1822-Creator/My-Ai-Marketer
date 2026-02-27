import streamlit as st
import pandas as pd

# --- CUSTOM CSS FOR ENHANCED UI ---
def local_css():
    st.markdown("""
        <style>
        /* Creation Status Cards Styling */
        .status-card {
            background: #161b22; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; text-align: center;
            transition: transform 0.2s;
        }
        .status-card:hover { border-color: #58a6ff; transform: translateY(-5px); }
        .status-label { color: #8b949e; font-size: 12px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .status-value { color: #ffffff; font-size: 28px; font-weight: 700; }
        
        /* Metric Box Tweaks */
        [data-testid="stMetricValue"] { font-size: 24px !important; color: #ffffff !important; }
        [data-testid="stMetricDelta"] { font-size: 14px !important; }
        </style>
    """, unsafe_allow_html=True)

def render_v78_dashboard():
    local_css()
    
    # --- HEADER & GLOBAL FILTERS ---
    st.markdown('<h1 style="font-size:32px; font-weight:700; margin-bottom:5px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    col_filter_1, col_filter_2 = st.columns([1, 1.5])
    with col_filter_1:
        # Timeframe Customization Feature
        timeframe = st.radio("Timeframe", ["Weekly", "Monthly", "Yearly", "Custom Range"], horizontal=True, label_visibility="collapsed")
    with col_filter_2:
        # Visual Filter as seen in Screenshot (40)
        v_filter = st.selectbox("Visual Filter", ["Bar Chart", "Line Chart", "Area Chart"], label_visibility="collapsed")

    st.write("")

    # --- 1. CONTENT CREATION STATUS (ENHANCED UI) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Content Creation Status</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    
    status_items = [
        {"label": "Drafting", "value": "12", "col": s1},
        {"label": "Pending", "value": "5", "col": s2},
        {"label": "Scheduled", "value": "18", "col": s3},
        {"label": "Published", "value": "145", "col": s4}
    ]
    
    for item in status_items:
        with item["col"]:
            st.markdown(f"""
                <div class="status-card">
                    <div class="status-label">{item['label']}</div>
                    <div class="status-value">{item['value']}</div>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.divider()

    # --- 2. PLATFORM METRICS (DEEP FACEBOOK INSIGHTS) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#8b949e; text-transform:uppercase; letter-spacing:1px;">Platform Performance Metrics</p>', unsafe_allow_html=True)
    
    p_tabs = st.tabs(["Facebook", "TikTok", "YouTube"])

    with p_tabs[0]: # Facebook Deep Metrics
        st.write("")
        # First Row of Metrics
        m1, m2, m3 = st.columns(3)
        m1.metric("Views", "85.2K", "+12.5%")
        m2.metric("Interactions", "3.2K", "+8.2%")
        m3.metric("Followers", "12,402", "+1.2%")
        
        # Second Row of Metrics (New Requirements)
        m4, m5, m6 = st.columns(3)
        m4.metric("Page Visits", "4.5K", "+15.0%")
        m5.metric("Link Clicks", "920", "+22.4%")
        m6.metric("Conversations", "128", "+5.6%")
        
        st.write("")
        # Integrated Chart
        chart_data = pd.DataFrame({
            'Category': ['Convert', 'Engage', 'Reach'],
            'Value': [25, 45, 32]
        }).set_index('Category')
        
        if v_filter == "Bar Chart":
            st.bar_chart(chart_data, color="#58a6ff")
        elif v_filter == "Line Chart":
            st.line_chart(chart_data, color="#58a6ff")
        else:
            st.area_chart(chart_data, color="#58a6ff")

    with p_tabs[1]:
        st.info("TikTok Metrics are being synced from Creator Center...")
    with p_tabs[2]:
        st.info("YouTube Studio insights are loading...")

# Test Execution
if __name__ == "__main__":
    render_v78_dashboard()
