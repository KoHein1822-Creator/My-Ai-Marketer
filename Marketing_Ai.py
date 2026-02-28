import streamlit as st

# --- 1. SETTINGS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v120.0")

def apply_v120_final_fix():
    # ဤ HTML/JS သည် Dashboard ပေါ်တွင် 🤖 ကို ညာဘက်အောက်ခြေ၌ အသေနေရာချပေးမည်
    # Streamlit Button မဟုတ်သောကြောင့် "AI" စာသား လုံးဝ ပေါ်မလာနိုင်ပါ
    st.markdown("""
        <div id="robot-container">
            <div id="robot-fab" onclick="document.dispatchEvent(new CustomEvent('openChat'))">
                🤖
            </div>
        </div>

        <style>
        /* Dashboard Spacing */
        .block-container { padding-top: 2rem; max-width: 94%; background-color: #0d1117; }
        
        /* Premium Cards */
        .v101-card {
            background: #161b22; border: 1px solid #30363d; border-radius: 12px;
            padding: 25px; margin-bottom: 25px; border-left: 5px solid #58a6ff;
        }

        /* --- THE UNSHAKABLE ROBOT FAB --- */
        #robot-fab {
            position: fixed !important;
            bottom: 60px !important;
            right: 60px !important;
            width: 85px !important;
            height: 85px !important;
            background: linear-gradient(135deg, #1f6feb 0%, #58a6ff 100%) !important;
            border-radius: 50% !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            font-size: 45px !important;
            cursor: pointer !important;
            z-index: 2147483647 !important; /* အပေါ်ဆုံး layer တွင်ရှိနေစေရန် */
            border: 3px solid #ffffff !important;
            box-shadow: 0 10px 40px rgba(0,0,0,0.8) !important;
            transition: all 0.3s ease !important;
        }

        #robot-fab:hover {
            transform: scale(1.1) rotate(10deg) !important;
            box-shadow: 0 15px 50px rgba(88, 166, 255, 0.6) !important;
        }

        /* Streamlit ၏ မူရင်း Button များအားလုံးကို အမြစ်ဖြတ်ဖျောက်ခြင်း */
        .stButton, button { display: none !important; }
        </style>

        <script>
        // ခလုတ်နှိပ်လျှင် Streamlit သို့ အချက်ပြရန်
        const fab = document.getElementById('robot-fab');
        document.addEventListener('openChat', function() {
            const btn = window.parent.document.querySelector('button[kind="primary"]');
            if (btn) btn.click();
        });
        </script>
    """, unsafe_allow_html=True)

# --- 2. THE STRATEGIC DIALOG ---
@
