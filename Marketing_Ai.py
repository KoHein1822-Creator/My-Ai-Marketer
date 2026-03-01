import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v149.0 | Integrated Side Panel",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS (FOR CLEAN ICON BUTTONS) ---
def apply_all_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Dashboard Label & Values (V143 Style) */
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 15px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }
        .status-box-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 30px 15px; border-radius: 12px; text-align: center;
        }
        .insight-card-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 22px; border-radius: 15px; margin-bottom: 15px;
        }

        /* Stable Sidebar Labels */
        .sb-label { font-size: 12px; color: #8b949e; font-weight: 600; text-transform: uppercase; margin-top: 25px; margin-bottom: 8px;}

        /* Icon Button Style (V149 - Requested) */
        .icon-btn-container {
            display: flex; flex-direction: column; gap: 8px; margin-bottom: 15px;
        }
        .icon-btn {
            background: #161b22; border: 1px solid #30363d; border-radius: 8px;
            padding: 10px 15px; color: #adbac7; font-size: 14px; text-align: left;
            display: flex; align-items: center; gap: 10px; cursor: pointer; text-decoration: none;
        }
        .icon-btn:hover { background: #21262d; border-color: #58a6ff; color: #ffffff; }
        .icon-btn.active { background: #1f6feb; border-color: #58a6ff; color: #ffffff; }
        .icon-btn i { font-size: 16px; }

        /* Report Paper Style (V100/101) */
        .report-paper {
            background: #ffffff; color: #1e293b; padding: 50px; border-radius: 4px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4); line-height: 1.8; font-family: 'Pyidaungsu', serif;
            margin-top: 20px;
        }

        /* Common Labels */
        .m-label-v88 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        .header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }
        </style>
        
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

# --- 3. STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = "Interactive Dashboard"

# --- 4. NAVIGATION (STABLE LOGIC WITH ICON BUTTONS) ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px; margin-bottom: 10px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        
        # model selection text
        st.write("Model: Gemini 1.5 Pro & GPT-4o", font_size=10, color='#8b949e')
        st.markdown('<div style="background:#161b22; padding:8px; border-radius:8px; border:1px solid #30363d; color:#ffffff; font-size:12px; margin-bottom: 20px;">'
                    '<i class="fa fa-link" style="color:#58a6ff; margin-right:8px;"></i>Sayar Gyi\'s Intelligence</div>', unsafe_allow_html=True) # Sayar Gyi's Intelligence

        st.markdown('<div class="sb-label">MENU</div>', unsafe_allow_html=True)
        
        # Deep Insights button
        st.markdown('<div style="background:#1f6feb; padding:8px 15px; border-radius:8px; color:white; font-size:12px; font-weight:bold; margin-bottom:15px; cursor:pointer; text-align:left;">'
                    '<i class="fa fa-chart-line" style="margin-right:8px;"></i>Deep Insights</div>', unsafe_allow_html=True) # Deep Insights

        # Clickable Icon Buttons (V149 - Requested style from V26)
        pages_and_icons = {
            "📊 Interactive Dashboard": "fa fa-tachometer-alt", # dashboard icon
            "🧬 Brand DNA": "fa fa-dna", # brand icon
            "📂 Project Archive": "fa fa-folder-open", # project icon
            "📚 Asset Library": "fa fa-book" # library icon
        }
        
        for page_name, icon_class in pages_and_icons.items():
            is_active = "active" if st.session_state.page == page_name else ""
            st.markdown(f'''
                <a class="icon-btn {is_active}" href="#" id="{page_name.replace(" ", "_")}" onclick="stSessionSetPage('{page_name}')">
                    <i class="{icon_class}"></i>{page_name.split(' ', 1)[1]}
                </a>
            ''', unsafe_allow_html=True) # button labels
        
        st.divider()
        # fire icon
        st.markdown('<button style="background:#ff5722; border:none; border-radius:8px; padding:10px 15px; color:white; width:100%; text-align:left;">'
                    '<i class="fa fa-fire" style="margin-right:10px;"></i>Switch to Creator Mode</button>', unsafe_allow_html=True) # Switch to Creator Mode
        
        st.markdown('<div class="sb-label">System Status</div>', unsafe_allow_html=True) # System Status
        st.success("Core Engine: Online") # status box

# ... [rest of the modules and main execution stay the same as V143 logic, just render based on page] ...
