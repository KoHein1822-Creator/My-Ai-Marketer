import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v101.0")

def apply_master_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        .perspective-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .perspective-header { color: #58a6ff; font-weight: 900; font-size: 22px; margin-bottom: 15px; border-bottom: 1px solid #30363d; padding-bottom: 10px; }
        .action-point { background: rgba(56, 189, 248, 0.1); border-radius: 8px; padding: 15px; margin-top: 15px; border: 1px dashed #38bdf8; }
        .report-paper {
            background: #ffffff; color: #1e293b; padding: 60px; border-radius: 4px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.4); line-height: 1.8; font-family: 'Pyidaungsu', 'Segoe UI', serif;
        }
        .highlight-red { color: #f85149; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE DEEP INSIGHT ENGINE ---
def render_deep_insights():
    st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence (February 2026 Edition)")
    st.info("Industry အပြောင်းအလဲများအပေါ် အခြေခံထားသော အသေးစိတ် ဗျူဟာမြောက် သုံးသပ်ချက်များ")

    # PERSPECTIVE 1: CONTENT & AEO
    st.markdown("""<div class="perspective-card">
        <div class="perspective-header">🖋️ Content Strategy: From SEO to AEO (Answer Engine Optimization)</div>
        <p style="color:#adbac7;">
            <b>အခြေအနေ:</b> ၂၀၂၆ မှာ Google Search ထက် SearchGPT နဲ့ Gemini တို့လို Answer Engines တွေက နေရာယူလာပါပြီ။ User တွေက Website ထဲကို ဝင်မကြည့်တော့ဘဲ AI ရဲ့ အဖြေကိုပဲ တိုက်ရိုက်ဖတ်တော့မှာပါ။<br><br>
            <b>Business Impact:</b> ကိုယ့်ရဲ့ Content တွေဟာ 'Keywords' ပေါ်မှာ အခြေမခံဘဲ AI က 'နားလည်နိုင်တဲ့' <b>Structured Data</b> ဖြစ်ဖို့ လိုပါတယ်။ Generic ဆန်တဲ့ AI Content တွေဟာ Algorithm ရဲ့ ဒဏ်ခတ်မှုကို ခံရပါလိမ့်မယ်။
        </p>
        <div class="action-point">
            <b>💡 CEO လုပ်ဆောင်ရန်:</b> ကိုယ့်လုပ်ငန်းရဲ့ Expert Opinion ပါတဲ့ Case Studies တွေကို အားဖြည့်ပါ။ AI က မပေးနိုင်တဲ့ 'ကိုယ်တွေ့ အတွေ့အကြုံ' (First-hand Experience) ကသာ ၂၀၂၆ ရဲ့ အဖိုးတန်ဆုံး Content ဖြစ်ပါတယ်။
        </div>
    </div>""", unsafe_allow_html=True)

    # PERSPECTIVE 2: MEDIA BUYING & AI SIGNALS
    st.markdown("""<div class="perspective-card" style="border-left-color: #f85149;">
        <div class="perspective-header">🎯 Media Buying: The Creative-Led AI Era</div>
        <p style="color:#adbac7;">
            <b>အခြေအနေ:</b> Facebook နဲ့ Google တို့ရဲ့ Targeting စနစ်တွေက 'Black-box' ဖြစ်သွားပါပြီ။ လူကိုယ်တိုင် Audience ရွေးစရာမလိုဘဲ AI ကပဲ အကုန်လုပ်ပေးနေတာပါ။ <br><br>
            <b>Business Impact:</b> အခုခေတ်မှာ Target ရွေးတာထက် <b>'Creative Quality'</b> က ပိုအရေးကြီးလာပါတယ်။ Creative မကောင်းရင် AI က Target မှားရှာပေးတတ်ပါတယ်။
        </p>
        <div class="action-point">
            <b>💡 CEO လုပ်ဆောင်ရန်:</b> Media Buying Budget ရဲ့ ၄၀% ကို Creative Testing (Video variations များများစမ်းခြင်း) မှာ သုံးခိုင်းပါ။ Targeting ထက် Hook နဲ့ Visual အပေါ်မှာပဲ အာရုံစိုက်ခိုင်းပါ။
        </div>
    </div>""", unsafe_allow_html=True)

    # PERSPECTIVE 3: COMMUNITY & BRAND SAFETY
    st.markdown("""<div class="perspective-card" style="border-left-color: #d2a8ff;">
        <div class="perspective-header">📱 Social & Community: Digital Resilience</div>
        <p style="color:#adbac7;">
            <b>အခြေအနေ:</b> မြန်မာပြည်မှာ Facebook ရဲ့ Reach က ပိုပြီးခန့်မှန်းရခက်လာပါတယ်။ Algorithm က User တွေရဲ့ <b>'Dwell Time'</b> (တစ်နေရာတည်းမှာ ကြာကြာနေမှု) ကိုပဲ ဦးစားပေးနေပါတယ်။ <br><br>
            <b>Business Impact:</b> Facebook ပေါ်မှာပဲ ပုံအောထားရင် လုပ်ငန်းက အန္တရာယ်ရှိပါတယ်။ Community ကို ပိုင်ဆိုင်ဖို့ (Own your audience) လိုအပ်ပါတယ်။
        </p>
        <div class="action-point">
            <b>💡 CEO လုပ်ဆောင်ရန်:</b> Telegram နှင့် Viber Community ကို 'VIP Loyalty Space' အဖြစ် အမြန်ဆုံး အကောင်အထည်ဖော်ပါ။ Facebook သည် 'Traffic' အတွက်သာဖြစ်ပြီး Community သည် 'Sales' အတွက်ဖြစ်ရပါမည်။
        </div>
    </div>""", unsafe_allow_html=True)

# --- 3. PROFESSIONAL BURMESE REPORT ---
def generate_master_report():
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

    [Social & Resilience]
    Facebook Reach ကျဆင်းမှုသည် အမြဲတမ်းဖြစ်စဉ် ဖြစ်လာပါသည်။ ကိုယ်ပိုင် Telegram/Viber Channel များမှတစ်ဆင့် 
    Direct-to-Consumer (D2C) ဆက်ဆံရေးကို အားဖြည့်ရန် ညွှန်ကြားလိုပါသည်။

    ၃။ ဆောင်ရွက်ရန် အကြံပြုချက် (RECOMMENDED ACTIONS)
    - SEO Strategy ကို 'Answer Engine-friendly' ဖြစ်အောင် ပြန်လည်စစ်ဆေးပါ။
    - Video Content များတွင် ၂ စက္ကန့်အတွင်း User ကို ဖမ်းစားနိုင်မည့် 'Hook' ၃ မျိုးထက်မနည်း စမ်းသပ်ပါ။
    - CRM Data (First-party Data) စုဆောင်းမှုကို ဦးစားပေးလုပ်ဆောင်ပါ။

    SAYAR GYI AI STRATEGY ENGINE (v101.0)
    ----------------------------------------------------------------------
    """

# --- 4. MAIN INTERFACE ---
def render_main():
    st.markdown('<h1 style="font-weight:900;">Sayar Gyi Mastermind Suite</h1>', unsafe_allow_html=True)
    
    t1, t2, t3, t4 = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with t3:
        render_deep_insights()

    with t4:
        st.markdown("### 📄 Professional Weekly Report (Burmese)")
        if st.button("Generate & Preview Executive Report"):
            report = generate_master_report()
            st.markdown(f'<div class="report-paper"><pre style="white-space: pre-wrap; color:#1e293b; font-size:15px;">{report}</pre></div>', unsafe_allow_html=True)
            st.download_button("Download Official Report", report, file_name=f"Executive_Report_{today}.txt")

if __name__ == "__main__":
    apply_master_styles()
    render_main()
