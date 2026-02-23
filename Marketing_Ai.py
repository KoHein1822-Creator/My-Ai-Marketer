import streamlit as st
import google.generativeai as genai

# --- 1. AI SETUP ---
st.set_page_config(page_title="AI Marketer Pro v5.0", layout="wide")

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-flash-lite-latest')
except:
    st.error("API Key Configuration လိုအပ်နေပါသေးတယ်။")

# --- 2. PROFESSIONAL CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    .workspace-card { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    .matrix-box { background: #0d1117; padding: 20px; border-radius: 10px; border-left: 4px solid #58a6ff; margin-bottom: 15px; }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; }
    .stButton>button { background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; color: white !important; font-weight: 700 !important; width: 100%; border-radius: 8px !important; height: 50px; border: none !important; }
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
        st.write("**Tone:** Elegant, Minimalist, Powerful")

# --- 4. MAIN WORKSPACE ---
st.markdown("<h1 style='color:white;'>Strategic Command Center</h1>", unsafe_allow_html=True)

col_in, col_out = st.columns([1, 2.2], gap="large")

with col_in:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Setup</p>', unsafe_allow_html=True)
    topic = st.text_input("Marketing Topic", placeholder="e.g. 18k White Gold Ring with Diamond")
    objective = st.selectbox("Objective", ["High Conversion", "Brand Awareness"])
    
    if st.button("GENERATE STRATEGY MATRIX"):
        if topic:
            with st.spinner("AI Marketer is analyzing market angles..."):
                # Professional Multi-Tasking Prompt
                master_prompt = f"""
                Act as a Senior Creative Director for a luxury brand.
                Topic: {topic}
                Objective: {objective}
                Brand Tone: Elegant, Elite, Scarcity-based.
                Language: Myanmar (Natural, not robot-like).

                Please provide:
                1. AIDA Copy: (Attention, Interest, Desire, Action)
                2. PAS Copy: (Problem, Agitation, Solution)
                3. Video Script: (Hook, Body, CTA)
                4. Visual Prompt: (Midjourney style for product photography)
                
                Format each section clearly.
                """
                response = model.generate_content(master_prompt)
                st.session_state['full_result'] = response.text
                st.session_state['run'] = True
        else:
            st.warning("Topic ဖြည့်စွက်ပေးပါဦး။")
    st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    if st.session_state.get('run'):
        res = st.session_state['full_result']
        
        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Generated Strategic Matrix</p>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📄 CONTENT DECK", "🎬 MEDIA BRIEF", "🎨 VISUAL PROMPTS"])
        
        with tab1:
            st.markdown("### Strategic Ad Copies")
            st.write(res.split("Video Script")[0]) # UI ထဲမှာ ခွဲထုတ်ပြခြင်း
            
        with tab2:
            st.markdown("### Production Script")
            if "Video Script" in res:
                script_part = res.split("Video Script:")[1].split("Visual Prompt:")[0]
                st.markdown(f"<div class='matrix-box'>{script_part}</div>", unsafe_allow_html=True)
            
        with tab3:
            st.markdown("### Art Direction Prompt")
            if "Visual Prompt" in res:
                prompt_part = res.split("Visual Prompt:")[1]
                st.code(prompt_part, language="bash")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="border: 2px dashed #30363d; padding: 100px; text-align: center; border-radius: 12px; background: #161b22; color: #8b949e;">Configuration အားဖြည့်စွက်ပြီး Execute ကိုနှိပ်ပါ။</div>', unsafe_allow_html=True)

