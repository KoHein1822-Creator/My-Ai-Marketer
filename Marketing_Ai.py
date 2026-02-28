import streamlit as st
from datetime import datetime

# --- 1. SETTINGS & CSS (FORCE OVERRIDE) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v111.0")

def apply_v111_styles():
    st.markdown("""
        <style>
        /* Main Theme Overrides */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Card Aesthetics */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE FINAL FLOATING ROBOT BUTTON FIX --- */
        /* ဒီ CSS က Streamlit ရဲ့ ဘယ် version မှာမဆို ခလုတ်ကို ညာဘက်အောက်ခြေ ရွှေ့ပေးမှာပါ */
        div[data-testid="stBaseButton-secondary"] {
            position: fixed !important;
            bottom: 40px !important;
            right: 40px !important;
            z-index: 999999 !important;
        }

        button[key="robot_trigger_btn"] {
            width: 80px !important;
            height: 80px !important;
            border-radius: 50% !important; /* စက်ဝိုင်းပုံစံပြောင်းလဲခြင်း */
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8) !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 0 !important;
        }

        /* "AI" စာသားကို ဖျောက်ပြီး Robot Emoji ကို အကြီးကြီး တင်ခြင်း */
        button[key="robot_trigger_btn"] p {
            display: none !important;
        }
        
        button[key="robot_trigger_btn"]::before {
            content: "🤖";
            font-size: 45px !important;
            line-height: 1 !important;
        }

        /* Hover Effect */
        button[key="robot_trigger_btn"]:hover {
            transform: scale(1.1) rotate(10deg) !important;
            box-shadow: 0 15px 45px rgba(88, 166, 255, 0.6) !important;
            border-color: #bc8cff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC AI")
def open_ai_dialog():
    st.markdown("### CEO Intelligence Portal")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        with st.chat_message("assistant"):
            response = f"CEO ခင်ဗျာ၊ '{prompt}' အတွက် ကျွန်တော်၏ သုံးသပ်ချက်မှာ..."
            st.write(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# --- 3. DASHBOARD MAIN ---
def main():
    apply_v111_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>Content Strategy:</b> AI Answer Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ad Strategy:</b> Signal Data Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE ROBOT TRIGGER ---
    # ဒီနေရာမှာ Button ကို ဘယ်နေရာမှာပဲထားထား CSS က ညာဘက်အောက်ခြေကို ဆွဲခေါ်သွားပါလိမ့်မယ်
    if st.button("AI", key="robot_trigger_btn"):
        open_ai_dialog()

if __name__ == "__main__":
    main()
