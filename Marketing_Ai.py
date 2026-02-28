import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v100.0")

def apply_master_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        .insight-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 20px; height: 100%; border-top: 4px solid #58a6ff;
        }
        .perspective-title { color: #58a6ff; font-weight: 800; font-size: 18px; margin-bottom: 10px; text-transform: uppercase; }
        .report-paper {
            background: #ffffff; color: #1e293b; padding: 50px; border-radius: 2px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5); line-height: 1.8; font-family: 'Pyidaungsu', serif;
        }
        .impact-tag { background: #238636; color: white; padding: 2px 8px; border-radius: 5px; font-size: 10px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE INSIGHT ENGINE (PERSPECTIVES) ---
def render_sayar_gyi_insights():
    st.markdown("### 🧠 Sayar Gyi's Multi-Perspective Analysis (Feb 2026)")
    st.caption("AI & Industry အပြောင်းအလဲများက Marketing ကဏ္ဍအလိုက် သက်ရောက်မှုများ")
    st.write("")
    
    row1_c1, row1_c2 = st.columns(2)
    row2_c1, row2_c2 = st.columns(2)
    
    with row1_c1:
        st.markdown("""<div class="insight-card">
            <div class="perspective-title">🖋️ Content Marketing Perspective</div>
            <p style="font-size:14px; color:#adbac7;">
                <b>Impact:</b> AI ကြောင့် Content အမြောက်အမြား ထွက်လာသော်လည်း 2026 တွင် "AI Slop" ကို လူများငြီးငွေ့လာသည်။ <br><br>
                <b>Strategy:</b> SearchGPT ကဲ့သို့ <b>Answer Engines</b> များတွင် ပါဝင်လာရန် Q&A-style content နှင့် Deep Insights များကို ဦးစားပေးပါ။ မြန်မာပြည်အတွက် 'Authentic Storytelling' က လူယုံကြည်မှု (Trust) ကို ရရှိစေမည့် တစ်ခုတည်းသော လမ်းစဖြစ်သည်။
            </p>
        </div>""", unsafe_allow_html=True)

    with row1_c2:
        st.markdown("""<div class="insight-card" style="border-top-color: #f85149;">
            <div class="perspective-title">🎯 Media Buying & Performance</div>
            <p style="font-size:14px; color:#adbac7;">
                <b>Impact:</b> Manual Targeting စနစ် ပျောက်ကွယ်လုနီးပါးဖြစ်ပြီး Meta ၏ Advantage+ နှင့် Google ၏ PMax တို့ကဲ့သို့ <b>Black-box AI</b> များက နေရာယူလာသည်။ <br><br>
                <b>Strategy:</b> Media Buyer များသည် Targeting ထက် <b>Creative Quality</b> နှင့် <b>Signal Data</b> (Customer Data အမှန်များ ကျွေးခြင်း) ကိုသာ အဓိက ကိုင်တွယ်ရမည်။ Cost-per-result ထက် Customer Lifetime Value (LTV) ကို ကြည့်၍ Bid လုပ်ပါ။
            </p>
        </div>""", unsafe_allow_html=True)

    with row2_c1:
        st.markdown("""<div class="insight-card" style="border-top-color: #d2a8ff;">
            <div class="perspective-title">📱 Social Media & Community</div>
            <p style="font-size:14px; color:#adbac7;">
                <b>Impact:</b> Algorithm များသည် Like/Share ထက် <b>Dwell Time</b> (ကြည့်ရှုချိန်) ကိုသာ ဦးစားပေးတော့သည်။ <br><br>
                <b>Strategy:</b> Video Content များတွင် Hook ကို ၂ စက္ကန့်အတွင်း ထည့်ပါ။ Facebook ၏ Reach ကျဆင်းမှုကို ကာကွယ်ရန် Telegram သို့မဟုတ် Viber ကဲ့သို့ <b>Private Communities</b> များသို့ Audience ကို ရွှေ့ပြောင်းထိန်းသိမ်းထားပါ။
            </p>
        </div>""", unsafe_allow_html=True)

    with row2_c2:
        st.markdown("""<div class="insight-card" style="border-top-color: #3fb950;">
            <div class="perspective-title">📊 Data & Analytics</div>
            <p style="font-size:14px; color:#adbac7;">
                <b>Impact:</b> Privacy ဥပဒေများကြောင့် Third-party Cookies များ သုံးမရတော့ပေ။ <br><br>
                <b>Strategy:</b> ကိုယ်ပိုင် <b>First-party Data</b> (Customer Phone/Email) စုဆောင်းမှုကို အားဖြည့်ပါ။ AI ကပေးသော Predictive Analytics (နောင်တွင် ဘာဖြစ်မည်ကို ခန့်မှန်းခြင်း) ကို သုံး၍ Budget ကို ကြိုတင်ခွဲဝေပါ။
            </p>
        </div>""", unsafe_allow_html=True)

# --- 3. BURMESE REPORT GENERATOR ---
def generate_burmese_report():
    today = datetime.now().strftime("%d-%m-%Y")
    report = f"""
    SAYAR GYI EXECUTIVE WEEKLY REPORT (မြန်မာဘာသာ)
    ထုတ်ပြန်သည့်ရက်စွဲ - {today}
    
    ၁။ အမှုဆောင်အနှစ်ချုပ် (EXECUTIVE SUMMARY)
    ယခုအပတ်တွင် AI လောက၌ SearchGPT ၏ ကြော်ငြာစနစ်သစ်နှင့် Meta ၏ Algorithm အပြောင်းအလဲများမှာ အဓိကဖြစ်သည်။ 
    ပြည်တွင်းဈေးကွက်တွင်လည်း Telegram Commerce အားကောင်းလာသည်ကို တွေ့ရပါသည်။
    
    ၂။ ကဏ္ဍအလိုက် ဗျူဟာမြောက် ညွှန်ကြားချက်များ
    
    [CONTENT MARKETING]
    - AI-generated content သက်သက်ထက် လူသားဆန်သော (Authentic) Content များကို ဦးစားပေးပါ။
    - Answer Engine Optimization (AEO) အတွက် ပြင်ဆင်ပါ။
    
    [MEDIA BUYING]
    - Creative is the new Targeting. ကြော်ငြာ၏ Creative ကောင်းမွန်မှုအပေါ် မူတည်၍ AI က Audience ရှာပေးပါလိမ့်မည်။
    - Signal Efficiency ကို မြှင့်တင်ရန် First-party data များကို စနစ်တကျသုံးပါ။
    
    [COMMUNITY & SOCIAL]
    - Facebook တစ်ခုတည်းကို မကိုးစားဘဲ Telegram Community ကို အရန်အဖြစ် တည်ဆောက်ပါ။
    - Dwell Time မြှင့်တင်ရန် Video hooks များကို အားဖြည့်ပါ။
    
    ၃။ အရေးကြီးသော သတိပေးချက် (CRITICAL ALERT)
    လက်ရှိ Algorithm များသည် User ၏ စိတ်ဝင်စားမှု (Interest) ကို အချိန်နှင့်အမျှ ပြောင်းလဲခန့်မှန်းနေသောကြောင့် 
    Content များကို ပုံသေ (Static) မထားဘဲ Dynamic ဖြစ်အောင် ပြင်ဆင်ရန် လိုအပ်ပါသည်။
    
    SAYAR GYI AI STRATEGY ENGINE (v100.0) မှ အတည်ပြုပြီး။
    ----------------------------------------------------------------------
    """
    return report

# --- 4. MAIN INTERFACE ---
def render_main():
    st.markdown('<h1 style="font-weight:900;">Sayar Gyi Intelligence Suite 100</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "🌐 Global Pulse", "🇲🇲 Local Pulse", "🧠 Sayar Gyi's Insight", "📄 Weekly Report"
    ])

    with tab3:
        render_sayar_gyi_insights()

    with tab4:
        st.markdown("### 📄 Weekly Executive Report (Burmese)")
