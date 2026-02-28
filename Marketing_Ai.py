import streamlit as st
import pandas as pd

# --- 1. GLOBAL SETTINGS & CSS ---
st.set_page_config(layout="wide", page_title="SAYAR GYI v98.0")

def apply_v98_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; }
        .news-card-v98 { background: #0d1117; border: 1px solid #30363d; border-radius: 12px; margin-bottom: 20px; overflow: hidden; }
        .burmese-summary { background: #161b22; padding: 12px; border-radius: 8px; font-size: 13px; margin-top: 10px; border-left: 3px solid #58a6ff; }
        .impact-badge { background: #238636; color: white; padding: 2px 8px; border-radius: 10px; font-size: 11px; font-weight: bold; }
        
        /* Styled Table for Ranking */
        .rank-table { width: 100%; border-collapse: collapse; margin-top: 15px; background: #0d1117; border-radius: 10px; overflow: hidden; }
        .rank-table th { background: #161b22; color: #58a6ff; text-align: left; padding: 15px; border-bottom: 2px solid #30363d; }
        .rank-table td { padding: 15px; border-bottom: 1px solid #21262d; color: #adbac7; font-size: 13px; }
        .rank-id { font-weight: 800; color: #58a6ff; }
        </style>
    """, unsafe_allow_html=True)

# --- 2. DATA ENGINE ---
def render_ranking_table(data_list, is_local=False):
    tbl_html = """<table class="rank-table">
        <thead><tr><th>Rank</th><th>Topic / Source</th><th>Summary</th><th>Impact</th></tr></thead><tbody>"""
    for item in data_list:
        source_icon = "🔵 FB" if "facebook.com" in item['link'] else "🌐 Web"
        summary_text = item['mm_summary']
        tbl_html += f"""<tr>
            <td class="rank-id">{item['rank']}</td>
            <td><b>{item['topic']}</b><br><a href="{item['link']}" target="_blank" style="color:#58a6ff; text-decoration:none; font-size:11px;">{source_icon} Link 🔗</a></td>
            <td>{summary_text}</td>
            <td><span class="impact-badge">{item['impact']}</span></td>
        </tr>"""
    tbl_html += "</tbody></table>"
    st.markdown(tbl_html, unsafe_allow_html=True)

# --- 3. INTERFACE ---
def render_hub():
    st.markdown('<h1 style="font-weight:900;">Intelligence Hub v98.0</h1>', unsafe_allow_html=True)
    
    tab_global, tab_local = st.tabs(["🌐 Global Market Pulse", "🇲🇲 Myanmar Local Pulse"])

    # --- TAB 1: GLOBAL PULSE ---
    with tab_global:
        st.markdown("### 🔥 High-Impact Global Highlights")
        g1, g2, g3 = st.columns(3)
        # (Top 3 Cards as per v97 style with Hyperlinks)
        global_top = [
            {"title": "OpenAI SearchGPT Ads 🔗", "url": "https://openai.com", "img": "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=400", "mm": "Conversational SEO ပြောင်းလဲလာမှု။"},
            {"title": "Meta Andromeda Update 🔗", "url": "https://about.fb.com", "img": "https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=400", "mm": "Dwell time rank ပေးသည့် စနစ်သစ်။"},
            {"title": "TikTok Discovery 2.0 🔗", "url": "https://newsroom.tiktok.com", "img": "https://images.unsplash.com/photo-1611162616305-c69b3fa7fbe0?w=400", "mm": "Search-based discovery အားကောင်းလာမှု။"}
        ]
        cols = [g1, g2, g3]
        for i, news in enumerate(global_top):
            with cols[i]:
                st.markdown(f"""<div class="news-card-v98"><img src="{news['img']}" style="width:100%; height:140px; object-fit:cover;">
                <div style="padding:15px;"><a href="{news['url']}" target="_blank" style="color:white; text-decoration:none; font-weight:bold;">{news['title']}</a>
                <div class="burmese-summary">🇲🇲 {news['mm']}</div></div></div>""", unsafe_allow_html=True)
        
        st.divider()
        st.markdown("### 📊 Top 5 Related Global Topics (Translated)")
        global_related = [
            {"rank": "#1", "topic": "Agentic Commerce", "link": "https://techcrunch.com", "mm_summary": "AI က စျေးဝယ်သူကိုယ်စား ဆုံးဖြတ်ချက်ချပေးသည့် စနစ်သစ်။", "impact": "98%"},
            {"rank": "#2", "topic": "SLM Optimization", "link": "https://openai.com", "mm_summary": "ကုန်ကျစရိတ်သက်သာသော AI Model ငယ်များ လုပ်ငန်းသုံးလာခြင်း။", "impact": "92%"},
            {"rank": "#3", "topic": "Voice-First SEO", "link": "https://searchengineland.com", "mm_summary": "စကားပြောရှာဖွေမှုအတွက် Keyword Strategy ပြောင်းလဲခြင်း။", "impact": "89%"},
            {"rank": "#4", "topic": "Ethical AI Policy", "link": "https://reuters.com", "mm_summary": "AI Content များကို အမှတ်အသားပြုလုပ်ရန် ဥပဒေသစ်များ။", "impact": "85%"},
            {"rank": "#5", "topic": "Video Personalization", "link": "https://meta.com", "mm_summary": "User တစ်ဦးချင်းစီအတွက် AI က Video ဖန်တီးပေးသည့် နည်းပညာ။", "impact": "82%"}
        ]
        render_ranking_table(global_related)

    # --- TAB 2: MYANMAR LOCAL PULSE ---
    with tab_local:
        st.markdown("### 🇲🇲 Myanmar Verified High-Impact")
        l1, l2, l3 = st.columns(3)
        local_top = [
            {"title": "Reali-Tea Trend 🔗", "url": "https://facebook.com/marketing_news_mm", "img": "https://images.unsplash.com/photo-1551818255-e6e10975bc17?w=400", "mm": "Authentic content များက Engagement ပိုရနေသည်။"},
            {"title": "Telegram Shift 🔗", "url": "https://facebook.com/tech_mm", "img": "https://images.unsplash.com/photo-1611606063065-ee7946f0787a?w=400", "mm": "လုပ်ငန်းများ Telegram Community သို့ ပြောင်းရွှေ့လာခြင်း။"},
            {"title": "AI Burmese Voice 🔗", "url": "https://ai_myanmar_web.com", "img": "https://images.unsplash.com/photo-1589254065878-42c9da997008?w=400", "mm": "မြန်မာသံဖြင့် AI နောက်ခံစကားပြောစနစ် ခေတ်စားလာခြင်း။"}
        ]
        l_cols = [l1, l2, l3]
        for i, news in enumerate(local_top):
            with l_cols[i]:
                st.markdown(f"""<div class="news-card-v98"><img src="{news['img']}" style="width:100%; height:140px; object-fit:cover;">
                <div style="padding:15px;"><a href="{news['url']}" target="_blank" style="color:white; text-decoration:none; font-weight:bold;">{news['title']}</a>
                <div class="burmese-summary">🇲🇲 {news['mm']}</div></div></div>""", unsafe_allow_html=True)

        st.divider()
        st.markdown("### 🏆 Top 5 Ranked Myanmar Topics (Verified)")
        local_related = [
            {"rank": "#1", "topic": "FB Marketplace Shift", "link": "https://facebook.com/groups/mm_business", "mm_summary": "Facebook Marketplace Algorithm အပြောင်းအလဲနှင့် ရောင်းသူများ၏ ပြင်ဆင်မှု။", "impact": "97%"},
            {"rank": "#2", "topic": "Kpay Integration Trends", "link": "https://mm_biz_web.com/fintech", "mm_summary": "Digital Payment များ Content ထဲတွင် တိုက်ရိုက်ချိတ်ဆက်လာမှု။", "impact": "94%"},
            {"rank": "#3", "topic": "Local Influencer ROI", "link": "https://facebook.com/agency_insight_mm", "mm_summary": "မြန်မာ Influencer များ၏ တကယ့် ROI ကို AI ဖြင့် တွက်ချက်ပြသခြင်း။", "impact": "90%"},
            {"rank": "#4", "topic": "Content Copyright MM", "link": "https://law_mm_web.org", "mm_summary": "မြန်မာပြည်တွင်း Content ခိုးယူမှုများအတွက် ဥပဒေပိုင်းဆိုင်ရာ သတိပေးချက်များ။", "impact": "88%"},
            {"rank": "#5", "topic": "Messenger Bot 2026", "link": "https://facebook.com/bot_strategy_mm", "mm_summary": "အလိုအလျောက်ပြန်ကြားပေးသည့် AI Bot များ ပိုမိုတွင်ကျယ်လာခြင်း။", "impact": "85%"}
        ]
        render_ranking_table(local_related, is_local=True)

if __name__ == "__main__":
    apply_v98_styles()
    render_hub()
