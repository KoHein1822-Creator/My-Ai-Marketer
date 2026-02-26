import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE CONFIG & UI STYLE (v30.0 Standards) ---
st.set_page_config(page_title="SAYAR GYI v31.0", layout="wide")

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

# --- 2. SIDE PANEL (v30.0 Structure) ---
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

# A. INTERACTIVE DASHBOARD (Standard v30.0 Logic)
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    f_cols = st.columns([2, 1, 1])
    with f_cols[0]: time_period = st.segmented_control("Timeframe", ["Weekly", "Monthly", "Yearly"], default="Monthly")
    with f_cols[1]: chart_view = st.selectbox("Visual Filter", ["Bar Chart", "Pie Chart", "Line Chart"])
    st.divider()
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12"); s2.metric("Pending", "5"); s3.metric("Scheduled", "18"); s4.metric("Published", "145")
    st.divider()
    t1, t2, t3 = st.tabs(["Facebook", "TikTok", "YouTube"])
    mock_data = pd.DataFrame({'Category': ['Engagement', 'Conversion', 'Retainment'], 'Value': [45, 30, 25]})

    def display_chart(chart_type, df, unique_key):
        if chart_type == "Bar Chart": st.bar_chart(df, x='Category', y='Value')
        elif chart_type == "Line Chart": st.line_chart(df, x='Category', y='Value')
        else:
            fig = px.pie(df, values='Value', names='Category', hole=0.4, template="plotly_dark")
            st.plotly_chart(fig, use_container_width=True, key=unique_key)
    with t1: display_chart(chart_view, mock_data, "fb_v31")
    with t2: display_chart(chart_view, mock_data, "tt_v31")
    with t3: display_chart(chart_view, mock_data, "yt_v31")

# B. BRAND DNA (LOCALIZED & UPDATED)
elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-green">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    dna_mode = st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)
    st.divider()

    if dna_mode == "Intelligence Mode (AI Research)":
        st.subheader("AI Intelligence Researcher (Myanmar Market Focused)")
        
        # Myanmar Market Industries Selection
        mm_industries = [
            "Jewelry & Gold (ကျောက်မျက်ရတနာနှင့် ရွှေဆိုင်)",
            "F&B / Coffee Shop (စားသောက်ဆိုင်နှင့် ကော်ဖီဆိုင်)",
            "Real Estate (အိမ်ခြံမြေ ဝန်ဆောင်မှု)",
            "Cosmetic & Skincare (အလှကုန်နှင့် အသားအရေထိန်းသိမ်းမှု)",
            "Travel & Tour (ခရီးသွားလာရေး ဝန်ဆောင်မှု)",
            "E-commerce / Retail (အွန်လိုင်းစျေးဆိုင်)",
            "Education / Training (ပညာရေးနှင့် သင်တန်း)",
            "Auto Mobile (မော်တော်ယာဉ် ရောင်းဝယ်ရေး)",
            "Health & Wellness (ကျန်းမာရေးနှင့် အားကစား)",
            "Digital Services / Tech (နည်းပညာနှင့် ဒစ်ဂျစ်တယ်ဝန်ဆောင်မှု)",
            "Other (အခြားလုပ်ငန်း အမျိုးအစား...)"
        ]
        
        selected_industry = st.selectbox("လုပ်ငန်းအမျိုးအစား ရွေးချယ်ပါ", mm_industries)
        
        # Manual Input if "Other" is selected
        final_industry = selected_industry
        if selected_industry == "Other (အခြားလုပ်ငန်း အမျိုးအစား...)":
            final_industry = st.text_input("သင့်လုပ်ငန်း အမျိုးအစားကို စာရိုက်ထည့်ပါ (ဥပမာ - စိုက်ပျိုးရေး)")

        if st.button("Generate Strategic Guideline"):
            with st.spinner(f"{final_industry} အတွက် မြန်မာ့စျေးကွက်အလိုက် Research လုပ်နေပါသည်..."):
                st.success(f"Strategy Generated for {final_industry}! AI Agent က သင့်လုပ်ငန်းအတွက် Tone of Voice နှင့် Audience Persona ကို ခွဲခြမ်းစိတ်ဖြာပြီးပါပြီ။")
    
    else:
        st.subheader("Manual Brand Configuration")
