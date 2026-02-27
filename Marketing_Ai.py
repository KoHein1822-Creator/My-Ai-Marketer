import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Database) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'brand_mode' not in st.session_state: st.session_state.brand_mode = "Intelligence Mode (AI Research)"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v32.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #010409; border-right: 1px solid #30363d; padding-top: 20px; }
    .nav-label { font-size: 10px; text-transform: uppercase; color: #8b949e; margin-top: 20px; margin-bottom: 5px; font-weight: 600; letter-spacing: 0.5px; }
    .header-blue { color: #58a6ff; font-weight: 600; font-size: 24px; margin-bottom: 20px; }
    .stMetric { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 6px; }
    div[data-testid="stExpander"] { border: 1px solid #30363d; background: #0d1117; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (Exact Match to Screenshot) ---
with st.sidebar:
    st.markdown("<p style='color:#58a6ff; font-weight:bold; margin-bottom:0;'>Sayar Gyi 's</p>", unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff; font-size:10px; margin-top:0;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    
    st.markdown('<p class="nav-label">INDUSTRY NEWS</p>', unsafe_allow_html=True)
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): st.session_state.menu = "Market Intelligence Hub"
    
    st.markdown('<p class="nav-label">MENU</p>', unsafe_allow_html=True)
    st.session_state.menu = st.radio("Menu", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    
    st.markdown('<p class="nav-label">MY AGENTS</p>', unsafe_allow_html=True)
    st.markdown("<p style='font-size:12px; color:#8b949e;'>🧘 Intel | 🎨 Creative | ⚖️ Auditor | ⚙️ Ops</p>", unsafe_allow_html=True)
    
    st.markdown('<p class="nav-label">CREATOR MODE</p>', unsafe_allow_html=True)
    if st.button("🔥 Switch to Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    
    st.divider()
    st.success("Core Engine: Online")
    
    st.markdown('<p class="nav-label">Model</p>', unsafe_allow_html=True)
    st.button("Gemini", type="primary", use_container_width=True)

# --- 4. MAIN INTERFACE ---

# A. DASHBOARD (Screenshot 4 Match)
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard 🔗</h1>', unsafe_allow_html=True)
    t_col1, t_col2 = st.columns([1, 4])
    with t_col1: st.radio("Timeframe", ["Weekly", "Monthly", "Yearly"], horizontal=True)
    with t_col2: st.selectbox("Visual Filter", ["Bar Chart", "Line Chart"])
    
    st.markdown('<p class="nav-label">CONTENT CREATION STATUS</p>', unsafe_allow_html=True)
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Drafting", "12")
    m_col2.metric("Pending", "5")
    m_col3.metric("Scheduled", "18")
    m_col4.metric("Published", "145")
    
    st.markdown('<p class="nav-label">PLATFORM METRICS</p>', unsafe_allow_html=True)
    st.tabs(["Facebook", "TikTok", "YouTube"])
    p_col1, p_col2, p_col3 = st.columns(3)
    p_col1.metric("Reach", "45.2K")
    p_col2.metric("Engagement", "3.2K")
    p_col3.metric("Followers", "12.4K")
    
    # Simple Bar Chart to mimic Screenshot
    chart_data = pd.DataFrame({'Category': ['Convert', 'Engage', 'Reach'], 'Value': [25, 45, 32]})
    st.bar_chart(chart_data.set_index('Category'), color="#58a6ff")

# B. BRAND DNA (Screenshots 2 & 3 Match)
elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 class="header-blue">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    st.session_state.brand_mode = st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)
    
    if st.session_state.brand_mode == "Intelligence Mode (AI Research)":
        st.subheader("AI Intelligence Researcher")
        st.write("လုပ်ငန်းအမျိုးအစား ရွေးချယ်ပါ")
        st.selectbox("", ["Jewelry & Gold (ကျောက်မျက်ရတနာနှင့် ရွှေဆိုင်)", "Fashion", "Tech"], label_visibility="collapsed")
        st.button("Generate Strategy")
    else:
        st.subheader("Manual Brand Configuration")
        b_c1, b_c2 = st.columns(2)
        b_c1.text_input("Brand Name")
        b_c2.text_input("Target Audience")
        b_c1.text_area("Brand Mission")
        b_c2.text_area("Unique Selling Point (USP)")
        b_c1.selectbox("Brand Tone", ["Professional", "Friendly", "Luxury"])
        b_c2.file_uploader("Upload Brand Guideline (PDF/DOC)")
        st.button("Save Brand DNA")

# C. PROJECT ARCHIVE (Screenshot 5 Match)
elif st.session_state.menu == "Project Archive":
    st.markdown('<h1 class="header-blue">Project Archive Database</h1>', unsafe_allow_html=True)
    archive_df = pd.DataFrame({
        "Client Name": ["Diamond Star", "Zen Coffee", "Tech Solutions"],
        "Status": ["Completed", "Active", "Pending"],
        "Start Date": ["2025-01-10", "2025-02-01", "2025-02-15"],
        "Budget": ["$2,500", "$1,200", "$4,000"]
    })
    st.table(archive_df)
    with st.expander("Add New Project"):
        st.text_input("New Client Name"); st.date_input("Start Date"); st.button("Save")

# D. ASSET LIBRARY (Screenshot 1 Match)
elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 class="header-blue">Asset Library</h1>', unsafe_allow_html=True)
    a_tab1, a_tab2, a_tab3 = st.tabs(["Media", "Copywriting", "Legal"])
    with a_tab1:
        st.table(pd.DataFrame({
            "File": ["Logo.png", "Promo.mp4"],
            "Type": ["Image", "Video"],
            "Platform": ["All", "TikTok"]
        }))
        st.markdown('<p class="nav-label">Upload Assets</p>', unsafe_allow_html=True)
        st.file_uploader("Drag and drop file here", help="Limit 200MB per file")

# E. MARKET INTELLIGENCE HUB (The Upgrade)
elif st.session_state.menu == "Market Intelligence Hub":
    st.markdown('<h1 class="header-blue">🌐 Market Intelligence Hub</h1>', unsafe_allow_html=True)
    i_tab1, i_tab2, i_tab3 = st.tabs(["📰 Industry News", "📊 Market Research", "🕵️ Spy Mode"])
