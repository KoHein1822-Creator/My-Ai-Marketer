import streamlit as st
import numpy as np
import pandas as pd

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v88.0 | Balanced", initial_sidebar_state="expanded")

# --- 2. V88.0 AUTHENTIC STYLES ---
st.markdown("""
    <style>
    /* Main Background */
    .main { background-color: #0d1117; color: #ffffff; }
    
    /* Sidebar Exact Styling */
    [data-testid="stSidebar"] {
        background-color: #0d1117 !important;
        border-right: 1px solid #30363d !important;
    }
    
    /* Typography for Sidebar Headers */
    .sb-label { 
        font-size: 11px; font-weight: 800; color: #8b949e; 
        letter-spacing: 1px; margin-top: 25px; margin-bottom: 5px;
    }
    .sb-sub-label { 
        font-size: 9px; color: #1f6feb; margin-bottom: 20px; 
    }

    /* Metric Cards (Drafting, Pending, etc.) */
    .metric-container {
        background: #161b22; border: 1px solid #30363d; border-radius: 4px;
        padding: 20px; text-align: center; height: 120px;
    }
    
    /* Insight Cards (Views, Interactions, etc.) */
    .insight-card {
        background: #161b22; border: 1px solid #30363d; border-radius: 4px;
        padding: 15px; position: relative; margin-bottom: 5px;
    }

    /* Delta Badge */
    .delta-badge {
        background: rgba(63, 185, 80, 0.1); color: #3fb950;
        font-size: 10px; padding: 2px 6px; border-radius: 3px;
        position: absolute; right: 15px; top: 15px;
    }

    /* Section Headers */
    .section-header {
        color: #58a6ff; font-size: 13px; font-weight: bold;
        border-left: 3px solid #1f6feb; padding-left: 10px;
        margin: 25px 0 15px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (V88.0 ORIGINAL) ---
with st.sidebar:
    st.markdown('<p class="sb-label">SAYAR GYI\'S</p>', unsafe_allow_html=True)
    st.markdown('<p class="sb-sub-label">AI MARKETING AGENCY</p>', unsafe_allow_html=True)
    
    st.markdown('<p class="sb-label">INDUSTRY NEWS</p>', unsafe_allow_html=True)
    st.button("🌐 Read Industry Trends", use_container_width=True)
    
    st.markdown('<p class="sb-label">MENU</p>', unsafe_allow_html=True)
    st.button("📊 Interactive Dashboard", use_container_width=True)
    st.button("🧬 Brand DNA", use_container_width=True)
    st.button("📂 Project Archive", use_container_width=True)
    st.button("📚 Asset Library", use_container_width=True)
    
    st.markdown('<p class="sb-label">MY AGENTS</p>', unsafe_allow_html=True)
    st.caption("🤖 Intel | 🎨 Creative | 📈 Auditor")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.button("🔥 Switch to Creator Mode", use_container_width=True)
    
    st.markdown('<div style="background:#161b22; padding:10px; border-radius:4px; border:1px solid #30363d; margin-top:20px;">'
                '<p style="color:#3fb950; font-size:12px; margin:0;">Core Engine: Online</p></div>', unsafe_allow_html=True)
    
    st.markdown('<p class="sb-label">MODEL</p>', unsafe_allow_html=True)
    st.caption("● Gemini 1.5 Pro | ● GPT-4o")

# --- 4. MAIN DASHBOARD (V88.0 ORIGINAL) ---
st.title("Strategic Dashboard")

# Top Metrics Row
st.markdown('<p class="section-header">CONTENT CREATION STATUS</p>', unsafe_allow_html=True)
c1, c2, c3, c4 = st.columns(4)
metrics_top = [("DRAFTING", "12"), ("PENDING", "5"), ("SCHEDULED", "18"), ("PUBLISHED", "145")]
for i, col in enumerate([c1, c2, c3, c4]):
    label, val = metrics_top[i]
    col.markdown(f'<div class="metric-container"><p style="color:#8b949e; font-size:11px;">{label}</p><h2>{val}</h2></div>', unsafe_allow_html=True)

# Facebook Insights 6-Grid
st.markdown('<p class="section-header">FACEBOOK DEEP INSIGHTS & TRENDS</p>', unsafe_allow_html=True)
insights_data = [
    ("VIEWS", "85.2K", "+12%"), ("INTERACTIONS", "3.2K", "+8%"), ("FOLLOWERS", "12.4K", "+1%"),
    ("PAGE VISITS", "4.5K", "+15%"), ("LINK CLICKS", "920", "+22%"), ("CONVERSATIONS", "128", "+5%")
]

for row_idx in range(2):
    cols = st.columns(3)
    for col_idx in range(3):
        idx = row_idx * 3 + col_idx
        l, v, d = insights_data[idx]
        with cols[col_idx]:
            st.markdown(f'''
                <div class="insight-card">
                    <span class="delta-badge">{d}</span>
                    <p style="color:#8b949e; font-size:11px; margin:0;">{l}</p>
                    <h3 style="margin:0;">{v}</h3>
                </div>
            ''', unsafe_allow_html=True)
            st.line_chart(np.random.randn(20), height=90, use_container_width=True)
