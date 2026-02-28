import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. PREMIUM STYLES & LAYOUT ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v102.0")

def apply_v102_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* Insight Card Styling */
        .insight-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 20px; border-top: 5px solid #58a6ff;
        }
        .insight-header { color: #58a6ff; font-weight: 800; font-size: 20px; margin-bottom: 12px; }
        
        /* Deep Dive Box (Detailed Mode) */
        .deep-dive-box {
            background: rgba(88, 166, 255, 0.05); border: 1px dashed #58a6ff;
            padding: 20px; border-radius: 10px; margin-top: 15px; font-size: 14px; color: #adbac7;
        }

        /* Executive Report Visual Style */
        .executive-report {
            background: #ffffff; color: #1e293b; padding: 60px; border-radius: 8px;
            box-shadow: 0 20px 50px rgba(0,0,0,0.3); border-top: 10px solid #1e293b;
            font-family: 'Inter', 'Pyidaungsu', sans-serif; max-width: 900px; margin: auto;
        }
        .report-header { border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; margin-bottom: 30px; text-align: center; }
        .report-section-title { color: #1e40af; border-left: 5px solid #1e40af; padding-left: 15px; font-weight: bold; margin-top: 25px; margin-bottom: 15px; font-size: 18px; }
        .action-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        .action-table th { background: #f8fafc; text-align: left; padding: 10px; border: 1px solid #e2e8f0; }
        .action-table td { padding: 10px; border: 1px solid #e2e8f0; font-size: 14px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE INTELLIGENT INSIGHT ENGINE ---
def render_insight_hub():
    st.markdown("### 🧠 Sayar Gyi's Strategic Insights")
    st.caption("Detailed Mode ကိုနှိပ်၍ နည်းပညာပိုင်းဆိုင်ရာ အကျယ်တဝင့် လေ့လာနိုင်ပါသည်။")
    
    col1, col2 = st.columns(2)

    with col1:
        # Perspective: AEO
        with st.container():
            st.markdown("""<div class="insight-card">
                <div class="insight-header">🖋️ Content Strategy: The AEO Shift</div>
                <p style="color:#adbac7;">Search Engine Optimization မှ <b>Answer Engine Optimization (AEO)</b> သို့ ကူးပြောင်းခြင်း။</p>
                <p style="font-size:13px; color:#8b949e;"><b>Impact:</b> User များသည် Google Link များအစား AI ၏ အဖြေကိုသာ တိုက်ရိုက်ဖတ်တော့မည်။</p>
            </div>""", unsafe_allow_html=True)
            with st.expander("🔍 Detailed Explanation Mode (အကျယ်တဝင့်ရှင်းပြချက်)"):
                st.markdown("""
                <div class="deep-dive-box">
                    <b>ဘာကြောင့် ဒါက အရေးကြီးတာလဲ?</b><br>
                    AI Answer Engines (ChatGPT, Perplexity) တွေက ကိုယ့် Website ထဲက အချက်အလက်တွေကို ဆွဲယူပြီး အဖြေထုတ်ပေးတာပါ။ 
                    အကယ်၍ ကိုယ့် Content က 'Structured' မဖြစ်ရင် AI က ကိုယ့် Brand အကြောင်းကို ချန်လှပ်ထားခဲ့ပါလိမ့်မယ်။<br><br>
                    <b>ဘယ်လိုပြင်ဆင်မလဲ?</b><br>
                    ၁။ Content တွေကို Q&A ပုံစံ (မေးခွန်းနှင့်အဖြေ) များများရေးပါ။<br>
                    ၂။ Schema Markup လို့ခေါ်တဲ့ နည်းပညာပိုင်းဆိုင်ရာ အချက်အလက်တွေကို Website ထဲမှာ ထည့်သွင်းပါ။<br>
                    ၃။ AI က ကိုးကားလို့ရမယ့် ခိုင်မာတဲ့ အချက်အလက် (Statistics) တွေ ပါဝင်ပါစေ။
                </div>
                """, unsafe_allow_html=True)

    with col2:
        # Perspective: Media Buying
        with st.container():
            st.markdown("""<div class="insight-card" style="border-top-color: #f85149;">
                <div class="perspective-title">🎯 Media Buying: Signal over Targeting</div>
                <p style="color:#adbac7;">Targeting ရွေးချယ်ခြင်းထက် <b>Data Signals</b> ကျွေးခြင်းက ပိုမိုအရေးကြီးလာသည်။</p>
                <p style="font-size:13px; color:#8b949e;"><b>Impact:</b> AI ကောင်းကောင်း အလုပ်လုပ်နိုင်ရန် Customer အမှန်များ၏ Data (Signals) လိုအပ်သည်။</p>
            </div>""", unsafe_allow_html=True)
            with st.expander("🔍 Detailed Explanation Mode (အကျယ်တဝင့်ရှင်းပြချက်)"):
                st.markdown("""
                <div class="deep-dive-box">
                    <b>Targeting မလိုတော့ဘူးဆိုတာ ဟုတ်လား?</b><br>
                    ဟုတ်ပါတယ်။ Meta ရဲ့ Advantage+ လိုစနစ်တွေမှာ လူကိုယ်တိုင် Target သွားရွေးတာထက် AI ကို လွှတ်ထားတာက ပိုထိရောက်ပါတယ်။ ဒါပေမယ့် AI က ဘယ်သူ့ကိုရှာရမလဲ သိဖို့အတွက် <b>'Signals'</b> လိုပါတယ်။<br><br>
                    <b>CEO အနေနဲ့ ဘာကို စစ်ဆေးရမလဲ?</b><br>
                    - Marketing Team က Website Pixel တွေ၊ API တွေ ကောင်းကောင်းတပ်ထားရဲ့လား?<br>
                    - ကိုယ့်ဆီမှာရှိတဲ့ ဖောက်သည်ဖုန်းနံပါတ်စာရင်း (Offline Conversions) တွေကို AI ထဲ ပြန်ကျွေးနေရဲ့လား? ဆိုတာကို စစ်ဆေးရပါမယ်။
                </div>
                """, unsafe_allow_html=True)

# --- 3. THE EXECUTIVE VISUAL REPORT ---
def render_visual_report():
    today = datetime.now().strftime("%d %B %Y")
    
    st.markdown(f"""
    <div class="executive-report">
        <div class="report-header">
            <h1 style="margin:0; color:#1e293b;">EXECUTIVE INTELLIGENCE MEMO</h1>
            <p style="color:#64748b; font-weight:bold;">CONFIDENTIAL | DATE: {today}</p>
        </div>
        
        <div class="report-section-title">၁။ အမှုဆောင်အနှစ်ချုပ် (EXECUTIVE SUMMARY)</div>
        <p>ယခုအပတ်အတွင်း AI နည်းပညာ၏ အပြောင်းအလဲများသည် Marketing ကဏ္ဍတွင် <b>Answer Engine Optimization</b> ကို မဖြစ်မနေ လုပ်ဆောင်ရန် တွန်းအားပေးနေပါသည်။ ပြည်တွင်း၌ <b>Digital Fatigue</b> ကြောင့် User များသည် ပုံသေကြော်ငြာများထက် ရိုးသားသော တင်ဆက်မှု (Authentic Content) ကို ပိုမိုတုံ့ပြန်လျက်ရှိသည်။</p>

        <div class="report-section-title">၂။ ဗျူဟာမြောက် လုပ်ဆောင်ချက်များ (ACTION GRID)</div>
        <table class="action-table">
            <tr style="background:#f1f5f9;">
                <th>Strategic Pillar</th>
                <th>Priority Action</th>
                <th>Expected Impact</th>
            </tr>
            <tr>
                <td><b>Content</b></td>
                <td>Transition to AEO (Q&A style)</td>
                <td>Higher AI Citation</td>
            </tr>
            <tr>
                <td><b>Media Buying</b></td>
                <td>Signal Data Integration</td>
                <td>30% Better Ad Efficiency</td>
            </tr>
            <tr>
                <td><b>Community</b></td>
                <td>Telegram/Viber VIP Group</td>
                <td>Owned Audience Resilience</td>
            </tr>
        </table>

        <div class="report-section-title">၃။ ဆရာကြီး၏ အကြံပြုချက် (SAYAR GYI'S COMMAND)</div>
        <p style="background:#f0f9ff; padding:15px; border-radius:5px; border:1px solid #bae6fd;">
            "နည်းပညာတွေ ဘယ်လောက်ပြောင်းပြောင်း လူသားတွေရဲ့ <b>ယုံကြည်မှု (Trust)</b> ကသာ အရောင်းကို အဆုံးအဖြတ်ပေးမှာပါ။ AI ကို အသုံးချပြီး အလုပ်လုပ်ပါ၊ ဒါပေမယ့် Content မှာတော့ လူသားဆန်တဲ့ စိတ်ခံစားမှုကို မပျောက်ပျက်ပါစေနဲ့။"
        </p>
        
        <div style="margin-top:40px; text-align:right; color:#64748b; font-style:italic;">
            <p>Certified by Sayar Gyi Strategy Engine v102.0</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Download functionality
    st.write("")
    st.download_button("📩 Download Professional Report (PDF/Print Ready)", "Report Content Placeholder", file_name="Executive_Report.txt")

# --- 4. EXECUTION ---
def main():
    apply_v102_styles()
    st.markdown('<h1 style="font-weight:900;">Sayar Gyi Intelligence Suite</h1>', unsafe_allow_html=True)
    
    tab_news, tab_local, tab_insight, tab_report = st.tabs([
        "🌐 Global News", "🇲🇲 Local Pulse", "🧠 Sayar Gyi's Insight", "📄 Executive Report"
    ])

    with tab_insight:
        render_insight_hub()
    
    with tab_report:
        render_visual_report()

if __name__ == "__main__":
    main()
