import streamlit as st
import sqlite3
from datetime import datetime
import time

# --- 1. CORE ENGINE & PERSISTENCE ---
def init_db():
    conn = sqlite3.connect('sayargyi_enterprise.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS project_logs 
                 (id INTEGER PRIMARY KEY, timestamp TEXT, client_name TEXT, 
                  content_body TEXT, strategy_used TEXT, status TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- 2. V14.0 LUXURY DESIGN STANDARDS ---
st.set_page_config(page_title="SAYAR GYI | ENTERPRISE COMMAND", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    
    .metric-card { 
        background: linear-gradient(145deg, #0d1117, #161b22); padding: 20px; border-radius: 12px; 
        border: 1px solid #30363d; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .sub-label { font-size: 11px; text-transform: uppercase; color: #8b949e; letter-spacing: 1px; font-weight: 600; }
    .status-pulse { height: 8px; width: 8px; background-color: #238636; border-radius: 50%; display: inline-block; margin-right: 5px; animation: pulse 2s infinite; }
    @keyframes pulse { 0% { box-shadow: 0 0 0 0 rgba(35, 134, 54, 0.7); } 70% { box-shadow: 0 0 0 10px rgba(35, 134, 54, 0); } 100% { box-shadow: 0 0 0 0 rgba(35, 134, 54, 0); } }
    
    .stButton>button { 
        background: #21262d !important; border: 1px solid #30363d !important; color: #c9d1d9 !important; 
        border-radius: 6px !important; transition: all 0.3s ease; width: 100%;
    }
    .stButton>button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR (MULTI-ACCOUNT NAVIGATION) ---
with st.sidebar:
    st.markdown("<h2 style='letter-spacing: -1px;'>SAYAR GYI <span style='color:#58a6ff; font-size:12px;'>v15.5</span></h2>", unsafe_allow_html=True)
    st.caption("Enterprise AI Command Center")
    st.divider()
    
    # [NEW] Multi-Account Selection
    st.markdown("<p class='sub-label'>Account Management</p>", unsafe_allow_html=True)
    client_list = ["SME Jewelry Shop", "Digital Marketing Academy", "Real Estate Enterprise"]
    selected_client = st.selectbox("Active Account", client_list, label_visibility="collapsed")
    
    st.divider()
    nav = st.radio("NAVIGATION", ["Dashboard", "Asset Library", "Project Archive"])
    
    st.divider()
    st.markdown("<p class='sub-label'>System Status</p>", unsafe_allow_html=True)
    st.markdown(f"<span class='status-pulse'></span> <span style='font-size:12px;'>Monitoring {selected_client}</span>", unsafe_allow_html=True)

# --- 4. MAIN INTERFACE (V14.0 STYLE) ---
if nav == "Dashboard":
    st.markdown(f"<h2 style='margin-bottom:0;'>{selected_client}</h2>", unsafe_allow_html=True)
    st.caption(f"Strategic Hub for {selected_client} Management")
    
    # --- ROW 1: REAL-TIME ADAPTIVE MONITORS ---
    st.markdown("<p class='sub-label' style='margin-top:20px;'>Operational Metrics</p>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    
    with m1:
        # Dynamic Metric Labeling based on Client
        ops_label = "Seats Remaining" if "Academy" in selected_client else "Inventory Level"
        ops_value = "2 / 30" if "Academy" in selected_client else "High"
        st.markdown(f'<div class="metric-card"><p class="sub-label">{ops_label}</p><h3 style="margin:0;">{ops_value}</h3><p style="font-size:12px; color:#3fb950;">Live Sync</p></div>', unsafe_allow_html=True)
    with m2:
        st.markdown('<div class="metric-card"><p class="sub-label">Market Pulse</p><h3 style="margin:0;">Andromeda</h3><p style="font-size:12px; color:#3fb950;">Optimized</p></div>', unsafe_allow_html=True)
    with m3:
        st.markdown('<div class="metric-card"><p class="sub-label">Campaign Reach</p><h3 style="margin:0;">+18.4%</h3><p style="font-size:12px; color:#3fb950;">Active Growth</p></div>', unsafe_allow_html=True)
    with m4:
        st.markdown('<div class="metric-card"><p class="sub-label">Tasks</p><h3 style="margin:0;">02</h3><p style="font-size:12px; color:#d29922;">Pending Approval</p></div>', unsafe_allow_html=True)

    st.divider()

    # --- ROW 2: STRATEGIC GENERATION ENGINE ---
    col_config, col_preview = st.columns([1, 1.8], gap="large")
    
    with col_config:
        st.markdown("<p class='sub-label'>Mission Configuration</p>", unsafe_allow_html=True)
        with st.container(border=True):
            mission_topic = st.text_input("Campaign Topic", placeholder="Enter product or event name")
            st.selectbox("Strategy Logic", ["Urgent (Scarcity)", "Educational", "Brand Awareness"])
            st.divider()
            if st.button("EXECUTE MISSION"):
                with st.spinner("Sayar Gyi is thinking..."):
                    time.sleep(1.5)
                    st.session_state['ready'] = True

    with col_preview:
        st.markdown("<p class='sub-label'>Strategic Output Preview</p>", unsafe_allow_html=True)
        if st.session_state.get('ready'):
            t1, t2, t3 = st.tabs(["Draft Content", "Strategic Insights", "Visual Direction"])
            with t1:
                st.markdown("### Social Media Architecture")
                st.info(f"Campaign generated specifically for {selected_client} using Scarcity Logic.")
                if st.button("✅ Approve & Launch to Vault"):
                    st.toast(f"Data for {selected_client} archived.")
            with t2:
                st.write(f"Insight: Target audience for {selected_client} shows 35% higher engagement on professional hooks.")
            with t3:
                st.image("https://via.placeholder.com/600x250/161b22/58a6ff?text=AI+Recommended+Visual", use_container_width=True)
        else:
            st.markdown("<div style='height:300px; display:flex; align-items:center; justify-content:center; border: 1px dashed #30363d; border-radius:12px; color:#484f58;'>System Idle. Select a client and execute mission.</div>", unsafe_allow_html=True)

elif nav == "Project Archive":
    st.title(f"Archive: {selected_client}")
    st.write(f"Displaying historical records for **{selected_client}** only.")
    # Archive filtering logic here

st.divider()
st.caption("SAYAR GYI ENTERPRISE | UNIFIED v15.5 | MULTI-ACCOUNT READY")
