import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
st.set_page_config(page_title="AI Marketer Pro v4.0", layout="wide")

# Secrets ထဲက Key ကို ချိတ်ဆက်ခြင်း
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Secrets ထဲမှာ API Key ထည့်ဖို့ လိုအပ်နေပါသေးတယ်ဗျာ။")

# --- 2. PROFESSIONAL CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .workspace-card { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; }
    .stButton>button { background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; border: none !important; color: white !important; font-weight: 700 !important; width: 100%; border-radius: 8px !important; height: 50px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.divider()
    brand = st.selectbox("Project", ["Jewelry Client A"])
    with st.expander("🧬 Brand DNA Insights", expanded=True):
        st.write("**Niche:** Luxury Jewelry")
        st.write("**Tone:** Elegant & Professional")
    st.markdown("<p style='color:#3fb950; margin-top:20px;'>● Elite Access Active</p>", unsafe_allow_html=True)

# --- 4. MAIN CONTENT ---
st.markdown("<h1 style='color:white;'>Strategic Command Center</h1>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 2], gap="large")

with col_in:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Setup</p>', unsafe_allow_html=True)
    topic = st.text_input("Marketing Topic", placeholder="ဥပမာ - ၁၈ ကာရက် ရွှေဖြူလက်စွပ်")
    goal = st.selectbox("Objective", ["High Conversion", "Brand Awareness"])
    
    if st.button("GENERATE STRATEGY MATRIX"):
        if topic:
            with st.spinner("AI က သင့်အတွက် Strategy တွက်ချက်နေပါတယ်..."):
                # AI Prompt ညွှန်ကြားချက်
                prompt = f"Act as a pro marketer. Write a creative Facebook ad copy using AIDA framework and PAS framework for {topic}. Brand tone is Luxury. Language: Myanmar."
                response = model.generate_content(prompt)
                st.session_state['ai_result'] = response.text
                st.session_state['run'] = True
        else:
            st.warning("Topic အရင်ရိုက်ထည့်ပေးပါဗျာ။")
    st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    if st.session_state.get('run'):
        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Generated Strategy Matrix</p>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📝 Content Deck", "🎬 Media Brief", "🎨 Visual Prompts"])
        
        with tab1:
            st.markdown("### AI Generated Copy (Myanmar)")
            st.write(st.session_state['ai_result']) # AI က ထွက်လာတဲ့စာသား
            
        with tab2:
            st.write("Video Script အကျဉ်းချုပ်...")
            
        with tab3:
            st.code(f"/imagine prompt: Luxury {topic}, 8k, cinematic lighting")
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="border: 2px dashed #30363d; padding: 100px; text-align: center; border-radius: 12px; background: #161b22; color: #8b949e;">ဘယ်ဘက်တွင် အချက်အလက်ဖြည့်ပြီး Execute ကိုနှိပ်ပါ။</div>', unsafe_allow_html=True)
