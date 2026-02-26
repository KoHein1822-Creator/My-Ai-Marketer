import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # For Pie Chart

# --- 1. PREMIUM UI CONFIG ---
st.set_page_config(page_title="SAYAR GYI v26.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 20px; font-weight: 600; letter-spacing: 1px; }
    .metric-card { background: #0d1117; padding: 15px; border-radius: 10px; border: 1px solid #30363d; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (v15.5 Structure) ---
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)

    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    menu_choice = st.radio("Navigation", 
                          ["Interactive Dashboard", "Industry News", "Creator Mode", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")

    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.caption("👤 Agent 1 | 👤 Agent 2 | 👤 Agent 3 | 👤 Agent 4")

    st.markdown('<p class="nav-label">System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")

    st.markdown('<p class="nav-label">The Brain</p>', unsafe_allow_html=True)
    brain_choice = st.segmented_control("Brain", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE LOGIC ---

# A. INTERACTIVE DASHBOARD (Horizontal Layout)
if menu_choice == "Interactive Dashboard":
    st.title("Strategic Dashboard")

    # 1. Performance Filtering (Horizontal)
    st.markdown('<p class="nav-label">Performance Filtering</p>', unsafe_allow_html=True)
    f1, f2, f3 = st.columns([1.5, 1, 2])
    with f1:
        time_filter = st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with f2:
        chart_type = st.selectbox("Visual Type", ["Bar Chart", "Line Chart", "Pie Chart"])
    
    st.divider()

    # 2. Content Creation Status (Horizontal)
    st.markdown('<p class="nav-label">Content Creation Status</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12", "+2")
    s2.metric("Pending", "5", "-1", delta_color="inverse")
    s3.metric("Scheduled", "18", "+5")
    s4.metric("Published", "145", "+12")

    st.divider()

    # 3. Platform Key Metrics (Horizontal Tabs)
    st.markdown('<p class="nav-label">Platform Metrics</p>', unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["Facebook", "TikTok", "YouTube"])

    # Mock Data for Visuals
    data = pd.DataFrame({
        'Metric': ['Reach/Views', 'Engage/Watch', 'Followers/Subs'],
        'Value': [45000, 3200, 1500]
    })

    def render_visual(df, chart_choice):
        if chart_choice == "Bar Chart":
            st.bar_chart(df.set_index('Metric'))
        elif chart_choice == "Line Chart":
            st.line_chart(df.set_index('Metric'))
        else:
            fig = px.pie(df, values='Value', names='Metric', hole=0.4, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True)

    with t1: # Facebook
        m1, m2, m3 = st.columns(3)
        m1.metric("Reach", "45.2K")
        m2.metric("Engagement", "3.2K")
        m3.metric("Followers", "12.4K")
        render_visual(data, chart_type)

    with t2: # TikTok
        m1, m2, m3 = st.columns(3)
        m1.metric("Total Views", "1.2M")
        m2.metric("Avg Watch Time", "18s")
        m3.metric("Profile Visits", "4.5K")
        render_visual(data, chart_type)

    with t3: # YouTube
        m1, m2, m3 = st.columns(3)
        m1.metric("CTR", "8.5%")
        m2.metric("Watch Time", "1.2K hrs")
        m3.metric("Subscribers", "8.9K")
        render_visual(data, chart_type)

# B. INDUSTRY NEWS (Functional)
elif menu_choice == "Industry News":
    st.title("🌐 Industry News & Global Trends")
    st.markdown('<p class="nav-label">Trending Topics</p>', unsafe_allow_html=True)
    
    n1, n2 = st.columns(2)
    with n1:
        with st.container(border=True):
            st.subheader("Meta Algorithm Update")
            st.write("Meta is now prioritizing original video content over shared reels. High-quality 9:16 format is essential for 2026.")
            st.caption("Source: Meta Newsroom | 2 hours ago")
    with n2:
        with st.container(border=True):
            st.subheader("TikTok Consumer Behavior")
            st.write("Users are spending more time on long-form (1 min+) educational content. The 'How-to' niche is growing.")
            st.caption("Source: TikTok Trends | 5 hours ago")

# C. CREATOR MODE (Functional)
elif menu_choice == "Creator Mode":
    st.title("💰 Creator Mode: Passive Income Hub")
    st.markdown('<p class="nav-label">Monetization Status</p>', unsafe_allow_html=True)
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Estimated Monthly Rev", "$1,250", "+$200")
    c2.metric("Active Assets", "42", "Digital Products")
    c3.metric("Affiliate Clicks", "8.4K", "+15%")
    
    st.divider()
