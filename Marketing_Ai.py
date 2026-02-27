import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v85.0 | Ultimate Command Center",
    page_icon="🚀"
)

# --- 2. PREMIUM CSS STYLING ---
def apply_custom_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 98%; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Section Headers */
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 20px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        /* Status Boxes (Top Pipeline) */
        .status-box-master {
            background: #161b22; border: 1px solid #30363d;
            padding: 30px 20px; border-radius: 12px; text-align: center;
        }
        
        /* Metric Box Integration - အပေါ်က Box လေးထဲမှာ Data ထည့်ရန် */
        .metric-header-box {
            background: #0d1117; border: 1px solid #30363d;
            padding: 10px 15px; border-radius: 8px 8px 0 0;
            display: flex; justify-content: space-between; align-items: center;
        }
        
        .chart-container-v85 {
            background: #161b22; border: 1px solid #30363d;
            border-top: none; padding: 15px; border-radius: 0 0 12px 12px;
            margin-bottom: 20px;
        }
        
        /* Font Tweaks */
        .m-label { color: #8b949e; font-size: 13px; font-weight: 600; }
        .m-value { color: #ffffff; font-size: 20px; font-weight: 800; }
        .m-delta { color: #3fb950; font-size: 12px; font-weight: 700; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. FINAL SIDE PANEL (RESTORED VERSION) ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        
        st.write("")
        st.markdown("### INDUSTRY NEWS")
        if st.button("🌐 Read Industry Trends", use_container_width=True):
            st.toast("Scanning global marketing nodes...")
            
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

# --- 4. INTEGRATED DASHBOARD ENGINE ---
def render_dashboard():
    # --- HEADER & FILTERS ---
    h_col, f_col = st.columns([1.5, 1])
    with h_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:35px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
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
            st.markdown(f'<div class="status-box-master"><div style="color:#8b949e; font-size:14px; text-transform:uppercase;">{label}</div>'
                        f'<div style="font-size:45px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- 2. DEEP INSIGHTS WITH INTEGRATED METRIC BOXES ---
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_integrated_card(label, value, delta):
        # အပေါ်က Box လေးထဲမှာ Metric ပြခြင်း
        st.markdown(f"""
            <div class="metric-header-box">
                <span class="m-label">{label}</span>
                <div>
                    <span class="m-value">{value}</span>
                    <span class="m-delta">&nbsp; {delta}</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
        
        # အောက်က Container ထဲမှာ Chart ပြခြင်း
        st.markdown('<div class="chart-container-v85">', unsafe_allow_html=True)
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=160, use_container_width=True)
        elif chart_style == "Area Chart": st.area_chart(data, height=160, use_container_width=True)
        else: st.bar_chart(data, height=160, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Dynamic Data Loading
    if platform == "Facebook":
        metrics = [("Views", "85.2K", "↑12%"), ("Interactions", "3.2K", "↑8%"), ("Followers", "12,402", "↑1.2%"),
                   ("Page Visits", "4.5K", "↑15%"), ("Link Clicks", "920", "↑22%"), ("Conversations", "128", "↑5.6%")]
    elif platform == "TikTok":
        metrics = [("Video Views", "1.2M", "↑45%"), ("Shares", "12K", "↑30%"), ("Saves", "4.5K", "↑18%"),
                   ("Profile Visits", "25K", "↑10%"), ("Bio Clicks", "1.5K", "↑25%"), ("Completion Rate", "65%", "↑5%")]
    else: # YouTube
        metrics = [("Impressions", "2.5M", "↑5%"), ("Watch Time", "14K h", "↑12%"), ("Subscribers", "420", "↑2%"),
                   ("Avg Duration", "4:32", "↑0:45"), ("CTR", "8.5%", "↑1.2%"), ("Comments", "850", "↑15%")]

    # Grid Render (3x2)
    row1 = st.columns(3)
    for i in range(3):
        with row1[i]: render_integrated_card(metrics[i][0], metrics[i][1], metrics[i][2])
    
    row2 = st.columns(3)
    for i in range(3, 6):
        with row2[i-3]: render_integrated_card(metrics[i][0], metrics[i][1], metrics[i][2])

# --- 5. EXECUTION ---
if __name__ == "__main__":
    apply_custom_styles()
    current_page = render_sidebar()
    
    if "Dashboard" in current_page:
        render_dashboard()
    else:
        st.title(current_page)
        st.info("Section currently under AI synchronization...")
