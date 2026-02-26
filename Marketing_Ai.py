import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- 1. PAGE CONFIG & UI ---
st.set_page_config(page_title="SAYAR GYI v34.0", layout="wide")

# (CSS မူလအတိုင်း ထိန်းသိမ်းထားပါသည်)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 10px; border-radius: 8px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .header-green { color: #aff5b4; font-weight: 600; }
    .header-purple { color: #d3b6ff; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL MEMORY INITIALIZATION ---
if 'brand_data' not in st.session_state:
    st.session_state.brand_data = None # Brand DNA သိမ်းမည့်နေရာ

# --- 3. SIDE PANEL (v27.0 Structure) ---
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

# --- 4. MAIN INTERFACE LOGIC ---

# A. BRAND DNA (Data Provider)
if st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-green">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    
    dna_mode = st.radio("Mode", ["Intelligence Mode (AI Research)", "Manual Mode"], horizontal=True)
    
    if dna_mode == "Intelligence Mode (AI Research)":
        industry = st.selectbox("လုပ်ငန်းအမျိုးအစား", ["Jewelry", "F&B", "Real Estate", "Tech", "Other"])
        if st.button("Generate & Sync Strategy"):
            # AI က Data ထုတ်ပေးပြီး Memory ထဲ သိမ်းလိုက်ခြင်း
            st.session_state.brand_data = {
                "industry": industry,
                "tone": "Elegant & Premium" if industry == "Jewelry" else "Professional",
                "target": "Middle to High Income Class",
                "usp": f"High quality {industry} services in Myanmar"
            }
            st.success(f"✅ {industry} Strategy ကို Generate လုပ်ပြီး Content Production ဆီ ချိတ်ဆက်ပေးလိုက်ပါပြီ!")
    
    else: # Manual Mode
        name = st.text_input("Brand Name")
        tone = st.selectbox("Tone", ["Professional", "Witty", "Friendly"])
        if st.button("Save & Sync"):
            st.session_state.brand_data = {"industry": "Manual Input", "tone": tone, "target": "Custom", "usp": "Custom USP"}
            st.success("✅ Manual Data ကို Sync လုပ်ပြီးပါပြီ!")

# B. CONTENT PRODUCTION (Data Consumer)
elif st.session_state.menu == "Content Production":
    st.markdown('<h1 class="header-purple">Automated Content Production</h1>', unsafe_allow_html=True)

    # ချိတ်ဆက်မှု ရှိမရှိ စစ်ဆေးခြင်း
    if st.session_state.brand_data is None:
        st.warning("⚠️ Brand DNA မရှိသေးပါ။ ကျေးဇူးပြု၍ Brand DNA Section မှာ အရင် Generate လုပ်ပေးပါ။")
    else:
        st.info(f"🧬 Linked to Brand DNA: **{st.session_state.brand_data['industry']}** ({st.session_state.brand_data['tone']} Tone)")
        
        tab1, tab2 = st.tabs(["AI Script Generator", "Asset Sync"])
        with tab1:
            st.subheader("AI Content Scripting")
            # Brand DNA ထဲက Data ကို ယူသုံးခြင်း
            brand_tone = st.session_state.brand_data['tone']
            if st.button("Generate Script based on Brand DNA"):
                st.markdown(f"**Target:** {st.session_state.brand_data['target']}")
                st.code(f"Hook: {st.session_state.brand_data['industry']} နဲ့ ပတ်သက်ပြီး ဒါကို သိပြီးပြီလား?\nTone: {brand_tone}\nCTA: Follow us for more!")

# C. INTERACTIVE DASHBOARD (v27.0 Logic ထိန်းသိမ်းထားဆဲ)
elif st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    # (Dashboard code အရင်အတိုင်း)
    st.metric("Total Published", "145", "+12")

else:
    st.title(st.session_state.menu)
