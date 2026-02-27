import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. GLOBAL SETTINGS & PREMIUM CSS (RESTORED v89 STYLES) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v94.0 | Intelligence Tabs")

def apply_master_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        
        /* News Card (v89 Style) */
        .news-card-v89 {
            background: #0d1117; border-left: 4px solid #58a6ff;
            padding: 22px; border-radius: 0 12px 12px 0; margin-bottom: 20px;
            border-top: 1px solid #30363d; border-right: 1px solid #30363d; border-bottom: 1px solid #30363d;
            height: 200px;
        }
        
        /* Advice Box (v89 Linear Gradient) */
        .advice-box-v89 {
            background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
            border: 1px solid #58a6ff; padding: 35px; border-radius: 18px;
            color: #c9d1d9; line-height: 1.8; font-size: 17px;
        }

        .status-pill {
            background: #238636; color: white; padding: 3px 12px;
            border-radius: 20px; font-size: 11px; font-weight: bold; text-transform: uppercase;
        }
        
        .tab-header { color: #58a6ff; font-weight: 800; font-size: 24px; margin-bottom: 20px; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR NAVIGATION ---
def render_sidebar():
    with st.sidebar:
        st.markdown('<h2 style="color:white; margin-bottom:0;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.caption("AI MARKETING AGENCY | 2026")
        st.divider()
        nav = st.radio("MAIN MENU", ["📊 Dashboard", "🧠 Sayar Gyi's Intelligence", "🧬 Brand DNA"], label_visibility="collapsed")
        st.divider()
        st.success("Core Sync: 100%")
    return nav

# --- 3. INTELLIGENCE TABS ENGINE ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-size:42px; font-weight:900; margin-bottom:5px;">Intelligence Hub</h1>', unsafe_allow_html=True)
    st.caption("Strategic Insights & Real-time Market Pulse | February 2026")
    st.write("")

    # --- THE 3 TABS ARCHITECTURE ---
    tab_news, tab_audit, tab_advice = st.tabs([
        "🌐 Market Pulse: AI & News", 
        "🎭 Sentiment & Competitor Audit", 
        "🤖 Strategic Advice"
    ])

    # --- TAB 1: MARKET PULSE (v89 NEWS GRID) ---
    with tab_news:
        st.markdown('<p class="tab-header">Industry Intelligence Feed</p>', unsafe_allow_html=True)
        
        # Grid System for News
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""<div class="news-card-v89">
                <span class="status-pill">CRITICAL</span>
                <p style="margin-top:15px; font-weight:bold; font-size:18px;">OpenAI testing Ads in ChatGPT Search</p>
                <p style="font-size:14px; color:#8b949e;">SEO Strategy ကို AI Recommendation ဦးစားပေးစနစ်သို့ ပြောင်းရန် လိုအပ်နေပြီဖြစ်သည်။</p>
            </div>""", unsafe_allow_html=True)
            with st.popover("🔍 Deep Dive: Ads Logic"):
                st.info("Source: OpenAI Newsroom (Feb 2026). Ads တွေက conversational answer တွေအဖြစ် ပေါ်လာမှာဖြစ်ပါတယ်။")

        with col2:
            st.markdown("""<div class="news-card-v89" style="border-left-color: #da3633;">
                <span class="status-pill" style="background:#da3633;">ALGORITHM</span>
                <p style="margin-top:15px; font-weight:bold; font-size:18px;">Meta: Dwell Time is the #1 Factor</p>
                <p style="font-size:14px; color:#8b949e;">Instagram Reels တွင် Like ထက် ကြည့်ရှုချိန် (Retention) ကို ပိုမိုဦးစားပေးတော့မည်။</p>
            </div>""", unsafe_allow_html=True)
            with st.popover("🔍 Deep Dive: Retention"):
                st.warning("Video Hook တွေကို ပထမ ၂ စက္ကန့်မှာပဲ ထိရောက်အောင်လုပ်ဖို့ Mosseri က အကြံပြုထားပါတယ်။")

        with col3:
            st.markdown("""<div class="news-card-v89" style="border-left-color: #1f6feb;">
                <span class="status-pill" style="background:#1f6feb;">TREND 2026</span>
                <p style="margin-top:15px; font-weight:bold; font-size:18px;">TikTok Discovery Mode Evolution</p>
                <p style="font-size:14px; color:#8b949e;">Passive scroll ထက် User Curiosity ကို အခြေခံသည့် Search-based Discovery ပိုအားကောင်းလာသည်။</p>
            </div>""", unsafe_allow_html=True)
            with st.popover("🔍 Deep Dive: TikTok"):
                st.success("BTS (Behind the Scenes) content တွေက Polished ads တွေထက် ၂ ဆ ပို viral ဖြစ်နေပါတယ်။")

        st.write("")
        # Space အလုံအလောက်ရှိသောကြောင့် Table ကို ထည့်သွင်းနိုင်ခြင်း
        st.markdown("#### Additional Headlines")
        st.table(pd.DataFrame({
            'Priority': ['High', 'Mid', 'Mid'],
            'Category': ['E-commerce', 'AI Model', 'Privacy'],
            'Headline': ['Google Agentic Commerce Launch', 'Small Language Models (SLMs) for Niche Brands', 'Threads Ads Global Rollout']
        }))

    # --- TAB 2: SENTIMENT & AUDIT (v90 DATA VISUALS) ---
    with tab_audit:
        st.markdown('<p class="tab-header">Market Position & Sentiment Audit</p>', unsafe_allow_html=True)
        
        c_radar, c_table = st.columns([1.5, 1])
        with c_radar:
            # Radar Chart - အကျယ်အဝန်းရသဖြင့် ပိုမိုကြည်လင်စွာ မြင်ရသည်
            categories = ['Sentiment', 'Engagement', 'Reach', 'Innovation', 'Retention']
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=[88, 72, 92, 60, 85], theta=categories, fill='toself', name='Our Brand', line_color='#58a6ff'))
            fig.add_trace(go.Scatterpolar(r=[65, 88, 78, 85, 50], theta=categories, fill='toself', name='Competitor A', line_color='#da3633'))
            fig.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
                template="plotly_dark", height=450, margin=dict(l=50, r=50, b=30, t=30)
            )
            st.plotly_chart(fig, use_container_width=True)

        with c_table:
            st.markdown("#### 🎭 Sentiment Deep Scan")
            st.write("AI Analyzed **2,400+ data points** this week.")
            st.progress(0.78, text="Positive Sentiment: 78%")
            st.write("")
            st.markdown("#### 🏁 Competitor Gap Analysis")
            st.table(pd.DataFrame({
                'Competitor': ['A', 'B'],
                'Strategy': ['Polished Ads', 'Viral Trends'],
                'Audit Result': ['Low Trust', 'High Reach']
            }))
            with st.popover("📂 View Sample Customer Feedback"):
                st.code("- 'AI support is incredibly fast!' (Pos)\n- 'Ads feel redundant lately' (Neu)")

    # --- TAB 3: STRATEGIC ADVICE (v89 GRAND BOX) ---
    with tab_advice:
        st.markdown('<p class="tab-header">Sayar Gyi\'s Strategic Action Room</p>', unsafe_allow_html=True)
        
        # v89.0 ရဲ့ ခန့်ထည်သော Advice Box ပုံစံ
        st.markdown("""
            <div class="advice-box-v89">
                <h2 style="color:#58a6ff; border-bottom:1px solid #30363d; padding-bottom:15px;">Executive Summary & Command</h2>
                <p><b>Analysis:</b> Meta Andromeda Update အရ ကျွန်တော်တို့ရဲ့ လက်ရှိ Content တွေမှာ <b>Retention (Dwell Time)</b> မြှင့်တင်ဖို့ လိုအပ်နေတာကို တွေ့ရပါတယ်။</p>
                <p><b>SAYAR GYI'S COMMANDS:</b></p>
                <ul style="list-style-type: square;">
                    <li><b>The 2-Second Rule:</b> Video တိုင်းရဲ့ Hook ကို ပထမ ၂ စက္ကန့်အတွင်းမှာ "Intriguing Question" သို့မဟုတ် "Visual Pattern Interrupt" ထည့်ပါ။</li>
                    <li><b>Human-Centric Content:</b> TikTok Discovery Trend အရ Polished Ads တွေအစား "Process-Driven" (လုပ်ငန်းနောက်ကွယ်က အဖြစ်အပျက်များ) ကို ပိုမိုတင်ပြပါ။</li>
                    <li><b>Conversational SEO:</b> OpenAI Ads စနစ်သစ်အတွက် Content Copy များကို မေးခွန်းနှင့် အဖြေ (Q&A Style) ပုံစံသို့ ပြောင်းလဲပါ။</li>
                </ul>
                <p style="margin-top:20px; color:#58a6ff; font-weight:bold;">Next Week Prediction: Strategic adjustment could increase reach by 18%.</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        with st.expander("🧠 Why this advice? (AI Logic Bridge)"):
            st.info("Market Pulse သတင်းအရ Platform များသည် Retention ကို ဦးစားပေးနေပြီး၊ Sentiment Audit အရ ကျွန်တော်တို့ User များသည် 'Honest BTS' Content များကို ပိုမိုတုံ့ပြန်မှုရှိနေသောကြောင့် ဖြစ်ပါသည်။")

# --- 4. EXECUTION ---
if __name__ == "__main__":
    apply_master_styles()
    current_page = render_sidebar()
    
    if current_page == "🧠 Sayar Gyi's Intelligence":
        render_intelligence_hub()
    elif current_page == "📊 Dashboard":
        st.title("Main Interactive Dashboard")
        st.info("Balanced v88.0 Dashboard is integrated here.")
    else:
        st.title(current_page)
        st.info("Module Development in Progress...")
