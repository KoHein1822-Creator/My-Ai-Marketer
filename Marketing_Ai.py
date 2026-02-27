import streamlit as st
import pandas as pd

def render_funnel_dashboard():
    # --- HEADER ---
    st.markdown("""
        <div style="background: #0d1117; border-bottom: 2px solid #58a6ff; padding-bottom: 10px; margin-bottom: 25px;">
            <h2 style="color: #ffffff; margin: 0; font-size: 24px;">🎯 Strategic Funnel Audit</h2>
            <p style="color: #8b949e; font-size: 13px; margin: 0;">Monitoring AI Performance Across TOFU, MOFU, and BOFU</p>
        </div>
    """, unsafe_allow_html=True)

    # --- FUNNEL STAGE 1: TOFU (AWARENESS) ---
    with st.container():
        st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">Stage 01: TOFU (Top of Funnel) - Awareness</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-top:-10px;">AI က လူတွေသိအောင် ဘယ်လောက်လုပ်နိုင်သလဲ?</p>', unsafe_allow_html=True)
        t1, t2, t3, t4 = st.columns(4)
        t1.metric("Content Velocity", "45 Posts", "AI Active")
        t2.metric("Total Reach", "150.2K", "+12%")
        t3.metric("New Followers", "1,200", "+150")
        t4.metric("Video Views", "85K", "+10%")
        st.divider()

    # --- FUNNEL STAGE 2: MOFU (CONSIDERATION) ---
    with st.container():
        st.markdown('<p style="font-size:11px; font-weight:700; color:#a371f7; letter-spacing:1px; text-transform:uppercase;">Stage 02: MOFU (Middle of Funnel) - Interest</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-top:-10px;">AI ရဲ့ Content ကို လူတွေ ဘယ်လောက် စိတ်ဝင်စားသလဲ?</p>', unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Engagement Rate", "5.8%", "High")
        m2.metric("Post Shares", "420", "+45")
        m3.metric("Post Saves", "150", "Valuable")
        m4.metric("Click to Message", "850 Clicks", "Conversion Lead")
        st.divider()

    # --- FUNNEL STAGE 3: BOFU (CONVERSION) ---
    with st.container():
        st.markdown('<p style="font-size:11px; font-weight:700; color:#3fb950; letter-spacing:1px; text-transform:uppercase;">Stage 03: BOFU (Bottom of Funnel) - Closing</p>', unsafe_allow_html=True)
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-top:-10px;">AI က အရောင်းပိတ်နိုင်တဲ့အထိ စွမ်းဆောင်နိုင်ရဲ့လား?</p>', unsafe_allow_html=True)
        b1, b2, b3, b4 = st.columns(4)
        b1.metric("Response Rate", "99.9%", "Instant")
        b2.metric("Total Inquiries", "620 Msgs", "Qualified")
        b3.metric("Confirmed Orders", "85 Units", "+12")
        b4.metric("Revenue (Lakhs)", "35.2 L", "Target Met")
        st.divider()

    # --- ROW 4: AI AGENT EFFICIENCY REPORT ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">AI Agent Efficiency Analysis (CEO Summary)</p>', unsafe_allow_html=True)
    c1, c2 = st.columns([1, 1])
    
    with c1:
        st.markdown("""
            <div style="background: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d;">
                <p style="color:#8b949e; font-size:12px;">BOTTLENECK DETECTION</p>
                <p style="color:#e1e4e8; font-size:14px;">လက်ရှိ <b>MOFU</b> မှာ Engagement ကောင်းသော်လည်း <b>BOFU</b> (Closing) ပိုင်းတွင် အနည်းငယ်နှေးနေပါသည်။ 
                Messenger Agent ၏ ဈေးနှုန်းတင်ပြပုံ (Sales Script) ကို ပြန်လည် Optimize လုပ်ရန် လိုအပ်ပါသည်။</p>
            </div>
        """, unsafe_allow_html=True)
        
    with c2:
        # Mini Efficiency Chart
        chart_data = pd.DataFrame({
            'Funnel Stage': ['TOFU', 'MOFU', 'BOFU'],
            'AI Efficiency Score': [95, 88, 72]
        })
        st.bar_chart(chart_data.set_index('Funnel Stage'), color="#58a6ff", height=150)

if __name__ == "__main__":
    render_funnel_dashboard()
