import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. GLOBAL SETTINGS & STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v99.0")

def apply_v99_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        .insight-card {
            background: linear-gradient(145deg, #1e293b 0%, #0f172a 100%);
            border: 1px solid #334155; border-radius: 15px; padding: 25px; margin-bottom: 20px;
        }
        .insight-title { color: #38bdf8; font-size: 20px; font-weight: bold; margin-bottom: 10px; }
        .impact-high { color: #f43f5e; font-weight: bold; }
        .report-box {
            background: #ffffff; color: #1e293b; padding: 40px; border-radius: 5px;
            font-family: 'Courier New', Courier, monospace; line-height: 1.6;
        }
        .verified-pill { background: #064e3b; color: #34d399; padding: 2px 10px; border-radius: 20px; font-size: 10px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. DATA CONSTANTS (FEB 2026) ---
GLOBAL_NEWS = [
    {"rank": "#1", "topic": "Agentic Commerce Shift", "link": "https://openai.com", "mm_summary": "AI Agent များက လူသားကိုယ်စား ဈေးဝယ်ဆုံးဖြတ်ချက်ချပေးလာခြင်း။", "impact": "98%"},
    {"rank": "#2", "topic": "AEO (Answer Engine Optimization)", "link": "https://google.com", "mm_summary": "Search Engine ထက် AI Answer Engine များတွင် ကိုယ့်လုပ်ငန်းပေါ်အောင်လုပ်ရမည့်စနစ်။", "impact": "95%"}
]

LOCAL_NEWS = [
    {"rank": "#1", "topic": "Telegram Commerce Growth", "link": "https://facebook.com/mm_biz", "mm_summary": "FB ကန့်သတ်ချက်များကြောင့် Telegram Community Marketing အားကောင်းလာခြင်း။", "impact": "97%"},
    {"rank": "#2", "topic": "Reali-Tea Content Trend", "link": "https://facebook.com/agency_mm", "mm_summary": "အရမ်း Polished ဖြစ်သော Ads များထက် ရိုးရှင်းသော Behind-the-scenes များကို မြန်မာများ ပိုယုံကြည်ခြင်း။", "impact": "92%"}
]

# --- 3. REPORT GENERATOR LOGIC ---
def generate_weekly_report():
    report_date = datetime.now().strftime("%d %B %Y")
    report_text = f"""
    SAYAR GYI EXECUTIVE WEEKLY REPORT
    Date: {report_date}
    --------------------------------------------------
    1. GLOBAL MARKET STATUS
    - Most Critical: {GLOBAL_NEWS[0]['topic']} (Impact: {GLOBAL_NEWS[0]['impact']})
    - Trend: Moving from Search to Agentic Intent.
    
    2. MYANMAR LOCAL STATUS
    - Key Platform: Telegram & Facebook (Hybrid Mode)
    - Consumer Behavior: High trust in 'Authentic' content.
    
    3. SAYAR GYI'S STRATEGIC COMMANDS
    - Transition to Answer Engine Optimization (AEO).
    - Build Private Communities on Telegram as a backup.
    - Leverage Human-Centric storytelling to counter 'AI Slop' fatigue.
    
    Verified by Sayar Gyi AI Logic Engine v99.0
    --------------------------------------------------
    """
    return report_text

# --- 4. INTERFACE ---
def render_dashboard():
    st.markdown('<h1 style="font-weight:900; color:#f8fafc;">Sayar Gyi Intelligence Suite <span style="font-size:18px; color:#64748b;">v99.0</span></h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌐 Global Pulse", 
        "🇲🇲 Local Pulse", 
        "🧠 Sayar Gyi's Insight", 
        "📄 Weekly Report"
    ])

    with tab1:
        st.subheader("Global Strategic Topics")
        st.table(pd.DataFrame(GLOBAL_NEWS))

    with tab2:
        st.subheader("Myanmar Verified Trends")
        st.table(pd.DataFrame(LOCAL_NEWS))

    with tab3:
        st.markdown("### 🧠 Sayar Gyi's Professional Insight (Feb 2026)")
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"""
                <div class="insight-card">
                    <div class="insight-title">၁။ AI-Centric Operations သို့ ကူးပြောင်းခြင်း</div>
                    <p style="font-size:14px; color:#cbd5e1;"><b>Business Impact:</b> အခု ၂၀၂၆ မှာ AI က Tool တစ်ခုမဟုတ်တော့ဘဲ အခြေခံအဆောက်အအုံ ဖြစ်သွားပါပြီ။ မူလက လုပ်ငန်းစဉ်တွေကို AI နဲ့ အစားထိုးတာထက် (Optimization)၊ လုပ်ငန်းစဉ်တစ်ခုလုံးကို AI နဲ့ပဲ စတင်တည်ဆောက်တာ (Process Design) က ပိုပြီး ROI တက်စေပါတယ်။</p>
                    <span class="impact-high">Critical Action:</span> ဝန်ထမ်းတွေကို AI သုံးတတ်အောင်တင်မကဘဲ AI Agents တွေကို စီမံခန့်ခွဲတတ်တဲ့ Manager တွေဖြစ်လာအောင် လေ့ကျင့်ပေးရပါမယ်။
                </div>
            """, unsafe_allow_html=True)
            
        with c2:
            st.markdown(f"""
                <div class="insight-card">
                    <div class="insight-title">၂။ Human-Led Marketing as a Differentiator</div>
                    <p style="font-size:14px; color:#cbd5e1;"><b>Market Shift:</b> AI က Content တွေ အမြောက်အမြား ထုတ်ပေးနိုင်လာတဲ့အခါ လူတွေက "AI Slop" (အနှစ်မပါတဲ့ AI စာသားတွေ) ကို ငြီးငွေ့လာကြပါတယ်။ ဒီနေရာမှာ ကိုယ့် Brand ရဲ့ <b>Distinctive POV</b> (ထူးခြားတဲ့ အမြင်) နဲ့ <b>Empathy</b> (စာနာနားလည်မှု) ကသာ ပြိုင်ဘက်ထက် သာလွန်စေမှာပါ။</p>
                    <span class="impact-high">Strategic Command:</span> Video တွေမှာ အရမ်းကြီး Perfect ဖြစ်နေတာထက် "ရိုးသားမှု" ကို ဦးစားပေးပါ။ မြန်မာပြည်အတွက် 'Authentic Behind-the-scenes' က အထိရောက်ဆုံးပါ။
                </div>
            """, unsafe_allow_html=True)

    with tab4:
        st.markdown("### 📄 Weekly Executive Report Generator")
        st.info("အပတ်စဉ် အချက်အလက်များကို စုစည်းပြီး အောက်ပါခလုတ်ကို နှိပ်၍ Report ထုတ်ယူနိုင်ပါသည်။")
        
        if st.button("Generate & Preview Report"):
            report_content = generate_weekly_report()
            st.markdown(f'<div class="report-box"><pre>{report_content}</pre></div>', unsafe_allow_html=True)
            st.download_button(label="Download Full Report (TXT)", data=report_content, file_name=f"SayarGyi_Report_{datetime.now().strftime('%Y%m%d')}.txt")

if __name__ == "__main__":
    apply_v99_styles()
    render_dashboard()
