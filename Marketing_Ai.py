import streamlit as st

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v135.0")

def apply_sidebar_styles():
    st.markdown("""
        <style>
        /* Main Dashboard Integrity */
        .block-container { padding-top: 2rem; max-width: 94%; }
        
        /* Premium Insight Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* Sidebar Design - Dark & Professional */
        [data-testid="stSidebar"] {
            background-color: #0d1117 !important;
            border-right: 1px solid #30363d !important;
            width: 350px !important;
        }

        /* Hide ALL floating buttons & previous experimental UI artifacts */
        div.stButton > button[key*="robot"], 
        div.stButton > button[key*="trigger"],
        .stCheckbox, .stToggle, div[data-testid="stCheckbox"] {
            display: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR AI INTERFACE (MY ROBOT) ---
def render_sidebar_robot():
    st.sidebar.markdown("## 🤖 My Robot")
    st.sidebar.info("CEO ဗျူဟာမြောက် မေးခွန်းများကို ဤနေရာတွင် မေးမြန်းနိုင်ပါသည်။")
    
    # Initialize Chat History for Sidebar
    if "sidebar_chat" not in st.session_state:
        st.session_state.sidebar_chat = []

    # Display Sidebar Chat
    with st.sidebar.container():
        for msg in st.session_state.sidebar_chat:
            with st.sidebar.chat_message(msg["role"]):
                st.sidebar.write(msg["content"])

    # Chat Input for Sidebar
    if query := st.sidebar.chat_input("Ask My Robot..."):
        st.session_state.sidebar_chat.append({"role": "user", "content": query})
        with st.sidebar.chat_message("user"):
            st.sidebar.write(query)
        
        with st.sidebar.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.sidebar.write(ans)
            st.session_state.sidebar_chat.append({"role": "assistant", "content": ans})

# --- 3. MAIN DASHBOARD ---
def main():
    apply_sidebar_styles()
    
    # Side Panel - My Robot Mode
    render_sidebar_robot()
    
    # Main Title
    st.title("Sayar Gyi Mastermind Suite")
    
    # Dashboard Tabs
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Signal များအတွက် Data Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
