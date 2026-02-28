import streamlit as st
from datetime import datetime

# --- 1. SETTINGS & RADICAL CSS OVERRIDE ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v112.0")

def apply_v112_styles():
    st.markdown("""
        <style>
        /* Main UI Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Restored Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE ULTIMATE FLOATING ROBOT OVERRIDE --- */
        /* Streamlit ရဲ့ ခလုတ်တည်ဆောက်ပုံ အဆင့်ဆင့်ကို လိုက်ဖမ်းခြင်း */
        
        /* ၁။ ခလုတ်တစ်ခုလုံးကို ညာဘက်အောက်ခြေမှာ Fix လုပ်ခြင်း */
        div.stButton {
            position: fixed !important;
            bottom: 50px !important;
            right: 50px !important;
            z-index: 999999 !important;
        }

        /* ၂။ ခလုတ်ရဲ့ ပုံပန်းသဏ္ဍာန်ကို စက်ဝိုင်းပုံစံပြောင်းပြီး Gradient ထည့်ခြင်း */
        div.stButton > button {
            width: 90px !important;
            height: 90px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.8), 0 0 20px rgba(0, 212, 255, 0.4) !important;
            padding: 0 !important;
            margin: 0 !important;
            overflow: visible !important;
        }

        /* ၃။ "AI" ဆိုတဲ့ စာသားကို လုံးဝ (လုံးဝ) ပျောက်သွားအောင်လုပ်ခြင်း */
        div.stButton > button p {
            display: none !important;
            visibility: hidden !important;
            opacity: 0 !important;
        }

        /* ၄။ စက်ရုပ် Emoji ကို ခလုတ်အလယ်မှာ အကြီးကြီး ထည့်သွင်းခြင်း */
        div.stButton > button::after {
            content: "🤖";
            font-size: 50px !important;
            display: block !important;
            line-height: 90px !important;
            text-align: center !important;
            width: 100% !important;
        }

        /* ၅။ Hover လုပ်ရင် ပိုပြီး Futuristic ဖြစ်အောင်လုပ်ခြင်း */
        div.stButton > button:hover {
            transform: scale(1.1) rotate(5deg) !important;
            border-color: #00d4ff !important;
            box-shadow: 0 20px 50px rgba(0, 212, 255, 0.6) !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC COMMAND")
def open_ai_dialog():
    st.markdown("### CEO Intelligence Portal")
    st.write("ဗျူဟာမြောက် မေးခွန်းများကို ဤနေရာတွင် မေးမြန်းနိုင်ပါသည်။")
    
    query = st.chat_input("Ask Sayar Gyi...")
    if query:
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            st.write(f"CEO ခင်ဗျာ၊ '{query}' နဲ့ ပတ်သက်တဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့...")

# --- 3. DASHBOARD MAIN ---
def main():
    apply_v112_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>Content Strategy:</b> AI Search Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ad Strategy:</b> Data Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE TRIGGER BUTTON ---
    # ဒီခလုတ်ကို ဘယ်နေရာမှာပဲ ရေးရေး CSS က ညာဘက်အောက်ခြေကို ဆွဲခေါ်သွားပါလိမ့်မယ်။
    # "AI" ဆိုတဲ့ စာသားက CSS ကြောင့် ပျောက်သွားပြီး စက်ရုပ်ရုပ်ပဲ ကျန်ပါမယ်။
    st.button("AI", key="robot_final_trigger", on_click=open_ai_dialog)

if __name__ == "__main__":
    main()
