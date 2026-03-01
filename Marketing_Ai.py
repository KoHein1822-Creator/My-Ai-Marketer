import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v145.0 | Mastermind Executive",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS ---
def apply_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        /* Dashboard Styles */
        .main-header { color: #58a6ff; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 15px; border-left: 5px solid #58a6ff; padding-left: 15px; }
        .status-box-v88 { background: #161b22; border: 1px solid #30363d; padding: 30px 15px; border-radius: 12px; text-align: center; }
        .insight-card-v88 { background: #161b22; border: 1px solid #30363d; padding: 22px; border-radius: 15px; margin-bottom: 15px; }
        .m-label-v88 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        .header-flex { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; }
        
        /* Intel Hub Styles */
        .intel-card { background: #161b22; border: 1px solid #30363d; border-radius: 12px; overflow: hidden; margin-bottom: 20px; transition: transform 0.2s;}
        .intel-card:hover { transform: translateY(-5px); border-color: #58a6ff;}
        .intel-img { width: 100%; height: 140px; object-fit: cover; border-bottom: 1px solid #30363d; }
        .intel-content { padding: 15px; }
        .intel-title a { font-size: 15px; font-weight: 700; color: #ffffff; margin-bottom: 8px; text-decoration: none; display:block; transition: color 0.2s;}
        .intel-title a:hover { color: #58a6ff; text-decoration: underline; }
        .intel-desc { font-size: 13px; color: #8b949e; background: #0d1117; padding: 8px; border-radius: 6px; border-left: 3px solid #58a6ff;}
        
        /* Custom Table */
        .intel-table { width: 100%; border-collapse: collapse; margin-top: 10px; }
        .intel-table th { text-align: left; padding: 12px 15px; color: #58a6ff; font-size: 14px; border-bottom: 1px solid #30363d; background: #161b22; }
        .intel-table td { padding: 15px; border-bottom: 1px solid #30363d; color: #e6edf3; font-size: 14px; vertical-align: middle; }
        .rank-col { color: #8b949e; font-weight: bold; }
        .link-text { color: #58a6ff; font-size: 12px; text-decoration: none; display: block; margin-top: 4px; font-weight: 600;}
        .link-text:hover { text-decoration: underline; color: #79c0ff;}
        .impact-badge { background: rgba(63, 185, 80, 0.15); color: #3fb950; padding: 5px 10px; border-radius: 20px; font-weight: 700; font-size: 12px; text-align: center; display: inline-block; border: 1px solid rgba(63, 185, 80, 0.3); }
        
        /* Report/Insights Styles */
        .report-box { background: #161b22; border: 1px solid #30363d; padding: 25px; border-radius: 12px; margin-top: 15px; }
        .report-header { color: #58a6ff; font-size: 18px; font-weight: 700; border-bottom: 1px solid #30363d; padding-bottom: 10px; margin-bottom: 15px;}
        
        /* Tabs Styling Override */
        [data-baseweb="tab-list"] { gap: 24px; }
        [data-baseweb="tab"] { padding-top: 10px; padding-bottom: 10px; }
        </style>
    """, unsafe_allow_html=True)

# --- 3. MASTER SIDE PANEL ---
def render_sidebar():
    if 'page' not in st.session_state:
        st.session_state.page = "Intelligence"

    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("### SAYAR GYI'S INTELLIGENCE")
        if st.button("🧠 Deep Strategy & Reports", use_container_width=True):
            st.session_state.page = "Intelligence"
        
        st.divider()
        st.markdown("### MENU")
        
        nav_options = ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive", "🎨 Asset Library"]
        current_idx = nav_options.index(st.session_state.page) if st.session_state.page in nav_options else None
        
        def on_nav_change():
            st.session_state.page = st.session_state.menu_radio

        st.radio("Nav", nav_options, index=current_idx, key="menu_radio", on_change=on_nav_change, label_visibility="collapsed")

        st.divider()
        st.markdown("### MY AGENTS")
        st.caption("🤖 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
        st.write("")
        st.button("🔥 Switch to Creator Mode", use_container_width=True)
        st.divider()
        st.success("Core Engine: Online")

# --- 4. DASHBOARD ENGINE (Hidden in this view, accessible via menu) ---
def render_dashboard():
    st.title("📊 Strategic Dashboard")
    st.info("Navigate to Intelligence to see the requested views.")

# --- 5. INTELLIGENCE HUB ENGINE ---
def render_intelligence_hub():
    st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px; margin-bottom: 20px;">Sayar Gyi Mastermind Suite</h1>', unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["🌐 Global News", "🇲🇲 MM Local Pulse", "🧠 Deep Insights", "📄 Weekly Report"])
    
    # --- TAB 1: GLOBAL NEWS ---
    with tab1:
        st.markdown('<h3 style="margin-top: 15px; margin-bottom: 15px;">🔥 High-Impact Global Highlights</h3>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        
        cards_data = [
            ("https://images.unsplash.com/photo-1677442136019-21780ecad995?auto=format&fit=crop&w=800&q=80", "OpenAI SearchGPT Ads 🔗", "https://openai.com/search", "MM Conversational SEO ပြောင်းလဲလာမှုများ"),
            ("https://images.unsplash.com/photo-1611162617474-5b21e879e113?auto=format&fit=crop&w=800&q=80", "Meta Andromeda Update 🔗", "https://about.meta.com", "MM Dwell time rank ပေးသည့် စနစ်သစ်"),
            ("https://images.unsplash.com/photo-1611605698335-8b1569810432?auto=format&fit=crop&w=800&q=80", "TikTok Discovery 2.0 🔗", "https://newsroom.tiktok.com", "MM Search-based discovery အားကောင်းလာမှုများ")
        ]
        
        for idx, col in enumerate([c1, c2, c3]):
            with col:
                st.markdown(f"""
                <div class="intel-card">
                    <img src="{cards_data[idx][0]}" class="intel-img">
                    <div class="intel-content">
                        <div class="intel-title"><a href="{cards_data[idx][2]}" target="_blank">{cards_data[idx][1]}</a></div>
                        <div class="intel-desc">{cards_data[idx][3]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="margin-top: 25px; margin-bottom: 10px;">📊 Top 5 Related Global Topics (Translated)</h3>', unsafe_allow_html=True)
        global_table_html = """
        <table class="intel-table">
            <tr><th>Rank</th><th>Topic / Source</th><th>Summary</th><th>Impact</th></tr>
            <tr><td class="rank-col">#1</td><td>Agentic Commerce<a href="https://techcrunch.com" target="_blank" class="link-text">🔗 Web Link</a></td><td>AI က ဈေးဝယ်သူကိုယ်စား ဆုံးဖြတ်ချက်ချပေးမည့် စနစ်သစ်</td><td><span class="impact-badge">95%</span></td></tr>
            <tr><td class="rank-col">#2</td><td>SLM Optimization<a href="https://huggingface.co" target="_blank" class="link-text">🔗 Web Link</a></td><td>ကုန်ကျစရိတ်သက်သာသော AI Model ငယ်များ လုပ်ငန်းသုံးလာခြင်း</td><td><span class="impact-badge">92%</span></td></tr>
            <tr><td class="rank-col">#3</td><td>Voice-First SEO<a href="https://searchengineland.com" target="_blank" class="link-text">🔗 Web Link</a></td><td>စကားပြောရှာဖွေမှုအတွက် Keyword Strategy ပြောင်းလဲခြင်း</td><td><span class="impact-badge">89%</span></td></tr>
            <tr><td class="rank-col">#4</td><td>Ethical AI Policy<a href="https://wired.com" target="_blank" class="link-text">🔗 Web Link</a></td><td>AI Content များကို အမှတ်အသားပြုလုပ်ရန် ဥပဒေသစ်များ</td><td><span class="impact-badge">85%</span></td></tr>
            <tr><td class="rank-col">#5</td><td>Video Personalization<a href="https://techradar.com" target="_blank" class="link-text">🔗 Web Link</a></td><td>User တစ်ဦးချင်းစီအတွက် AI က Video ဖန်တီးပေးသည့် နည်းပညာ</td><td><span class="impact-badge">83%</span></td></tr>
        </table>
        """
        st.markdown(global_table_html, unsafe_allow_html=True)

    # --- TAB 2: MYANMAR LOCAL PULSE ---
    with tab2:
        st.markdown('<h3 style="margin-top: 15px; margin-bottom: 15px;">🇲🇲 MM Myanmar Verified High-Impact</h3>', unsafe_allow_html=True)
        c1, c2, c3 = st.columns(3)
        
        local_cards_data = [
            ("https://images.unsplash.com/photo-1543269865-cbf427effbad?auto=format&fit=crop&w=800&q=80", "Reali-Tea Trend 🔗", "https://facebook.com", "MM Authentic content များက Engagement ပိုရနေသည်"),
            ("https://images.unsplash.com/photo-1614680376593-902f74cf0d41?auto=format&fit=crop&w=800&q=80", "Telegram Shift 🔗", "https://telegram.org", "MM လုပ်ငန်းများ Telegram Community သို့ ပြောင်းရွှေ့လာခြင်း"),
            ("https://images.unsplash.com/photo-1589254065878-42c9da997008?auto=format&fit=crop&w=800&q=80", "AI Burmese Voice 🔗", "https://github.com", "MM မြန်မာလိုပြော၍ AI မှတ်တမ်းရေးသည့် စနစ် ခေတ်စားလာခြင်း")
        ]
        
        for idx, col in enumerate([c1, c2, c3]):
            with col:
                st.markdown(f"""
                <div class="intel-card">
                    <img src="{local_cards_data[idx][0]}" class="intel-img">
                    <div class="intel-content">
                        <div class="intel-title"><a href="{local_cards_data[idx][2]}" target="_blank">{local_cards_data[idx][1]}</a></div>
                        <div class="intel-desc">{local_cards_data[idx][3]}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="margin-top: 25px; margin-bottom: 10px;">🏆 Top 5 Ranked Myanmar Topics (Verified)</h3>', unsafe_allow_html=True)
        local_table_html = """
        <table class="intel-table">
            <tr><th>Rank</th><th>Topic / Source</th><th>Summary</th><th>Impact</th></tr>
            <tr><td class="rank-col">#1</td><td>FB Marketplace Shift<a href="https://facebook.com/business" target="_blank" class="link-text">🔗 FB Link</a></td><td>Facebook Marketplace Algorithm အပြောင်းအလဲကြောင့် ရောင်းချသူများအခက်တွေ့</td><td><span class="impact-badge">97%</span></td></tr>
            <tr><td class="rank-col">#2</td><td>Kpay Integration Trends<a href="https://kbzpay.com" target="_blank" class="link-text">🔗 Web Link</a></td><td>Digital Payment များ Content ထဲတွင် တိုက်ရိုက်ချိတ်ဆက်လာမှု</td><td><span class="impact-badge">94%</span></td></tr>
            <tr><td class="rank-col">#3</td><td>Local Influencer ROI<a href="https://facebook.com" target="_blank" class="link-text">🔗 FB Link</a></td><td>မြန်မာ Influencer များ၏ တကယ်တမ်း ROI ချပြရန် တောင်းဆိုမှုများလာခြင်း</td><td><span class="impact-badge">90%</span></td></tr>
            <tr><td class="rank-col">#4</td><td>Content Copyright MM<a href="https://google.com/search?q=Myanmar+Copyright" target="_blank" class="link-text">🔗 Web Link</a></td><td>မြန်မာပြည်တွင် Content ခိုးယူမှုများအတွက် ဥပဒေပိုင်းဆိုင်ရာ သတိပေးချက်များ</td><td><span class="impact-badge">88%</span></td></tr>
            <tr><td class="rank-col">#5</td><td>Messenger Bot 2026<a href="https://developers.facebook.com" target="_blank" class="link-text">🔗 FB Link</a></td><td>လမ်းကြောင်းပြောင်းလာသော Messenger Bot များကို ပြန်လည်အသုံးပြုလာခြင်း</td><td><span class="impact-badge">85%</span></td></tr>
        </table>
        """
        st.markdown(local_table_html, unsafe_allow_html=True)

    # --- TAB 3: DEEP INSIGHTS (V101) ---
    with tab3:
        st.markdown('<h3 style="margin-top: 15px; margin-bottom: 5px;">🧠 AI Deep Strategic Insights</h3>', unsafe_allow_html=True)
        st.caption("Auto-generated based on Global & Local Pulse Data")
