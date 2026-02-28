import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Ensuring no data loss) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"
if 'model_choice' not in st.session_state: st.session_state.model_choice = "Gemini"

# --- 2. PAGE CONFIG ---
st.set_page_config(page_title="SAYAR GYI v76.0", layout="wide")

# v72.0 SIDEBAR + v32.0 DASHBOARD + BRAND DNA CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0d1117; color: #e1e4e8; }
    
    /* v72.0 Sidebar Exact Restoration */
    section[data-testid="stSidebar"] { background-color: #010409 !important; min-width: 320px !important; border-right: 1px solid #30363d; }
    .sidebar-header { font-size: 13px; font-weight: 700; color: #58a6ff; margin-top: 25px; margin-bottom: 12px; letter-spacing: 1.5px; text-transform: uppercase; }
    
    /* The Brain Buttons Grid */
    div.stButton > button {
        height: 48px !important; font-size: 15px !important; font-weight: 600 !important;
        border-radius: 8px !important; background-color: #161b22 !important;
        border: 1px solid #30363d !important; color: #ffffff !important;
    }
    div.stButton > button:hover { border-color: #58a6ff !important; color: #58a6ff !important; }

    /* Dashboard Metric Card Style */
    div[data-testid="stMetric"] {
        background-color: #161b22; border: 1px solid #30363d;
        padding: 20px !important; border-radius: 12px;
    }

    /* Status Panel Restoration */
    .status-panel { background: #0d1117; border: 1px solid #30363d; padding: 18px; border-radius: 10px; margin-top: 10px; }
    .status-node-info { font-size: 10px; color: #8b949e; margin-top: 8px; border-top: 1px solid #21262d; padding-top: 8px; display: flex; justify-content: space-between; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v72.0 Engine) ---
with st.sidebar:
    st.markdown('<h1 style="color:white; margin-bottom:0; font-size:28px;">Sayar Gyi\'s</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#58a6ff; font-weight:600; letter-spacing:3px; font-size:12px; margin-top:-5px;">COMMAND CENTER</p>', unsafe_allow_html=True)
    st.divider()

    # THE BRAIN
    st.markdown('<p class="sidebar-header">The Brain</p>', unsafe_allow_html=True)
    m_col1, m_col2 = st.columns(2)
    with m_col1:
        if st.button("Gemini 💎", key="gem", use_container_width=True): st.session_state.model_choice = "Gemini"
        if st.button("Claude 🧠", key="cla", use_container_width=True): st.session_state.model_choice = "Claude"
    with m_col2:
        if st.button("GPT 🤖", key="gpt", use_container_width=True): st.session_state.model_choice = "ChatGPT"
    st.markdown(f'<div style="background:rgba(88,166,255,0.1); border:1px solid rgba(88,166,255,0.3); padding:8px; border-radius:6px; text-align:center; margin-top:10px; font-size:12px; color:#58a6ff;">Active Core: <b>{st.session_state.model_choice}</b></div>', unsafe_allow_html=True)
    st.divider()

    # MENU NAVIGATION
    st.markdown('<p class="sidebar-header">System Menu</p>', unsafe_allow_html=True)
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    st.session_state.menu = nav_choice
    st.divider()

    # SPECIAL FUNCTIONS
    st.markdown('<p class="sidebar-header">Special Functions</p>', unsafe_allow_html=True)
    if st.button("🌐 Intelligence Hub", use_container_width=True): st.session_state.menu = "Intelligence Hub"
    if st.button("🔥 Creator Mode", use_container_width=True): st.session_state.menu = "Creator Mode"
    st.divider()

    # SYSTEM STATUS
    st.markdown('<p class="sidebar-header" style="margin-top:10px;">System Status</p>', unsafe_allow_html=True)
    st.markdown(f"""
        <div class="status-panel">
            <p style="color:#3fb950; font-weight:700; font-size:15px; margin:0;">● Core Engine: Online</p>
            <div class="status-node-info"><span>NODE: SG-MASTER-01</span><span>UPTIME: 99.9%</span></div>
        </div>
    """, unsafe_allow_html=True)

# --- 4. MAIN INTERFACE LOGIC (RESTORING ALL VIEWS) ---

# --- A. INTERACTIVE DASHBOARD (v32.0 Exact Recovery) ---
if st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Strategic Dashboard</h1>', unsafe_allow_html=True)
    
    f_col1, f_col2 = st.columns([1, 1])
    with f_col1:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Timeframe</p>', unsafe_allow_html=True)
        st.segmented_control("T1", ["Weekly", "Monthly", "Yearly"], default="Monthly", label_visibility="collapsed")
    with f_col2:
        st.markdown('<p style="font-size:12px; color:#8b949e; margin-bottom:5px;">Visual Filter</p>', unsafe_allow_html=True)
        st.selectbox("F1", ["Bar Chart", "Line Chart", "Trend Analysis"], label_visibility="collapsed")
    
    st.write("") 
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase;">Content Creation Status</p>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Drafting", "12", "+2")
    m2.metric("Pending", "5", "-1")
    m3.metric("Scheduled", "18", "+5")
    m4.metric("Published", "145", "+12")
    
    st.divider()
    st.markdown('<p style="font-size:13px; font-weight:600; color:#8b949e; text-transform:uppercase;">Platform Performance</p>', unsafe_allow_html=True)
    p_tabs = st.tabs(["Facebook", "TikTok", "YouTube"])
    with p_tabs[0]:
        c1, c2, c3 = st.columns(3)
        c1.metric("Reach", "45.2K", "+15%")
        c2.metric("Engagement", "3.2K", "+8%")
        c3.metric("Followers", "12.4K", "+1.2K")
        chart_data = pd.DataFrame({'Category': ['Convert', 'Engage', 'Reach'], 'Value': [25, 45, 32]})
        st.bar_chart(chart_data.set_index('Category'), color="#58a6ff")

# --- B. BRAND DNA (New Intelligence Features) ---
elif st.session_state.menu == "Brand DNA":
    st.markdown('<h1 style="font-size:32px; font-weight:700;">Brand DNA Intelligence</h1>', unsafe_allow_html=True)
    mode = st.radio("Select Mode", ["Intelligence Mode (AI Research)", "Manual Mode (User Input)"], horizontal=True)
    
    if "Intelligence Mode" in mode:
        st.subheader("AI Intelligence Researcher")
        industries = ["Jewelry & Gold (ကျောက်မျက်ရတနာနှင့် ရွှေဆိုင်)", "Fashion & Clothing", "Real Estate", "F&B / Restaurant", "Others (စာရင်းထဲတွင်မပါပါ)"]
        choice = st.selectbox("လုပ်ငန်းအမျိုးအစား ရွေးချယ်ပါ", industries)
        if choice == "Others (စာရင်းထဲတွင်မပါပါ)":
            st.text_input("သင့်လုပ်ငန်းအမျိုးအစားကို ရေးပေးပါ")
        st.button("Generate Strategy")
    else:
        st.subheader("Manual Brand Configuration")
        col1, col2 = st.columns(2)
        col1.text_input("Brand Name"); col1.text_area("Brand Mission")
        col2.text_input("Target Audience"); col2.text_area("USP")
        st.button("Save Brand DNA")

# --- C. PROJECT ARCHIVE & ASSET LIBRARY (Placeholders) ---
elif st.session_state.menu == "Project Archive":
    st.markdown('<h1>Project Archive Database</h1>', unsafe_allow_html=True)
    df = pd.DataFrame({'Client': ['Diamond Star', 'Zen Coffee'], 'Status': ['Completed', 'Active']})
    st.table(df)

elif st.session_state.menu == "Asset Library":
    st.markdown('<h1>Asset Library</h1>', unsafe_allow_html=True)
    st.tabs(["Media", "Copywriting", "Legal"])

else:
    st.markdown(f"<h1>{st.session_state.menu}</h1>", unsafe_allow_html=True)
    st.info("Module is ready and synchronized.")
