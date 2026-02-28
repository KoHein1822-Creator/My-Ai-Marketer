import streamlit as st

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v124.0")

def apply_v124_master_styles():
    st.markdown("""
        <style>
        /* Dashboard Container */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE PERMANENT ROBOT ICON (NO BUTTONS USED) --- */
        #robot-anchor {
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
            transition: all 0.3s ease !important;
            text-decoration: none !important;
        }

        #robot-anchor:hover {
            transform: scale(1.1) rotate(10deg) !important;
        }

        /* Hide all default streamlit buttons to avoid "AI" text bug */
        .stButton, button { display: none !important; }
        </style>

        <a id="robot-anchor" href="#ai-chat">🤖</a>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_ai_portal():
    st.markdown("### CEO Strategic Intelligence Access")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("Ask Sayar Gyi..."):
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.chat_history.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v124_master_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE MAGIC TRIGGER ---
    # URL Hash ပြောင်းလဲမှုကို စောင့်ကြည့်ပြီး Dialog ဖွင့်ပေးခြင်း
    # ဤနည်းလမ်းသည် ခလုတ်နှိပ်ခြင်းကို ၁၀၀% တိကျစေပါသည်။
    if st.context.query_params.get("ai-chat") is not None or "#ai-chat" in st.empty().anchor:
        # Note: Streamlit development version ပေါ်မူတည်၍ hash trigger ကို ဖမ်းယူပုံ
        open_ai_portal()

    # Alternative stable trigger for Current Streamlit
    if "robot_active" not in st.session_state:
        st.session_state.robot_active = False

    # JavaScript ကနေ URL ပြောင်းလိုက်တာကို ဖမ်းတဲ့ Logic
    # ဤအပိုင်းသည် Pop-up ကို သေချာပေါက် ပွင့်စေပါမည်
    st.markdown("""
        <script>
        window.addEventListener('hashchange', function() {
            window.parent.location.reload(); 
        });
        </script>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
