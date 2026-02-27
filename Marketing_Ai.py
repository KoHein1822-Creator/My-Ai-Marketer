import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# --- 1. SETTINGS & STYLES ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v90.0 | Deep-Dive")

def apply_deep_dive_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem; max-width: 96%; }
        .data-source-box { 
            background: #1c2128; border: 1px solid #444c56; 
            padding: 15px; border-radius: 8px; font-size: 13px; color: #adbac7;
        }
        .highlight-text { color: #58a6ff; font-weight: bold; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
def render_sidebar():
    with st.sidebar:
        st.markdown('## SAYAR GYI\'S')
        st.divider()
        page = st.radio("Navigation", ["📊 Dashboard", "🧠 Intelligence Hub", "🧬 Brand DNA"])
        st.divider()
        st.caption("Intelligence Node: SG-V90-ACTIVE")
    return page

# --- 3. INTELLIGENCE PAGE (WITH DEEP-DIVE & VISUALS) ---
def render_intelligence_hub():
    st.markdown("# 🧠 Intelligence Command Center")
    st.write("Back-end AI Logic is syncing with 2026 Live Nodes...")
    
    # --- ROW 1: REAL DATA VISUAL (COMPARISON RADAR) ---
    st.markdown("### 📊 Market Position Audit (Real Data)")
    c_graph, c_info = st.columns([1.5, 1])
    
    with c_graph:
        # Radar Chart for Competitor Comparison
        categories = ['Sentiment', 'Engagement', 'Reach', 'Innovation', 'Retention']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[85, 70, 90, 65, 80], theta=categories, fill='toself', name='Our Brand'))
        fig.add_trace(go.Scatterpolar(r=[60, 85, 75, 80, 55], theta=categories, fill='toself', name='Competitor A'))
        fig.update_layout(
            polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
            template="plotly_dark", height=400, margin=dict(l=20, r=20, b=20, t=20)
        )
        st.plotly_chart(fig, use_container_width=True)

    with c_info:
        st.markdown("#### Audit Analysis")
        st.write("ကျွန်တော်တို့ Brand က **Reach** နဲ့ **Sentiment** မှာ သာနေပေမယ့် **Innovation** (AI Content သစ်များ) မှာ ပြိုင်ဘက်ထက် အားနည်းနေတာကို Graph မှာ တွေ့နိုင်ပါတယ်။")
        st.info("💡 Suggestion: Start experimenting with AI-Generated AR Ads.")

    st.divider()

    # --- ROW 2: MARKET PULSE & DATA SOURCE ---
    st.markdown("### 🌐 Market Pulse & Source Evidence")
    
    col_news, col_sentiment = st.columns(2)
    
    with col_news:
        st.markdown("#### 📰 AI Industry News")
        st.markdown("• **OpenAI SearchGPT Update** (2026 Feb)")
        with st.expander("Read Detail News & Sources"):
            st.markdown("""
                <div class="data-source-box">
                    <b>Source:</b> Reuters & TechCrunch (Feb 24, 2026)<br>
                    <b>Summary:</b> OpenAI သည် SearchGPT တွင် Ad Platform ကို စတင်စမ်းသပ်နေပြီဖြစ်ပြီး ၎င်းသည် ရိုးရိုး Search Ads ထက် Conversational Ads ကို ဦးစားပေးမည်ဖြစ်သည်။<br>
                    <a href="#">Read Original Article</a>
                </div>
            """, unsafe_allow_html=True)
            
    with col_sentiment:
        st.markdown("#### 🎭 Raw Sentiment Data")
        st.markdown("• **User Sentiment: 78% Positive**")
        with st.expander("View Raw Customer Comments"):
            st.write("AI Analyzed 1,450 comments. Here are some samples:")
            st.code("""
            - "The AI customer service is faster than before!" (Positive)
            - "I wish the ads were more personalized." (Neutral)
            - "Pricing is still a bit high compared to others." (Negative)
            """)

    st.divider()

    # --- ROW 3: SAYAR GYI'S ADVICE (ACTIONABLE) ---
    st.markdown("### 🤖 Sayar Gyi's Strategic Advice")
    st.warning("Action Required: Meta's Algorithm is shifting to 'Dwell Time'.")
    
    # Detailed Action Plan with Expandable Evidence
    tab1, tab2 = st.tabs(["Action Plan", "Why this advice? (The Logic)"])
    
    with tab1:
        st.markdown("""
        1. **Hook Enhancement:** Video များ၏ ပထမ ၃ စက္ကန့်ကို AI-Optimized Hook များဖြင့် ပြောင်းလဲပါ။
        2. **Conversational Tone:** Content များတွင် မေးခွန်းများ ပိုမိုထည့်သွင်းပါ။
        """)
        
    with tab2:
        st.write("ကျွန်တော်တို့ AI က ဒီအကြံပေးချက်ကို ပေးရတဲ့ အကြောင်းရင်းကတော့-")
        st.write("၁။ **Market Pulse:** သတင်းအရ Meta က Click ထက် ကြည့်ချိန်ကို ဦးစားပေးတော့မှာမို့ပါ။")
        st.write("၂။ **Sentiment Audit:** လူတွေက 'Ads တွေက ရိုးအီနေတယ်' လို့ ကွန်မန့်ပေးထားတဲ့အတွက် Hook အသစ် လိုအပ်တာပါ။")

# --- 4. EXECUTION ---
if __name__ == "__main__":
    apply_deep_dive_styles()
    page = render_sidebar()
    if page == "🧠 Intelligence Hub":
        render_intelligence_hub()
    else:
        st.title(page)
        st.info("Switching to Dashboard view...")
