import streamlit as st
import time

# --- 1. CEO INTERFACE SETUP ---
st.set_page_config(page_title="Sayar Gyi | CEO Command Center", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e11; color: #c9d1d9; }
    .agent-box { background: #161b22; padding: 15px; border-radius: 10px; border-left: 5px solid #8957e5; margin-bottom: 10px; }
    .approval-card { background: #1c2128; padding: 25px; border-radius: 15px; border: 1px solid #3fb950; }
    .status-tag { font-size: 10px; font-weight: bold; padding: 2px 8px; border-radius: 5px; }
    .tag-live { background: #238636; color: white; }
    .tag-wait { background: #d29922; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR: THE EXECUTIVE SUITE ---
with st.sidebar:
    st.markdown("### 👑 CEO Control Panel")
    st.caption("Monitoring: Autonomous Department")
    st.divider()
    
    # SYSTEM HEALTH (Monitoring Agent Activity)
    st.markdown("**Department Status**")
    st.markdown("📡 **Ops Agent:** <span class='status-tag tag-live'>SYNCED</span>", unsafe_allow_html=True)
    st.markdown("🧠 **Intel Agent:** <span class='status-tag tag-live'>ACTIVE</span>", unsafe_allow_html=True)
    st.markdown("✍️ **Creative Agent:** <span class='status-tag tag-live'>READY</span>", unsafe_allow_html=True)
    
    st.divider()
    if st.button("RESCAN ALL SYSTEMS"):
        st.toast("Sayar Gyi is resyncing with Google Sheets & Meta...")

# --- 3. MAIN DASHBOARD: CEO MONITORING VIEW ---
st.title("Sayar Gyi's Mission Control")

# TOP ROW: REAL-TIME DATA (From Ops Agent)
col_ops, col_intel, col_asset = st.columns(3)

with col_ops:
    st.markdown('<div class="agent-box">', unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff;'>📊 OPS AGENT REPORT</p>", unsafe_allow_html=True)
    st.metric(label="Current Enrollment", value="28/30", delta="-2 Seats Left")
    st.caption("Source: Google Sheets (Synced 1m ago)")
    st.markdown('</div>', unsafe_allow_html=True)

with col_intel:
    st.markdown('<div class="agent-box">', unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff;'>🧠 INTEL AGENT REPORT</p>", unsafe_allow_html=True)
    st.write("Current Trend: Meta Andromeda Logic favors 'Direct Hook' Storytelling.")
    st.write("Market Focus: Professional Development.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_asset:
    st.markdown('<div class="agent-box">', unsafe_allow_html=True)
    st.markdown("<p style='color:#58a6ff;'>🖼️ ASSET AGENT REPORT</p>", unsafe_allow_html=True)
    st.write("Library: 15 Product Images, 3 Course Intro Videos Ready.")
    st.caption("Auto-Selection: Enabled")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# MIDDLE ROW: THE APPROVAL QUEUE (The CEO's Main Task)
st.subheader("📝 Approval Queue (Pending Review)")

with st.container():
    st.markdown('<div class="approval-card">', unsafe_allow_html=True)
    col_content, col_action = st.columns([3, 1])
    
    with col_content:
        st.markdown("### Campaign: Final 2 Seats Alert (Urgent)")
        st.markdown("**Strategy:** Scarcity (based on Ops Agent Data)")
        st.info("""
        [FACEBOOK COPY]
        သင်တန်းသား ၂ ယောက်ပဲ ကျန်ပါတော့တယ်! 🚀 
        နောက် ၃ လစောင့်စရာမလိုဘဲ အခုပဲ အမြန်စာရင်းသွင်းလိုက်ပါ။
        """)
        st.markdown("**Attached Asset:** `Course_Promo_Video_02.mp4`")
    
    with col_action:
        st.write("CEO DECISION")
        if st.button("✅ APPROVE & PUBLISH"):
            st.success("Mission Executed!")
        if st.button("❌ REJECT / RE-EDIT"):
            st.warning("Sent back to Creative Agent.")
        st.button("✍️ EDIT MANUALLY")
    st.markdown('</div>', unsafe_allow_html=True)

# --- 4. FUTURE LOGIC: DYNAMIC ADAPTATION ---
st.divider()
st.markdown("### 🧬 Sayar Gyi's Logic Log")
st.caption("CEO-only view of how Sayar Gyi is thinking.")
st.write("1. Ops Agent detected 28/30 seats. Switched strategy from 'Awareness' to 'Hard Sell (Urgent)'.")
st.write("2. Intel Agent confirmed 9:00 PM is the peak time for target audience. Scheduled for tonight.")
