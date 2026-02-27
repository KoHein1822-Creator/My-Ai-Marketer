import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v87.0 | Ultimate Executive View",
    page_icon="🏆"
)

# --- 2. ELITE CSS STYLING (SPACE OPTIMIZATION) ---
def apply_v87_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 98%; padding-bottom: 0rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Headers */
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 20px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        /* Status Boxes (Top Pipeline) */
        .status-box-v87 {
            background: #161b22; border: 1px solid #30363d;
            padding: 35px 20px; border-radius: 12px; text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        }
        
        /* Deep Insight Card - Space Adjustments */
        .insight-card-v87 {
            background: #161b22; border: 1px solid #30363d;
            padding: 25px; border-radius: 15px; margin-bottom: 10px;
            min-height: 320px; /* အောက်က Space ကို ယူရန် အရပ်မြှင့်ထားသည် */
        }
        
        .m-label-v87 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 8px; }
        .m-value-v87 { color: #ffffff; font-size: 40px; font-weight: 900; line-height: 1; }
        .m-delta-v87 { color: #3fb950; font-size: 16px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 4px 10px; border-radius: 6px; }
        
        /* Layout Alignment */
        .insight-header-v87 {
            display: flex; justify-content: space-between; align-items: flex-end;
            margin-bottom: 25px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 3. THE MASTER SIDE PANEL ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        st.markdown("### INDUSTRY NEWS")
        st.button("🌐 Read Industry Trends", use_container_width=True)
        st.divider()
        st.markdown("### MENU")
        nav = st.radio("Nav", ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive", "🎨 Asset Library"], label_visibility="collapsed")
        st.divider()
        st.markdown("### MY AGENTS")
        st.caption("🤖 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
        st.write("")
        st.button("🔥 Switch to Creator Mode", use_container_width=True)
        st.divider()
        st.success("Core Engine: Online")
        st.write("")
        st.markdown("### MODEL")
        st.radio("Engine", ["Gemini 1.5 Pro", "GPT-4o", "Claude 3.5"], horizontal=True, label_visibility="collapsed")
    return nav

# --- 4. ULTIMATE DASHBOARD ENGINE ---
def render_dashboard():
    # --- HEADER CONTROLS ---
    h_col, f_col = st.columns([1.5, 1])
    with h_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:42px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with f_col:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    # --- 1. CONTENT CREATION STATUS ---
    st.markdown('<p class="main-header" style="margin-top:20px;">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-v87"><div class="m-label-v87">{label}</div>'
                        f'<div style="font-size:48px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")

    # --- 2. DEEP INSIGHTS (FINAL BOLD & BALANCED DESIGN) ---
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_ultimate_card(label, value, delta):
        st.markdown(f"""
            <div class="insight-card-v87">
                <div class="m-label-v87">{label}</div>
                <div class="insight-header-v87">
                    <span class="m-value-v87">{value}</span>
                    <span class="m-delta-v87">{delta}</span>
                </div>
        """, unsafe_allow_html=True)
        
        # Chart Height ကို ၂၀၀ အထိ တိုးမြှင့်လိုက်ခြင်းဖြင့် အောက်က Space ကို အပြည့်ယူစေသည်
        data = pd.DataFrame(np.random.randn(30, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=200, use_container_width=True)
        elif chart_style == "Area Chart": st.area_chart(data, height=200, use_container_width=True)
        else: st.bar_chart(data, height=200, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Data Source
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
    rows = [st.columns(3), st.columns(3)]
    for r_idx, cols in enumerate(rows):
        for c_idx in range(3):
            m_idx = (r_idx * 3) + c_idx
            with cols[c_idx]:
                render_ultimate_card(metrics[m_idx][0], metrics[m_idx][1], metrics[m_idx][2])

# --- 5. EXECUTION ---
if __name__ == "__main__":
    apply_v87_styles()
    current_page = render_sidebar()
    if "Dashboard" in current_page: render_dashboard()
    else: st.title(current_page); st.info("SAYAR GYI is preparing this module...")
