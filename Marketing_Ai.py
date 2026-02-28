import streamlit as st

# --- 1. SETTINGS & FORCE STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v133.0")

def apply_v133_force_styles():
    # CSS ဖြင့် အခြေခံ ပုံဖော်ခြင်း
    st.markdown("""
        <style>
        .main .block-container { padding-top: 2rem; }
        
        /* Premium Card Design */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* Target the specific button key */
        div.stButton > button[key="v133_ultra_robot"] {
            position: fixed !important;
            bottom: 50px !important;
            right: 50px !important;
            z-index: 999999 !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            color: white !important;
            border-radius: 50% !important;
            /* JavaScript က လွှမ်းမိုးနိုင်ရန် အောက်ပါတို့ကို JS ဖြင့် ပြင်ပါမည် */
        }

        /* Hide unwanted widgets */
        .stCheckbox, div[data-testid="stCheckbox"], .stToggle { display: none !important; }
        </style>
    """, unsafe_allow_html=True)

    # JavaScript ဖြင့် ခလုတ်အရွယ်အစားကို အတင်းအဓမ္မ ချဲ့ခြင်း
    st.components.v1.html("""
        <script>
        function resizeRobot() {
            const buttons = window.parent.document.querySelectorAll('button');
            buttons.forEach(btn => {
                if (btn.innerText.includes('🤖')) {
                    btn.style.width = '90px';
                    btn.style.height = '90px';
                    btn.style.fontSize = '50px';
                    btn.style.display = 'flex';
                    btn.style.alignItems = 'center';
                    btn.style.justifyContent = 'center';
                    btn.style.borderRadius = '50%';
                }
            });
        }
        // စက္ကန့်အနည်းငယ်ခြားပြီး ခလုတ်ကို ရှာဖွေပြင်ဆင်ရန်
        setTimeout(resizeRobot, 500);
        setInterval(resizeRobot, 2000); 
        </script>
    """, height=0)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_portal():
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
    apply_v133_force_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Signal အတွက် Data Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE ULTRA TRIGGER ---
    # 🤖 စာသားကို တိုက်ရိုက်သုံးထားပြီး JS က အရွယ်အစားကို လှမ်းချဲ့ပါမည်
    st.button("🤖", key="v133_ultra_robot", on_click=open_portal)

if __name__ == "__main__":
    main()
