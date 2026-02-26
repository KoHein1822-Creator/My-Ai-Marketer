import streamlit as st
import sqlite3
from datetime import datetime

# --- 1. DATABASE ENGINE (THE VAULT - LOCAL STORAGE) ---
# ဒါက AI အကောင့် ဘာဖြစ်ဖြစ် ကိုယ့်ဒေတာ ကိုယ့်ဆီမှာ ကျန်နေအောင် လုပ်ပေးတဲ့အပိုင်းပါ
def init_db():
    conn = sqlite3.connect('project_archive.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS archives 
                 (id INTEGER PRIMARY KEY, date TEXT, client TEXT, content TEXT, strategy TEXT)''')
    conn.commit()
    conn.close()

def save_to_archive(client, content, strategy):
    conn = sqlite3.connect('project_archive.db')
    c = conn.cursor()
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    c.execute("INSERT INTO archives (date, client, content, strategy) VALUES (?, ?, ?, ?)",
              (date_now, client, content, strategy))
    conn.commit()
    conn.close()

init_db()

# --- 2. PREMIUM UI STYLING ---
st.set_page_config(page_title="Sayar Gyi | Strategic Hub", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .hub-card { background: #161b22; padding: 20px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 15px; }
    .status-active { color: #3fb950; font-weight: bold; font-size: 12px; }
    .section-header { color: #58a6ff; font-size: 14px; font-weight: bold; text-transform: uppercase; margin-bottom: 10px; }
    .launch-btn button { 
        background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; 
        color: white !important; width: 100%; border: none !important; height: 50px; font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: CEO NAVIGATION ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=80)
    st.title("Sayar Gyi")
    st.caption("Strategic Content Architect")
    st.divider()
    
    menu = st.selectbox("ဗဟိုထိန်းချုပ်ခန်း", ["🎯 Strategic Hub", "📂 Project Archive", "⚙️ Settings"])
    
    st.divider()
    st.markdown("<p class='section-header'>စနစ်အခြေအနေ</p>", unsafe_allow_html=True)
    st.markdown("✅ AI Connect: **Official API**")
    st.markdown("✅ Archive: **Local Encrypted**")

# --- 4. MAIN INTERFACE ---

if menu == "🎯 Strategic Hub":
    st.title("Strategic Hub")
    
    # TOP SECTION: TEAM UPDATES
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="hub-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">လက်ကျန်နှင့် အရောင်း</p>', unsafe_allow_html=True)
        st.metric("သင်တန်းသား လက်ကျန်", "၂ နေရာ", "-၂")
        st.markdown('<span class="status-active">● Live Sync Active</span>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="hub-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">ဈေးကွက်ရေစီးကြောင်း</p>', unsafe_allow_html=True)
        st.write("Trending: Meta Andromeda Logic")
        st.write("Focus: Short-form Video Storytelling")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col3:
        st.markdown('<div class="hub-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-header">အကြောင်းအရာ ဖန်တီးသူ</p>', unsafe_allow_html=True)
        st.write("Drafting: Urgent Enrollment Post")
        st.write("Style: Professional & Urgent")
        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()

    # REVIEW AREA
    st.subheader("📝 Review & Launch (စစ်ဆေးပြီး ထုတ်လွှင့်ရန်)")
    
    with st.container():
        st.markdown('<div class="hub-card" style="border: 1px solid #58a6ff;">', unsafe_allow_html=True)
        c_body, c_action = st.columns([3, 1])
        
        client_name = "SME Jewelry Shop" # Example
        proposed_content = "သင်တန်းသား ၂ ယောက်ပဲ ကျန်ပါတော့တယ်! 🚀 အခုပဲ စာရင်းသွင်းလိုက်ပါ။"
        proposed_strategy = "Scarcity & Urgent Logic"

        with c_body:
            st.markdown(f"**လုပ်ငန်းအမည်:** {client_name}")
            st.markdown(f"**ဗျူဟာ:** {proposed_strategy}")
            st.info(proposed_content)
            st.caption("Attached: 🎥 Promo_Video.mp4")
            
        with c_action:
            st.markdown('<div class="launch-btn">', unsafe_allow_html=True)
            if st.button("✅ Launch Now"):
                save_to_archive(client_name, proposed_content, proposed_strategy)
                st.success("Archive ထဲသို့ သိမ်းဆည်းပြီး Facebook သို့ ထုတ်လွှင့်လိုက်ပါပြီ။")
            st.markdown('</div>', unsafe_allow_html=True)
            st.button("❌ ပြန်ပြင်ရန် ခိုင်းစေမည်")
        st.markdown('</div>', unsafe_allow_html=True)

elif menu == "📂 Project Archive":
    st.title("Project Archive (လုပ်ငန်းမှတ်တမ်းတိုက်)")
    st.write("ယခင်က လုပ်ဆောင်ခဲ့သမျှ Campaign အားလုံးကို ဤနေရာတွင် လုံခြုံစွာ သိမ်းဆည်းထားပါသည်။")
    
    conn = sqlite3.connect('project_archive.db')
    import pandas as pd
    df = pd.read_sql_query("SELECT * FROM archives ORDER BY id DESC", conn)
    st.dataframe(df, use_container_width=True)
    conn.close()
