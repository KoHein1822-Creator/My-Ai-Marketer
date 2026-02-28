import streamlit as st
import streamlit.components.v1 as components
from datetime import datetime

# --- 1. GLOBAL SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v114.0")

def apply_v114_ui():
    st.markdown("""
        <style>
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        /* Streamlit ရဲ့ မူရင်း Button တွေကို ဖျောက်ထားခြင်း (Floating အတွက် အသုံးမပြုတော့ပါ) */
        .stButton button[key="hidden_trigger"] { display: none; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE INFALLIBLE FLOATING ROBOT COMPONENT ---
def render_robot_fab():
    # ညာဘက်အောက်ခြေမှာ အမြဲတမ်းရှိနေမယ့် Custom HTML/JS Button
    robot_html = """
    <div id="robot-fab" style="
        position: fixed;
        bottom: 40px;
        right: 40px;
        width: 80px;
        height: 80px;
        background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 45px;
        cursor: pointer;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        z-index: 999999;
        transition: transform 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 3px solid #ffffff;
    " onmouseover="this.style.transform='scale(1.1) rotate(10deg)'" 
      onmouseout="this.style.transform='scale(1) rotate(0deg)'">
        🤖
    </div>

    <script>
        // Parent Streamlit app ဆီကို ခလုတ်နှိပ်လိုက်တဲ့အချက်ပြမှု ပေးပို့ခြင်း
        const fab = document.getElementById('robot-fab');
        fab.addEventListener('click', function() {
            window.parent.postMessage({
                type: 'streamlit:setComponentValue',
                value: Math.random() // Unique value to trigger update
            }, '*');
        });
    </script>
    """
    # Component ကို Dashboard ထဲ ထည့်သွင်းခြင်း
    return components.html(robot_html, height=0)

# --- 3. THE STRATEGIC DIALOG ---
@st.dialog("🦾 SAYAR GYI COMMAND CENTER")
def open_ai_command():
    st.markdown("### CEO Strategic Intelligence Access")
    query = st.chat_input("ဗျူဟာမြောက် မေးခွန်းများ မေးမြန်းပါ...")
    if query:
        with st.chat_message("assistant"):
            st.write(f"CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော့်ရဲ့ ဗျူဟာမြောက် အကြံပြုချက်ကတော့...")

# --- 4. MAIN DASHBOARD ---
def main():
    apply_v114_ui()
    st.title("Sayar Gyi Mastermind Suite")
    
    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tabs[2]:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><b>Content Strategy:</b> AI Search Optimization ကို အာရုံစိုက်ပါ။</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><b>Ad Strategy:</b> Data Signal Quality ကို မြှင့်တင်ပါ။</div>', unsafe_allow_html=True)

    # Robot FAB ကို Render လုပ်ခြင်း
    clicked = render_robot_fab()
    
    # ခလုတ်နှိပ်လိုက်ရင် Dialog ပွင့်စေမယ့် Logic
    if clicked:
        open_ai_command()

if __name__ == "__main__":
    main()
