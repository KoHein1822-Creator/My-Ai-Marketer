import streamlit as st
import google.generativeai as genai
import re

# --- 1. AI SETUP ---
st.set_page_config(page_title="AI Marketer Pro v5.1", layout="wide")

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-flash-latest')
except:
    st.error("API Key Configuration လိုအပ်နေပါသေးတယ်။")

# --- 2. PROFESSIONAL CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .workspace-card { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    .matrix-box { background: #0d1117; padding: 18px; border-radius: 10px; border-left: 4px solid #58a6ff; margin-bottom: 15px; line-height: 1.6; }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; }
    .stButton>button { background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; color: white !important; font-weight: 700 !important; width: 100%; border-radius: 8px !important; height: 50px; border: none !important; }
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; background-color: transparent !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.divider()
    brand = st.selectbox("Project", ["Jewelry Client A"])
    with st.expander("🧬 Brand DNA", expanded=True):
        st.write("**Niche:** Luxury Jewelry")
        st.write("**Target:** High-Net-Worth Women")
        st.write("**Tone:** Elegant, Elite, Scarcity-based")
    st.markdown("<p style='color:#3fb950; margin-top:20px;'>● System Online</p>", unsafe_allow_html=True)

# --- 4. MAIN WORKSPACE ---
st.markdown("<h1 style='color:white;'>Strategic Command Center</h1>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 2.2], gap="large")

with col_in:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Setup</p>', unsafe_allow_html=True)
    topic = st.text_input("Marketing Topic", placeholder="e.g. 18k White Gold Ring")
    objective = st.selectbox("Objective", ["High Conversion", "Brand Awareness", "Social Viral"])
    
    if st.button("GENERATE STRATEGY MATRIX"):
        if topic:
            with st.spinner("Analyzing market psychology and crafting strategy..."):
                master_prompt = f"""
                You are a world-class Luxury Marketing Consultant. 
                Write strategic assets for: {topic}. 
                Brand: {brand}. Objective: {objective}.
                Tone: Sophisticated, Professional, Emotional.
                Language: Myanmar (Natural, High-end vocabulary).

                Please follow this structure EXACTLY:
                [COPY_SECTION]
                Write AIDA and PAS copies here.
                
                [SCRIPT_SECTION]
                Write a 20-second Video Script (Hook, Body, CTA).
                
                [VISUAL_SECTION]
                Write a detailed AI Image Prompt in English.
                """
                try:
                    response = model.generate_content(master_prompt)
                    st.session_state['full_result'] = response.text
                    st.session_state['run'] = True
                except Exception as e:
                    st.error(f"AI Error: {e}")
        else:
            st.warning("Topic အရင်ဖြည့်ပေးပါခင်ဗျာ။")
    st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    if st.session_state.get('run'):
        res = st.session_state['full_result']
        
        # Helper function to extract sections safely
        def get_section(tag, text):
            pattern = f"\[{tag}\](.*?)(?=\[|$)"
            match = re.search(pattern, text, re.DOTALL)
            return match.group(1).strip() if match else "Content not found."

        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Strategic Result Matrix</p>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📝 CONTENT DECK", "🎬 MEDIA BRIEF", "🎨 VISUAL PROMPTS"])
        
        with tab1:
            st.markdown("### Expert Ad Copy Deck")
            copy_content = get_section("COPY_SECTION", res)
            st.markdown(f"<div class='matrix-box'>{copy_content}</div>", unsafe_allow_html=True)
            
        with tab2:
            st.markdown("### Production Script (Short-form)")
            script_content = get_section("SCRIPT_SECTION", res)
            st.markdown(f"<div class='matrix-box'>{script_content}</div>", unsafe_allow_html=True)
            
        with tab3:
            st.markdown("### AI Art Direction")
            visual_content = get_section("VISUAL_SECTION", res)
            st.info("Copy the prompt below for Midjourney/DALL-E:")
            st.code(visual_content, language="bash")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="border: 2px dashed #30363d; padding: 100px; text-align: center; border-radius: 12px; background: #161b22; color: #8b949e;">
                ဘယ်ဘက်တွင် အချက်အလက်ဖြည့်သွင်းပြီး <br><b>GENERATE STRATEGY MATRIX</b> ကိုနှိပ်ပါ။
            </div>
        """, unsafe_allow_html=True)
