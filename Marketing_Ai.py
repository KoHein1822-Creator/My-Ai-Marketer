import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PREMIUM CSS & COLOR HIGHLIGHTS ---
st.set_page_config(page_title="SAYAR GYI v28.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    
    /* Highlight Labels */
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    
    /* Customized Headings with Colors */
    .header-dashboard { color: #58a6ff; font-weight: 600; border-left: 4px solid #58a6ff; padding-left: 10px; margin-bottom: 20px; }
    .header-status { color: #aff5b4; font-weight: 600; border-left: 4px solid #aff5b4; padding-left: 10px; }
    .header-news { color: #ffab70; font-weight: 600; border-left: 4px solid #ffab70; padding-left: 10px; }
    .header-creator { color: #d3b6ff; font-weight: 600; border-left: 4px solid #d3b6ff; padding-left: 10px; }
    
    /* Metric Card Styling */
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (Dividers & Highlighted Functional Buttons) ---
with st.sidebar:
    st.markdown("<h2 style='margin:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    
    st.divider()

    st.markdown('<p class="nav-label">Mode Swapping</p>', unsafe_allow_html=True)
    if st.button("🌐 Read Industry Trends", use_container_width=True, type="secondary"): 
        st.session_state.menu = "Industry News"
    if st.button("💰 Switch to Creator Mode", use_container_width=True, type="secondary"):
        st.session_state.menu = "Creator Mode"

    st.divider()

    st.markdown('<p class="nav-label">Main Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", 
                          ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")
    
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else: st.session_state.menu = nav_choice

    st.divider()

    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.caption("👤 Intel Agent | 🎨 Creative Agent")
    st.caption("⚖️ Auditor Agent | ⚙️ Ops Agent")

    st.divider()

    st.markdown('<p class="nav-label">System Control</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")
    brain_choice = st.segmented_control("Brain", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE LOGIC ---

# A. INTERACTIVE DASHBOARD
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h2 class="header-dashboard">Strategic Dashboard Control</h2>', unsafe_allow_html=True)

    # Filtering Section
    f_cols = st.columns([2, 1, 1])
    with f_cols[0]:
        time_period = st.segmented_control("Performance Period", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with f_cols[1]:
        chart_view = st.selectbox("Visualization Style", ["Bar Chart", "Pie Chart", "Line Chart"])

    st.divider()

    # Content Creation Status Section
    st.markdown('<h3 class="header-status">Content Creation Status</h3>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12", "+2")
    s2.metric("Pending Approval", "5", "-1", delta_color="inverse")
    s3.metric("Scheduled", "18", "+5")
    s4.metric("Published", "145", "+12")

    st.divider()

    # Platform Metrics Section
    st.markdown('<p class="nav-label">Multi-Platform Analytics</p>', unsafe_allow_html=True)
    p_tab1, p_tab2, p_tab3 = st.tabs(["Facebook Insights", "TikTok Performance", "YouTube Metrics"])

    mock_data = pd.DataFrame({'Category': ['Awareness', 'Engagement', 'Conversion'], 'Value': [45, 35, 20]})

    def display_chart(chart_type, df, unique_key):
        if chart_type == "Bar Chart": st.bar_chart(df, x='Category', y='Value')
        elif chart_type == "Line Chart": st.line_chart(df, x='Category', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Category', hole=0.4, template="plotly_dark", color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=350)
            st.plotly_chart(fig, use_container_width=True, key=unique_key)

    with p_tab1:
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K", "+15%")
        c2.metric("Engagement", "3.2K", "+8%")
        c3.metric("Followers", "12,450", "+1.2%")
        display_chart(chart_view, mock_data, "fb_v28")

    with p_tab2:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Views", "1.2M", "+20%")
        c2.metric("Avg. Watch Time", "18s", "+2s")
        c3.metric("Profile Visits", "4,200", "+500")
        display_chart(chart_view, mock_data, "
