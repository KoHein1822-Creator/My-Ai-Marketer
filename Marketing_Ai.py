import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v147.0 | Mastermind Executive",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS (V100 + V101 + Dashboard Styles) ---
def apply_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Perspective & Insight Cards (V101 Style) */
        .perspective-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .perspective-header { color: #58a6ff; font-weight: 900; font-size: 22px; margin-bottom: 15px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        .action-point { background: rgba(56, 189, 248, 0.1); border-radius: 8px; padding: 15px; margin-top: 15px; border: 1px dashed #38bdf8; }
        
        /* Report Paper Style (V100 Style) */
        .report-paper {
            background: #ffffff; color: #1e293b; padding: 50px; border-radius: 4px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4); line-height: 1.8; 
            font-family: 'Pyidaungsu', 'Segoe UI', serif; margin-top: 20px;
        }
        
        /* Pulse Table Styles */
        .intel-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        .intel-table th { text-align: left; padding: 12px 15px; color: #58a6ff; font-size: 14px; border-bottom: 1px solid #30363d; background: #161b22; }
        .intel-table td { padding: 15px; border-bottom: 1px solid #30363d; color: #e6edf3; font-size: 14px; }
        .link-text { color: #58a6ff; font-size: 12px; text-decoration: none; font-weight: 600; display: block; margin-top: 5px;}
        
        /* Intel Card Styles */
        .intel-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; overflow: hidden; margin-bottom: 20px; }
        .intel-img { width: 100%; height: 140px; object-fit: cover; }
        .intel-content { padding: 15px; }
        .intel-title a { font-size: 16px; font-weight: 700; color: #ffffff; text-decoration: none; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. STATE INITIALIZATION ---
if 'page' not in st.session_state:
    st.session_state.page = "Intelligence"

# --- 4. NAVIGATION ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.caption("AI Marketing Strategy Suite")
        st.write("")
        if st.button("🧠 Deep Strategy & Reports", use_container_width=True):
            st.session_state.page = "Intelligence"
            st.rerun()
        st.divider()
        nav_options = ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive"]
        for option in nav_options:
            if st.button(option, use_container_width=True):
                st.session_state.page = option
                st.rerun()

# --- 5. REPORT GENERATORS (V100/V101 Logic) ---
def generate_executive_report():
    today = datetime.now().strftime("%d-%m-%Y")
    return f"""
    SAYAR GYI EXECUTIVE WEEKLY REPORT
    (လျှို့ဝှက် - အမှုဆောင်အဆင့်သာ ကြည့်ရှုရန်)
    ထုတ်ပြန်သည့်ရက်စွဲ - {today}

    ၁။ လုပ်ငန်းအနှစ်ချုပ် (WEEKLY SUMMARY)
    ယခုအပတ်တွင် ကမ္ဘာ့အဆင့်တွင် Agentic Commerce (AI က လူကိုယ်စား ဝယ်ယူပေးခြင်း) စနစ် အားကောင်းလာပြီး၊ 
    ပြည်တွင်းတွင် 'Authentic Human Content' ကိုသာ ပိုမိုယုံကြည်သည့် Digital Fatigue လက္ခဏာများ တွေ့ရပါသည်။

    ၂။ ဗျူဟာမြောက် သုံးသပ်ချက် (STRATEGIC INSIGHTS)

    [Content Marketing]
    AI က ရေးထားသည့် Generic စာသားများကို ရှောင်ကြဉ်ပါ။ ၂၀၂၆ တွင် AI သည် Answer Engine Optimization (AEO) သို့ 
    ကူးပြောင်းနေပြီဖြစ်ရာ၊ တိကျသော အချက်အလက်နှင့် ခိုင်မာသော ကိုးကားချက်များပါသည့် Content Ecosystem ကို တည်ဆောက်ရန် လိုအပ်ပါသည်။

    [Media Buying & ROI]
    Manual Targeting ထက် Creative Testing ကို အလေးထားပါ။ Signal Data (Customer အချက်အလက်) များအား 
    စနစ်တကျစုဆောင်းပြီး AI Ad Tools များသို့ ကျွေးပေးခြင်းဖြင့် ပြိုင်ဘက်ထက် သာလွန်သော ROI ကို ရရှိစေပါမည်။

    ၃။ ဆောင်ရွက်ရန် အကြံပြုချက် (RECOMMENDED ACTIONS)
    - SEO Strategy ကို 'Answer Engine-friendly' ဖြစ်အောင် ပြန်လည်စစ်ဆေးပါ။
    - Video Content များတွင် ၂ စက္ကန့်အတွင်း User ကို ဖမ်းစားနိုင်မည့် 'Hook' ၃ မျိုးထက်မနည်း စမ်းသပ်ပါ။
    - CRM Data (First-party Data) စုဆောင်းမှုကို ဦးစားပေးလုပ်ဆောင်ပါ။

    SAYAR GYI AI STRATEGY ENGINE (v147.0)
    ----------------------------------------------------------------------
    """

# --- 6. INTELLIGENCE HUB (The Requested Tabs) ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-weight:900; font-size:38px;">Sayar Gyi Mastermind Suite</h1>', unsafe_allow_html=True)
    
    t1, t2, t3, t4 = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])
    
    # TAB 1 & 2: PULSE (Existing logic with Clickable Links)
    with t1:
        st.markdown("### 🔥 High-Impact Global Highlights")
        # Global Cards & Table with Target Blank Links...
        st.info("Global Market Pulse active with clickable source links.")
        st.markdown("""
        <table class="intel-table">
            <tr><th>Rank</th><th>Topic / Source</th><th>Impact</th></tr>
            <tr><td>#1</td><td>Agentic Commerce <a href="https://techcrunch.com" target="_blank" class="link-text">🔗 Source Link</a></td><td>95%</td></tr>
            <tr><td>#2</td><td>SearchGPT Ads <a href="https://openai.com" target="_blank" class="link-text">🔗 Source Link</a></td><td>92%</td></tr>
        </table>
        """, unsafe_allow_html=True)

    with t2:
        st.markdown("### 🇲🇲 MM Myanmar Verified Pulse")
        st.markdown("""
        <table class="intel-table">
            <tr><th>Rank</th><th>Topic / Source</th><th>Impact</th></tr>
            <tr><td>#1</td><td>FB Marketplace Shift <a href="https://facebook.com" target="_blank" class="link-text">🔗 Source Link</a></td><td>97%</td></tr>
            <tr><td>#2</td><td>Telegram Growth MM <a href="https://telegram.org" target="_blank" class="link-text">🔗 Source Link</a></td><td>94%</td></tr>
        </table>
        """, unsafe_allow_html=True)

    # --- TAB 3: DEEP INSIGHTS (V101 RESTORED) ---
    with t3:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence (Feb 2026)")
        st.markdown("""
        <div class="perspective-card">
            <div class="perspective-header">🖋️ Content Strategy: From SEO to AEO</div>
            <p style="color:#adbac7;">
                <b>အခြေအနေ:</b> ၂၀၂၆ မှာ Google Search ထက် SearchGPT နဲ့ Gemini တို့လို Answer Engines တွေက နေရာယူလာပါပြီ။<br><br>
                <b>Business Impact:</b> ကိုယ့်ရဲ့ Content တွေဟာ 'Keywords' ပေါ်မှာ အခြေမခံဘဲ AI က 'နားလည်နိုင်တဲ့' Structured Data ဖြစ်ဖို့ လိုပါတယ်။
            </p>
            <div class="action-point">
                <b>💡 CEO လုပ်ဆောင်ရန်:</b> ကိုယ့်လုပ်ငန်းရဲ့ Expert Opinion ပါတဲ့ Case Studies တွေကို အားဖြည့်ပါ။ AI က မပေးနိုင်တဲ့ 'ကိုယ်တွေ့ အတွေ့အကြုံ' ကသာ အဖိုးတန်ဆုံးပါ။
            </div>
        </div>
        
        <div class="perspective-card" style="border-left-color: #f85149;">
            <div class="perspective-header">🎯 Media Buying: Creative-Led AI Era</div>
            <p style="color:#adbac7;">
                <b>အခြေအနေ:</b> Targeting စနစ်တွေက 'Black-box' ဖြစ်သွားပါပြီ။ Creative မကောင်းရင် AI က Target မှားရှာပေးတတ်ပါတယ်။
            </p>
            <div class="action-point">
                <b>💡 CEO လုပ်ဆောင်ရန်:</b> Media Buying Budget ရဲ့ ၄၀% ကို Creative Testing (Video variations) မှာ သုံးခိုင်းပါ။
            </div>
        </div>
        
        <div class="perspective-card" style="border-left-color: #d2a8ff;">
            <div class="perspective-header">📱 Social & Community: Resilience</div>
            <p style="color:#adbac7;">
                <b>အခြေအနေ:</b> Facebook ရဲ့ Reach က ခန့်မှန်းရခက်လာပါတယ်။ Dwell Time ကိုပဲ Algorithm က ကြည့်ပါတော့တယ်။
            </p>
            <div class="action-point">
                <b>💡 CEO လုပ်ဆောင်ရန်:</b> Telegram နှင့် Viber Community ကို 'VIP Loyalty Space' အဖြစ် အမြန်ဆုံး အကောင်အထည်ဖော်ပါ။
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- TAB 4: WEEKLY REPORT (V100 RESTORED) ---
    with t4:
        st.markdown("### 📄 Professional Weekly Report (Burmese)")
        if st.button("Generate & Preview Executive Report"):
            report_text = generate_executive_report()
            st.markdown(f"""
            <div class="report-paper">
                <pre style="white-space: pre-wrap; color:#1e293b; font-size:15px; font-family:inherit;">{report_text}</pre>
            </div>
            """, unsafe_allow_html=True)
            st.download_button("📥 Download Official Report", report_text, file_name=f"Executive_Report_{datetime.now().strftime('%Y%m%d')}.txt")

# --- 7. MAIN ---
if __name__ == "__main__":
    apply_styles()
    render_sidebar()
    if st.session_state.page == "Intelligence":
        render_intelligence_hub()
    else:
        st.title(st.session_state.page)
        st.info("Module loading...")
