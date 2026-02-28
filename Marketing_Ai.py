import streamlit as st
import numpy as np

# --- 1. SETTINGS (V88.0 EXACT) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v88.0 | Balanced", initial_sidebar_state="expanded")

def apply_v88_styles():
    st.markdown("""
        <style>
        /* Exact V88.0 Background & Text Colors */
        .main { background-color: #0d1117; color: #ffffff; }
        .block-container { padding-top: 1.5rem; max-width: 95%; }
        
        /* Sidebar Professional Look */
        [data-testid="stSidebar"] {
            background-color: #0d1117 !important;
            border-right: 1px solid #30363d !important;
        }
        
        /* Side Panel Headers & Dividers */
        .sb-header { font-size: 13px; font-weight: 800; color: #8b949e; letter-spacing: 0.5px; margin-top: 10px; }
        .sb-sub-header { font-size: 10px; color: #1f6feb; margin-bottom: 20px; }
        .sidebar-divider { margin: 15px 0; border-top: 1px solid #21262d; }

        /* V88.0 Metric & Insight Cards */
        .metric-container {
            background: #161b22; border: 1px solid #30363d; border-radius: 4px;
            padding: 20px; text-align: center;
        }
        .insight-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 4px;
            padding: 15px; margin-bottom: 10px;
        }
        .delta-tag { color: #3fb950; font-size: 12px; background: rgba(63, 185, 80, 0.1); padding: 2px 6px; border-radius: 3px; }
        
        /* Section Title */
        .section-title { color: #58a6ff; font-weight: bold; font-size: 14px; border-left: 3px solid #1f6feb; padding-left: 10px; margin: 20px 0; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (V88.0 + NEW BUTTON) ---
def render_sidebar():
    with st.sidebar:
        # Header Section
        st.markdown('<p class="sb-header">SAYAR GYI\'S</p>', unsafe_allow_html=True)
        st.markdown('<p class="sb-sub-header">AI MARKETING AGENCY</p>', unsafe_allow_html=True)
        
        # --- NEW: Sayar Gyi's Intelligence Button (Section Break ခွဲထားသည်) ---
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        if st.button("🧠 Sayar Gyi's Intelligence", use_container_width=True):
            st.session_state.page = "intelligence"
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Menu Section
        st.markdown('<p class="sb-header">MENU</p>', unsafe_allow_html=True)
        if st.button("📊 Interactive Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
        st.button("🧬 Brand DNA", use_container_width=True)
        st.button("📂 Project Archive", use_container_width=True)
        st.button("📚 Asset Library", use_container_width=True)
        
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # Creator Mode Section
        st.button("✨ Switch to Creator Mode", use_container_width=True)
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
        
        # System Status Section
        st.markdown('<p class="sb-header">SYSTEM STATUS</p>', unsafe_allow_html=True)
        st.success("Core Engine: Online")
        st.caption("Model: Gemini 1.5 Pro & GPT-4o")

# --- 3. THE ORIGINAL V88.0 DASHBOARD ---
def render_dashboard():
    st.title("Strategic Dashboard")
    
    # 1. Content Creation Status
    st.markdown('<p class="section-title">CONTENT CREATION STATUS</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    data = [("DRAFTING", "12"), ("PENDING", "5"), ("SCHEDULED", "18"), ("PUBLISHED", "145")]
    for i, col in enumerate([c1, c2, c3, c4]):
        label, val = data[i]
        col.markdown(f'<div class="metric-container"><p style="color:#8b949e; font-size:10px;">{label}</p><h2>{val}</h2></div>', unsafe_allow_html=True)

    # 2. Facebook Deep Insights (The 6-Grid)
    st.markdown('<p class="section-title">FACEBOOK DEEP INSIGHTS & TRENDS</p>', unsafe_allow_html=True)
    
    # Row 1
    r1c1, r1c2, r1c3 = st.columns(3)
    insights_r1 = [("VIEWS", "85.2K", "+12%"), ("INTERACTIONS", "3.2K", "+8%"), ("FOLLOWERS", "12.4K", "+1%")]
    for i, col in enumerate([r1c1, r1c2, r1c3]):
        label, val, delta = insights_r1[i]
        with col:
            st.markdown(f'<div class="insight-card"><p style="font-size:10px; color:#8b949e;">{label}</p><h3>{val} <span class="delta-tag">{delta}</span></h3></div>', unsafe_allow_html=True)
            st.line_chart(np.random.randn(20), height=80)

    # Row 2
    r2c1, r2c2, r2c3 = st.columns(3)
    insights_r2 = [("PAGE VISITS", "4.5K", "+15%"), ("LINK CLICKS", "920", "+22%"), ("CONVERSATIONS", "128", "+5%")]
    for i, col in enumerate([r2c1, r2c2, r2c3]):
        label, val, delta = insights_r2[i]
        with col:
            st.markdown(f'<div class="insight-card"><p style="font-size:10px; color:#8b949e;">{label}</p><h3>{val} <span class="delta-tag">{delta}</span></h3></div>', unsafe_allow_html=True)
            st.line_chart(np.random.randn(20), height=80)

# --- 4. THE INTELLIGENCE INTERFACE ---
def render_intelligence():
    st.title("Sayar Gyi's Intelligence")
    tabs = st.tabs(["🧠 Deep Insights", "📄 Weekly Report"])
    with tabs[0]:
        st.markdown('<p class="section-title">STRATEGIC INTELLIGENCE</p>', unsafe_allow_html=True)
        # CEO Confirm ထားသော UI များ ဤနေရာတွင် ပေါ်လာမည်
        st.info("CEO ပို့ပေးမည့် Main Interface ပုံများကို စောင့်ဆိုင်းနေပါသည်...")

# --- MAIN ---
def main():
    apply_v8
