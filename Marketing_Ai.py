import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v130.0")

def apply_v130_master_styles():
    st.markdown("""
        <style>
        /* Main UI Restore */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE UNSHAKABLE FAB OVERRIDE --- */
        /* မလိုလားအပ်သော Widget များနှင့် ခလုတ်များအားလုံးကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
        .stButton, div[data-testid="stButton"], button, .stCheckbox, div[data-testid="stCheckbox"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Create a secure Floating Action Button Layer */
        #master-robot-layer {
            position: fixed;
            bottom: 50px;
            right: 50px;
            width: 90px;
            height: 90px;
            z-index: 9999999;
        }
        </style>

        <div id="master-robot-layer">
            <button id="real-robot-btn" onclick="triggerStreamlit()">
                🤖
            </button>
        </div>

        <style>
        #real-robot-btn {
            width: 85px;
            height: 85px;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%);
            border-radius: 50%;
            border: 3px solid #ffffff;
            font-size: 45px;
            cursor: pointer;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8);
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        #real-robot-btn:hover {
            transform: scale(1.1) rotate(10deg);
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6);
        }
        </style>

        <script>
        function triggerStreamlit() {
            // Streamlit ၏ URL parameter ကို အသုံးပြု၍ Dialog ကို Trigger လုပ်ခြင်း
            const currentUrl = new URL(window.location.href);
            currentUrl.searchParams.set('action', 'chat');
            window.parent.location.hash = 'ai-chat-' + Math.random(); 
            
            // Hidden Link ကို နှိပ်စေခြင်း
            const link = window.parent.document.getElementById('hidden-trigger-link');
            if (link) { link.click(); }
        }
        </script>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI COMMAND CENTER")
def open_strategic_portal():
    st.markdown("### CEO Strategic Intelligence Access")
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ..."):
        st.session_state.messages.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.messages.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_v130_master_styles()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE INVISIBLE BRIDGE (SECURE) ---
    # ဤနေရာတွင် မည်သည့် Button မှ မသုံးတော့ဘဲ Query Param ပြောင်းလဲမှုကို စောင့်ကြည့်မည်
    if "chat_open" not in st.session_state:
        st.session_state.chat_open = False

    # Hidden Toggle for JavaScript to click
    if st.checkbox("Chat Trigger", key="hidden_checkbox", label_visibility="hidden"):
        open_strategic_portal()

    # Link for JS to trigger checkbox
    st.markdown("""
        <a id="hidden-trigger-link" style="display:none;" 
           href="javascript:document.querySelector('input[aria-label=\\'Chat Trigger\\']').click();">
           Trigger
        </a>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
