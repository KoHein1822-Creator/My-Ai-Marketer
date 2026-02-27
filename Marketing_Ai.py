import streamlit as st
import pandas as pd

# --- [V32.0 ORIGINAL DATABASE & SESSION STATE] ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
# Industry News Data (Restored)
news_data = [
    {"date": "2026-02-25", "news": "ရွှေဈေးကွက်အတွင်း ဝယ်လိုအား ပြန်လည်မြင့်တက်လာ"},
    {"date": "2026-02-24", "news": "AI Video Generation နည်းပညာအသစ် TikTok တွင် ခေတ်စားလာ"}
]
# Project Archive & Asset Library (Restored)
archive_data = pd.DataFrame({"Project": ["Promotion A", "Brand Launch"], "Status": ["Finished", "Ongoing"]})

# --- [PAGE CONFIG - V32.0 ORIGINAL] ---
st.set_page_config(page_title="SAYAR GYI v32.0+", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- [SIDE PANEL - V32.0 ORIGINAL STRUCTURE + ADD-ONS] ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    # --- [UPGRADES SECTION - NEW ADD-ONS ONLY] ---
    st.markdown('<p class="nav-label">Executive Upgrades (New)</p>', unsafe_allow_html=True)
    if st.button("📊 Executive Report AI", use_container_width=True): st.session_state.menu = "Executive Report"
    if st.button("🛡️ Strategy & Guard Dog", use_container_width=True): st.session_state.menu = "Guard Dog"
    if st.button("👥 Ethical Lead CRM", use_container_width=True): st.session_state.menu = "Leads"

    st.divider()
    # --- [V32.0 ORIGINAL EXECUTION BUTTONS] ---
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content Production"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"
    if st.button("🚨 Monitoring & Spy Center", use_container_width=True): st.session_state.menu = "Monitoring"

    st.divider()
    # --- [V32.0 ORIGINAL RADIO NAV] ---
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    # Sync radio with menu
    if nav_choice in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"] and st.session_state.menu not in ["Executive Report", "Guard Dog", "Leads", "Content Production", "Engagement", "Monitoring"]:
        st.session_state.menu = nav_choice

    st.divider()
    st.success("Core Engine: v32.0 Original + Upgrades")

# --- [MAIN INTERFACE - V32.0 ORIGINAL LAYOUTS + ADD-ON PAGES] ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    # Original V32.0 Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Total Engagement", "12,450", "+15%")
    m2.metric("Active Campaigns", "4", "Stable")
    m3.metric("AI Efficiency", "98%", "+2%")
    
    st.divider()
    # Original V32.0 Industry News Section
    st.subheader("📰 Industry News (Restored)")
    for news in news_data:
        st.write(f"**[{news['date']}]** - {news['news']}")

elif st.session_state.menu == "Project Archive":
    st.title("📂 Project Archive")
    st.table(archive_data)

elif st.session_state.menu == "Asset Library":
    st.title("📦 Asset Library")
    st.write("Original assets and media files preserved.")

# --- [LOGIC FOR NEW UPGRADES] ---
elif st.session_state.menu == "Executive Report":
    st.markdown('<h1 class="header-blue">📊 Executive Report</h1>', unsafe_allow_html=True)
    st.write("AI-Generated Monthly Summary...")

elif st.session_state.menu == "Guard Dog":
    st.markdown('<h1 style="color:#ff4b4b;">🛡️ Guard Dog Crisis Control</h1>', unsafe_allow_html=True)
    st.error("No Crisis Detected. Monitoring 24/7.")

elif st.session_state.menu == "Leads":
    st.markdown('<h1 style="color:#aff5b4;">👥 Lead CRM</h1>', unsafe_allow_html=True)
    st.write("Ethical leads from inbox-only strategy.")

elif st.session_state.menu == "Content Production":
    st.title("🎬 Content Production")
    st.info("Upgraded: 1-Month Bulk Generation Ready.")
    st.button("Start Bulk Multimedia Render")

else:
    st.title(st.session_state.menu)
