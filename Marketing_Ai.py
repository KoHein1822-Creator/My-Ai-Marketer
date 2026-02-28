import streamlit as st

# --- 1. GLOBAL SETTINGS & DESIGN ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v125.0")

def apply_v125_styles():
    st.markdown("""
        <style>
        /* Dashboard Container */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE FLOATING ROBOT BUTTON (NO MORE AI TEXT) --- */
        div.stButton > button[key="robot_final_trigger"] {
            position: fixed !important;
            bottom: 60px !important;  /* Screenshot 59 အတိုင်း ညာဘက်အောက်ခြေ */
            right: 60px !important;
            left: auto !important;
            width: 85px !important;
            height: 85px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8) !important;
            z-index: 1000000 !important;
            color: transparent !important; /* "AI" စာသားကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
            font-size: 0px !important;
            padding: 0 !important;
        }

        /* စက်ရုပ် Emoji အား ခလုတ်အလယ်တွင် ထည့်ခြင်း */
        div.stButton > button[key="robot_final_trigger"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 45px; color: white; visibility: visible;
        }

        div.stButton > button[key="robot_final_trigger"]:hover {
            transform: scale(1.1) rotate(5deg) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }

        /* မလိုလားအပ်သော Widget များနှင့် အမှန်ခြစ်များအားလုံးကို ဖျောက်ခြင်း */
        .stCheckbox, div[data-testid="stCheckbox"], .stToggle, div[data-testid="stToggle"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_ai_portal():
    st.markdown("### CEO Strategic Intelligence Access")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ..."):
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် အကြံပြုချက်ကတော့..."
            st.write(ans)
            st.session_state.chat_history.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v125_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE DIRECT TRIGGER (NO REDIRECTION) ---
    # Standard Button ကို သုံးထားသော်လည်း CSS ဖြင့် 🤖 အဖြစ် ပြောင်းလဲထားပါသည်
    # Error မတက်စေရန် ရိုးရှင်းသော on_click ကိုသာ သုံးထားပါသည်
    st.button("AI", key="robot_final_trigger", on_click=open_ai_portal)

if __name__ == "__main__":
    main()
