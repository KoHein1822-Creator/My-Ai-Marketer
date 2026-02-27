import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIG & STYLING ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v84.0")

def apply_v84_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 97%; }
        
        /* ခေါင်းစဉ်များအတွက် ပိုမိုကောင်းမွန်သော Styling */
        .main-header {
            color: #58a6ff; font-size: 14px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 25px; margin-top: 20px;
            border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        /* Status Box များကို ပိုကြီးအောင် လုပ်ထားသည် */
        .status-box-v84 {
            background: #161b22; border: 1px solid #30363d;
            padding: 35px 20px; border-radius: 15px; text-align: center;
            box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        }
        
        /* Metrics Container */
        .metric-container-v84 {
            background: #161b22; border: 1px solid #30363d;
            padding: 25px; border-radius: 15px; margin-top: 15px;
        }
        </style>
    """, unsafe_allow_html=True)

def render_v84_dashboard():
    # Render Sidebar from previous versions
    with st.sidebar:
        st.title("SAYAR GYI'S")
        st.caption("AI Marketing Agency")
        st.divider()
        st.markdown("### MENU")
        st.radio("Navigate", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    apply_v84_styles()
    
    # --- TOP CONTROL BAR ---
    t_col, c_col = st.columns([1.5, 1])
    with t_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:35px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with c_col:
        sub_c1, sub_c2, sub_c3 = st.columns(3)
        with sub_c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with sub_c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with sub_c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    # --- 1. CONTENT CREATION STATUS (NEW HEADER & BIGGER BOXES) ---
    st.markdown('<p class="main-header">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f"""
                <div class="status-box-v84">
                    <div style="color:#8b949e; font-size:15px; font-weight:600;">{label}</div>
                    <div style="font-size:45px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div>
                </div>
            """, unsafe_allow_html=True)

    # အောက်ဘက်သို့ Space နည်းနည်းချပေးခြင်း
    st.write("")
    st.write("")

    # --- 2. DEEP INSIGHTS (WITH PUSHED DOWN LAYOUT) ---
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_metric_card(label, value, delta):
        st.markdown('<div class="metric-container-v84">', unsafe_allow_html=True)
        st.metric(label, value, delta)
        st.write("")
        # Chart အမြင့်ကို အောက်က Space နဲ့ အံကိုက်ဖြစ်အောင် ၁၈၀ အထိ မြှင့်ထားသည်
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=180, use_container_width=True)
        elif chart_style == "Area Chart": st.area_chart(data, height=180, use_container_width=True)
        else: st.bar_chart(data, height=180, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # Metrics Layout Logic
    if platform == "Facebook":
        m_data = [("Views", "85.2K", "+12%"), ("Interactions", "3.2K", "+8%"), ("Followers", "12.4K", "+1%"),
                  ("Page Visits", "4.5K", "+15%"), ("Link Clicks", "920", "+22%"), ("Conversations", "128", "+5%")]
    elif platform == "TikTok":
        m_data = [("Video Views", "1.2M", "+45%"), ("Shares", "12K", "+30%"), ("Saves", "4.5K", "+18%"),
                  ("Profile Visits", "25K", "+10%"), ("Bio Clicks", "1.5K", "+25%"), ("Completion Rate", "65%", "+5%")]
    else: # YouTube
        m_data = [("Impressions", "2.5M", "+5%"), ("Watch Time", "14K hrs", "+12%"), ("Subscribers", "420", "+2%"),
                  ("Avg Duration", "4:32", "+0:45"), ("CTR", "8.5%", "+1.2%"), ("Comments", "850", "+15%")]

    # Render Grid 3x2
    r1_c1, r1_c2, r1_c3 = st.columns(3)
    with r1_c1: render_metric_card(m_data[0][0], m_data[0][1], m_data[0][2])
    with r1_c2: render_metric_card(m_data[1][0], m_data[1][1], m_data[1][2])
    with r1_c3: render_metric_card(m_data[2][0], m_data[2][1], m_data[2][2])

    r2_c1, r2_c2, r2_c3 = st.columns(3)
    with r2_c1: render_metric_card(m_data[3][0], m_data[3][1], m_data[3][2])
    with r2_c2: render_metric_card(m_data[4][0], m_data[4][1], m_data[4][2])
    with r2_c3: render_metric_card(m_data[5][0], m_data[5][1], m_data[5][2])

if __name__ == "__main__":
    render_v84_dashboard()
