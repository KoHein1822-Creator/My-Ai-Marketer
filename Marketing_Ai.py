import streamlit as st
import pandas as pd
from datetime import datetime

# --- 1. PREMIUM DARK UI & FLOATING POSITIONING ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v107.0")

def apply_v107_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* v101 Restored Insight Cards (CEO's Favorite) */
        .v101-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 900; font-size: 20px; margin-bottom: 12px; }
        
        /* --- THE ADVANCED FLOATING ROBOT BUTTON --- */
        div[data-testid="stButton"]:last-of-type {
            position: fixed;
            bottom: 60px; /* ဒေါင့်ကနေ အပေါ်နည်းနည်းတက် */
            right: 60px;  /* ဘေးဘောင်ကနေ နည်းနည်းခွာ */
            z-index: 99999;
        }
        
        div[data-testid="stButton"]:last-of-type > button {
            width: 85px;
            height: 85px;
            border-radius: 25px; /* Square with rounded corners for a modern tech look */
            background: #161b22;
            border: 2px solid #58a6ff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6), 0 0 20px rgba(88, 166, 255, 0.3);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            padding: 0;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        
        /* Modern Android/Robot Icon Styling */
        div[data-testid="stButton"]:last-of-type > button p {
            font-size: 42px;
            margin: 0;
            filter: drop-shadow(0 0 5px #58a6ff);
        }
        
        div[data-testid="stButton"]:last-of-type > button:hover {
            transform: scale(1.15) rotate(5deg);
            border-color: #bc8cff; /* Color shift on hover */
            box-shadow: 0 15px 40px rgba(188, 140, 255, 0.5);
        }
        
        /* Report Style */
        .v101-report-box {
            background: #0d1117; border: 1px solid #30363d; padding: 45px;
            border-radius: 12px; line-height: 1.8; color: #adbac7;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE INTELLIGENT COMMAND CENTER (POP-UP) ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC COMMAND")
def open_strategic_ai():
    st.markdown("### CEO's Direct Intelligence Access")
    st.write("Marketing, Media Buying နှင့် Content Strategy ဆိုင်ရာများကို တိကျစွာ မေးမြန်းနိုင်ပါသည်။")
    
    # Session state for chat-like experience
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history in popup
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Input for new question
    if prompt := st.chat_input("ဗျူဟာမြောက် မေးခွန်းတစ်ခု မေးပါ..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing data & formulating strategy..."):
                # AI Logic: Here we simulate a deep expert response
                response = f"CEO ခင်ဗျာ၊ '{prompt}' နဲ့ ပတ်သက်ပြီး ကျွန်တော် သုံးသပ်ပေးပါမယ်။ Marketing ရှုထောင့်ကကြည့်ရင် ဒါက အခုဖြစ်နေတဲ့ trend တွေနဲ့ ဘယ်လိုချိတ်ဆက်နေလဲဆိုတော့..."
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

# --- 3. MAIN INTERFACE ---
def main():
    apply_v107_styles()
    
    st.markdown('<h1 style="font-weight:900;">Sayar Gyi Mastermind Suite</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tab3:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("""<div class="v101-card">
                <div class="v101-header">🖋️ Content & AEO Mastery</div>
                <p style="color:#adbac7;"><b>Focus:</b> Google Search ထက် AI Answers (AEO) မှာ နေရာရဖို့ ဦးစားပေးပါ။</p>
            </div>""", unsafe_allow_html=True)
        with col2:
            st.markdown("""<div class="v101-card" style="border-left-color: #f85149;">
                <div class="v101-header">🎯 Media Buying: High-Signal Data</div>
                <p style="color:#adbac7;"><b>Focus:</b> Manual Targeting ထက် AI ကို Signal Data အမှန်ပေးဖို့ အလေးထားပါ။</p>
            </div>""", unsafe_allow_html=True)

    with tab4:
        today = datetime.now().strftime("%d %B, %Y")
        st.markdown(f'<div class="v101-report-box"><b>WEEKLY REPORT: {today}</b><br><br>၁။ Content အရည်အသွေးမြှင့်တင်ပါ။<br>၂။ Telegram Community ကို အားကောင်းအောင်လုပ်ပါ။<br>၃။ Creative testing ကို အရှိန်မြှင့်ပါ။</div>', unsafe_allow_html=True)

    # THE TRIGGER (Floating Robot Button)
    # 🤖 (Robot) အစား 🦾 (Bionic Arm) သို့မဟုတ် ⚙️ (Gear) စတဲ့ icon တွေကိုလည်း စမ်းကြည့်နိုင်ပါတယ်
    # အခုကတော့ ပိုပြီး Smart ကျတဲ့ Robot Icon ကို Spacing မှန်မှန်နဲ့ ထည့်ပေးထားပါတယ်။
    st.write("") 
    if st.button("🤖", key="master_ai_trigger"):
        open_strategic_ai()

if __name__ == "__main__":
    main()
