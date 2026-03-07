import streamlit as st
import pandas as pd
import numpy as np

# Page Config
st.set_page_config(page_title="Momentum AI Command Center", layout="wide", initial_sidebar_state="expanded")

# --- REFINED CUSTOM CSS ---
st.markdown("""
    <style>
    /* Main Backgrounds */
    .stApp { background-color: #0B0F19; }
    
    /* Typography */
    h1, h2, h3, h4, p, span { font-family: 'Inter', sans-serif !important; color: #E2E8F0 !important; }
    
    /* Metrics Card Style */
    div[data-testid="stMetric"] {
        background-color: #1A1F2B;
        border: 1px solid #2D3748;
        border-radius: 12px;
        padding: 15px 20px;
    }
    
    /* Fix Button Styling (No more ugly full-width) */
    .stButton>button {
        background-color: #4F46E5;
        color: white !important;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: 500;
        transition: all 0.2s ease-in-out;
    }
    .stButton>button:hover {
        background-color: #4338CA;
        box-shadow: 0 0 10px rgba(79, 70, 229, 0.4);
    }
    
    /* Outline Button for Secondary Actions */
    .stButton>button[kind="secondary"] {
        background-color: transparent;
        border: 1px solid #4F46E5;
        color: #4F46E5 !important;
    }
    
    /* Inputs & Selectboxes */
    .stTextInput>div>div>input, .stSelectbox>div>div>div, .stTextArea>div>div>textarea {
        background-color: #1A1F2B !important;
        color: white !important;
        border: 1px solid #2D3748 !important;
        border-radius: 6px;
    }
    
    /* Custom Container Borders */
    div[data-testid="stVerticalBlock"] > div[style*="border"] {
        border-color: #2D3748 !important;
        border-radius: 12px !important;
        background-color: #121620 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("<h3 style='color: #4F46E5;'>✦ MOMENTUM AI</h3>", unsafe_allow_html=True)
    st.write("---")
    client = st.selectbox("Client Workspace", ["More & More Jewelry", "ANP Media", "Personal Brand"])
    mode = st.radio("System Focus", ["Growth", "Efficiency", "Creative"])
    st.write("---")
    st.caption("Settings")
    st.slider("AI Creativity", 0.0, 1.0, 0.7)

# --- MAIN INTERFACE ---
st.markdown(f"<h2>Control Center : {client}</h2>", unsafe_allow_html=True)
st.caption(f"Active Campaign: {mode} Optimization")
st.write("")

# 1. TREND ANALYSIS
st.markdown("#### 📊 Real-time Market Intel")
m1, m2, m3, m4 = st.columns(4)
m1.metric("Viral Score", "88%", "+5%")
m2.metric("Trend Velocity", "High", "Jewelry")
m3.metric("Engagement Prediction", "4.2k", "avg/post")
m4.metric("Ad Spend Efficiency", "1.2x", "optimal")

st.write("---")

# 2. STRATEGY & GENERATION
col_left, col_right = st.columns([1.5, 1], gap="large")

with col_left:
    st.markdown("#### 🛠️ Strategy & Generation")
    with st.container(border=True):
        industry = st.selectbox("Industry Playbook", ["Luxury Jewelry", "SME E-commerce", "Digital Service"])
        brief = st.text_area("Campaign Brief", placeholder="Describe your marketing objective here...", height=100)
        
        # Fixed Button Alignment
        bc1, bc2 = st.columns([1, 1])
        with bc1: 
            st.button("✨ Generate Master Copy", type="primary", use_container_width=True)
        with bc2: 
            st.button("🖼️ Generate Visuals", use_container_width=True)

with col_right:
    st.markdown("#### 🎯 Personalization Layer")
    with st.container(border=True):
        st.multiselect("Audience Persona", ["New Leads", "VIP Customers", "Gen-Z Shoppers"], default=["New Leads"])
        st.select_slider("Tone Depth", ["Casual", "Warm", "Luxury", "Authority"])
        st.write("")
        st.button("Refine for Personas", use_container_width=True)

st.write("---")

# 3. CONTENT PREVIEW HUB
st.markdown("#### 🎬 Production Preview")
preview_tabs = st.tabs(["Facebook", "TikTok", "Instagram", "Email"])

with preview_tabs[0]:
    p_col1, p_col2 = st.columns([1.2, 1])
    with p_col1:
        st.text_area("Generated Copy (Editable)", "Draft content will appear here...", height=250)
        # Action Buttons aligned neatly
        ac1, ac2, ac3 = st.columns(3)
        with ac1: st.button("✅ Approve", type="primary", use_container_width=True)
        with ac2: st.button("🔄 Redraft", use_container_width=True)
        with ac3: st.button("🗑️ Discard", use_container_width=True)
    with p_col2:
        st.image("https://via.placeholder.com/600x400/1A1F2B/E2E8F0?text=Visual+Preview", use_container_width=True)
