import streamlit as st
from datetime import datetime

# --- 1. SETTINGS & ABSOLUTE CSS INJECTION ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v115.0")

def apply_v115_styles():
    st.markdown("""
        <style>
        /* Main Dashboard Spacing */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Card Style */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE ABSOLUTE FLOATING ROBOT FIX --- */
        /* Streamlit Button ကို အခြေခံပြီး ညာဘက်အောက်ခြေမှာ အသေနေရာချခြင်း */
        div.stButton > button[key="robot_final"] {
            position: fixed !important;
            bottom: 45px !important;
            right: 45px !important;
            left: auto !important;
            width: 85px !important;
            height: 85px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
            z-index: 1000000 !important;
            cursor: pointer !important;
            color: transparent !important; /* "AI" စာသားကို ဖျောက်ခြင်း */
            overflow: visible !important;
        }

        /* စက်ရုပ် Emoji ကို ခလုတ်အလယ်မှာ အစားထိုးခြင်း */
        div.stButton > button[key="robot_final"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0;
            width: 100%; height: 100%;
            font-size: 45px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            color: white !important;
            visibility: visible !important;
        }

        div.stButton > button[key="robot_final"]:hover {
            transform: scale(1.1) rotate(5deg) !important;
            box-shadow: 0 15px 40px rgba(88, 166, 255, 0.5) !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_strategic_ai():
    st.markdown("### CEO Intelligence Access")
    query = st.chat_input("Ask Sayar Gyi...")
    if query:
        st.write(f"**CEO:** {query}")
        st.info(f"**Sayar Gyi 🤖:** CEO ခင်ဗျာ၊ ဗျူဟာမြောက် သုံးသပ်ချက်မှာ...")

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v115_styles()
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Answers မှာ နေရာရဖို့ ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE TRIGGER ---
    # ဤနေရာရှိ Button သည် CSS ကြောင့် ညာဘက်အောက်ခြေတွင် 🤖 အဖြစ် ပေါ်နေပါမည်။
    if st.button("AI", key="robot_final"):
        open_strategic_ai()

if __name__ == "__main__":
    main()
