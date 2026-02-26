import streamlit as st
import pandas as pd

# --- 1. PAGE CONFIG & BRANDING ---
st.set_page_config(page_title="SAYAR GYI v55.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .header-perfection { color: #d4af37; font-weight: 700; text-shadow: 0px 0px 15px rgba(212, 175, 55, 0.6); font-size: 2.5rem; }
    .guard-dog-box { background: rgba(255, 75, 75, 0.1); border: 1px solid #ff4b4b; padding: 20px; border-radius: 12px; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 15px; font-weight: 600; letter-spacing: 1.5px; }
    .stButton>button { border-radius: 8px; font-weight: 600; transition: 0.3s; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (Final Command Structure) ---
with st.sidebar:
    st.markdown("<h1 class='header-perfection'>SAYAR GYI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#d4af37; margin-top:-20px; font-size: 12px;'>v55.0 | PERFECTION EDITION</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Main Controls</p>', unsafe_allow_html=True)
    if st.button("🧠 Strategy & Guard Dog", use_container_width=True): st.session_state.menu = "Strategy"
    if st.button("🎬 Monthly Content Factory", use_container_width=True): st.session_state.menu = "Content"
    if st.button("👥 Ethical Lead CRM", use_container_width=True): st.session_state.menu = "Leads"
    
    st.divider()
    st.markdown('<p class="nav-label">Intelligence</p>', unsafe_allow_html=True)
    if st.button("🚨 Spy & Monitoring", use_container_width=True): st.session_state.menu = "Monitoring"
    if st.button("📊 Executive AI Report", use_container_width=True): st.session_state.menu = "Report"
    
    st.divider()
    st.success("AI Core Status: Fully Autonomous")
    st.info(f"Today: {pd.to_datetime('today').strftime('%d %B %Y')}")

# --- 3. MAIN INTERFACE ---

# A. STRATEGY & GUARD DOG (The v55.0 Addition)
if st.session_state.get('menu') == "Strategy":
    st.markdown('<h1 class="header-perfection">🛡️ Strategy & Guard Dog Control</h1>', unsafe_allow_html=True)
    
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        st.markdown("### ⚠️ Crisis Management (Active)")
        st.markdown("""<div class="guard-dog-box">
        <b style='color:#ff4b4b;'>Critical Alert:</b> Facebook Post #24 တွင် Negative Sentiment တစ်ခု တွေ့ရှိရပါသည်။<br>
        <b>Comment:</b> "ဒီဇိုင်းက ကြည့်ရတာ တစ်မျိုးကြီးပဲ..."<br><br>
        <b>AI Strategy:</b> မချေပပါနှင့်။ Brand ၏ Craftsmanship Video အား Reply တွင် အကျိုးအကြောင်းပြ၍ ပြန်လည်ဖြေရှင်းရန် အကြံပြုပါသည်။
        </div>""", unsafe_allow_html=True)
        if st.button("Execute Crisis Response", use_container_width=True):
            st.success("AI is handling the situation...")

    with g_col2:
        st.markdown("### 🧬 Strategy Optimization")
        st.info("Trend Detected: 'Vibe အသစ်နဲ့ ရွှေဆင်မယ်' Transition Videos are peaking.")
        if st.button("Inject Trend Content into Calendar", use_container_width=True):
            st.balloons()
            st.success("Calendar updated with trending content.")

# B. CONTENT FACTORY (Monthly Autopilot)
elif st.session_state.get('menu') == "Content":
    st.markdown('<h1 class="header-perfection">🎬 Monthly Content Factory</h1>', unsafe_allow_html=True)
    st.write("တစ်လစာ Content (၃၀) ခုလုံးအား AI မှ Multimedia Render လုပ်ပြီးပါပြီ။")
    st.progress(100)
    if st.button("✅ Batch Approve All & Autopilot Start"):
        st.success("System is now running on Autopilot for 30 days!")

# C. MONITORING (The Spy)
elif st.session_state.get('menu') == "Monitoring":
    st.markdown('<h1 class="header-perfection">🚨 Intelligence Monitoring</h1>', unsafe_allow_html=True)
    st.write("ပြိုင်ဘက်များ၏ ဈေးနှုန်းနှင့် လှုပ်ရှားမှုများကို AI မှ ၂၄ နာရီ စောင့်ကြည့်နေပါသည်။")

else:
    st.markdown('<h1 class="header-perfection">Welcome, CEO</h1>', unsafe_allow_html=True)
    st.write("သင်၏ AI Agency သည် အပြည့်အဝ အဆင်သင့်ဖြစ်နေပါပြီ။ ဘယ်ဘက်မှ Menu များကို အသုံးပြု၍ စတင်ခိုင်းစေနိုင်ပါသည်။")
