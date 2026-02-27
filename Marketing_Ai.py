import streamlit as st
import pandas as pd

# --- 1. SMART NEWS ENGINE (Logic) ---
def get_smart_news():
    # ဒါက AI ကနေ Fetch လုပ်လာမယ့် သတင်းစုစုပေါင်းစာရင်းပါ။
    all_news = [
        {"tag": "CRITICAL", "title": "OpenAI SearchGPT Global Rollout", "impact": "SEO Strategy ပြောင်းရန် လိုအပ်။", "score": 98},
        {"tag": "ALGORITHM", "title": "Instagram Andromeda Retention Update", "impact": "Dwell time ပိုအရေးကြီးလာ။", "score": 95},
        {"tag": "AD TECH", "title": "TikTok Conversational Ads 2.0", "impact": "Lead generation ပိုကောင်းလာ။", "score": 90},
        {"tag": "POLICY", "title": "New Privacy Rules in 2026", "impact": "Data tracking ပြောင်းလဲမည်။", "score": 85},
        {"tag": "AI TREND", "title": "Generative Video for B2B", "impact": "Production cost ၄၀% လျော့ကျနိုင်။", "score": 82},
    ]
    return all_news

# --- 2. UI LAYOUT ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-weight:900;">Intelligence Command Center</h1>', unsafe_allow_html=True)
    
    # --- SMART NEWS SECTION ---
    st.markdown("### 🌐 Smart Market Pulse")
    
    news_data = get_smart_news()
    
    # ထိပ်ဆုံးက အရေးကြီးဆုံး (၃) ခုကို Card အဖြစ်ပြမည်
    top_3 = news_data[:3]
    cols = st.columns(3)
    
    for i, news in enumerate(top_3):
        with cols[i]:
            st.markdown(f"""
                <div style="background:#161b22; border: 1px solid #30363d; padding:20px; border-radius:12px; height:180px;">
                    <span style="background:rgba(218, 54, 51, 0.2); color:#ff7b72; padding:2px 10px; border-radius:10px; font-size:10px; font-weight:bold;">{news['tag']}</span>
                    <p style="font-weight:bold; margin-top:10px;">{news['title']}</p>
                    <p style="color:#8b949e; font-size:12px;">{news['impact']}</p>
                </div>
            """, unsafe_allow_html=True)

    # --- THE SMART CONTROL: NEWS FEED ARCHIVE ---
    st.write("")
    with st.expander("📂 View All Relevant Industry News (Today's Feed)"):
        # သတင်းအားလုံးကို ဇယားပုံစံ (သို့မဟုတ်) List ပုံစံနဲ့ နေရာမစားဘဲ ဖတ်နိုင်ရန်
        for news in news_data[3:]:
            st.markdown(f"""
                <div style="padding: 10px; border-bottom: 1px solid #30363d; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <b style="color:#58a6ff;">[{news['tag']}]</b> {news['title']}
                    </div>
                    <div style="font-size: 11px; color:#8b949e;">Impact Score: {news['score']}%</div>
                </div>
            """, unsafe_allow_html=True)
        
        st.write("")
        st.button("🔄 Sync Live AI News Nodes")

    st.divider()
    st.markdown("### 🎭 Deep Audit & Strategy")
    # ... ကျန်ရှိသော Radar Chart နှင့် Advice များ ...

if __name__ == "__main__":
    render_intelligence_hub()
