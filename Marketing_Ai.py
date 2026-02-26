import streamlit as st
import time

# --- 1. PREMIUM PAGE CONFIG & CSS ---
st.set_page_config(page_title="SAYAR GYI | AI AGENCY", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        background-color: #05070a;
        color: #e1e4e8;
    }
    
    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0d1117;
        border-right: 1px solid #30363d;
        padding-top: 20px;
    }
    
    .sidebar-title {
        font-size: 22px;
        font-weight: 600;
        letter-spacing: -1px;
        color: #f0f6fc;
        margin-bottom: 5px;
    }
    
    .sidebar-subtitle {
        font-size: 14px;
        color: #58a6ff;
        margin-bottom: 25px;
        font-weight: 400;
    }

    .nav-label {
        font-size: 11px;
        text-transform: uppercase;
        color: #8b949e;
        margin-top: 20px;
        margin-bottom: 10px;
        font-weight: 600;
        letter-spacing: 1px;
    }

    /* Industry News Box */
    .news-box {
        background: #161b22;
        border-radius: 8px;
        padding: 12px;
        border: 1px solid #30363d;
        font-size: 12px;
        margin-bottom: 20px;
    }
    
    /* Metric Cards */
    .metric-card {
        background: #0d1117;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363d;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDE PANEL (SIDEBAR) ---
with st.sidebar:
    # Title Section
    st.markdown('<p class="sidebar-title">Sayar Gyi \'s</p>', unsafe_allow_html=True)
    st.markdown('<p class="sidebar-subtitle">Ai Marketing Agency</p>', unsafe_allow_html=True)

    # Industry News Section
    st.markdown('<p class="nav-label">Industry News</p>', unsafe_allow_html=True)
    st.markdown("""
        <div class="news-box">
            🔥 <b>Meta Andromeda:</b> New algorithm favors 9:16 video reels today.<br>
            📈 <b>Trend:</b> Jewelry searches up by 15% in Myanmar.
        </div>
    """, unsafe_allow_html=True)

    # Menu Section
    st.markdown('<p class="nav-label">Menu</p>', unsafe_allow_html=True)
    menu_choice = st.radio("Navigation", 
                          ["Interactive Dashboard", "Brand DNA", "Project Archive", "Asset Library"], 
                          label_visibility="collapsed")

    st.divider()

    # My Agents Section
    st.markdown('<p class="nav-label">My Agents</p>', unsafe_allow_html=True)
    st.markdown("""
        <div style="font-size: 13px; line-height: 2;">
            👤 Agent 1: Intel Strategist<br>
            👤 Agent 2: Creative Engine<br>
            👤 Agent 3: Executive Auditor<br>
            👤 Agent 4: Ops Manager
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    # Creator Mode Section
    st.markdown('<p class="nav-label">Creator Mode</p>', unsafe_allow_html=True)
    creator_mode = st.toggle("Enable Creator Mode", value=True)

    # System Status Section
    st.markdown('<p class="nav-label">System Status</p>', unsafe_allow_html=True)
    st.success("Core Engine: Online")
    st.info("API Latency: 120ms")

    st.divider()

    # The Brain Section
    st.markdown('<p class="nav-label">The Brain</p>', unsafe_allow_html=True)
    brain_choice = st.segmented_control("Model Selection", ["Gemini", "ChatGPT", "Claude"], default="Gemini")

# --- 3. MAIN CONTENT (INTERACTIVE DASHBOARD) ---
if menu_choice == "Interactive Dashboard":
    st.title(f"Dashboard: {brain_choice} Powered")
    
    # Overview Metrics
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown('<div class="metric-card"><p class="sub-label">Active Campaigns</p><h3>12</h3></div>', unsafe_allow_html=True)
    with m2: st.markdown('<div class="metric-card"><p class="sub-label">Content Generated</p><h3>145</h3></div>', unsafe_allow_html=True)
    with m3: st.markdown('<div class="metric-card"><p class="sub-label">Audit Score</p><h3>98%</h3></div>', unsafe_allow_html=True)
    with m4: st.markdown('<div class="metric-card"><p class="sub-label">Tokens Used</p><h3>4.2k</h3></div>', unsafe_allow_html=True)

    st.divider()

    # Simple Simulation of Content Generation Flow
    col_input, col_output = st.columns([1, 1.5], gap="large")
    
    with col_input:
        st.subheader("Mission Setup")
        task = st.text_area("What is the mission today?", placeholder="e.g., Create a TOFU post for Jewelry SME...")
        if st.button("RUN AGENT PIPELINE"):
            with st.status("Agents working...", expanded=True):
                st.write("🧠 Agent 1 (Intel) is researching...")
                time.sleep(1)
                st.write("🎨 Agent 2 (Creative) is drafting...")
                time.sleep(1)
                st.write("⚖️ Agent 3 (Auditor) is verifying...")
                time.sleep(1)
            st.session_state['ready'] = True

    with col_output:
        st.subheader("Final Asset Preview")
        if st.session_state.get('ready'):
            st.success("Verification Complete. Ready for CEO Approval.")
            with st.container(border=True):
                st.markdown("**Copywriting Draft:**")
                st.write("နွေရာသီမှာ သင့်ကို ပိုဝင်းပစေမယ့် ရတနာရွေးချယ်နည်း ၅ ဆင့်... ✨")
                st.button("✅ Approve & Post")
        else:
            st.info("Waiting for Agent Pipeline to execute...")

# --- PLACEHOLDERS FOR OTHER MENUS ---
elif menu_choice == "Brand DNA":
    st.title("Brand DNA Vault")
    st.info("Centralized Identity for all active clients.")

elif menu_choice == "Project Archive":
    st.title("Project Archive")
    st.write("History of all approved and deployed campaigns.")

elif menu_choice == "Asset Library":
    st.title("Asset Library")
    st.write("Cloud storage for client images, videos, and raw files.")
