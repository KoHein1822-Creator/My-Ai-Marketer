import streamlit as st
import pandas as pd
import numpy as np

# --- 1. GLOBAL CONFIGURATION ---
st.set_page_config(
    layout="wide", 
    page_title="SAYAR GYI v88.0 | Balanced Executive",
    page_icon="⚖️"
)

# --- 2. PREMIUM CSS ---
def apply_v88_styles():
    st.markdown("""
        <style>
        .block-container { padding-top: 1.5rem; max-width: 96%; padding-bottom: 5rem; }
        [data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
        
        .main-header {
            color: #58a6ff; font-size: 13px; font-weight: 700;
            text-transform: uppercase; letter-spacing: 2px;
            margin-bottom: 15px; border-left: 5px solid #58a6ff; padding-left: 15px;
        }

        .status-box-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 30px 15px; border-radius: 12px; text-align: center;
        }
        
        .insight-card-v88 {
            background: #161b22; border: 1px solid #30363d;
            padding: 22px; border-radius: 15px; margin-bottom: 15px;
        }
        
        .m-label-v88 { color: #8b949e; font-size: 14px; font-weight: 600; text-transform: uppercase; margin-bottom: 5px; }
        .m-value-v88 { color: #ffffff; font-size: 34px; font-weight: 800; line-height: 1.1; }
        .m-delta-v88 { color: #3fb950; font-size: 14px; font-weight: 700; background: rgba(63, 185, 80, 0.1); padding: 3px 8px; border-radius: 5px; }
        
        .header-flex {
            display: flex; justify-content: space-between; align-items: center;
            margin-bottom: 18px;
        }
        </style>
    """, unsafe_allow_html=True)

# --- 3. MASTER SIDE PANEL (FIXED STATE LOGIC) ---
def render_sidebar():
    # Session State စတင်သတ်မှတ်ခြင်း
    if 'page' not in st.session_state:
        st.session_state.page = "📊 Interactive Dashboard"

    with st.sidebar:
        st.markdown('<h2 style="margin-bottom:0; color:white;">SAYAR GYI\'S</h2>', unsafe_allow_html=True)
        st.markdown('<p style="color:#58a6ff; font-size:11px; text-transform:uppercase; letter-spacing:1px;">AI Marketing Agency</p>', unsafe_allow_html=True)
        st.write("")
        
        st.markdown("### SAYAR GYI'S INTELLIGENCE")
        # Intelligence Button နှိပ်လျှင် State ပြောင်းရန် Logic
        if st.button("🧠 Deep Strategy & Reports", use_container_width=True):
            st.session_state.page = "Intelligence"
        
        st.divider()
        st.markdown("### MENU")
        
        nav_options = ["📊 Interactive Dashboard", "🧬 Brand DNA", "📂 Project Archive", "🎨 Asset Library"]
        
        # FIX: အကယ်၍ Intelligence Page ရောက်နေလျှင် Menu Radio ကို Unselect လုပ်ထားမည် (index=None)
        # သို့မှသာ Button နှင့် Radio အချင်းချင်း ငြိခြင်း (Conflict) ဖြစ်မည်မဟုတ်ပါ။
        current_idx = nav_options.index(st.session_state.page) if st.session_state.page in nav_options else None
        
        def on_nav_change():
            st.session_state.page = st.session_state.menu_radio

        # Callback သုံးပြီး Radio ရဲ့ အပြောင်းအလဲကို ဖမ်းယူခြင်း
        st.radio("Nav", nav_options, index=current_idx, key="menu_radio", on_change=on_nav_change, label_visibility="collapsed")

        st.divider()
        st.markdown("### MY AGENTS")
        st.caption("🤖 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops")
        st.write("")
        st.button("🔥 Switch to Creator Mode", use_container_width=True)
        st.divider()
        st.success("Core Engine: Online")
        st.write("")
        st.markdown("### MODEL")
        st.radio("Engine", ["Gemini 1.5 Pro", "GPT-4o", "Claude 3.5"], horizontal=True, label_visibility="collapsed")

# --- 4. BALANCED DASHBOARD ENGINE ---
def render_dashboard():
    h_col, f_col = st.columns([1.5, 1])
    with h_col:
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    with f_col:
        c1, c2, c3 = st.columns(3)
        with c1: platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"])
        with c2: timeframe = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly"])
        with c3: chart_style = st.selectbox("View Style", ["Line Chart", "Area Chart", "Bar Chart"])

    st.markdown('<p class="main-header" style="margin-top:20px;">Content Creation Status</p>', unsafe_allow_html=True)
    p1, p2, p3, p4 = st.columns(4)
    pipeline = [("Drafting", "12"), ("Pending", "5"), ("Scheduled", "18"), ("Published", "145")]
    for i, (label, val) in enumerate(pipeline):
        with [p1, p2, p3, p4][i]:
            st.markdown(f'<div class="status-box-v88"><div class="m-label-v88">{label}</div>'
                        f'<div style="font-size:42px; font-weight:900; color:#58a6ff; margin-top:10px;">{val}</div></div>', unsafe_allow_html=True)

    st.write("")
    st.write("")
    st.markdown(f'<p class="main-header">{platform} Deep Insights & Trends</p>', unsafe_allow_html=True)

    def render_balanced_card(label, value, delta):
        st.markdown(f"""
            <div class="insight-card-v88">
                <div class="m-label-v88">{label}</div>
                <div class="header-flex">
                    <span class="m-value-v88">{value}</span>
                    <span class="m-delta-v88">{delta}</span>
                </div>
        """, unsafe_allow_html=True)
        data = pd.DataFrame(np.random.randn(25, 1), columns=['Val'])
        if chart_style == "Line Chart": st.line_chart(data, height=170, use_container_width=True)
        elif chart_style == "Area Chart": st.area_chart(data, height=170, use_container_width=True)
        else: st.bar_chart(data, height=170, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    metrics = {
        "Facebook": [("Views", "85.2K", "↑12%"), ("Interactions", "3.2K", "↑8%"), ("Followers", "12.4K", "↑1%"), ("Page Visits", "4.5K", "↑15%"), ("Link Clicks", "920", "↑22%"), ("Conversations", "128", "↑5%")],
        "TikTok": [("Video Views", "1.2M", "↑45%"), ("Shares", "12K", "↑30%"), ("Saves", "4.5K", "↑18%"), ("Profile Visits", "25K", "↑10%"), ("Bio Clicks", "1.5K", "↑25%"), ("Completion", "65%", "↑5%")],
        "YouTube": [("Impressions", "2.5M", "↑5%"), ("Watch Time", "14K h", "↑12%"), ("Subscribers", "420", "↑2%"), ("Avg Duration", "4:32", "↑0:45"), ("CTR", "8.5%", "↑1.2%"), ("Comments", "850", "↑15%")]
    }
    selected_metrics = metrics[platform]

    col_group1 = st.columns(3)
    for i in range(3):
        with col_group1[i]: render_balanced_card(selected_metrics[i][0], selected_metrics[i][1], selected_metrics[i][2])
    col_group2 = st.columns(3)
    for i in range(3, 6):
        with col_group2[i-3]: render_balanced_card(selected_metrics[i][0], selected_metrics[i][1], selected_metrics[i][2])

# --- 5. EXECUTION ---
if __name__ == "__main__":
    apply_v88_styles()
    render_sidebar()
    
    # ရှင်းလင်းပြတ်သားသော Page Display Logic
    if st.session_state.page == "📊 Interactive Dashboard":
        render_dashboard()
    elif st.session_state.page == "Intelligence":
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Sayar Gyi\'s Intelligence</h1>', unsafe_allow_html=True)
        st.divider()
        st.info("Ready for Deep Insights & Weekly Reports Integration...")
    else:
        # အခြား Menu များ (Brand DNA, Project Archive, etc.)
        st.markdown(f'<h1 style="font-weight:900; margin:0; font-size:38px;">{st.session_state.page}</h1>', unsafe_allow_html=True)
        st.write("")
        st.info(f"{st.session_state.page} Module syncing...")

# --- 6. INTELLIGENCE HUB ENGINE ---
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
