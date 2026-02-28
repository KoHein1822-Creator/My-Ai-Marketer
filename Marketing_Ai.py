import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. GLOBAL SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v103.0")

def apply_v103_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* Reverting Insight Cards to v101 Style */
        .v101-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 900; font-size: 20px; margin-bottom: 12px; }
        
        /* Notion-style Floating AI Button */
        .floating-ai-btn {
            position: fixed; bottom: 30px; right: 30px;
            background: linear-gradient(135deg, #58a6ff 0%, #bc8cff 100%);
            color: white; width: 60px; height: 60px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center;
            font-size: 24px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
            cursor: pointer; z-index: 1000; transition: transform 0.2s;
        }
        .floating-ai-btn:hover { transform: scale(1.1); }
        
        /* Report Styling - Reverted to Clean & Dark */
        .v101-report-box {
            background: #161b22; border: 1px solid #30363d; padding: 40px;
            border-radius: 10px; font-family: 'Pyidaungsu', sans-serif; line-height: 1.8;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE FLOATING AI ASSISTANT (NOTION STYLE) ---
def render_ai_assistant():
    # Adding the Visual Sparkle Icon
    st.markdown('<div class="floating-ai-btn">✨</div>', unsafe_allow_html=True)
    
    with st.sidebar:
        st.markdown("### ✨ Sayar Gyi AI Assistant")
        st.caption("Ask me anything about these strategies...")
        user_query = st.chat_input("ဗျူဟာများအကြောင်း သိလိုသည်များကို မေးမြန်းပါ...")
        if user_query:
            st.write(f"**CEO:** {user_query}")
            st.info(f"**Sayar Gyi:** CEO ခင်ဗျာ၊ '{user_query}' နဲ့ ပတ်သက်ပြီး ကျွန်တော် အသေးစိတ် သုံးသပ်ပေးပါမယ်။ (ဤသည်မှာ Notion-style AI Assistant Prototype ဖြစ်ပါသည်။)")

# --- 3. THE INSIGHT ENGINE (v101 RESTORED) ---
def render_v101_insights():
    st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence (Restored v101)")
    
    # Category 1
    st.markdown("""<div class="v101-card">
        <div class="v101-header">🖋️ Content & AEO Strategy</div>
        <p style="color:#adbac7;">
            <b>အခြေအနေ:</b> SEO ထက် Answer Engine Optimization (AEO) က ပိုအရေးကြီးလာသည်။ <br>
            <b>Business Impact:</b> AI က ကိုယ့် Brand အကြောင်းကို ရှင်းပြနိုင်ဖို့ 'Source' ကောင်းဖို့လိုသည်။
        </p>
    </div>""", unsafe_allow_html=True)

    # Category 2
    st.markdown("""<div class="v101-card" style="border-left-color: #f85149;">
        <div class="v101-header">🎯 Media Buying: Creative-Led Signals</div>
        <p style="color:#adbac7;">
            <b>အခြေအနေ:</b> Targeting ကို AI က အကုန်လုပ်ပေးမည်။ <br>
            <b>Business Impact:</b> Creative အရည်အသွေးကသာ ရလဒ်ကို အဆုံးအဖြတ်ပေးမည်။
        </p>
    </div>""", unsafe_allow_html=True)

# --- 4. THE CLEAN REPORT (v101 RESTORED) ---
def render_v101_report():
    today = datetime.now().strftime("%d-%m-%Y")
    report_content = f"""
    SAYAR GYI EXECUTIVE WEEKLY REPORT
    ----------------------------------
    ရက်စွဲ - {today}

    [၁] ဗျူဟာမြောက် အနှစ်ချုပ်
    - AI Search စနစ်များသို့ ကူးပြောင်းရန် ပြင်ဆင်ပါ။
    - Creative Testing ကို အဓိကထား လုပ်ဆောင်ပါ။

    [၂] လုပ်ဆောင်ရန် အကြံပြုချက်များ
    - Video hooks များကို ၂ စက္ကန့်အတွင်း ပြောင်းလဲပါ။
    - Telegram/Viber Private Communities တည်ဆောက်ပါ။
    
    [၃] နည်းပညာ သတိပေးချက်
    - First-party Data စုဆောင်းမှုကို အားဖြည့်ပါ။
    """
    st.markdown(f'<div class="v101-report-box"><pre style="color:#adbac7; white-space: pre-wrap;">{report_content}</pre></div>', unsafe_allow_html=True)

# --- 5. EXECUTION ---
def main():
    apply_v103_styles()
    render_ai_assistant()
    
    tab_global, tab_local, tab_insight, tab_report = st.tabs([
        "🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"
    ])

    with tab_insight:
        render_v101_insights()
    
    with tab_report:
        render_v101_report()

if __name__ == "__main__":
    main()
