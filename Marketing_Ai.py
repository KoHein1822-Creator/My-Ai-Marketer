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
        with st.chat_
