import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px # Pie Chart အတွက် requirements.txt ထဲမှာ plotly ထည့်ပေးပါ

# --- 1. PAGE CONFIG & UI STYLE (v15.5 Standards) ---
st.set_page_config(page_title="SAYAR GYI v25.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 20px; font-weight: 600; letter-spacing: 1px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (v15.5 UI Structure) ---
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)

    st.markdown('<p class="nav-label">Industry News</p>', unsafe_allow_html=True)
    if st.button("Read Industry Trends"): 
        st.session_state.menu = "Industry News"

    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", 
                          ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")
    
    # Session State Logic for Industry News & Creator Mode Overrides
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else: st.session_state.menu = nav_choice # Sync back

    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.caption("👤 Agent 1 | 👤 Agent 2 | 👤 Agent 3 | 👤 Agent 4")

    st.markdown('<p class="nav-label">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("Switch to Creator Mode"):
        st.session_state.menu = "Creator Mode"

    st.markdown('<p class="nav-label">System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")

    st.markdown('<p class="nav-label">The Brain</p>', unsafe_allow_html=True)
    brain_choice = st.segmented_control("Model", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE LOGIC ---

# A. INTERACTIVE DASHBOARD
if st.session_state.menu == "Interactive Dashboard":
    st.title("Strategic Dashboard")

    # --- HORIZONTAL 1: Performance Filtering ---
    st.markdown('<p class="nav-label">Performance Filtering</p>', unsafe_allow_html=True)
    filter_cols = st.columns([2, 1, 1])
    with filter_cols[0]:
        time_period = st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with filter_cols[1]:
        chart_view = st.selectbox("Visual Filter", ["Bar Chart", "Pie Chart", "Line Chart"])

    st.divider()

    # --- HORIZONTAL 2: Content Creation Status ---
    st.markdown('<p class="nav-label">Content Creation Status</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12", "+2")
    s2.metric("Pending", "5", "-1", delta_color="inverse")
    s3.metric("Scheduled", "18", "+5")
    s4.metric("Published", "145", "+12")

    st.divider()

    # --- HORIZONTAL 3: Platform Key Metrics (The Power 3) ---
    st.markdown('<p class="nav-label">Platform Metrics</p>', unsafe_allow_html=True)
    p_tab1, p_tab2, p_tab3 = st.tabs(["Facebook", "TikTok", "YouTube"])

    # Mock Data for Visuals
    mock_data = pd.DataFrame({
        'Category': ['Category A', 'Category B', 'Category C'],
        'Value': [45, 30, 25]
    })

    def display_chart(chart_type, df):
        if chart_type == "Bar Chart": st.bar_chart(df, x='Category', y='Value')
        elif chart_type == "Line Chart": st.line_chart(df, x='Category', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Category', hole=0.4, template="plotly_dark")
            fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=300)
            st.plotly_chart(fig, use_container_width=True)

    with p_tab1: # FB: Reach / Engagement / Followers
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K")
        c2.metric("Engagement", "3.2K")
        c3.metric("Followers", "12,450")
        display_chart(chart_view, mock_data)

    with p_tab2: # TikTok: Total Views / Avg. Watch Time / Profile Visits
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Views", "1.2M")
        c2.metric("Avg. Watch Time", "18s")
        c3.metric("Profile Visits", "4,200")
        display_chart(chart_view, mock_data)

    with p_tab3: # YouTube: CTR / Watch Time / Subscribers
        c1, c2, c3 = st.columns(3)
        c1.metric("CTR", "8.5%")
        c2.metric("Watch Time", "1,240h")
        c3.metric("Subscribers", "8,900")
        display_chart(chart_view, mock_data)

# B. INDUSTRY NEWS
elif st.session_state.menu == "Industry News":
    st.title("🌐 Industry News & Market Trends")
    st.info("AI curated marketing insights for 2026.")
    st.markdown("""
    * **Meta News:** New AI targeting for Jewelry SMEs.
    * **Trend Alert:** Vertical videos under 15s are converting 3x better.
    """)
    if st.button("Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"

# C. CREATOR MODE
elif st.session_state.menu == "Creator Mode":
    st.title("💰 Creator Mode")
    st.write("Passive Income Strategy & Monitoring.")
    st.metric("Total Revenue", "$1,250", "+$150")
    if st.button("Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"

else:
    st.title(st.session_state.menu)
    st.write("Section under construction.")
