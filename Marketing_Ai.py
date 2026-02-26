import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE CONFIG & UI STYLE ---
st.set_page_config(page_title="SAYAR GYI v27.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    hr { margin: 1rem 0; border-color: #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (v15.5 Style with Dividers) ---
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    
    st.divider() # --- Line 1 ---

    st.markdown('<p class="nav-label">Industry News</p>', unsafe_allow_html=True)
    if st.button("🌐 Read Industry Trends", use_container_width=True): 
        st.session_state.menu = "Industry News"

    st.divider() # --- Line 2 ---

    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", 
                          ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")
    
    # Session State Logic
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else: st.session_state.menu = nav_choice

    st.divider() # --- Line 3 ---

    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.caption("👤 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")

    st.divider() # --- Line 4 ---

    st.markdown('<p class="nav-label">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("💰 Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"

    st.divider() # --- Line 5 ---

    st.markdown('<p class="nav-label">System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")
    st.caption("Latency: 115ms")

    st.divider() # --- Line 6 ---

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
        'Category': ['Engagement', 'Conversion', 'Retainment'],
        'Value': [45, 30, 25]
    })

    # Fixed Function with Unique Key to prevent DuplicateElementId
    def display_chart(chart_type, df, unique_key):
        if chart_type == "Bar Chart": 
            st.bar_chart(df, x='Category', y='Value')
        elif chart_type == "Line Chart": 
            st.line_chart(df, x='Category', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Category', hole=0.4, template="plotly_dark")
            fig.update_layout(margin=dict(t=10, b=10, l=10, r=10), height=350)
            # unique_key ကို သုံးပြီး Error ကို ဖြေရှင်းထားပါသည်
            st.plotly_chart(fig, use_container_width=True, key=unique_key)

    with p_tab1: # FB: Reach / Engagement / Followers
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K")
        c2.metric("Engagement", "3.2K")
        c3.metric("Followers", "12,450")
        display_chart(chart_view, mock_data, "fb_chart_key")

    with p_tab2: # TikTok: Total Views / Avg. Watch Time / Profile Visits
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Views", "1.2M")
        c2.metric("Avg. Watch Time", "18s")
        c3.metric("Profile Visits", "4,200")
        display_chart(chart_view, mock_data, "tt_chart_key")

    with p_tab3: # YouTube: CTR / Watch Time / Subscribers
        c1, c2, c3 = st.columns(3)
        c1.metric("CTR", "8.5%")
        c2.metric("Watch Time", "1,240h")
        c3.metric("Subscribers", "8,900")
        display_chart(chart_view, mock_data, "yt_chart_key")

# B. INDUSTRY NEWS
elif st.session_state.menu == "Industry News":
    st.title("🌐 Industry News & Market Trends")
    st.info("AI curated marketing insights for 2026.")
    st.markdown("""
    ### 📈 Meta Algorithm Change
    - Video Reels under 15 seconds are getting **30% more reach** this month.
    
    ### 💎 Jewelry SME Trend
    - Minimalist aesthetics are trending in Southeast Asia.
    """)
    if st.button("← Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"

# C. CREATOR MODE
elif st.session_state.menu == "Creator Mode":
    st.title("💰 Creator Mode")
    st.markdown('<p class="nav-label">Passive Income Streams</p>', unsafe_allow_html=True)
    st.metric("Total Revenue", "$1,250", "+$150")
    if st.button("← Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"

else:
    st.title(st.session_state.menu)
    st.write(f"The {st.session_state.menu} section is ready for development.")
