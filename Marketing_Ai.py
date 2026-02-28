import streamlit as st
import numpy as np

# --- 1. SETTINGS & V88.0 AUTHENTIC STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v138.0", initial_sidebar_state="expanded")

def apply_v88_authentic_styles():
    st.markdown("""
        <style>
        /* Main Theme Recovery */
        .main { background-color: #0d1117; color: #ffffff; }
        .block-container { padding-top: 1rem; max-width: 96%; }
        
        /* Sidebar Professional Look */
        [data-testid="stSidebar"] {
            background-color: #0d1117 !important;
            border-right: 1px solid #30363d !important;
            width: 320px !important;
        }
        .sidebar-header { font-size: 14px; font-weight: bold; color: #8b949e; letter-spacing: 1px; margin-top: 20px; }
        .sidebar-divider { margin: 15px 0; border-top: 1px solid #30363d; }
        
        /* Dashboard Metric Cards */
        .status-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 6px;
            padding: 15px; text-align: center; height: 100px;
        }
        .insight-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 8px;
            padding: 15px; margin-bottom: 10px;
        }
        
        /* Custom Button Styling */
        .stButton > button {
            width: 100%; border-radius: 6px; background: #21262d; border: 1px solid #30363d;
            color: #c9d1d9; transition: 0.3s; text-align: left; padding: 8px 15px;
        }
        .stButton > button:hover { background: #30363d; border-color: #8b949e; color: white; }
        
        /* Highlight for Intelligence Button */
        div[data-testid="stVerticalBlock"] > div:nth-child(3) .stButton > button {
            background: linear-gradient(90deg, #1f6feb 0%, #161b22 100%);
            border-left: 4px solid #58a6ff; font-weight: bold; color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. UPGRADED SIDEBAR ---
def render_sidebar():
    with st.sidebar:
        # Section 1: Command Center Header
        st.markdown('<p class="sidebar-header">SAYAR GYI\'S</p>', unsafe_allow_html=True)
        st.caption("AI MARKETING AGENCY")
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Section 2: Sayar Gyi's Intelligence (Primary Action)
        if st.button("🧠 Sayar Gyi's Intelligence"):
            st.session_state.page = "intelligence"
            
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Section 3: Menu
        st.markdown('<p class="sidebar-header">MENU</p>', unsafe_allow_html=True)
        if st.button("📊 Interactive Dashboard"):
            st.session_state.page = "dashboard"
        st.button("🧬 Brand DNA")
        st.button("📂 Project Archive")
        st.button("📚 Asset Library")
        
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Section 4: Creator Mode
        st.button("✨ Switch to Creator Mode")
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Section 5: System Status
        st.markdown('<p class="sidebar-header">SYSTEM STATUS</p>', unsafe_allow_html=True)
        st.success("Core Engine: Online")
        st.caption("Model: Gemini 1.5 Pro & GPT-4o")

# --- 3. THE 100% AUTHENTIC V88 DASHBOARD ---
def render_dashboard():
    st.markdown("### Strategic Dashboard")
    
    # Content Creation Status Row
    st.markdown("#### ┃ CONTENT CREATION STATUS")
    c1, c2, c3, c4 = st.columns(4)
    statuses = [("DRAFTING", "12", "#1f6feb"), ("PENDING", "5", "#f1e05a"), 
                ("SCHEDULED", "18", "#58a6ff"), ("PUBLISHED", "145", "#238636")]
    for i, col in enumerate([c1, c2, c3, c4]):
        label, val, color = statuses[i]
        col.markdown(f'<div class="status-card" style="border-top: 3px solid {color}"><p style="font-size:12px; color:#8b949e; margin:0;">{label}</p><h2 style="margin:0;">{val}</h2></div>', unsafe_allow_html=True)

    # Facebook Deep Insights (6-Grid with Charts)
    st.markdown("#### ┃ FACEBOOK DEEP INSIGHTS & TRENDS")
    
    # First Row of Metrics
    r1_c1, r1_c2, r1_c3 = st.columns(3)
    metrics_r1 = [("VIEWS", "85.2K", "+12%"), ("INTERACTIONS", "3.2K", "+8%"), ("FOLLOWERS", "12.4K", "+1%")]
    for i, col in enumerate([r1_c1, r1_c2, r1_c3]):
        label, val, delta = metrics_r1[i]
        with col:
            st.markdown(f'<div class="insight-card"><p style="font-size:12px; color:#8b949e; margin:0;">{label}</p><h3>{val} <span style="color:#3fb950; font-size:14px;">{delta}</span></h3></div>', unsafe_allow_html=True)
            st.line_chart(np.random.randn(15), height=80, use_container_width=True)

    # Second Row of Metrics
    r2_c1, r2_c2, r2_c3 = st.columns(3)
    metrics_r2 = [("PAGE VISITS", "4.5K", "+15%"), ("LINK CLICKS", "920", "+22%"), ("CONVERSATIONS", "128", "+5%")]
    for i, col in enumerate([r2_c1, r2_c2, r2_c3]):
        label, val, delta = metrics_r2[i]
        with col:
            st.markdown(f'<div class="insight-card"><p style="font-size:12px; color:#8b949e; margin:0;">{label}</p><h3>{val} <span style="color:#3fb950; font-size:14px;">{delta}</span></h3></div>', unsafe_allow_html=True)
            st.line_chart(np.random.randn(15), height=80, use_container_width=True)

# --- 4. THE INTELLIGENCE INTERFACE ---
def render_intelligence():
    st.markdown("### Sayar Gyi's Intelligence")
    tabs = st.tabs(["🧠 Deep Insights", "📄 Weekly Report"])
    
    with tabs[0]:
        st.markdown("#### Strategic Insights")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="insight-card" style="border-left: 4px solid #58a6ff;"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="insight-card" style="border-left: 4px solid #f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)
            
    with tabs[1]:
        st.markdown("#### Weekly Performance")
        st.markdown('<div class="insight-card" style="border-left: 4px solid #3fb950;">Performance Summary: ယခုအပတ်အတွင်း Ads Reach 15% တိုးတက်လာပါသည်။</div>', unsafe_allow_html=True)

# --- MAIN ---
def main():
    apply_v88_authentic_styles()
    if 'page' not in st.session_state: st.session_state.page = "dashboard"
    render_sidebar()
    
    if st.session_state.page == "dashboard":
        render_dashboard()
    else:
        render_intelligence()

if __name__ == "__main__": main()
