import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v86.0 | Executive View",
    page_icon="💎"
)

# --- 2. ENHANCED CSS STYLING (FOR CLARITY & BEAUTY) ---
def apply_v86_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 98%; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Headers */
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 20px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        /* Pipeline Boxes (From your reference style) */
        .status-box-v86 {
            background: #161b22; border: 1px solid #30363d;
            padding: 30px 20px; border-radius: 12px; text-align: center;
        }
        
        /* Deep Insight Card - Optimized for Boldness */
        .insight-card-v86 {
            background: #161b22; border: 1px solid #30363d;
            padding: 20px; border-radius: 15px; margin-bottom: 20px;
        }
        
        .insight-header {
            display: flex; justify-content: space-between; align-items: baseline;
            margin-bottom: 10px;
        }

        .m-label-v86 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; }
        .m-value-v86 { color: #ffffff; font-size: 32px; font-weight: 800; display: block; }
        .m-delta-v86 { color: #3fb950; font-size: 16px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 2px 8px; border-radius: 5px; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. THE UPDATED SIDE PANEL ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        
        st.write("")
        st.markdown("### INDUSTRY NEWS")
        if st.button("🌐 Read Industry Trends", use_container_width=True):
            st.toast("Syncing with Marketing Nodes...")
            
        st.divider()
        st.markdown("### MENU")
        nav = st.radio("Navigate", ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive", "🎨 Asset Library"], label_visibility="collapsed")
        
        st.divider()
        st.markdown("### MY AGENTS")
        st.caption("🤖 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
        
        st.write("")
        st.button("🔥 Switch to Creator Mode", use_container_width=True)
            
        st.divider()
        st.success("Core Engine: Online")
        st.info("Node: SG-AI-MASTER-01")
        
        st.write("")
        st.markdown("### MODEL")
        st.radio("Engine", ["Gemini 1.5 Pro", "GPT-4o", "Claude 3.5"], horizontal=True, label_visibility="collapsed")
    return nav

# --- 4. OPTIMIZED DASHBOARD ENGINE ---
def render_dashboard():
    # --- HEADER CONTROLS ---
    h_col, f_col = st.columns([1.5, 1])
    with h_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with f_col:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    # --- 1. CONTENT CREATION STATUS ---
    st.markdown('<p class="main-header">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-v86"><div class="m-label-v86">{label}</div>'
                        f'<div style="font-size:45px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- 2. DEEP INSIGHTS (NEW BOLD DESIGN) ---
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_bold_insight_card(label, value, delta):
        st.markdown(f"""
            <div class="insight-card-v86">
                <div class="m-label-v86">{label}</div>
                <div class="insight-header">
                    <span class="m-value-v86">{value}</span>
                    <span class="m-delta-v86">{delta}</span>
                </div>
        """, unsafe_allow_html=True)
        
        # Chart with proper spacing
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=150, use_container_width=True)
        elif chart_style == "Area Chart": st.area_chart(data, height=150, use_container_width=True)
        else: st.bar_chart(data, height=150, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Metrics Config
    if platform == "Facebook":
        metrics = [("Views", "85.2K", "↑12%"), ("Interactions", "3.2K", "↑8%"), ("Followers", "12,402", "↑1.2%"),
                   ("Page Visits", "4.5K", "↑15%"), ("Link Clicks", "920", "↑22%"), ("Conversations", "128", "↑5.6%")]
    elif platform == "TikTok":
        metrics = [("Video Views", "1.2M", "↑45%"), ("Shares", "12K", "↑30%"), ("Saves", "4.5K", "↑18%"),
                   ("Profile Visits", "25K", "↑10%"), ("Bio Clicks", "1.5K", "↑25%"), ("Completion Rate", "65%", "↑5%")]
    else: # YouTube
        metrics = [("Impressions", "2.5M", "↑5%"), ("Watch Time", "14K h", "↑12%"), ("Subscribers", "420", "↑2%"),
                   ("Avg Duration", "4:32", "↑0:45"), ("CTR", "8.5%", "↑1.2%"), ("Comments", "850", "↑15%")]

    # Render Grid
    row1 = st.columns(3)
    for i in range(3):
        with row1[i]: render_bold_insight_card(metrics[i][0], metrics[i][1], metrics[i][2])
    
    row2 = st.columns(3)
    for i in range(3, 6):
        with row2[i-3]: render_bold_insight_card(metrics[i][0], metrics[i][1], metrics[i][2])

# --- 5. EXECUTION ---
if __name__ == "__main__":
    apply_v86_styles()
    current_page = render_sidebar()
    if "Dashboard" in current_page: render_dashboard()
    else: st.title(current_page); st.info("Under AI Synchronization...")
