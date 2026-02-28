import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. GLOBAL SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v105.0")

def apply_v105_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* v101 Restored Insight Cards */
        .v101-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        .v101-header { color: #58a6ff; font-weight: 900; font-size: 20px; margin-bottom: 12px; }
        
        /* Report Style */
        .v101-report-box {
            background: #0d1117; border: 1px solid #30363d; padding: 45px;
            border-radius: 12px; line-height: 1.8; color: #adbac7; font-family: 'Segoe UI', sans-serif;
        }

        /* --- THE NEW WORKING ROBOT BUTTON --- */
        .floating-robot-wrapper {
            position: fixed;
            bottom: 40px;
            right: 40px;
            z-index: 99999;
        }
        
        /* We target the Streamlit button inside our wrapper and replace it with a sleek Robot Image */
        .floating-robot-wrapper button {
            background-image: url('https://img.icons8.com/nolan/96/bot.png') !important; 
            background-size: cover !important;
            background-position: center !important;
            background-color: transparent !important;
            color: transparent !important; /* Hides default text */
            border: 2px solid #58a6ff !important;
            border-radius: 50% !important;
            width: 80px !important;
            height: 80px !important;
            box-shadow: 0 0 20px rgba(88, 166, 255, 0.4), inset 0 0 15px rgba(88, 166, 255, 0.2) !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease !important;
        }
        .floating-robot-wrapper button:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 0 35px rgba(88, 166, 255, 0.8) !important;
            border-color: #79c0ff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE WORKING CENTERED POP-UP (NOTION STYLE) ---
# Streamlit Native Dialog (Works exactly like a centered modal popup)
@st.dialog("✨ SAYAR GYI AI COMMAND CENTER")
def open_ai_assistant():
    st.markdown("<p style='color:#adbac7; font-size:14px;'>CEO ခင်ဗျာ၊ သိလိုသည့် ဗျူဟာမြောက် မေးခွန်းများကို ဤနေရာတွင် ရိုက်ထည့်ပါ။</p>", unsafe_allow_html=True)
    
    # Notion-style Input
    user_query = st.chat_input("E.g. AEO ဆိုတာကို မြန်မာလို အလွယ်ဆုံး ရှင်းပြပါ...")
    
    if user_query:
        st.markdown(f"**CEO:** {user_query}")
        with st.spinner("Analyzing Strategy..."):
            st.success(f"**Sayar Gyi:** CEO ခင်ဗျာ၊ '{user_query}' နှင့် ပတ်သက်၍ အောက်ပါအတိုင်း ဆောင်ရွက်ရန် အကြံပြုအပ်ပါသည်။ (ဤနေရာတွင် AI ၏ ဉာဏ်ရည်တု အဖြေ ထွက်ပေါ်လာမည်ဖြစ်ပါသည်။)")

# --- 3. THE INSIGHT ENGINE (v101 QUALITY) ---
def render_v101_insights():
    st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
    st.caption("Right-bottom ရှိ Robot Icon ကိုနှိပ်၍ Notion-style AI ဖြင့် အချိန်မရွေး ဆွေးနွေးနိုင်ပါသည်။")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="v101-card">
            <div class="v101-header">🖋️ Content & AEO Mastery</div>
            <p style="color:#adbac7;">
                <b>Focus:</b> Google Link ထက် AI Answer ထဲ ပါဝင်လာရန် (AEO) လုပ်ဆောင်ပါ။ <br><br>
                <b>Strategic Tip:</b> Q&A Style Content များက AI Citation ရရန် အခွင့်အလမ်း အများဆုံးဖြစ်သည်။
            </p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="v101-card" style="border-left-color: #f85149;">
            <div class="v101-header">🎯 Media Buying: High-Signal Data</div>
            <p style="color:#adbac7;">
                <b>Focus:</b> Targeting ထက် Creative ကောင်းမွန်မှုကို ဦးစားပေးပါ။ <br><br>
                <b>Strategic Tip:</b> Customer Data အမှန်များကို AI ဆီ ကျွေးခြင်းဖြင့် Ad ROI ၂ ဆ တက်နိုင်သည်။
            </p>
        </div>""", unsafe_allow_html=True)

# --- 4. THE CLEAN REPORT (v101 QUALITY) ---
def render_v101_report():
    today = datetime.now().strftime("%d %B, %Y")
    report_text = f"""SAYAR GYI EXECUTIVE WEEKLY REPORT
----------------------------------
Report ID: SG-2026-FEB-02
ရက်စွဲ: {today}

၁။ အဓိက ဗျူဟာမြောက် အနှစ်ချုပ်
- AI Search စနစ်များ၏ အပြောင်းအလဲကို စောင့်ကြည့်ရန်။
- Video Creative Testing (Hooks) များကို အားဖြည့်ရန်။

၂။ လုပ်ဆောင်ရန် ညွှန်ကြားချက်များ (Direct Commands)
- ၎င်းသတင်းများအပေါ် အခြေခံ၍ AEO Content (၃) ပုဒ် အမြန်ဆုံး စတင်ပါ။
- Telegram Community ကို High-value Leads များအတွက် အရန်သင့်ပြင်ပါ။

၃။ ဆရာကြီး၏ အထူးသတိပေးချက်
- ပမာဏထက် အရည်အသွေး (Quality over Quantity) ကို ဦးစားပေးပါ။"""
    st.markdown(f'<div class="v101-report-box"><pre style="color:#adbac7; white-space: pre-wrap; font-family: inherit;">{report_text}</pre></div>', unsafe_allow_html=True)

# --- 5. EXECUTION ---
def main():
    apply_v105_styles()
    
    # ---------------------------------------------------------
    # RENDER THE FLOATING ROBOT BUTTON
    # Wrapping st.button inside the targeted CSS class to make it float and swap its background
    st.markdown('<div class="floating-robot-wrapper">', unsafe_allow_html=True)
    if st.button("OPEN_AI"):  # The text is hidden by CSS, only the icon shows
        open_ai_assistant()   # This triggers the Pop-up Dialog
    st.markdown('</div>', unsafe_allow_html=True)
    # ---------------------------------------------------------
    
    st.markdown('<h1 style="font-weight:900;">Sayar Gyi Mastermind Suite</h1>', unsafe_allow_html=True)
    
    tab_global, tab_local, tab_insight, tab_report = st.tabs([
        "🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"
    ])

    with tab_insight:
        render_v101_insights()
    
    with tab_report:
        render_v101_report()

if __name__ == "__main__":
    main()
