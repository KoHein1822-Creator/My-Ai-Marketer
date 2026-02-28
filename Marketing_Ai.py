import streamlit as st

# --- 1. GLOBAL SETTINGS & STABLE POSITIONING ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v118.0")

def apply_v118_final_styles():
    st.markdown("""
        <style>
        /* Main Theme Spacing */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE ARCHITECTURAL ROBOT BUTTON (STABLE & SMART) --- */
        /* div.stButton ကို တိုက်ရိုက် Target ထားပြီး ညာဘက်အောက်ခြေတွင် Fix လုပ်ခြင်း */
        div.stButton > button[key="v118_final_robot"] {
            position: fixed !important;
            bottom: 60px !important;
            right: 60px !important;
            left: auto !important;
            width: 85px !important;
            height: 85px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.7) !important;
            z-index: 999999 !important;
            
            /* "AI" စာသားကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
            color: rgba(0,0,0,0) !important;
            font-size: 0px !important;
            line-height: 0 !important;
            padding: 0 !important;
        }

        /* စက်ရုပ် Emoji ကို အလယ်တည့်တည့်တွင် ထည့်ခြင်း */
        div.stButton > button[key="v118_final_robot"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 45px; color: white; visibility: visible;
        }

        div.stButton > button[key="v118_final_robot"]:hover {
            transform: scale(1.1) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def show_ai_portal():
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
    apply_v118_final_styles()
    
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
    # ခလုတ်နှိပ်လိုက်လျှင် Dialog တန်းပွင့်စေရန် session_state ကို အသုံးမပြုဘဲ Direct Trigger သုံးထားပါသည်
    if st.button("AI", key="v118_final_robot"):
        show_ai_portal()

if __name__ == "__main__":
    main()
