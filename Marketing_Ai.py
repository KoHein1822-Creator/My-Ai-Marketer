import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="AI Marketer Suite Pro", layout="wide", page_icon="🚀")

# --- FORCE STYLE FIX (အရောင်ပြဿနာကို ဖြေရှင်းရန်) ---
st.markdown("""
    <style>
    /* တစ်ခုလုံးကို Light Theme အနေနဲ့ စာလုံးအရောင် အမည်း Force လုပ်ပါမယ် */
    html, body, [data-testid="stappview-container"] {
        color: #000000 !important;
    }
    
    /* ခေါင်းစဉ်ကြီးများ စာလုံးအမည်း ပြောင်းရန် */
    h1, h2, h3, p, span, label {
        color: #1e293b !important;
    }

    /* Card Background နှင့် Border */
    .stAlert, div[data-testid="stVerticalBlock"] > div > div {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* Sidebar အရောင်ကို သီးသန့် အမှောင်ထားပါမယ် */
    [data-testid="stSidebar"] {
        background-color: #0f172a !important;
    }
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] p, [data-testid="stSidebar"] label {
        color: #ffffff !important;
    }
    
    /* Input Box အရောင် */
    .stTextInput input {
        color: #000000 !important;
        background-color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR ---
with st.sidebar:
    st.title("💎 AI Marketer")
    st.markdown("---")
    selected_brand = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X"])
    st.success("Elite Agency Plan - Active")

# --- MAIN CONTENT ---
st.title("🚀 AI Marketer Command Center")
st.write(f"**Current Project:** {selected_brand}")
st.divider()

col_input, col_output = st.columns([1, 1.5], gap="large")

with col_input:
    st.subheader("🎯 Campaign Design")
    
    # Toggle အစား Selectbox သုံးခြင်းက Visibility ပိုကောင်းစေပါတယ်
    app_mode = st.selectbox("Engine Mode", ["⚡ Smart Mode", "🛠️ Architect Mode"])
    
    topic = st.text_input("Marketing Topic", placeholder="ဥပမာ - ရွှေဖြူဆွဲကြိုး")
    
    if "Smart" in app_mode:
        goal = st.selectbox("Select Goal", ["Instant Sales", "Awareness", "Storytelling"])
    else:
        framework = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB"], default="AIDA")
        creativity = st.slider("Creativity Level", 0.0, 1.0, 0.7)
        
    if st.button("EXECUTE CAMPAIGN"):
        st.session_state['run'] = True

with col_output:
    if st.session_state.get('run'):
        st.subheader("🔥 Content Matrix")
        tab1, tab2, tab3 = st.tabs(["📝 Ad Copies", "🎬 Video Scripts", "🎨 Visuals"])
        
        with tab1:
            st.info("AI Generating Framework-based copies...")
            st.text_area("AIDA Variation", "Content goes here...", height=200)
        
        with tab2:
            st.text_area("Short Video Script", "Hook: ...\nBody: ...", height=200)
            
        with tab3:
            st.code("/imagine prompt: high quality jewelry...")
    else:
        # ရှင်းလင်းသော အပြာရောင် Box ဖြင့် ပြပေးခြင်း
        st.info("👈 ဘယ်ဘက်ခြမ်းတွင် အချက်အလက်များဖြည့်သွင်းပြီး Execute ကို နှိပ်ပါ။")
