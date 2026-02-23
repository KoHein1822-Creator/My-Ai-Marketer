import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Marketer Suite Pro", layout="wide", page_icon="🚀")

# --- IMPROVED CSS (Better Visibility) ---
st.markdown("""
    <style>
    /* တစ်ခုလုံးရဲ့ Background ကို ခပ်မှိန်မှိန် အရောင်ပေးထားပါမယ် (မျက်စိမအေးအောင်) */
    .stApp {
        background-color: #f0f2f6;
    }
    
    /* Input ကွက်တွေရှိတဲ့ ဘေးဘောင် (Card) */
    .command-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 25px;
        border: 1px solid #d1d5db;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        color: #1f2937; /* စာလုံးအရောင်ကို အမည်းရောင် ပေးထားပါတယ် */
    }

    /* Output Section ရဲ့ Background */
    .output-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
    }

    /* ခလုတ်အရောင်ကို ပိုတောက်အောင် ပြောင်းထားပါတယ် */
    .stButton>button {
        background: linear-gradient(135deg, #4338ca 0%, #6d28d9 100%);
        color: white !important;
        border: none;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    /* Sidebar ကို အရောင်ခွဲထားပါမယ် */
    [data-testid="stSidebar"] {
        background-color: #1e293b;
    }
    [data-testid="stSidebar"] .stMarkdown, [data-testid="stSidebar"] p {
        color: #f8fafc;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("💎 AI Marketer")
    st.markdown("---")
    selected_brand = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X", "+ Add New"])
    st.info("Elite Agency Plan - Active")

# --- MAIN CONTENT ---
st.title("🚀 AI Marketer Command Center")
st.caption(f"Project: {selected_brand}")
st.divider()

col_input, col_output = st.columns([1, 1.5], gap="large")

with col_input:
    # Card ပုံစံလေးနဲ့ Input အကွက်
    st.markdown('<div class="command-card">', unsafe_allow_html=True)
    st.subheader("🎯 Campaign Design")
    
    app_mode = st.toggle("Switch to Architect Mode (Manual)", value=False)
    
    topic = st.text_input("What is the topic?", placeholder="e.g. ရွှေဖြူဆွဲကြိုး လက်ရာသစ်")
    
    if not app_mode:
        st.info("⚡ **Smart Mode Active**")
        goal = st.selectbox("Goal", ["Sales", "Awareness", "Storytelling"])
    else:
        st.warning("🛠️ **Architect Mode Active**")
        framework = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB"], default="AIDA")
        creativity = st.slider("Creativity", 0.0, 1.0, 0.7)
        
    if st.button("EXECUTE NOW"):
        st.session_state['run'] = True
    st.markdown('</div>', unsafe_allow_html=True)

with col_output:
    if st.session_state.get('run'):
        st.subheader("🔥 Generated Content Matrix")
        tab1, tab2, tab3 = st.tabs(["📝 Copies", "🎬 Scripts", "🎨 Visuals"])
        
        with tab1:
            st.markdown("### Framework Variations")
            st.text_area("AIDA Output", "Attention: Look at this!\nInterest: Pure White Gold...\n...", height=200)
            
        with tab2:
            st.markdown("### Social Media Scripts")
            st.text_area("TikTok/Reels Script", "0-3s Hook: \n3-15s Value: \n...", height=200)
            
        with tab3:
            st.markdown("### Image Generation Prompts")
            st.code("/imagine prompt: jewelry photography, white gold necklace, cinematic lighting --ar 4:5")
    else:
        st.info("ဘယ်ဘက်တွင် အချက်အလက်များဖြည့်ပြီး Execute ကိုနှိပ်ပါ။")
