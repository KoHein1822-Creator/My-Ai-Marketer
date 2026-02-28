import streamlit as st
import streamlit.components.v101 as components
from datetime import datetime

# --- 1. SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v109.0")

def apply_v109_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }
        .v101-header { color: #58a6ff; font-weight: 800; font-size: 20px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. THE FLOATING ROBOT BUTTON (STABLE VERSION) ---
def render_robot_button():
    # CSS နဲ့ HTML ကို တိုက်ရိုက် Component အနေနဲ့ သုံးပြီး နေရာကို ညှိပါမယ်
    # ညာဘက်အောက်ခြေကနေ ၄၀ pixels စီ ခွာထားပါတယ်
    button_html = """
    <div id="robot-container" style="position: fixed; bottom: 40px; right: 40px; z-index: 999999; cursor: pointer;">
        <div style="background: #1f6feb; width: 80px; height: 80px; border-radius: 20px; 
                    display: flex; align-items: center; justify-content: center; 
                    font-size: 40px; border: 2px solid #58a6ff; 
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            🤖
        </div>
    </div>
    <script>
        const robot = document.getElementById('robot-container');
        robot.addEventListener('click', function() {
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: true}, '*');
        });
    </script>
    """
    # နေရာအသေဖြစ်အောင် Component အနေနဲ့ ထည့်သွင်းခြင်း
    return components.html(button_html, height=0)

# --- 3. THE STRATEGIC DIALOG ---
@st.dialog("🛡️ SAYAR GYI AI COMMAND CENTER")
def open_ai():
    st.markdown("<p style='color:#adbac7;'>CEO ခင်ဗျာ၊ မည်သည့်ဗျူဟာကို ဆွေးနွေးလိုပါသနည်း?</p>", unsafe_allow_html=True)
    query = st.chat_input("Ask Sayar Gyi...")
    if query:
        st.info(f"**Sayar Gyi 🤖:** CEO ခင်ဗျာ၊ '{query}' အတွက် ကျွန်တော်၏ သုံးသပ်ချက်မှာ...")

# --- 4. MAIN INTERFACE ---
def main():
    apply_v109_styles()
    st.title("Sayar Gyi Mastermind Suite")
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Global News", "🇲🇲 Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])

    with tab3:
        st.markdown("### 🧠 Sayar Gyi's Strategic Intelligence")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="v101-card"><div class="v101-header">🖋️ Content & AEO Mastery</div><p>AI Answers မှာ နေရာရဖို့ Q&A Content တွေ ပြင်ဆင်ပါ။</p></div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="v101-card" style="border-left-color:#f85149;"><div class="v101-header">🎯 Media Buying: Signals</div><p>Creative အရည်အသွေးနဲ့ Signal Data ကို ဦးစားပေးပါ။</p></div>', unsafe_allow_html=True)

    # Robot Button ကို Render လုပ်ပြီး အလုပ်လုပ်အောင် Logic ချိတ်ပါမယ်
    # အကယ်၍ အောက်က button ကို နှိပ်လိုက်ရင် Dialog ပွင့်လာမှာပါ
    st.write("---")
    # Floating Button အစစ်
    if st.button("Open AI Assistant 🤖", key="fallback_btn"):
        open_ai()
    
    # CSS-based Floating Robot (Visual only for now due to Streamlit limitations)
    st.markdown("""
        <style>
        div[data-testid="stButton"] > button:first-child {
            position: fixed; bottom: 50px; right: 50px; width: 80px; height: 80px;
            border-radius: 20px; font-size: 35px; background: #1f6feb; z-index: 1000;
            border: 2px solid #58a6ff; color: white;
        }
        </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
