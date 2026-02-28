import streamlit as st
from datetime import datetime

# --- 1. GLOBAL SETTINGS & TRUE FLOATING CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v108.0")

def apply_v108_styles():
    st.markdown("""
        <style>
        /* Container Spacing */
        .block-container { padding-top: 2rem; max-width: 94%; }
        
        /* v101 Restored Cards */
        .v101-card {
            background: #0d1117; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 800; font-size: 20px; margin-bottom: 10px; }

        /* --- THE PERFECT FLOATING ROBOT BUTTON --- */
        /* ဒေါင့်ကပ်နေတာကို ပြင်ဖို့ 'Right: 4vw' နဲ့ 'Bottom: 4vh' (Viewport based) ကို သုံးထားပါတယ် */
        div[data-testid="stButton"] > button[key="master_ai_trigger"] {
            position: fixed;
            bottom: 50px !important;
            right: 50px !important;
            width: 90px !important;
            height: 90px !important;
            border-radius: 20px !important;
            background: #161b22 !important;
            border: 2px solid #58a6ff !important;
            box-shadow: 0 15px 40px rgba(0,0,0,0.7), 0 0 20px rgba(88, 166, 255, 0.4) !important;
            z-index: 999999 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 45px !important;
            transition: all 0.3s ease-in-out !important;
        }

        div[data-testid="stButton"] > button[key="master_ai_trigger"]:hover {
            transform: translateY(-10px) scale(1.05) !important;
            border-color: #bc8cff !important;
            box-shadow: 0 20px 50px rgba(188, 140, 255, 0.5) !important;
        }
        
        /* Button ထဲက စာသားတွေကို ဖျောက်ပြီး Icon ကိုပဲ အသားပေးခြင်း */
        div[data-testid="stButton"] > button[key="master_ai_trigger"] p {
            display: none !important;
        }
        div[data-testid="stButton"] > button[key="master_ai_trigger"]::after {
            content: "🤖";
            font-size: 45px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG (NOTION STYLE) ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_strategic_ai():
    st.markdown("<p style='color:#adbac7;'>CEO ခင်ဗျာ၊ လုပ်ငန်းဗျူဟာနှင့် ပတ်သက်သမျှ မေးမြန်းနိုင်ပါသည်။</p>", unsafe_allow_html=True)
    
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Simple Chat Interface
    for chat in st.session_state.chat_history:
        with st.chat_message(chat["role"]):
            st.write(chat["content"])

    if prompt := st.chat_input("ဗျူဟာမြောက် မေးခွန်းတစ်ခု မေးပါ..."):
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            response = f"CEO ခင်ဗျာ၊ '{prompt}' နှင့် ပတ်သက်၍ ကျွန်တော်၏ သုံးသပ်ချက်မှာ..."
            st.write(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v108_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tab3:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><div class="v101-header">🖋️ Content & AEO Mastery</div><p>AI Answer Engine များတွင် ကိုယ်စီနေရာရစေရန် Q&A content များ အားဖြည့်ပါ။</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><div class="v101-header">🎯 Media Buying: Signal Data</div><p>AI Algorithms များဆီသို့ Customer Signals အမှန်များ ပေးပို့ရန် အလေးထားပါ။</p></div>', unsafe_allow_html=True)

    # --- THE TRIGGER BUTTON ---
    # CSS နဲ့ 'fixed' ပေးထားလို့ ဘယ်နေရာမှာ ရေးရေး ညာဘက်အောက်ခြေမှာပဲ ပေါ်နေပါမယ်။
    if st.button("AI", key="master_ai_trigger"):
        open_strategic_ai()

if __name__ == "__main__":
    main()
