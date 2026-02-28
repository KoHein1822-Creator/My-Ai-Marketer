import streamlit as st

# --- 1. GLOBAL SETTINGS & TRUE FLOATING UI ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v123.0")

def apply_v123_final_styles():
    # ဤ HTML/JS သည် စက်ရုပ် Icon ကိုနှိပ်လိုက်ပါက Pop-up ကို တိုက်ရိုက်ပွင့်စေမည်
    st.markdown("""
        <style>
        /* Main Dashboard Container */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE MASTER ROBOT ICON --- */
        #master-robot-btn {
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
            z-index: 1000000 !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8) !important;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
        }

        #master-robot-btn:hover {
            transform: scale(1.1) rotate(10deg) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }

        /* မလိုလားအပ်သော Widget များနှင့် Checkbox များအားလုံးကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
        .stCheckbox, div[data-testid="stCheckbox"], .stButton, button {
            display: none !important;
        }
        </style>

        <div id="master-robot-btn" onclick="triggerPopUp()">
            🤖
        </div>

        <script>
        function triggerPopUp() {
            // Invisible trigger button ကို နှိပ်ရန် JavaScript အမိန့်ပေးခြင်း
            const hiddenBtn = window.parent.document.querySelector('button[key="hidden_trigger"]');
            if (hiddenBtn) {
                hiddenBtn.click();
            }
        }
        </script>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_strategic_dialog():
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
    apply_v123_final_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> Data Signal Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE INVISIBLE BRIDGE ---
    # ဤ Button သည် UI တွင် မပေါ်ဘဲ စက်ရုပ် Icon ကိုနှိပ်မှ Dialog ကို တိုက်ရိုက်ခေါ်ပေးမည်
    st.button("Trigger", key="hidden_trigger", on_click=open_strategic_dialog)

if __name__ == "__main__":
    main()
