import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- 1. GLOBAL SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v95.0 | Visual Pulse")

def apply_v95_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        
        /* News Card with Image Support */
        .news-card-visual {
            background: #0d1117; border: 1px solid #30363d;
            border-radius: 12px; margin-bottom: 20px; overflow: hidden;
            transition: transform 0.3s;
        }
        .news-card-visual:hover { transform: translateY(-5px); border-color: #58a6ff; }
        
        .news-content { padding: 20px; border-left: 4px solid #58a6ff; }
        
        .rank-badge {
            background: #238636; color: white; padding: 2px 8px;
            border-radius: 5px; font-size: 10px; font-weight: bold;
        }
        
        /* Table Styling */
        .styled-table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        .styled-table th { background: #161b22; color: #58a6ff; text-align: left; padding: 12px; border-bottom: 2px solid #30363d; }
        .styled-table td { padding: 12px; border-bottom: 1px solid #30363d; color: #adbac7; }
        
        .advice-box-v95 {
            background: linear-gradient(135deg, #161b22 0%, #0d1117 100%);
            border: 1px solid #58a6ff; padding: 30px; border-radius: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 2. INTELLIGENCE TABS ENGINE ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-size:42px; font-weight:900;">Intelligence Command Center</h1>', unsafe_allow_html=True)
    st.write("")

    tab_news, tab_audit, tab_advice = st.tabs([
        "🌐 Market Pulse (Visual Feed)", 
        "🎭 Sentiment & Competitor Audit", 
        "🤖 Strategic Advice"
    ])

    # --- TAB 1: MARKET PULSE (WITH IMAGES & RANKING) ---
    with tab_news:
        st.markdown("### 🔥 Top 3 High-Impact News")
        n1, n2, n3 = st.columns(3)
        
        # News Data with Mock Image URLs (Using high-quality placeholders for 2026 tech)
        news_items = [
            {
                "tag": "CRITICAL", "title": "OpenAI SearchGPT Ads Rollout", 
                "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=400&q=80",
                "desc": "AI conversational search ထဲမှာ Ads တွေ စတင်စမ်းသပ်နေပြီဖြစ်သည်။"
            },
            {
                "tag": "ALGORITHM", "title": "Meta Andromeda Engine Sync", 
                "img": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=400&q=80",
                "desc": "Dwell time ပေါ်အခြေခံပြီး Content တွေကို Rank ပေးမည့် စနစ်သစ်။"
            },
            {
                "tag": "TREND 2026", "title": "TikTok Discovery Ads 2.0", 
                "img": "https://images.unsplash.com/photo-1611605698335-8b1569810432?auto=format&fit=crop&w=400&q=80",
                "desc": "User ၏ စိတ်ဝင်စားမှုကို AI က ကြိုတင်ခန့်မှန်းပြသသည့် Ads များ။"
            }
        ]
        
        cols = [n1, n2, n3]
        for i, item in enumerate(news_items):
            with cols[i]:
                st.markdown(f"""
                <div class="news-card-visual">
                    <img src="{item['img']}" style="width:100%; height:150px; object-fit:cover;">
                    <div class="news-content">
                        <span class="rank-badge">{item['tag']}</span>
                        <p style="font-weight:bold; margin-top:10px; font-size:16px;">{item['title']}</p>
                        <p style="font-size:13px; color:#8b949e;">{item['desc']}</p>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                with st.popover("📖 Read Full Story"):
                    st.write(f"**Detailed Analysis:** {item['desc']} ဤအချက်သည် ကျွန်တော်တို့၏ ဖေဖော်ဝါရီလ Content Strategy ကို ၅% ပြောင်းလဲစေနိုင်ပါသည်။")

        st.write("")
        st.divider()

        # --- RANKING TABLE SECTION ---
        st.markdown("### 🏆 Top 5 Strategic Topics Ranking")
        
        ranking_data = [
            {"Rank": "01", "Topic": "Agentic Commerce", "Category": "E-commerce", "Impact": "Extreme", "Source": "https://techcrunch.com"},
            {"Rank": "02", "Topic": "Small Language Models (SLM)", "Category": "Tech Strategy", "Impact": "High", "Source": "https://openai.com"},
            {"Rank": "03", "Topic": "Voice-First SEO", "Category": "Marketing", "Impact": "High", "Source": "https://searchengineland.com"},
            {"Rank": "04", "Topic": "Ethical AI Labeling", "Category": "Policy", "Impact": "Medium", "Source": "https://reuters.com"},
            {"Rank": "05", "Topic": "Hyper-Personalized Video", "Category": "Content Creation", "Impact": "Medium", "Source": "https://meta.com"}
        ]
        
        # Custom HTML Table for Professional Look
        table_html = """<table class="styled-table">
            <thead><tr><th>Rank</th><th>Strategic Topic</th><th>Industry Category</th><th>Impact</th><th>Source Link</th></tr></thead>
            <tbody>"""
        for row in ranking_data:
            table_html += f"""<tr>
                <td><b style="color:#58a6ff;">#{row['Rank']}</b></td>
                <td>{row['Topic']}</td>
                <td><span style="background:#30363d; padding:2px 8px; border-radius:10px; font-size:12px;">{row['Category']}</span></td>
                <td>{row['Impact']}</td>
                <td><a href="{row['Source']}" target="_blank" style="color:#58a6ff; text-decoration:none;">🌐 View Source</a></td>
            </tr>"""
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)

    # --- TAB 2: AUDIT (REMAINS AS PER v94) ---
    with tab_audit:
        st.markdown("### 🎭 Market Position & Sentiment Audit")
        c1, c2 = st.columns([1.5, 1])
        with c1:
            categories = ['Sentiment', 'Engagement', 'Reach', 'Innovation', 'Retention']
            fig = go.Figure()
            fig.add_trace(go.Scatterpolar(r=[88, 72, 92, 60, 85], theta=categories, fill='toself', name='Our Brand'))
            fig.add_trace(go.Scatterpolar(r=[65, 88, 78, 85, 50], theta=categories, fill='toself', name='Competitor A'))
            fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), template="plotly_dark", height=450)
            st.plotly_chart(fig, use_container_width=True)
        with c2:
            st.info("**Audit Result:** ကျွန်တော်တို့ Brand က Sentiment မှာ အားသာနေပေမယ့် Innovation (AI Content) မှာ ပြိုင်ဘက်ထက် အားနည်းနေပါတယ်။")

    # --- TAB 3: ADVICE (REMAINS AS PER v94) ---
    with tab_advice:
        st.markdown("### 🤖 Sayar Gyi's Strategic Action Room")
        st.markdown("""
            <div class="advice-box-v95">
                <h2 style="color:#58a6ff;">Executive Command</h2>
                <p>၁။ <b>Hook Evolution:</b> Video အစ ၂ စက္ကန့်ကို Visual Interrupt အသစ်များဖြင့် ပြောင်းလဲပါ။</p>
                <p>၂။ <b>Voice SEO:</b> Content များကို Conversational Q&A ပုံစံသို့ ပြောင်းလဲပါ။</p>
                <p style="margin-top:20px; color:#3fb950; font-weight:bold;">Next Week Prediction: Engagement up by 18%.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 3. EXECUTION ---
if __name__ == "__main__":
    apply_v95_styles()
    render_intelligence_hub()
