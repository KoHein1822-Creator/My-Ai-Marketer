import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE CONFIG & UI STYLE (v27.0 Based) ---
st.set_page_config(page_title="SAYAR GYI v30.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .header-green { color: #aff5b4; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (v27.0 Structure) ---
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Industry News</p>', unsafe_allow_html=True)
    if st.button("🌐 Read Industry Trends", use_container_width=True): 
        st.session_state.menu = "Industry News"

    st.divider()

    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else: st.session_state.menu = nav_choice

    st.divider()
    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.caption("👤 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
    st.divider()

    st.markdown('<p class="nav-label">Creator Mode</p>', unsafe_allow_html=True)
    if st.button("💰 Switch to Creator Mode", use_container_width=True):
        st.session_state.menu = "Creator Mode"

    st.divider()
    st.success("Core Engine: Online")
    brain_choice = st.segmented_control("Model", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN INTERFACE LOGIC ---

# A. INTERACTIVE DASHBOARD (v27.0 Logic)
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    f_cols = st.columns([2, 1, 1])
    with f_cols[0]:
        time_period = st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with f_cols[1]:
        chart_view = st.selectbox("Visual Filter", ["Bar Chart", "Pie Chart", "Line Chart"])
    
    st.divider()
    st.markdown('<p class="nav-label">Content Creation Status</p>', unsafe_allow_html=True)
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12")
    s2.metric("Pending", "5")
    s3.metric("Scheduled", "18")
    s4.metric("Published", "145")
    
    st.divider()
    st.markdown('<p class="nav-label">Platform Metrics</p>', unsafe_allow_html=True)
    t1, t2, t3 = st.tabs(["Facebook", "TikTok", "YouTube"])
    mock_data = pd.DataFrame({'Category': ['Engagement', 'Conversion', 'Retainment'], 'Value': [45, 30, 25]})

    def display_chart(chart_type, df, unique_key):
        if chart_type == "Bar Chart": st.bar_chart(df, x='Category', y='Value')
        elif chart_type == "Line Chart": st.line_chart(df, x='Category', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Category', hole=0.4, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True, key=unique_key)

    with t1:
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K"); c2.metric("Engagement", "3.2K"); c3.metric("Followers", "12.4K")
        display_chart(chart_view, mock_data, "fb_v30")
    with t2:
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Views", "1.2M"); c2.metric("Avg Watch Time", "18s"); c3.metric("Profile Visits", "4.2K")
        display_chart(chart_view, mock_data, "tt_v30")
    with t3:
        c1, c2, c3 = st.columns(3)
        c1.metric("CTR", "8.5%"); c2.metric("Watch Time", "1.2K h"); c3.metric("Subscribers", "8.9K")
        display_chart(chart_view, mock_data, "yt_v30")

# B. BRAND DNA (NEW FEATURE)
elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-green">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    
    dna_mode = st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)
    st.divider()

    if dna_mode == "Intelligence Mode (AI Research)":
        st.subheader("AI Intelligence Researcher")
        industry = st.text_input("လုပ်ငန်းအမျိုးအစား ထည့်သွင်းပါ (ဥပမာ - Jewelry, Coffee Shop, Tech)")
        if st.button("Generate Brand Guideline"):
            with st.spinner("AI Agent က Market Research လုပ်နေပါသည်..."):
                st.info(f"{industry} လုပ်ငန်းအတွက် Brand Voice, Audience Persona နှင့် Strategy Guideline ကို AI က ရေးဆွဲပေးနေပါသည်...")
    
    else:
        st.subheader("Manual Brand Configuration")
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.text_input("Brand Name")
            st.text_area("Brand Mission")
            st.selectbox("Brand Tone", ["Professional", "Witty", "Elegant", "Friendly"])
        with col_m2:
            st.text_input("Target Audience")
            st.text_area("Unique Selling Point (USP)")
            st.file_uploader("Upload Existing Brand Guideline (PDF/DOC)", type=["pdf", "docx"])
        st.button("Save Brand DNA")

# C. PROJECT ARCHIVE (NEW FEATURE)
elif st.session_state.menu == "Project Archive":
    st.markdown('<h1 class="header-blue">Project Archive Database</h1>', unsafe_allow_html=True)
    
    # Client Project Database Table
    project_data = {
        "Client Name": ["Diamond Star", "Zen Coffee", "Tech Solutions", "Sky High Real Estate"],
        "Status": ["Completed", "Active", "Pending", "Completed"],
        "Start Date": ["2025-01-10", "2025-02-01", "2025-02-15", "2024-12-20"],
        "Budget": ["$2,500", "$1,200", "$4,000", "$3,500"]
    }
    df_projects = pd.DataFrame(project_data)
    
    st.subheader("Client Project Database")
    st.dataframe(df_projects, use_container_width=True)
    
    st.divider()
    st.markdown('<p class="nav-label">Add New Project</p>', unsafe_allow_html=True)
    with st.expander("Register New Project"):
        st.text_input("Client Name")
        st.date_input("Start Date")
        st.selectbox("Status", ["Active", "Completed", "Pending"])
        st.number_input("Budget ($)")
        st.button("Save to Archive")

# OTHER SECTIONS
elif st.session_state.menu == "Industry News":
    st.title("Industry News")
    if st.button("Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"
elif st.session_state.menu == "Creator Mode":
    st.title("Creator Mode")
    if st.button("Back to Dashboard"): st.session_state.menu = "Interactive Dashboard"
else:
    st.title(st.session_state.menu)
