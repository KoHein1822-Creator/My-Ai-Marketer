import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v150.0",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS (V143 Dashboard + Professional Sidebar) ---
def apply_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Dashboard Styling */
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
        .m-label-v88 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        .header-flex { display: flex; justify-content: space-between
