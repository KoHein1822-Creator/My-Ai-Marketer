import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE CONFIG & UI ---
st.set_page_config(page_title="SAYAR GYI v35.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .header-purple { color: #d3b6ff; font-weight: 600; }
    .preview-box { background: #0d1117; border: 1px solid #30363d; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL MEMORY ---
if 'brand_data' not in st.session_state: st.session_state.brand_data = None

# --- 3. SIDE PANEL (v27.0 Structure Unchanged) ---
with st.sidebar:
    st.markdown("<h2 style='margin-bottom:0;'>Sayar Gyi 's</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content Production"
    st.divider()
    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else: 
        if st.session_state.menu in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"]:
            st.session_state.menu = nav_choice
    st.divider()
    st.success("Core Engine: Online")
    brain_choice = st.segmented_control("Model", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 4. MAIN INTERFACE ---

# A. CONTENT PRODUCTION (With Preview, Approve, Reject, Remark)
if st.session_state.menu == "Content Production":
    st.markdown('<h1 class="header-purple">Content Production & Approval</h1>', unsafe_allow_html=True)
    
    if st.session_state.brand_data is None:
        st.warning("⚠️ Brand DNA မရှိသေးပါ။ Brand DNA Section မှာ အရင် Generate လုပ်ပေးပါ။")
    else:
        tab1, tab2 = st.tabs(["Production Engine", "Review & Publisher"])
        
        with tab1:
            st.subheader("Generate New Content")
            st.button("AI Generate Multi-Channel Scripts")
            
        with tab2:
            st.markdown('<p class="nav-label">Multi-Channel Preview</p>', unsafe_allow_html=True)
            
            # Simulated Multi-Channel Preview
            col_p1, col_p2, col_p3 = st.columns(3)
            with col_p1:
                st.markdown("**📱 TikTok Preview**")
                st.markdown('<div class="preview-box"><i>Video Hook:</i> "ရွှေဝယ်တော့မယ်ဆို ဒါကိုသတိထား..."<br><small>Duration: 15s</small></div>', unsafe_allow_html=True)
            with col_p2:
                st.markdown("**🔵 Facebook Preview**")
                st.markdown('<div class="preview-box"><i>Caption:</i> "ရွှေချစ်သူတို့အတွက် အထူးသတင်းကောင်း..."<br><small>Visual: Static Image</small></div>', unsafe_allow_html=True)
            with col_p3:
                st.markdown("**🔴 YouTube Preview**")
                st.markdown('<div class="preview-box"><i>Title:</i> "How to Choose Quality Jewelry"<br><small>Format: Shorts</small></div>', unsafe_allow_html=True)

            st.divider()
            
            # Sayar Gyi's Command Center (Approval & Remark)
            st.markdown('<p class="nav-label">Sayar Gyi\'s Decision Center</p>', unsafe_allow_html=True)
            remark = st.text_area("Sayar Gyi's Remark (မှတ်ချက်ပေးရန်)", placeholder="ဥပမာ - စာသားနည်းနည်းပြင်ပါ၊ Background သီချင်းပြောင်းပါ...")
            
            c_btn1, c_btn2, c_btn3 = st.columns([1, 1, 4])
            with c_btn1:
                if st.button("✅ Approve & Publish", use_container_width=True): st.success("Published to all channels!")
            with c_btn2:
                if st.button("❌ Reject", use_container_width=True): st.error("Content Rejected.")
            with c_btn3:
                if st.button("📝 Save Changes & Edit"): st.info("Draft Saved.")

# B. INTERACTIVE DASHBOARD (With Monitoring Update)
elif st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard & Live Monitoring</h1>', unsafe_allow_html=True)
    
    # Live Monitoring Status (New Addition)
    st.markdown('<p class="nav-label">Live Activity Feed</p>', unsafe_allow_html=True)
    st.caption("🟢 Live: TikTok Video 'How to...' is trending (+500 views/hr) | 🔵 Status: FB Ad Campaign Active")
    
    st.divider()
    # Traditional v27.0 Monitoring Metrics
    f_cols = st.columns([2, 1, 1])
    with f_cols[1]: chart_view = st.selectbox("Visual Filter", ["Bar Chart", "Pie Chart", "Line Chart"])
    
    st.divider()
    s1, s2, s3, s4 = st.columns(4)
    s1.metric("Drafting", "12"); s2.metric("Pending Approval", "5", delta="-2"); s3.metric("Scheduled", "18"); s4.metric("Published", "145")
    st.divider()
    t1, t2, t3 = st.tabs(["Facebook Insights", "TikTok Performance", "YouTube Metrics"])
    # (Metrics logic as before)
    with t1: st.metric("Reach", "45.2K", "+12%")

else: st.title(st.session_state.menu)
