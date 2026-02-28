import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. PREMIUM DARK UI & POP-UP STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v104.0")

def apply_v104_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* v101 Insight Cards (Restored) */
        .v101-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 900; font-size: 20px; margin-bottom: 12px; }
        
        /* The Robotic Floating Button */
        .robot-btn {
            position: fixed; bottom: 40px; right: 40px;
            background: #1f6feb; color: white; width: 65px; height: 65px; 
            border-radius: 20px; display: flex; align-items: center; justify-content: center;
            font-size: 30px; box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            cursor: pointer; z-index: 9999; transition: all 0.3s ease;
            border: 1px solid #58a6ff;
        }
        .robot-btn:hover { transform: translateY(-5px) scale(1.05); background: #388bfd; }

        /* Centered AI Pop-up Style (Simulated via Overlay) */
        .ai-overlay {
            position: fixed; top: 20%; left: 30%; width: 40%; 
            background: #161b22; border: 1px solid #58a6ff; border-radius: 15px;
            padding: 30px; z-index: 10000; box-shadow: 0 0 50px rgba(0,0,0,0.8);
        }
        
        /* Report Style (v101 Restored) */
        .v101-report-box {
            background: #0d1117; border: 1px solid #30363d; padding: 45px;
            border-radius: 12px; line-height: 1.8; color: #adbac7;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE ROBOTIC AI POP-UP ---
def render_robot_assistant():
    # The Robot Floating Icon
    st.markdown('<div class="robot-btn">🤖</div>', unsafe_allow_html=True)
    
    # State Management for Pop-up
    if "ai_open" not in st.session_state:
        st.session_state.ai_open = False

    # Minimalist Control in a small Expander to simulate 'Clicking' the Robot
    with st.expander("🤖 Open Sayar Gyi AI (Notion-style)"):
        st.markdown("### 🤖 Strategy Command AI")
        st.caption("CEO ခင်ဗျာ၊ သိလိုသည့် ဗျူဟာမြောက် မေးခွန်းများကို မေးမြန်းနိုင်ပါသည်။")
        query = st.text_input("Ask Sayar Gyi...", placeholder="E.g. AEO အကြောင်း အသေးစိတ် ရှင်းပြပါ")
        
        if query:
            st.markdown(f"**CEO:** {query}")
            st.info(f"**Sayar Gyi:** CEO ခင်ဗျာ၊ {query} နှင့် ပတ်သက်၍ ကျွန်တော် ချက်ချင်း သုံးသပ်ပေးပါမည်။ (ဗျူဟာမြောက် အချက်အလက်များ ရှာဖွေနေပါသည်...)")

# --- 3. THE INSIGHT ENGINE (v101 QUALITY) ---
def render_v101_insights():
    st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="v101-card">
            <div class="v101-header">🖋️ Content & AEO Mastery</div>
            <p style="color:#adbac7;">
                <b>Focus:</b> Google Link ထက် AI Answer ထဲ ပါဝင်လာရန် (AEO) လုပ်ဆောင်ပါ။ <br>
                <b>Strategic Tip:</b> Q&A Style Content များက AI Citation ရရန် အခွင့်အလမ်း အများဆုံးဖြစ်သည်။
            </p>
        </div>""", unsafe_allow_html=True)

    with col2:
        st.markdown("""<div class="v101-card" style="border-left-color: #f85149;">
            <div class="v101-header">🎯 Media Buying: High-Signal Data</div>
            <p style="color:#adbac7;">
                <b>Focus:</b> Targeting ထက် Creative ကောင်းမွန်မှုကို ဦးစားပေးပါ။ <br>
                <b>Strategic Tip:</b> Customer Data အမှန်များကို AI ဆီ ကျွေးခြင်းဖြင့် Ad ROI ၂ ဆ တက်နိုင်သည်။
            </p>
        </div>""", unsafe_allow_html=True)

# --- 4. THE CLEAN REPORT (v101 QUALITY) ---
def render_v101_report():
    today = datetime.now().strftime("%d-%m-%Y")
    report_text = f"""
    SAYAR GYI EXECUTIVE WEEKLY REPORT
    ----------------------------------
    Report ID: SG-2026-FEB-01
    ရက်စွဲ: {today}

    ၁။ အဓိက ဗျူဟာမြောက် အနှစ်ချုပ်
    - AI Search စနစ်များ၏ အပြောင်းအလဲကို စောင့်ကြည့်ရန်။
    - Video Creative Testing (Hooks) များကို အားဖြည့်ရန်။

    ၂။ လုပ်ဆောင်ရန် ညွှန်ကြားချက်များ (Direct Commands)
    - ၎င်းသတင်းများအပေါ် အခြေခံ၍ AEO Content (၃) ပုဒ် အမြန်ဆုံး စတင်ပါ။
    - Telegram Community ကို High-value Leads များအတွက် အရန်သင့်ပြင်ပါ။

    ၃။ ဆရာကြီး၏ အထူးသတိပေးချက်
    - ပမာဏထက် အရည်အသွေး (Quality over Quantity) ကို ဦးစားပေးပါ။
    """
    st.markdown(f'<div class="v101-report-box"><pre style="color:#adbac7; white-space: pre-wrap; font-family: sans-serif;">{report_text}</pre></div>', unsafe_allow_html=True)

# --- 5. EXECUTION ---
def main():
    apply_v104_styles()
    render_robot_assistant()
    
    tab_global, tab_local, tab_insight, tab_report = st.tabs([
        "🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"
    ])

    with tab_insight:
        render_v101_insights()
    
    with tab_report:
        render_v101_report()

if __name__ == "__main__":
    main()
