import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. SETTINGS & CSS (PREMIUM v89 LOOK) ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v91.0")

def apply_executive_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        /* v89 style card containers */
        .intel-card {
            background: #161b22; border: 1px solid #30363d;
            padding: 20px; border-radius: 12px; height: 100%;
        }
        .advice-box-v91 {
            background: #0d1117; border-left: 5px solid #58a6ff;
            padding: 20px; border-radius: 8px; margin-top: 15px;
        }
        .status-pill {
            background: rgba(88, 166, 255, 0.1); color: #58a6ff;
            padding: 2px 10px; border-radius: 12px; font-size: 11px; font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. INTELLIGENCE INTERFACE (RE-ARRANGED) ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-weight:900;">Intelligence Command Center</h1>', unsafe_allow_html=True)
    st.write("")

    # --- TOP ROW: MARKET PULSE (v89 GRID STYLE) ---
    st.markdown("### 🌐 Market Pulse: AI & Industry Insights")
    n1, n2, n3 = st.columns(3)
    
    news_items = [
        ("AI BREAKTHROUGH", "OpenAI SearchGPT Ads testing.", "B2B Brand discovery လမ်းစသစ်များ။"),
        ("ALGORITHM", "Meta's Andromeda AI Update.", "Click ထက် ကြည့်ရှုချိန် (Dwell Time) ကို ဦးစားပေးမည်။"),
        ("2026 TREND", "Voice Search Optimization.", "Conversational keywords များ မဖြစ်မနေလိုအပ်။")
    ]
    
    cols = [n1, n2, n3]
    for i, (tag, title, impact) in enumerate(news_items):
        with cols[i]:
            st.markdown(f"""<div class="intel-card">
                <span class="status-pill">{tag}</span>
                <p style="font-weight:bold; margin-top:10px; font-size:16px;">{title}</p>
                <p style="color:#8b949e; font-size:13px;">{impact}</p>
            </div>""", unsafe_allow_html=True)
            # အသေးစိတ်ဖတ်ရန် ခလုတ်ကို card အောက်မှာ သပ်ရပ်စွာ ထားခြင်း
            with st.popover(f"🔍 View {tag} Evidence"):
                st.write(f"Source: Tech Analysis 2026 - {tag} Report")
                st.info(f"Detailed analysis for CEO: {impact} အပေါ်အခြေခံပြီး Content Strategy ကို ၅% ပြုပြင်ရန်လိုအပ်ပါသည်။")

    st.write("")
    st.divider()

    # --- MIDDLE ROW: DATA VISUALS & AUDIT (BALANCED) ---
    st.markdown("### 🎭 Deep Audit & Forecast")
    c_graph, c_audit = st.columns([1.2, 1])
    
    with c_graph:
        # Radar Chart (Cleaned up size)
        categories = ['Sentiment', 'Engagement', 'Reach', 'Innovation', 'Retention']
        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=[85, 70, 90, 65, 80], theta=categories, fill='toself', name='Our Brand', line_color='#58a6ff'))
        fig.add_trace(go.Scatterpolar(r=[60, 85, 75, 80, 55], theta=categories, fill='toself', name='Competitor A', line_color='#da3633'))
        fig.update_layout(polar=dict(radialaxis=dict(visible=False)), template="plotly_dark", 
                          height=350, margin=dict(l=40, r=40, b=20, t=20), showlegend=True)
        st.plotly_chart(fig, use_container_width=True)

    with c_audit:
        # Real Data Table and Deep Dive
        st.markdown("#### Competitor Sentiment Gap")
        st.table(pd.DataFrame({
            'Metric': ['User Satisfaction', 'Response Rate', 'Viral Content'],
            'Our Score': ['85%', '2 mins', '12/mo'],
            'Competitor': ['62%', '15 mins', '18/mo']
        }))
        with st.popover("📂 Explore Raw Comment Data"):
            st.markdown("**Sample Raw Comments (Analyzed by AI):**")
            st.code("- 'Very fast response!' (Pos)\n- 'Competitor is too slow.' (Pos-rel)\n- 'Need more video tutorials' (Neutral)")

    # --- BOTTOM ROW: STRATEGIC ACTION (EXECUTIVE SUMMARY) ---
    st.write("")
    st.markdown("### 🤖 Sayar Gyi's Strategic Advice")
    
    # Tabs သုံးပြီး Information ကို ရှင်းလင်းစွာ ခွဲခြားထားခြင်း
    tab_plan, tab_logic = st.tabs(["📋 Immediate Action Plan", "🧠 AI Reasoning Logic"])
    
    with tab_plan:
        st.markdown("""
        <div class="advice-box-v91">
            <b>Target: Meta Andromeda Update</b><br>
            • Video များတွင် Hook ကို ပထမ ၂ စက္ကန့်အတွင်း ထည့်ပါ။<br>
            • Comment များတွင် မေးခွန်းပြန်မေးခြင်းဖြင့် Dwell Time ကို မြှင့်တင်ပါ။
        </div>
        """, unsafe_allow_html=True)
        
    with tab_logic:
        st.info("Why this? သတင်းအရ Meta သည် Retention ကို Score ပိုပေးနေပြီး၊ ကျွန်တော်တို့၏ Sentiment Audit အရ User များသည် Discussion ပြုလုပ်ရခြင်းကို နှစ်သက်ကြောင်း တွေ့ရှိရသောကြောင့်ဖြစ်သည်။")

# --- 3. EXECUTION ---
if __name__ == "__main__":
    apply_executive_styles()
    # Sidebar selection logic (Simplified for demo)
    with st.sidebar:
        st.title("SAYAR GYI")
        mode = st.radio("Menu", ["📊 Dashboard", "🧠 Intelligence Hub"])
        
    if mode == "🧠 Intelligence Hub":
        render_intelligence_hub()
    else:
        st.title("Main Dashboard View")
