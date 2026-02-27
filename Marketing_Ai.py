import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v84.0 | Master Command Center",
    page_icon="📊"
)

# --- 2. PREMIUM CSS STYLING ---
def apply_custom_styles():
    st.markdown("""
        <style>
        /* Overall Page Optimization */
        .block-container { padding-top: 1.5rem; max-width: 97%; }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Section Headers */
        .main-header {
            color: #58a6ff; font-size: 14px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 25px; margin-top: 20px;
            border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        /* Status Boxes (Bigger & Bolder) */
        .status-box-master {
            background: #161b22; border: 1px solid #30363d;
            padding: 35px 20px; border-radius: 15px; text-align: center;
            transition: transform 0.3s;
        }
        .status-box-master:hover { border-color: #58a6ff; transform: translateY(-5px); }
        
        /* Metrics Container */
        .metric-container-master {
            background: #161b22; border: 1px solid #30363d;
            padding: 25px; border-radius: 15px; margin-top: 10px;
        }

        /* Sidebar Logo/Title Area */
        .sidebar-brand { font-size: 20px; font-weight: 800; color: white; margin-bottom: 0px; }
        .sidebar-tag { font-size: 11px; color: #58a6ff; text-transform: uppercase; letter-spacing: 1px; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL NAVIGATION ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<p class="sidebar-brand">SAYAR GYI\'S</p>', unsafe_allow_html=True)
        st.markdown('<p class="sidebar-tag">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("### INDUSTRY NEWS")
        if st.button("🌐 Read Industry Trends", use_container_width=True):
            st.toast("Fetching latest marketing trends...")
            
        st.divider()
        st.markdown("### MENU")
        nav = st.radio("Navigate", 
            ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive", "🎨 Asset Library"], 
            label_visibility="collapsed")
        
        st.divider()
        st.markdown("### MY AGENTS")
        st.caption("🤖 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
        
        st.write("")
        if st.button("🔥 Switch to Creator Mode", use_container_width=True):
            st.balloons()
            
        st.divider()
        st.success("Core Engine: Online")
        st.info("Node: SG-AI-MASTER-01")
        
        st.write("")
        st.markdown("### MODEL")
        st.radio("Engine", ["Gemini 1.5 Pro", "GPT-4o", "Claude 3.5"], horizontal=True, label_visibility="collapsed")
        
    return nav

# --- 4. MAIN DASHBOARD ENGINE ---
def render_dashboard_content():
    # --- TOP CONTROL BAR ---
    t_col, c_col = st.columns([1.5, 1])
    with t_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with c_col:
        sub_c1, sub_c2, sub_c3 = st.columns(3)
        with sub_c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with sub_c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with sub_c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    # --- SECTION 1: CONTENT CREATION STATUS ---
    st.markdown('<p class="main-header">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f"""
                <div class="status-box-master">
                    <div style="color:#8b949e; font-size:14px; font-weight:600; text-transform:uppercase;">{label}</div>
                    <div style="font-size:48px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div>
                </div>
            """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- SECTION 2: DEEP INSIGHTS GRID ---
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True
