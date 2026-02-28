import streamlit as st

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v136.0")

def apply_confirmed_styles():
    st.markdown("""
        <style>
        /* Main Dashboard Background */
        .block-container { 
            padding-top: 2rem; 
            max-width: 94%; 
            background-color: #0d1117; 
        }
        
        /* V101 Deep Insights Card UI */
        .v101-card {
            background: #161b22; 
            border: 1px solid #30363d; 
            border-radius: 12px;
            padding: 25px; 
            margin-bottom: 25px; 
            border-left: 5px solid #58a6ff;
        }

        /* Sidebar Styling for My Robot */
        [data-testid="stSidebar"] {
            background-color: #0d1117 !important;
            border-right: 1px solid #30363d !important;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR MY ROBOT ---
def render_sidebar():
    with st.sidebar:
        st.markdown("## 🤖 My Robot")
        if "sidebar_chat" not in st.session_state:
            st.session_state.sidebar_chat = []
        
        for msg in st.session_state.sidebar_chat:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
        
        if query := st.chat_input("Ask My Robot..."):
            st.session_state.sidebar_chat.append({"role": "user", "content": query})
            # Response logic simplified for structure
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ဗျူဟာမြောက် အကြံပြုချက် ရှိပါတယ်..."
            st.session_state.sidebar_chat.append({"role": "assistant", "content": ans})
            st.rerun()

# --- 3. MAIN DASHBOARD ---
def main():
    apply_confirmed_styles()
    render_sidebar()
    
    st.title("Sayar Gyi Mastermind Suite")
    
    # Combined Confirmed UI Components
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    # UI 1: V101 Deep Insights Tab
    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Citation ရရှိရန် Content များကို ပြင်ဆင်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> AI Algorithms အတွက် Signal Data ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # UI 2: V100 Weekly Report Tab
    with tabs[3]:
        st.markdown("### 📄 Sayar Gyi's Weekly Report")
        st.markdown('<div class="v101-card" style="border-left-color:#3fb950;"><b>Performance Summary:</b> ယခုအပတ်အတွင်း Ads Reach 15% တိုးတက်လာပြီး Conversion Rate မှာ တည်ငြိမ်နေပါသည်။</div>', unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric(label="Total Spend", value="$1,200", delta="-5%")
        with col_b:
            st.metric(label="Total Conversions", value="450", delta="12%")

if __name__ == "__main__":
    main()
