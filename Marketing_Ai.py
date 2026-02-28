import streamlit as st

# --- 1. SETTINGS & RECOVERY ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v134.0")

def apply_final_ultimate_styles():
    st.markdown("""
        <style>
        /* Restore Main Dashboard Integrity */
        .main .block-container { padding-top: 2rem; max-width: 94%; }
        
        /* Premium Card Design */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE FINAL FLOATING COMMANDER (NO FAIL) --- */
        div.stButton > button[key="final_ultra_robot"] {
            position: fixed !important;
            bottom: 40px !important;   /* ညာဘက်အောက်ခြေ နေရာအတိအကျ */
            right: 40px !important;
            width: 85px !important;    /* CEO စိတ်ကြိုက် အရွယ်အစား */
            height: 85px !important;
            border-radius: 50% !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8) !important;
            z-index: 9999999 !important;
            font-size: 0px !important; /* "AI" စာသားကို ဖျောက်ခြင်း */
            padding: 0 !important;
        }

        div.stButton > button[key="final_ultra_robot"]::after {
            content: "🤖";
            position: absolute;
            left: 0; top: 0; width: 100%; height: 100%;
            display: flex; align-items: center; justify-content: center;
            font-size: 45px; color: white; visibility: visible;
        }

        /* Hide all experimental debris from previous versions */
        .stCheckbox, div[data-testid="stCheckbox"], .stToggle, button:not([key="final_ultra_robot"]) { 
            display: none !important; 
        }
        
        /* Sidebar Chat Styling */
        section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE AI COMMAND CENTER (FUNCTION) ---
def render_ai_interface(location="dialog"):
    st.markdown(f"### 🛡️ SAYAR GYI COMMAND CENTER ({location})")
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if query := st.chat_input(f"Ask Sayar Gyi ({location})...", key=f"input_{location}"):
        st.session_state.chat_history.append({"role": "user", "content": query})
        with st.chat_message("user"):
            st.write(query)
        with st.chat_message("assistant"):
            ans = f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် သုံးသပ်ချက်ကတော့..."
            st.write(ans)
            st.session_state.chat_history.append({"role": "assistant", "content": ans})

# --- 3. DIALOG WRAPPER ---
@st.dialog("STRATEGIC INTELLIGENCE")
def open_pop_up():
    render_ai_interface(location="Pop-up")

# --- 4. MAIN DASHBOARD ---
def main():
    apply_final_ultimate_styles()
    
    # --- SIDEBAR BACKUP (CEO အမိန့်အတိုင်း) ---
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/robot-2.png", width=80)
        st.title("Sayar Gyi AI")
        st.info("Pop-up အဆင်မပြေပါက ဤနေရာတွင် တိုက်ရိုက်မေးမြန်းနိုင်ပါသည်။")
        render_ai_interface(location="Sidebar")

    # MAIN CONTENT
    st.title("Sayar Gyi Mastermind Suite")
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>AEO Strategy:</b> AI Search Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ads Strategy:</b> Conversion Data Signal ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # --- THE FINAL FLOATING TRIGGER ---
    st.button("🤖", key="final_ultra_robot", on_click=open_pop_up)

if __name__ == "__main__":
    main()
