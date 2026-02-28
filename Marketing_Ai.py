import streamlit as st

# --- 1. SETTINGS & STABLE UI ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v131.0")

def apply_final_styles():
    st.markdown("""
        <style>
        /* Restore all Main Dashboard visibility */
        .main .block-container { 
            display: block !important; 
            visibility: visible !important; 
            padding-top: 2rem; 
        }
        
        /* v101 Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE CLEAN FLOATING ROBOT (STRICTLY NO "AI" TEXT) --- */
        div.stButton > button[key="final_robot_trigger"] {
            position: fixed !important;
            bottom: 40px !important;
            right: 40px !important;
            width: 75px !important;
            height: 75px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 2px solid #ffffff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
            z-index: 1000000 !important;
            font-size: 35px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            padding: 0 !important;
            color: white !important;
        }

        div.stButton > button[key="final_robot_trigger"]:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 15px 40px rgba(88, 166, 255, 0.4) !important;
        }

        /* Remove all other experimental toggles/buttons */
        .stCheckbox, .stToggle, div[data-testid="stCheckbox"] { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_ai_dialog():
    st.markdown("### CEO Strategic Intelligence Access")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_final_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    # 100% Guaranteed to show Tabs back
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE DIRECT TRIGGER ---
    # ခလုတ်နာမည်ကို Emoji တိုက်ရိုက်ပေးထားလို့ စာသားကြီး ပေါ်မလာနိုင်တော့ပါ
    st.button("🤖", key="final_robot_trigger", on_click=open_ai_dialog)

if __name__ == "__main__":
    main()
