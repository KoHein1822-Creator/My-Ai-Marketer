import streamlit as st

# --- 1. GLOBAL SETTINGS & TRUE FLOATING UI ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v116.0")

def apply_v116_master_styles():
    # ဤ CSS သည် Dashboard ၏ ဘယ်နေရာရောက်ရောက် ညာဘက်အောက်ခြေတွင် 🤖 ကို အသေထားပေးမည်
    st.markdown("""
        <style>
        /* Main Container Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE BULLETPROOF ROBOT BUTTON (NO MORE 'AI' TEXT) --- */
        #custom-robot-btn {
            position: fixed;
            bottom: 40px;
            right: 40px;
            width: 85px;
            height: 85px;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 45px;
            cursor: pointer;
            z-index: 9999999;
            border: 3px solid #ffffff;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            text-decoration: none;
        }

        #custom-robot-btn:hover {
            transform: scale(1.1) rotate(10deg);
            box-shadow: 0 15px 45px rgba(88, 166, 255, 0.5);
        }

        /* Streamlit ၏ မူရင်း Button များအားလုံးကို ဖျောက်ထားခြင်း (Error ကာကွယ်ရန်) */
        .stButton button { display: none !important; }
        </style>
        
        <a id="custom-robot-btn" href="?chat=open">
            🤖
        </a>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI STRATEGIC COMMAND")
def open_strategic_ai():
    st.markdown("### CEO Intelligence Access")
    st.write("ကျွန်တော် (Gemini) သည် CEO သိလိုသမျှ Marketing ဗျူဟာများကို တိကျစွာ ရှင်းပြပေးပါမည်။")
    
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("Ask Sayar Gyi..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
        
        with st.chat_message("assistant"):
            # CEO မေးသမျှကို တိကျစွာဖြေကြားရန် Logic
            response = f"CEO ခင်ဗျာ၊ '{prompt}' အတွက် ကျွန်တော်၏ ဗျူဟာမြောက် သုံးသပ်ချက်မှာ..."
            st.write(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v116_master_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><p style="color:#58a6ff; font-weight:bold;">AEO Strategy</p><p>AI Answers မှာ CEO ရဲ့ Brand ကို Citation ရအောင် လုပ်ဆောင်ပါ။</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><p style="color:#f85149; font-weight:bold;">Ads Strategy</p><p>Quality Signal Data ကို AI Algorithms ဆီသို့ ပေးပို့ပါ။</p></div>', unsafe_allow_html=True)

    # --- TRIGGER LOGIC ---
    # URL parameter ကိုသုံးပြီး Dialog ကိုဖွင့်ခြင်း (Button နေရာလွဲမှုကို အမြစ်ပြတ်ဖြေရှင်းရန်)
    query_params = st.query_params
    if query_params.get("chat") == "open":
        st.query_params.clear() # URL ကို ပြန်ရှင်းခြင်း
        open_strategic_ai()

if __name__ == "__main__":
    main()
