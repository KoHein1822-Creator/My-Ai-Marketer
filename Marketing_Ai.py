import streamlit as st
from datetime import datetime

# --- 1. GLOBAL SETTINGS & SMART FLOATING CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v113.0")

def apply_v113_styles():
    st.markdown("""
        <style>
        /* Overall Dashboard Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Restored Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE SMART FLOATING ROBOT (STABLE POSITION) --- */
        /* div.stButton ကို တိုက်ရိုက်မကိုင်ဘဲ Button Element ကိုပဲ သီးသန့် Fixed လုပ်ခြင်း */
        
        button[key="robot_smart_trigger"] {
            position: fixed !important;
            bottom: 40px !important;
            right: 40px !important;  /* ညာဘက်သို့ သေချာရွှေ့ထားခြင်း */
            left: auto !important;   /* ဘယ်ဘက်ရောက်နေတဲ့ default ကို override လုပ်ခြင်း */
            width: 85px !important;
            height: 85px !important;
            border-radius: 50% !important;
            background: rgba(31, 111, 235, 0.2) !important;
            backdrop-filter: blur(10px) !important; /* Glassmorphism Effect */
            border: 2px solid #58a6ff !important;
            box-shadow: 0 0 20px rgba(88, 166, 255, 0.4) !important;
            z-index: 1000000 !important;
            padding: 0 !important;
            cursor: pointer !important;
            animation: pulse-blue 2s infinite !important;
        }

        /* Pulse Animation for Smart Look */
        @keyframes pulse-blue {
            0% { box-shadow: 0 0 0 0 rgba(88, 166, 255, 0.7); }
            70% { box-shadow: 0 0 0 15px rgba(88, 166, 255, 0); }
            100% { box-shadow: 0 0 0 0 rgba(88, 166, 255, 0); }
        }

        /* "AI" စာသားကို ဖျောက်ပြီး Robot Emoji တင်ခြင်း */
        button[key="robot_smart_trigger"] p {
            display: none !important;
        }
        button[key="robot_smart_trigger"]::after {
            content: "🤖";
            font-size: 45px !important;
            line-height: 85px !important;
            display: block !important;
        }

        button[key="robot_smart_trigger"]:hover {
            transform: scale(1.1) !important;
            background: rgba(31, 111, 235, 0.4) !important;
            border-color: #bc8cff !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. STRATEGIC AI DIALOG ---
@st.dialog("🦾 SAYAR GYI STRATEGIC COMMAND")
def open_ai_command():
    st.markdown("### CEO Strategic Intelligence Access")
    if "chat_log" not in st.session_state:
        st.session_state.chat_log = []

    for msg in st.session_state.chat_log:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ..."):
        st.session_state.chat_log.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် အကြံပြုချက်ကတော့..."
            st.write(ans)
            st.session_state.chat_log.append({"role": "assistant", "content": ans})

# --- 3. DASHBOARD MAIN ---
def main():
    apply_v113_styles()
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>Content Strategy:</b> AI Search Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ad Strategy:</b> Data Signal Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE TRIGGER BUTTON ---
    # CSS မှာ 'left: auto' နဲ့ 'right: 40px' ပေးထားလို့ ညာဘက်အောက်ခြေမှာပဲ သေချာပေါက် ပေါ်နေပါမယ်။
    st.button("AI", key="robot_smart_trigger", on_click=open_ai_command)

if __name__ == "__main__":
    main()
