import streamlit as st
from datetime import datetime

# --- 1. SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v110.0")

def apply_v110_styles():
    st.markdown("""
        <style>
        /* Container Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Restored Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 800; font-size: 20px; margin-bottom: 10px; }

        /* --- THE BULLETPROOF FLOATING ROBOT BUTTON --- */
        /* Streamlit ရဲ့ Key-based button ကို တိုက်ရိုက် Target ထားပြီး ညာဘက်အောက်ခြေမှာ Fix လုပ်ခြင်း */
        div[data-testid="stButton"] > button[key="robot_trigger_btn"] {
            position: fixed !important;
            bottom: 40px !important;   /* အောက်ခြေကနေ 40px */
            right: 40px !important;    /* ညာဘက်ကနေ 40px (Screenshot 53 အမှားကိုပြင်ရန်) */
            width: 80px !important;
            height: 80px !important;
            border-radius: 20px !important;
            background-color: #1f6feb !important;
            border: 2px solid #58a6ff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
            z-index: 999999 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            transition: all 0.3s ease !important;
        }

        /* Robot Icon ကို စာသားအစား Emoji နဲ့ အစားထိုးခြင်း */
        div[data-testid="stButton"] > button[key="robot_trigger_btn"] p {
            display: none !important; /* "AI" ဆိုတဲ့ စာသားကို ဖျောက်ထားရန် */
        }
        div[data-testid="stButton"] > button[key="robot_trigger_btn"]::after {
            content: "🤖";
            font-size: 40px;
        }

        div[data-testid="stButton"] > button[key="robot_trigger_btn"]:hover {
            transform: scale(1.1) !important;
            background-color: #388bfd !important;
            box-shadow: 0 15px 40px rgba(56, 139, 253, 0.4) !important;
        }

        /* Report Style */
        .v101-report-box {
            background: #0d1117; border: 1px solid #30363d; padding: 40px;
            border-radius: 12px; color: #adbac7; line-height: 1.8;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_ai_dialog():
    st.markdown("### CEO Direct Line")
    st.write("ဗျူဟာမြောက် မေးခွန်းများကို ဤနေရာတွင် မေးမြန်းနိုင်ပါသည်။")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Ask Sayar Gyi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            response = f"CEO ခင်ဗျာ၊ '{prompt}' နှင့် ပတ်သက်၍ ကျွန်တော်၏ ဗျူဟာမြောက် သုံးသပ်ချက်မှာ..."
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 3. MAIN APP ---
def main():
    apply_v110_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><div class="v101-header">🖋️ Content & AEO Mastery</div><p>AI Answers မှာ နေရာရဖို့ Q&A Content တွေ ပြင်ဆင်ပါ။</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><div class="v101-header">🎯 Media Buying: Signals</div><p>Creative အရည်အသွေးနဲ့ Signal Data ကို ဦးစားပေးပါ။</p></div>', unsafe_allow_html=True)

    with tabs[3]:
        st.markdown('<div class="v101-report-box">Weekly Report Summary: v101 Design Restored.</div>', unsafe_allow_html=True)

    # --- THE FLOATING ROBOT TRIGGER ---
    # CSS က ဒီ Button ကို ဖမ်းပြီး ညာဘက်အောက်ခြေမှာ 🤖 အနေနဲ့ ပြပေးမှာပါ။
    if st.button("AI", key="robot_trigger_btn"):
        open_ai_dialog()

if __name__ == "__main__":
    main()
