import streamlit as st
import pandas as pd

# --- 1. SESSION STATE (Data Persistence) ---
if 'menu' not in st.session_state: st.session_state.menu = "Interactive Dashboard"

# --- 2. PAGE CONFIG & v32.0 ORIGINAL UI THEME ---
st.set_page_config(page_title="SAYAR GYI v60.0", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    section[data-testid="stSidebar"] { background-color: #0d1117; border-right: 1px solid #30363d; }
    .nav-label { font-size: 11px; text-transform: uppercase; color: #8b949e; margin-top: 10px; font-weight: 600; letter-spacing: 1px; }
    .header-blue { color: #58a6ff; font-weight: 600; }
    .intel-card { background: #161b22; border: 1px solid #30363d; padding: 15px; border-radius: 8px; margin-bottom: 15px; }
    .status-tag { background: #238636; color: white; padding: 2px 8px; border-radius: 10px; font-size: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDE PANEL (v32.0 Structure with Re-organized Buttons) ---
with st.sidebar:
    st.markdown("## Sayar Gyi 's")
    st.markdown("<p style='color:#58a6ff; margin-top:-15px;'>Ai Marketing Agency</p>", unsafe_allow_html=True)
    st.divider()

    # --- INTELLIGENCE SECTION (The New Combined Hub) ---
    st.markdown('<p class="nav-label">Intelligence Center</p>', unsafe_allow_html=True)
    if st.button("🌐 Market Intelligence Hub", use_container_width=True): 
        st.session_state.menu = "Intel Hub"

    st.divider()
    # --- EXECUTION SECTION ---
    st.markdown('<p class="nav-label">Execution</p>', unsafe_allow_html=True)
    if st.button("🎬 Content Production", use_container_width=True): st.session_state.menu = "Content"
    if st.button("💬 AI Auto-Responder", use_container_width=True): st.session_state.menu = "Engagement"

    st.divider()
    # --- NAVIGATION (v32.0 Original Radio) ---
    nav_choice = st.radio("Nav", ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], label_visibility="collapsed")
    if nav_choice in ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"] and st.session_state.menu not in ["Intel Hub", "Content", "Engagement"]:
        st.session_state.menu = nav_choice

    st.divider()
    st.success("v60.0 | Intelligence Integrated")

# --- 4. MAIN INTERFACE ---

# A. MARKET INTELLIGENCE HUB (The 3-in-1 Integration)
if st.session_state.menu == "Intel Hub":
    st.markdown('<h1 class="header-blue">🌐 Market Intelligence Hub</h1>', unsafe_allow_html=True)
    st.write("Industry News, Market Trends နှင့် Competitor Spy Reports များကို တစ်နေရာတည်းတွင် စုစည်းထားပါသည်။")
    
    tab_news, tab_market, tab_spy = st.tabs(["📰 Industry & AI News", "📊 Market Trends & Analytics", "🕵️ Competitor Spy Mode"])
    
    with tab_news:
        st.subheader("Global Industry Updates")
        st.markdown("""
        <div class="intel-card">
            <span class="status-tag">LATEST</span> <b>Facebook Algorithm Update:</b> ဗီဒီယိုအတိုများကို ပိုမိုတွန်းတင်ရန် ဆုံးဖြတ်လိုက်သည်။<br>
            <small>Source: TechCrunch | 2 hours ago</small>
        </div>
        <div class="intel-card">
            <b>AI Trend:</b> Google Gemini 1.5 Pro က ဗမာစာကို ပိုမိုကောင်းမွန်စွာ နားလည်လာသည်။
        </div>
        """, unsafe_allow_html=True)

    with tab_market:
        st.subheader("Local Market Research")
        st.info("ရွှေနှင့် ရတနာလုပ်ငန်းနယ်ပယ်တွင် ယခုအပတ် 'Wedding Set' ရှာဖွေမှု ၁၅% တိုးတက်လာသည်။")
        # Sample Chart/Data for Analytics
        chart_data = pd.DataFrame({"Trend": [30, 45, 80, 60], "Week": ["W1", "W2", "W3", "W4"]})
        st.line_chart(chart_data.set_index("Week"))

    with tab_spy:
        st.subheader("Competitor Spy Watch")
        st.error("Alert: ပြိုင်ဘက် 'ABC Jewelry' မှ ယနေ့ညနေ ၆ နာရီတွင် အထူးအရောင်းပွဲစတင်ရန် စီစဉ်နေသည်။")
        st.table(pd.DataFrame({
            "Competitor": ["ABC Jewelry", "Golden King"],
            "Latest Activity": ["FB Live (Promotion)", "TikTok Video (Viral)"],
            "Price Range": ["Higher", "Standard"]
        }))

# B. INTERACTIVE DASHBOARD (v32.0 Original)
elif st.session_state.menu == "Interactive Dashboard":
    st.markdown('<h1 class="header-blue">Strategic Dashboard</h1>', unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    c1.metric("Engagement", "12.5k", "+12%")
    c2.metric("Reach", "45k", "+5%")
    c3.metric("Efficiency", "98%", "Stable")
    st.divider()
    st.write("### Internal Database Status")
    st.info("Project Archive and Asset Library are fully secured and connected.")

# Other sections (Brand DNA, Project Archive, Asset Library)
elif st.session_state.menu == "Project Archive":
    st.title("📂 Project Archive")
    st.table(pd.DataFrame({"Project": ["Promotion A", "Brand Launch"], "Status": ["Finished", "Ongoing"]}))

elif st.session_state.menu == "Asset Library":
    st.title("📦 Asset Library")
    st.write("All media assets are preserved.")

else:
    st.title(st.session_state.menu)
