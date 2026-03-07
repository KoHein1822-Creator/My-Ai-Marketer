import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Momentum AI Command Center", layout="wide")

# --- CUSTOM CSS (Momentum Branding Inspiration) ---
st.markdown("""
    <style>
    /* Main Background & Font */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
        background-color: #0F111A; /* Deep Dark Background */
        color: #E0E0E0;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }
    
    /* Card/Module Styling */
    div[data-testid="stMetric"] {
        background-color: #1C2128;
        border: 1px solid #30363D;
        padding: 20px;
        border-radius: 16px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }
    
    /* Button Styling */
    .stButton>button {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%);
        color: white;
        border: none;
        border-radius: 12px;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover {
        opacity: 0.8;
        transform: translateY(-2px);
    }
    
    /* Container Box Styling */
    .element-container img {
        border-radius: 12px;
    }
    
    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px 4px 0 0;
        gap: 1px;
        padding-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (Momentum Style) ---
with st.sidebar:
    st.markdown("<h2 style='color: #4F46E5;'>MOMENTUM AI</h2>", unsafe_allow_html=True)
    st.divider()
    client = st.selectbox("Client Workspace", ["More & More Jewelry", "ANP Media", "Personal Brand"])
    st.caption("Strategic Mode")
    mode = st.radio("System Focus", ["Growth", "Efficiency", "Creative"], label_visibility="collapsed")
    
    st.divider()
    with st.expander("System Configuration"):
        st.write("Engine: Gemini 1.5 Pro")
        st.slider("Creativity Temp", 0.0, 1.0, 0.7)

# --- MAIN INTERFACE ---
# Header Row
head_col1, head_col2 = st.columns([3, 1])
with head_col1:
    st.title(f"Control Center : {client}")
    st.write(f"Active Campaign: {mode} Optimization")

# 1. TREND ANALYSIS (Momentum Metrics Card)
st.markdown("### 📈 Real-time Market Intel")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Viral Score", "88%", "+5%")
m2.metric("Trend Velocity", "High", "Jewelry")
m3.metric("Engagement Prediction", "4.2k", "avg/post")
m4.metric("Ad Spend Efficiency", "1.2x", "optimal")

# 2. THE GENERATIVE ENGINE (Inspired Layout)
st.divider()
col_left, col_right = st.columns([1.6, 1])

with col_left:
    st.markdown("#### 🛠️ Strategy & Generation")
    with st.container(border=True):
        industry = st.selectbox("Industry Playbook", ["Luxury Jewelry", "SME E-commerce", "Digital Service"])
        brief = st.text_area("What are we building today?", placeholder="Describe your marketing objective...")
        
        c1, c2 = st.columns(2)
        with c1: st.button("Generate Master Copy")
        with c2: st.button("Generate Visual Prompts")

with col_right:
    st.markdown("#### 🎯 Personalization Layer")
    st.multiselect("Audience Persona", ["New Leads", "VIP Customers", "Gen-Z Shoppers"], default=["New Leads"])
    st.select_slider("Tone Depth", ["Casual", "Warm", "Luxury", "Authority"])
    st.button("✨ Refine for Personas")

# 3. CONTENT PREVIEW HUB
st.divider()
st.markdown("### 🎬 Production Preview")
preview_tabs = st.tabs(["[ Facebook ]", "[ TikTok ]", "[ Instagram ]", "[ Email ]"])

with preview_tabs[0]:
    col_pre_text, col_pre_img = st.columns([1, 1])
    with col_pre_text:
        st.text_area("Generated Copy", "More & More Jewelry အတွက် အမိုက်စား စာသားများ ဤနေရာတွင် ပေါ်လာပါမည်...", height=300)
    with col_pre_img:
        st.image("https://via.placeholder.com/600x600/161B22/E0E0E0?text=AI+Visual+Draft", use_container_width=True)

# 4. ACTION BAR (Bottom Floating Style)
st.divider()
st.markdown("#### 🚀 Execution & Monitoring")
a1, a2, a3, a4 = st.columns(4)
with a1: st.button("✅ Approve & Schedule")
with a2: st.button("📝 Manual Edit")
with a3: st.button("🔄 Regenerate")
with a4: st.button("🗑️ Archive")

# Performance Preview (Mini Chart)
chart_data = pd.DataFrame(np.random.randn(15, 2), columns=['Reach', 'Conversions'])
st.line_chart(chart_data, height=150)
