import streamlit as st

# --- 1. GLOBAL SETTINGS & STABLE UI ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v122.0")

def apply_v122_styles():
    # ဒီ HTML/JS က "AI" စာသားခလုတ်ကို အသုံးမပြုဘဲ 🤖 ကို ညာဘက်အောက်ခြေမှာ အသေနေရာချပေးမှာပါ
    st.markdown("""
        <div id="robot-trigger" onclick="window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*')">
            🤖
        </div>

        <style>
        /* Main UI Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE UNSHAKABLE ROBOT FAB (NO BUTTON USED) --- */
        #robot-trigger {
            position: fixed !important;
            bottom: 60px !important;
            right: 60px !important;
            width: 85px !important;
            height: 85px !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border-radius: 50% !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 45px !important;
            cursor: pointer !important;
            z-index: 9999999 !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8) !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
            user-select: none !important;
        }

        #robot-trigger:hover {
            transform: scale(1.1) rotate(10deg) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }

        /* Streamlit ရဲ့ မလိုလားအပ်တဲ့ Standard Button တွေအားလုံးကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
        .stButton, button { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC COMMAND")
def open_strategic_portal():
    st.markdown("### CEO Intelligence Access")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("Ask Sayar Gyi..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v122_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို Q&A ပုံစံ ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE INVISIBLE TRIGGER ---
    # HTML Robot ကို နှိပ်လိုက်ရင် ဒီ toggle က 'True' ဖြစ်သွားပြီး Dialog ပွင့်လာမှာပါ
    if st.checkbox("Trigger", key="robot_gate", label_visibility="hidden"):
        open_strategic_portal()
        # Dialog ပိတ်သွားရင် ပြန် Reset လုပ်ဖို့ (Optional)
        # st.session_state.robot_gate = False

if __name__ == "__main__":
    main()
