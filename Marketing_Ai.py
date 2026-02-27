import streamlit as st
import pandas as pd

def render_multi_platform_monitor():
    # --- 1. GLOBAL FILTERS (Meta Business Suite Style) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1px; text-transform:uppercase;">Global Insight Filters</p>', unsafe_allow_html=True)
    
    f1, f2, f3 = st.columns([1, 1, 1])
    with f1:
        platform = st.selectbox("Select Platform", ["Meta (FB & IG)", "TikTok", "YouTube"])
    with f2:
        date_range = st.selectbox("Date Range", ["Last 7 Days", "Last 28 Days", "Last 90 Days", "Custom Range"])
    with f3:
        content_type = st.multiselect("Content Type", ["Reels/Shorts", "Static Posts", "Long Video", "Stories"], default=["Reels/Shorts"])

    st.divider()

    # --- 2. PLATFORM SPECIFIC DEEP INSIGHTS ---
    
    # --- A. META (FACEBOOK/INSTAGRAM) VIEW ---
    if platform == "Meta (FB & IG)":
        st.subheader("🔵 Meta Business Performance")
        
        # Funnel Metrics (TOFU -> BOFU)
        t1, t2, t3 = st.columns(3)
        with t1:
            st.metric("Total Reach (TOFU)", "142.5K", "+15%")
            st.caption("Awareness through Ads & Reels")
        with t2:
            st.metric("Link Clicks / Msg (MOFU)", "2,840", "+8%")
            st.caption("Interest & Inquiries")
        with t3:
            st.metric("Closing / Sales (BOFU)", "420 Units", "+5%")
            st.caption("Completed Transactions")

        st.write("")
        # Deep Metrics Table (Like Meta Insights)
        st.markdown("##### Post Performance Breakdown")
        meta_data = pd.DataFrame({
            'Content Title': ['Jewelry Promo #1', 'Customer Review Video', 'Behind the Scene'],
            'Reach': [45000, 32000, 15000],
            'Eng. Rate': ['4.2%', '5.8%', '3.1%'],
            'Messages': [120, 340, 45],
            'Closing %': ['12%', '25%', '8%']
        })
        st.table(meta_data)

    # --- B. TIKTOK VIEW ---
    elif platform == "TikTok":
        st.subheader("🎵 TikTok Creator Insights")
        
        t1, t2, t3 = st.columns(3)
        with t1:
            st.metric("Video Views", "850K", "+42%")
            st.caption("TOFU: Discovery Velocity")
        with t2:
            st.metric("Avg. Watch Time", "12.4s", "Optimal")
            st.caption("MOFU: Content Retention")
        with t3:
            st.metric("Bio Link Clicks", "1,150", "+12%")
            st.caption("BOFU: Traffic to Sales")

        st.write("")
        st.markdown("##### Video Completion & Hook Analysis")
        # Visualizing Retention (Placeholder for Chart)
        st.info("AI Analysis: 'Hook' ၃ စက္ကန့်အတွင်း လူဝင်ကြည့်နှုန်း ၇၀% ရှိပါတယ်။ ဒါကြောင့် Retention ကောင်းနေပါတယ်။")

    # --- C. YOUTUBE VIEW ---
    elif platform == "YouTube":
        st.subheader("📽️ YouTube Channel Analytics")
        
        t1, t2, t3 = st.columns(3)
        with t1:
            st.metric("Impressions", "2.1M", "+5%")
            st.caption("TOFU: Search Presence")
        with t2:
            st.metric("CTR (Click-Through)", "8.2%", "Healthy")
            st.caption("MOFU: Thumbnail Efficiency")
        with t3:
            st.metric("Watch Time (Hours)", "14.5K", "+2.1K")
            st.caption("BOFU: Authority Building")

    st.divider()

    # --- 3. AI AUDIT LOG (Cross-Platform) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#3fb950; letter-spacing:1px; text-transform:uppercase;">AI Agent Efficiency Log</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div style="background: #161b22; padding: 15px; border-radius: 8px; border: 1px solid #30363d;">
            <p style="color: #e1e4e8; font-size: 14px;">
            <b>Audit Report:</b> {platform} အား စစ်ဆေးရာတွင် <b>{content_type}</b> များသည် <b>{date_range}</b> အတွင်း 
            Closing Rate ပိုကောင်းလာကြောင်း တွေ့ရပါသည်။ Messenger Agent ၏ လုပ်ဆောင်ချက်မှာ ပုံမှန်ရှိသော်လည်း 
            Comment များကို Reply ပြန်သည့်နှုန်း ၅% တိုးမြှင့်ရန် လိုအပ်ပါသည်။
            </p>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    render_multi_platform_monitor()
