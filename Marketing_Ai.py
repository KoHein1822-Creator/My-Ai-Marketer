import streamlit as st
import pandas as pd

# --- 1. SESSION STATE & DATABASE ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Interactive Dashboard"

# Mock Databases for v32.0
news_list = [
    {"date": "2026-02-25", "news": "AI Trend: Short-form video contents are leading the market."},
    {"date": "2026-02-24", "news": "Facebook algorithm update affects organic reach for businesses."}
]

archive_data = pd.DataFrame({
    "Project Name": ["New Year Promotion", "Brand DNA Setup", "Valentine Special"],
    "Status": ["Completed", "Active", "Archived"],
    "Date": ["Jan 2026", "Feb 2026", "Feb 2026"]
})

# --- 2. PAGE CONFIG & v32.0 THEME ---
st.set_page_config(page_title="SAYAR GYI v32.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v32.0 Structure) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content Production"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"

    st.divider()
    st.markdown('<p class="nav-label">Intelligence</p>', unsafe_allow_html=True)
    if st.button("🚨 Monitoring & Spy Center", use_container_width=True): st.session_state.menu = "Monitoring"

    st.divider()
    # v32.0 Original Radio Navigation
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    # Logic to prioritize button clicks over radio if necessary
    if nav_choice in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"] and st.session_state.menu not in ["Content Production", "Engagement", "Monitoring"]:
        st.session_state.menu = nav_choice

    st.divider()
    st.success("Core Engine: v32.0 Active")

# --- 4. MAIN INTERFACE ---

if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    # Original Metrics
    m1, m2, m3 = st.columns(3)
    m1.metric("Engagement", "12,450", "+15%")
    m2.metric("Active Campaigns", "4", "Stable")
    m3.metric("AI Efficiency", "98%", "+2%")
    
    st.divider()
    
    # Original Industry News
    st.subheader("📰 Industry News")
    for item in news_list:
        st.write(f"**[{item['date']}]** - {item['news']}")

elif st.session_state.menu == "Project Archive":
    st.title("📂 Project Archive")
    st.table(archive_data)

elif st.session_state.menu == "Asset Library":
    st.title("📦 Asset Library")
    st.info("Storage for all generated images, videos, and branding assets.")
    st.write("Current Assets: 125 Files")

elif st.session_state.menu == "Brand DNA":
    st.title("🧬 Brand DNA")
    st.write("Brand voice, target audience, and core values settings.")

else:
    # Fallback for other buttons
    st.title(st.session_state.menu)
    st.write(f"This is the {st.session_state.menu} section of v32.0.")
