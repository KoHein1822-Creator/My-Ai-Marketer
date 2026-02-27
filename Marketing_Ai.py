import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (v32.0 Original) ---
if 'menu' not in st.session_state:
    st.session_state.menu = "Interactive Dashboard"

# --- 2. PAGE CONFIG & v32.0 THEME ---
st.set_page_config(page_title="SAYAR GYI v62.0", layout="wide")

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

# --- 3. SIDE PANEL (v32.0 Original Structure) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    st.markdown('<p class="nav-label">Main Menu</p>', unsafe_allow_html=True)
    if st.button("📊 Strategic Dashboard", use_container_width=True): st.session_state.menu = "Interactive Dashboard"
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): st.session_state.menu = "Market Intelligence Hub"
    if st.button("🎨 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    
    st.divider()
    st.markdown('<p class="nav-label">Management</p>', unsafe_allow_html=True)
    if st.button("📂 Project Archive", use_container_width=True): st.session_state.menu = "Project Archive"
    if st.button("📦 Asset Library", use_container_width=True): st.session_state.menu = "Asset Library"
    
    st.divider()
    st.success("v62.0 | Syntax Corrected")

# --- 4. MAIN INTERFACE ---

# A. INTERACTIVE DASHBOARD (v32.0 Base)
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("Engagement", "12.5k", "+12%")
    col2.metric("Efficiency", "98%", "+2%")
    col3.metric("Leads", "150", "Stable")

# B. PROJECT ARCHIVE (CEO Original Snippet)
elif st.session_state.menu == "Project Archive":
    st.markdown('<h1 class="header-blue">Project Archive</h1>', unsafe_allow_html=True)
    with st.expander("Add New Project"):
        st.text_input("Client Name"); st.date_input("Start Date"); st.button("Save")
    # Table from v32.0 original data
    st.table(pd.DataFrame({"Project": ["Promotion A", "Brand DNA Setup"], "Status": ["Finished", "Active"]}))

# C. ASSET LIBRARY (CEO Original Snippet)
elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 class="header-blue">Asset Library</h1>', unsafe_allow_html=True)
    a_tab1, a_tab2, a_tab3 = st.tabs(["Media", "Copywriting", "Legal"])
    with a_tab1:
        st.table(pd.DataFrame({"File": ["Logo.png", "Promo.mp4"], "Type": ["Image", "Video"], "Platform": ["All", "TikTok"]}))
        st.file_uploader("Upload Assets")
    with a_tab2: st.write("Copywriting Templates Store")
    with a_tab3: st.write("Legal & Contract Templates")

# D. MARKET INTELLIGENCE HUB (The Fixed Integrated Section)
elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 class="header-blue">🌐 Market Intelligence Hub</h1>', unsafe_allow_html=True)
    if st.button("Back"): st.session_state.menu = "Interactive Dashboard"
    
    # syntax error ပြင်ထားသော နေရာ
    i_tab1, i_tab2, i_tab3 = st.tabs(["📰 Industry & AI News", "📈 Market Research & Analytic", "🕵️ Competitor Spy Mode"])
    
    with i_tab1:
        st.subheader("Industry News")
        st.write("• AI Trend: Short-form video contents are leading the market.")
        st.write("• Facebook algorithm update affects organic reach.")
        
    with i_tab2:
        st.subheader("Market Research & Analytic")
        st.info("Market follow-up for your Industry:")
        st.line_chart(pd.DataFrame([10, 20, 50, 40, 80], columns=["Market Trend"]))
        
    with i_tab3:
        st.subheader("Competitor Spy Mode")
        st.write("Follow up on what competitors are doing:")
        st.table(pd.DataFrame({"Competitor": ["Comp A", "Comp B"], "Active Strategy": ["Live Promo", "Viral Content"]}))

# E. CREATOR MODE (CEO Original Snippet)
elif st.session_state.menu == "Creator Mode":
    st.title("Creator Mode")
    if st.button("Back"): st.session_state.menu = "Interactive Dashboard"
    st.write("Creator tools and workspace for AI content generation.")

else:
    st.title(st.session_state.menu)
