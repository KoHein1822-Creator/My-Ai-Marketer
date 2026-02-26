import streamlit as st
import pandas as pd

# --- 1. CORE DATA PERSISTENCE (Database Logic) ---
# ဒါက Feature တွေနဲ့ Data တွေ ပျောက်မသွားအောင် ထိန်းထားပေးတဲ့ Database အပိုင်းပါ
if 'bulk_generated' not in st.session_state: st.session_state.bulk_generated = False
if 'leads_list' not in st.session_state:
    st.session_state.leads_list = [
        {"Name": "Ma Thandar", "Phone": "09-4500XXX", "Source": "FB Comment", "Status": "Hot Lead", "Interest": "Diamond Ring"},
        {"Name": "Ko Kyaw Zin", "Phone": "09-7980XXX", "Source": "TikTok Form", "Status": "Interested", "Interest": "Gold Chain"}
    ]
if 'report_data' not in st.session_state: st.session_state.report_data = "ယခုလတွင် Engagement ၃၅% တက်လာပြီး ဝယ်သူအသစ် ၁၅၀ စုဆောင်းနိုင်ခဲ့ပါသည်။"
if 'crisis_alert' not in st.session_state: st.session_state.crisis_alert = True

# --- 2. PAGE CONFIG & ORIGINAL v27.0 UI ---
st.set_page_config(page_title="SAYAR GYI v57.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .visual-preview { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 20px; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v27.0 Original Structure) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Intelligence Control</p>', unsafe_allow_html=True)
    if st.button("🧠 Strategy & Guard Dog", use_container_width=True): st.session_state.menu = "Strategy"
    if st.button("🚨 Monitoring & Spy Center", use_container_width=True): st.session_state.menu = "Monitoring"
    if st.button("📊 Executive Report AI", use_container_width=True): st.session_state.menu = "Report"

    st.divider()
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"
    if st.button("👥 Ethical Lead CRM", use_container_width=True): st.session_state.menu = "Leads"

    st.divider()
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    if 'menu' not in st.session_state: st.session_state.menu = nav_choice
    else:
        if st.session_state.menu in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"]:
            st.session_state.menu = nav_choice

    st.divider()
    st.success("Core Engine: v57.0 (Restored)")

# --- 4. MAIN INTERFACE (All Integrated Sections) ---

# A. STRATEGY & GUARD DOG (Trend + Crisis)
if st.session_state.menu == "Strategy":
    st.markdown('<h1 class="header-blue">🧠 Strategy & Guard Dog</h1>', unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔥 Trend Watch")
        st.warning("Trend: 'Gold Transition' Videos are Viral.")
        st.button("Update Monthly Strategy")
    with col2:
        st.subheader("🛡️ Crisis Control")
        if st.session_state.crisis_alert:
            st.error("Negative Comment Detected!")
            if st.button("Approve Crisis Response"): 
                st.session_state.crisis_alert = False
                st.success("Crisis Handled.")

# B. CONTENT PRODUCTION (Monthly Bulk + Rendering)
elif st.session_state.menu == "Content":
    st.markdown('<h1 style="color:#d3b6ff;">🎬 Content Factory</h1>', unsafe_allow_html=True)
    t1, t2 = st.tabs(["🗓️ Monthly Calendar", "🚀 Bulk Generator"])
    with t2:
        st.subheader("Generate 1-Month Batch")
        if st.button("🚀 Start Multimedia Generation"): st.session_state.bulk_generated = True
    with t1:
        if st.session_state.bulk_generated:
            c1, c2 = st.columns([2, 1])
            with c1: st.write("**Day 1:** Gold Quality Education Video")
            with c2: st.markdown('<div class="visual-preview">📹 AI Rendered Video</div>', unsafe_allow_html=True)
            st.button("✅ Approve 30-Day Batch")
        else: st.info("Bulk Generator ကို အရင်သုံးပေးပါ။")

# C. LEAD CRM (Database)
elif st.session_state.menu == "Leads":
    st.markdown('<h1 style="color:#aff5b4;">👥 Ethical Lead CRM</h1>', unsafe_allow_html=True)
    st.table(pd.DataFrame(st.session_state.leads_list))

# D. EXECUTIVE REPORT AI
elif st.session_state.menu == "Report":
    st.markdown('<h1 style="color:#f2c94c;">📊 Executive AI Report</h1>', unsafe_allow_html=True)
    st.markdown(f"**CEO Summary:** {st.session_state.report_data}")
    st.button("📥 Download Report")

# E. INTERACTIVE DASHBOARD
elif st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    s1, s2, s3 = st.columns(3)
    s1.metric("Autonomy", "98%")
    s2.metric("Response Rate", "100%")
    s3.metric("Monthly Leads", "150")

else: st.title(st.session_state.menu)
