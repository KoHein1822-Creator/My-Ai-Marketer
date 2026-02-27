import streamlit as st
import pandas as pd

def render_myanmar_telemetry():
    # --- HEADER: LOCALIZED COMMAND CENTER ---
    st.markdown("""
        <div style="background: #0d1117; border-bottom: 2px solid #58a6ff; padding-bottom: 10px; margin-bottom: 20px;">
            <h2 style="color: #ffffff; margin: 0; font-size: 24px;">🇲🇲 Business Operations Monitor</h2>
            <p style="color: #8b949e; font-size: 13px; margin: 0;">Fully Autonomous AI Management | <span style="color:#3fb950;">System Active</span></p>
        </div>
    """, unsafe_allow_html=True)

    # --- ROW 1: LOCAL BUSINESS METRICS (Lakhs & Percentage) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">ယနေ့ လုပ်ငန်းအခြေအနေ</p>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Daily Sales (Kpay/Cash)", "45.5 Lakhs", "+5.2L")
    m2.metric("Messenger Response", "99%", "Fast (Instant)")
    m3.metric("Facebook Ad Reach", "12.4K", "+15%")
    m4.metric("Active Leads", "42 People", "In Pipeline")

    st.write("")

    # --- ROW 2: LIVE AGENT LOG (MYANMAR CONTEXT) ---
    feed_col, deli_col = st.columns([1.5, 1])

    with feed_col:
        st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">AI Agent Activity Log (ဘာတွေလုပ်နေလဲ)</p>', unsafe_allow_html=True)
        st.markdown("""
            <div style="background: #010409; border: 1px solid #30363d; padding: 15px; border-radius: 8px; height: 220px; font-family: 'Inter', sans-serif; font-size: 13px; overflow-y: auto;">
                <p style="color: #8b949e; margin: 5px 0;">[09:15 AM] <span style="color: #3fb950;">●</span> <b>[Messenger Agent]</b> က Customer (၃) ဦးကို ဈေးနှုန်းဖြေကြားပြီးပါပြီ။</p>
                <p style="color: #8b949e; margin: 5px 0;">[09:42 AM] <span style="color: #58a6ff;">●</span> <b>[Data Agent]</b> KPay Screenshot (၅) ခုကို စစ်ဆေးအတည်ပြုပြီးပါပြီ။</p>
                <p style="color: #e1e4e8; margin: 5px 0;">[10:05 AM] <span style="color: #a371f7;">●</span> <b>[Content Agent]</b> ယနေ့ Trend ဖြစ်နေသော သီချင်းဖြင့် TikTok Video (၁) ပုဒ်တင်ပြီးပါပြီ။</p>
                <p style="color: #8b949e; margin: 5px 0;">[10:30 AM] <span style="color: #d29922;">●</span> <b>[Ad Manager]</b> Engagement ကျနေသော Post ကို Ads Budget (၅၀၀၀) ကျပ် ထပ်တိုးလိုက်သည်။</p>
                <p style="color: #3fb950; margin-top: 10px; font-weight: bold;">> AI Network is managing your page autonomously.</p>
            </div>
        """, unsafe_allow_html=True)

    with deli_col:
        st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">Transaction & Deli Flow</p>', unsafe_allow_html=True)
        # Simple Local Flow Table
        deli_data = pd.DataFrame({
            'Order': ['ORD-001', 'ORD-002', 'ORD-003'],
            'Status': ['On Deli', 'Checking Pay', 'Confirmed'],
            'Payment': ['KPay', 'Wave', 'Cash']
        })
        st.table(deli_data)

    st.write("")

    # --- ROW 3: LOCAL MARKET INSIGHTS ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">Market Intelligence (မြန်မာ့ဈေးကွက် အခြေအနေ)</p>', unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    
    with r1:
        st.info("**Trend Alert:** လက်ရှိ ရွှေဈေး/ဒေါ်လာဈေး အတက်အကျကြောင့် Customer များ ဈေးနှုန်းမေးမြန်းမှု (Messenger) ပိုများနေပါသည်။ AI က ဈေးနှုန်းများကို Real-time Update လုပ်ပေးနေပါသည်။")

    with r2:
        st.success("**Opportunity:** ယနေ့ညနေ (၆:၀၀) မှ (၉:၀၀) အတွင်း Content တင်လျှင် Reach ပိုရနိုင်ကြောင်း AI က ခန့်မှန်းထားပါသည်။ Video Content ကို ဦးစားပေးရန် အကြံပြုပါသည်။")

if __name__ == "__main__":
    render_myanmar_telemetry()
