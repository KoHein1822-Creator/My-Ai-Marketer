import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. SETTINGS & CSS (Preserving v15.5 Layout) ---
st.set_page_config(page_title="SAYAR GYI v29.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    
    /* Sidebar Layout Fix */
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; padding-top: 20px; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 20px; font-weight: 600; letter-spacing: 1px; }
    
    /* Strategic Color Highlights */
    .h-dash { color: #58a6ff; font-weight: 600; } /* Blue */
    .h-status { color: #aff5b4; font-weight: 600; } /* Green */
    .h-platform { color: #ffab70; font-weight: 600; } /* Orange */
    
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 12px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (V15.5 ORIGINAL STRUCTURE) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)

    # Industry News (Functional Interface)
    st.markdown('<p class="nav-label">Industry News</p>', unsafe_allow_html=True)
    if st.button("Open Industry Insights", use_container_width=True):
        st.session_state.current_page = "Industry News"

    st.divider()

    # Main Menu
    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Menu", 
                          ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")
    
    # Page state management
    if 'current_page' not in st.session_state:
        st.session_state.current_page = "Interactive Dashboard"
    
    # If a radio button is clicked, it updates the page unless News/Creator is active
    if nav_choice:
        st.session_state.current_page = nav_choice

    st.divider()

    # My Agents
    st.markdown('<p class="nav-label">My Agent</p>', unsafe_allow_html=True)
    st.markdown("- Agent 1\n- Agent 2\n- Agent 3\n- Agent 4")

    st.divider()

    # Creator Mode (Functional Interface)
    st.markdown('<p class="nav-label">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("Open Creator Mode", use_container_width=True):
        st.session_state.current_page = "Creator Mode"

    st.divider()

    # System Status
    st.markdown('<p class="nav-label">System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")

    st.divider()

    # The Brain
    st.markdown('<p class="nav-label">The Brain</p>', unsafe_allow_html=True)
    brain_choice = st.segmented_control("Brain", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE LOGIC ---

# A. INTERACTIVE DASHBOARD
if st.session_state.current_page == "Interactive Dashboard":
    st.markdown('<h1 class="h-dash">Interactive Dashboard</h1>', unsafe_allow_html=True)

    # 1. Performance Filtering (Horizontal)
    st.markdown('<p class="nav-label">Performance Filtering</p>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([2, 1, 1])
    with f1:
        time_filter = st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with f2:
        chart_view = st.selectbox("Visual Filter", ["Bar Chart", "Pie Chart", "Line Chart"])
    
    st.divider()

    # 2. Content Creation Status (Horizontal)
    st.markdown('<h3 class="h-status">Content Creation Status</h3>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12")
    s2.metric("Pending", "5")
    s3.metric("Scheduled", "18")
    s4.metric("Published", "145")

    st.divider()

    # 3. Platform Key Metrics (Horizontal Tabs)
    st.markdown('<h3 class="h-platform">Platform Key Metrics</h3>', unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["Facebook", "TikTok", "YouTube"])

    mock_data = pd.DataFrame({'Metric': ['Engage', 'Reach', 'Convert'], 'Value': [40, 35, 25]})

    def display_chart(chart_type, df, key):
        if chart_type == "Bar Chart": st.bar_chart(df, x='Metric', y='Value')
        elif chart_type == "Line Chart": st.line_chart(df, x='Metric', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Metric', hole=0.4, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True, key=key)

    with t1: # FB
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K")
        c2.metric("Engagement", "3.2K")
        c3.metric("Followers", "12.4K")
        display_chart(chart_view, mock_data, "fb_v29")

    with t2: # TT
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Views", "1.2M")
        c2.metric("Avg. Watch Time", "18s")
        c3.metric("Profile Visits", "4.2K")
        display_chart(chart_view, mock_data, "tt_v29")

    with t3: # YT
        c1, c2, c3 = st.columns(3)
        c1.metric("CTR", "8.5%")
        c2.metric("Watch Time", "1.2K h")
        c3.metric("Subscribers", "8.9K")
        display_chart(chart_view, mock_data, "yt_v29")

# B. INDUSTRY NEWS
elif st.session_state.current_page == "Industry News":
    st.title("Industry News")
    st.write("Displaying latest AI Marketing trends...")
    if st.button("Back to Dashboard"): st.session_state.current_page = "Interactive Dashboard"

# C. CREATOR MODE
elif st.session_state.current_page == "Creator Mode":
    st.title("Creator Mode")
    st.write("Passive Income tracking...")
    if st.button("Back to Dashboard"): st.session_state.current_page = "Interactive Dashboard
