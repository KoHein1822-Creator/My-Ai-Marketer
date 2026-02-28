import streamlit as st

# --- 1. GLOBAL SETTINGS & SMOOTH UI ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v117.0")

def apply_v117_styles():
    st.markdown("""
        <style>
        /* Dashboard Container */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE PERFECT FLOATING ROBOT (CSS ONLY FOR STYLE) --- */
        /* Streamlit Button ကို ညာဘက်အောက်ခြေမှာ သပ်ရပ်စွာ နေရာချခြင်း */
        div.stButton > button[key="seamless_robot_btn"] {
            position: fixed !important;
            bottom: 55px !important;  /* Screenshot 59 ထက် နည်းနည်းပိုမြှင့်ထားသည် */
            right: 55px !important;   /* ဘေးဘောင်မှ နည်းနည်းခွာပေးထားသည် */
            width: 85px !important;
            height: 85px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.7) !important;
            z-index: 1000000 !important;
            color: transparent !important;
            padding: 0 !important;
        }

        /* Emoji Icon အား ခလုတ်အလယ်တွင် ထည့်ခြင်း */
        div.stButton > button[key="seamless_robot_btn"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 45px; color: white; visibility: visible;
        }

        div.stButton > button[key="seamless_robot_btn"]:hover {
            transform: scale(1.1) rotate(5deg) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }
        
        /* Dialog Box Styling (Notion-style Dark) */
        div[data-testid="stDialog"] {
            background-color: #0d1117 !important;
            border: 1px solid #30363d !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE SEAMLESS AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_seamless_ai():
    st.markdown("### CEO Strategic Intelligence Access")
    st.write("ကျွန်တော် (Gemini) သည် CEO သိလိုသမျှကို တိကျစွာ ဆွေးနွေးပေးပါမည်။")
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Chat Display
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Instant Query Input
    if prompt := st.chat_input("ဗျူဟာမြောက် မေးခွန်းတစ်ခု မေးပါ..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            # ကျွန်တော် Gemini က တိုက်ရိုက်အဖြေပေးမည်
            response = f"CEO ခင်ဗျာ၊ '{prompt}' အတွက် Marketing ရှုထောင့်ကနေ ကျွန်တော့်ရဲ့ အကြံပြုချက်ကတော့..."
            st.write(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v117_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><p style="color:#58a6ff; font-weight:bold;">AEO Strategy</p><p>AI Search မှာ CEO ရဲ့ Brand ကို Citation ရအောင် content များကို Q&A ပုံစံ ပြင်ဆင်ပါ။</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><p style="color:#f85149; font-weight:bold;">Ads Strategy</p><p>AI Signal အတွက် ရှင်းလင်းသော Conversion Data ပေးပို့ပါ။</p></div>', unsafe_allow_html=True)

    # --- THE TRIGGER ---
    # Tab အသစ်မပွင့်စေရန် on_click function ကို တိုက်ရိုက်ချိတ်ဆက်ထားပါသည်
    st.button("AI", key="seamless_robot_btn", on_click=open_seamless_ai)

if __name__ == "__main__":
    main()
