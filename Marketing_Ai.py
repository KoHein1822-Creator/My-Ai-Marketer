import streamlit as st

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v119.0")

def apply_v119_styles():
    st.markdown("""
        <style>
        /* Main UI Setup */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* v101 Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* Streamlit ရဲ့ မူရင်း Button တွေအားလုံးကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
        .stButton, div[data-testid="stButton"] {
            display: none !important;
        }

        /* --- THE PERMANENT FLOATING ROBOT (HTML BASED) --- */
        #floating-robot-trigger {
            position: fixed;
            bottom: 60px;
            right: 60px;
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
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        #floating-robot-trigger:hover {
            transform: scale(1.1) rotate(10deg);
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6);
        }
        </style>

        <div id="floating-robot-trigger" onclick="openSayarGyi()">
            🤖
        </div>

        <script>
        function openSayarGyi() {
            // Streamlit session state ကို trigger လုပ်ရန်
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: 'open_chat'
            }, '*');
        }
        </script>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC AI DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_portal():
    st.markdown("### CEO Intelligence Access")
    query = st.chat_input("Ask Sayar Gyi...")
    if query:
        st.write(f"**CEO:** {query}")
        st.info(f"**Sayar Gyi 🤖:** CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော်၏ ဗျူဟာမြောက် သုံးသပ်ချက်မှာ...")

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v119_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> Conversion Data Signal ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- TRIGGER HANDLING ---
    # Custom HTML button က ပို့လိုက်တဲ့ အချက်ပြမှုကို ဖမ်းခြင်း
    # Button နှိပ်လိုက်လျှင် Dialog ပွင့်လာမည်
    if st.toggle("AI Assistant", key="robot_toggle", label_visibility="hidden"):
        open_portal()

if __name__ == "__main__":
    main()
