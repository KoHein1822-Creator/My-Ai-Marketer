import streamlit as st
import pandas as pd
import numpy as np

# --- 1. CONFIG & STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI Intelligence Hub")

def apply_intelligence_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 98%; }
        .stButton>button { width: 100%; border-radius: 8px; }
        
        /* Intelligence Cards */
        .news-card {
            background: #0d1117; border-left: 4px solid #58a6ff;
            padding: 15px; border-radius: 0 10px 10px 0; margin-bottom: 15px;
            border-top: 1px solid #30363d; border-right: 1px solid #30363d; border-bottom: 1px solid #30363d;
        }
        .advice-box {
            background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
            border: 1px solid #58a6ff; padding: 25px; border-radius: 15px;
            color: #c9d1d9; line-height: 1.6;
        }
        .status-pill {
            background: #238636; color: white; padding: 2px 10px;
            border-radius: 20px; font-size: 12px; font-weight: bold;
        }
        .ai-title { color: #58a6ff; font-weight: 800; font-size: 18px; margin-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR WITH NEW FEATURE BUTTON ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.divider()
        st.markdown("### MAIN MENU")
        # Feature Button အသစ်ထည့်သွင်းခြင်း
        menu_choice = st.radio("Features", 
            ["📊 Dashboard", "🧠 Sayar Gyi's Intelligence", "🧬 Brand DNA", "📂 Archive"], 
            label_visibility="collapsed")
        
        st.divider()
        st.markdown("### SYSTEM STATUS")
        st.success("AI Analysis: ACTIVE")
        st.info("Next Sync: 5 mins left")
    return menu_choice

# --- 3. INTELLIGENCE INTERFACE (CEO READABLE) ---
def render_intelligence_page():
    st.markdown('<h1 style="font-size:40px; font-weight:900;">Intelligence Command Center</h1>', unsafe_allow_html=True)
    st.caption("2026 February Real-time Strategy & Market Pulse")
    st.write("")

    # --- TOP ROW: MARKET PULSE (သတင်းဖတ်ခြင်းအပိုင်း) ---
    st.markdown("### 🌐 Market Pulse: AI & Industry News")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="news-card">
            <span class="status-pill">AI BREAKTHROUGH</span>
            <p style="margin-top:10px; font-weight:bold;">OpenAI starts testing Ads in ChatGPT free tier.</p>
            <p style="font-size:13px; color:#8b949e;">Impact: B2B Brand Discovery နယ်ပယ်မှာ လမ်းစသစ်တွေ ပေါ်လာနိုင်ပါတယ်။</p>
        </div>""", unsafe_allow_html=True)
        
    with col2:
        st.markdown("""<div class="news-card">
            <span class="status-pill" style="background:#da3633;">ALGORITHM UPDATE</span>
            <p style="margin-top:10px; font-weight:bold;">Meta's Andromeda AI: Dwell Time is the new Like.</p>
            <p style="font-size:13px; color:#8b949e;">Impact: Content ကို Click လုပ်တာထက် ကြည့်ရှုချိန် (Retention) ကို ပိုဦးစားပေးတော့မှာပါ။</p>
        </div>""", unsafe_allow_html=True)
        
    with col3:
        st.markdown("""<div class="news-card">
            <span class="status-pill" style="background:#1f6feb;">CONSUMER TREND</span>
            <p style="margin-top:10px; font-weight:bold;">Voice Search is now core to SEO visibility in 2026.</p>
            <p style="font-size:13px; color:#8b949e;">Impact: Conversational Keywords တွေကို Strategy မှာ အမြန်ပေါင်းစပ်ရပါမယ်။</p>
        </div>""", unsafe_allow_html=True)

    st.write("")

    # --- MIDDLE ROW: ANALYSIS & AUDIT (အခြေအနေသုံးသပ်ခြင်းအပိုင်း) ---
    c_audit, c_forecast = st.columns([1, 1])
    
    with c_audit:
        st.markdown('<p class="ai-title">🎭 Sentiment & Competitor Audit</p>', unsafe_allow_html=True)
        # Mock Analysis Data
        audit_data = {
            'Metric': ['Our Sentiment', 'Competitor A', 'Competitor B', 'Market Gap'],
            'Score': ['78% (Positive)', '62% (Neutral)', '85% (Strong)', 'High Opportunity']
        }
        st.table(pd.DataFrame(audit_data))
        st.caption("AI Note: ပြိုင်ဘက် B သည် Video Long-form တွင် အားသာနေသော်လည်း Community Engagement တွင် အားနည်းနေသည်။")

    with c_forecast:
        st.markdown('<p class="ai-title">🔮 Trend Forecast (Next 14 Days)</p>', unsafe_allow_html=True)
        forecast_df = pd.DataFrame({'Growth': np.random.randint(20, 100, 7)}, index=['Video', 'Audio', 'Ads', 'Image', 'Blog', 'Live', 'AR'])
        st.bar_chart(forecast_df, height=180)

    # --- BOTTOM ROW: SAYAR GYI'S ADVICE (အကြံပေးချက်အပိုင်း) ---
    st.write("")
    st.markdown('<p class="ai-title">🤖 Sayar Gyi\'s Strategic Advice</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="advice-box">
            <b>လက်ရှိသုံးသပ်ချက်:</b> Meta ရဲ့ Andromeda Update အရ ကျွန်တော်တို့ရဲ့ Content တွေဟာ Click တော့များပေမယ့် Dwell Time (ကြည့်ရှုချိန်) နည်းနေတာကို တွေ့ရပါတယ်။ <br><br>
            <b>အကြံပြုချက် (Action Plan):</b>
            <ul>
                <li>Content ရဲ့ ပထမ ၃ စက္ကန့်မှာ "Hook" ပြင်းပြင်းထည့်ပါ။ </li>
                <li>စကားပြောတဲ့ပုံစံကို Voice Search နဲ့ အံဝင်ခွင်ကျဖြစ်အောင် Conversational Tone ပြောင်းပါ။</li>
                <li>Competitor B ထက်သာအောင် Community Group များအတွင်း Discussion Content များ တိုးမြှင့်တင်ပါ။</li>
            </ul>
            <p style="color:#58a6ff; font-weight:bold;">Expected Result: Next week engagement could rise by 15-20%.</p>
        </div>
    """, unsafe_allow_html=True)
    st.write("") # Graceful bottom space

# --- 4. EXECUTION ---
if __name__ == "__main__":
    apply_intelligence_styles()
    choice = render_sidebar()
    
    if choice == "🧠 Sayar Gyi's Intelligence":
        render_intelligence_page()
    elif choice == "📊 Dashboard":
        st.title("Main Dashboard")
        st.info("အရင်က Dashboard Page ကို ဒီနေရာမှာ မြင်ရပါမယ်။")
    else:
        st.title(choice)
        st.info("Developing Module...")
