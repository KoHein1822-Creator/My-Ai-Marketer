import streamlit as st
import numpy as np

# --- 1. SETTINGS (V88.0 EXACT CLONE) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v88.0 | Balanced", initial_sidebar_state="expanded")

def apply_v88_original_styles():
    st.markdown("""
        <style>
        /* Exact V88.0 Aesthetics */
        .main { background-color: #0d1117; color: #ffffff; }
        [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #30363d !important; width: 300px !important; }
        
        /* Sidebar Typography & Spacing */
        .sb-label { font-size: 11px; font-weight: 800; color: #8b949e; letter-spacing: 1px; margin: 25px 0 10px 0; }
        .sb-sub-label { font-size: 9px; color: #1f6feb; margin-top: -10px; margin-bottom: 20px; }
        
        /* V88.0 Card UI */
        .v88-metric-card { background: #161b22; border: 1px solid #30363d; border-radius: 4px; padding: 20px; text-align: center; }
        .v88-insight-card { background: #161b22; border: 1px solid #30363d; border-radius: 4px; padding: 15px; position: relative; }
        
        /* Delta Badge Style */
        .delta-badge { background: rgba(63, 185, 80, 0.15); color: #3fb950; font-size: 11px; padding: 2px 6px; border-radius: 3px; position: absolute; right: 15px; top: 15px; }
        
        /* Dashboard Headers */
        .dash-header { color: #58a6ff; font-size: 13px; font-weight: bold; border-left: 3px solid #1f6feb; padding-left: 10px; margin: 25px 0 15px 0; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR (V88.0 CODE WITH INTELLIGENCE REPLACEMENT) ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<p class="sb-label">SAYAR GYI\'S</p>', unsafe_allow_html=True)
        st.markdown('<p class="sb-sub-label">AI MARKETING AGENCY</p>', unsafe_allow_html=True)
        
        # --- REPLACED: Industry News with Intelligence ---
        st.markdown('<p class="sb-label">SAYAR GYI\'S INTELLIGENCE</p>', unsafe_allow_html=True)
        if st.button("🧠 Deep Strategy & Reports", use_container_width=True):
            st.session_state.page = "intelligence"
            
        st.markdown('<p class="sb-label">MENU</p>', unsafe_allow_html=True)
        if st.button("📊 Interactive Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
        st.button("🧬 Brand DNA", use_container_width=True)
        st.button("📂 Project Archive", use_container_width=True)
        st.button("📚 Asset Library", use_container_width=True)
        
        st.markdown('<p class="sb-label">MY AGENTS</p>', unsafe_allow_html=True)
        st.caption("🤖 Intel | 🎨 Creative | 📈 Auditor")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("🔥 Switch to Creator Mode", use_container_width=True)
        
        st.markdown('<p class="sb-label">SYSTEM STATUS</p>', unsafe_allow_html=True)
        st.success("Core Engine: Online")
        st.markdown('<p class="sb-label">MODEL</p>', unsafe_allow_html=True)
        st.caption("● Gemini 1.5 Pro | ● GPT-4o")

# --- 3. DASHBOARD (V88.0 EXACT 6-GRID) ---
def render_dashboard():
    st.title("Strategic Dashboard")
    
    st.markdown('<p class="dash-header">CONTENT CREATION STATUS</p>', unsafe_allow_html=True)
    c1, c2, c3, c4 = st.columns(4)
    for i, (l, v) in enumerate([("DRAFTING", "12"), ("PENDING", "5"), ("SCHEDULED", "18"), ("PUBLISHED", "145")]):
        with [c1, c2, c3, c4][i]:
            st.markdown(f'<div class="v88-metric-card"><p style="color:#8b949e; font-size:11px;">{l}</p><h2>{v}</h2></div>', unsafe_allow_html=True)

    st.markdown('<p class="dash-header">FACEBOOK DEEP INSIGHTS & TRENDS</p>', unsafe_allow_html=True)
    
    # 6-Grid Logic
    metrics = [
        ("VIEWS", "85.2K", "+12%"), ("INTERACTIONS", "3.2K", "+8%"), ("FOLLOWERS", "12.4K", "+1%"),
        ("PAGE VISITS", "4.5K", "+15%"), ("LINK CLICKS", "920", "+22%"), ("CONVERSATIONS", "128", "+5%")
    ]
    
    for row in range(2):
        cols = st.columns(3)
        for col in range(3):
            idx = row * 3 + col
            l, v, d = metrics[idx]
            with cols[col]:
                st.markdown(f'''
                    <div class="v88-insight-card">
                        <span class="delta-badge">{d}</span>
                        <p style="color:#8b949e; font-size:11px; margin:0;">{l}</p>
                        <h3 style="margin:0;">{v}</h3>
                    </div>
                ''', unsafe_allow_html=True)
                st.line_chart(np.random.randn(20), height=85)

# --- MAIN ---
def main():
    apply_v88_original_styles()
    if 'page' not in st.session_state: st.session_state.page = "dashboard"
    render_sidebar()
    if st.session_state.page == "dashboard": render_dashboard()
    else: 
        st.title("Sayar Gyi's Intelligence")
        st.info("Ready to integrate the confirmed Strategic Intelligence UI")

if __name__ == "__main__": main()
