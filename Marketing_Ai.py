import streamlit as st

# --- 1. SETTINGS & RECOVERY ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v132.0")

def apply_executive_styles():
    st.markdown("""
        <style>
        /* Restore Dashboard Integrity */
        .main .block-container { padding-top: 2rem; max-width: 94%; }
        
        /* v101 Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE COMMANDER ROBOT (FIXED & LARGE) --- */
        div.stButton > button[key="executive_robot"] {
            position: fixed !important;
            bottom: 50px !important;   /* ညာဘက်အောက်ခြေတွင် အသေထားခြင်း */
            right: 50px !important;
            width: 90px !important;    /* အရွယ်အစားကို အကြီးစား ပြုလုပ်ခြင်း */
            height: 90px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #007bff 0%, #00d4ff 100%) !important;
            border: 4px solid #ffffff !important;
            box-shadow: 0 15px 50px rgba(0,0,0,0.7) !important;
            z-index: 999999 !important;
            font-size: 0px !important; /* "AI" စာသားကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
            padding: 0 !important;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        /* 🤖 Emoji ကို ခန့်ညားစွာ အလယ်တွင် ထားခြင်း */
        div.stButton > button[key="executive_robot"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 48px; color: white; visibility: visible;
        }

        div.stButton > button[key="executive_robot"]:hover {
            transform: scale(1.15) rotate(10deg) !important;
            box-shadow: 0 20px 60px rgba(0, 212, 255, 0.5) !important;
        }

        /* မလိုလားအပ်သော အခြား Widget များအားလုံးကို ဖျောက်ခြင်း */
        .stCheckbox, div[data-testid="stCheckbox"], .stToggle { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC CENTER")
def open_strategic_portal():
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
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.chat_history.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_executive_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    # Ensuring Tabs are visible
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Quality Signal ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE EXECUTIVE COMMAND BUTTON ---
    # ခလုတ်နာမည်ကို Emoji တိုက်ရိုက်ပေးထားပြီး CSS ဖြင့် ကြီးအောင်လုပ်ထားပါသည်
    st.button("🤖", key="executive_robot", on_click=open_strategic_portal)

if __name__ == "__main__":
    main()
