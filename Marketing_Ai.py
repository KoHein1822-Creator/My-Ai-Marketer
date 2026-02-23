import streamlit as st
import google.generativeai as genai
import re

# --- 1. CORE SETUP ---
st.set_page_config(page_title="AI Marketer Pro | Enterprise", layout="wide", page_icon="💎")

try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Security Authentication Failed: Check Secrets Configuration.")

# --- 2. PREMIUM SaaS CSS ---
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    .workspace-card { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }
    .matrix-box { background: #0d1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; line-height: 1.6; }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 10px; }
    .main-header { font-size: 30px; font-weight: 800; color: #ffffff; }
    .stButton>button { background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; color: white !important; font-weight: 700 !important; border-radius: 8px !important; height: 50px; border: none !important; width: 100%; transition: 0.3s; }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(46,160,67,0.4); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: BRAND ARCHITECTURE ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.caption("Commercial Enterprise Edition v7.0")
    st.divider()
    
    st.markdown('<p class="section-label">Brand Vault</p>', unsafe_allow_html=True)
    brand = st.selectbox("Active Brand Profile", ["Luxury Client A", "Global Tech X"], label_visibility="collapsed")
    
    with st.expander("🧬 Brand DNA Insights", expanded=True):
        st.write("**Niche:** Luxury High-End")
        st.write("**Tone:** Professional & Elegant")
        st.write("**Persona:** Wealthy Elite")
    
    st.divider()
    st.markdown('<p class="section-label">System Status</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:#3fb950;'>● Commercial License Active</p>", unsafe_allow_html=True)

# --- 4. COMMAND CENTER INTERFACE ---
st.markdown('<p class="main-header">Strategic Command Center</p>', unsafe_allow_html=True)
st.caption(f"Architecting Growth Strategy for **{brand}**")

col_in, col_out = st.columns([1, 2.2], gap="large")

with col_in:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Intelligence</p>', unsafe_allow_html=True)
    
    # Dual-Mode Intelligence
    mode = st.radio("Intelligence Mode", ["Smart Mode", "Architect Mode"], horizontal=True)
    
    topic = st.text_input("Marketing Topic", placeholder="e.g. 18k Rose Gold Watch")
    objective = st.selectbox("Objective", ["High Conversion", "Brand Awareness", "Direct Sales"])
    
    if mode == "Architect Mode":
        st.markdown('<p class="section-label">Framework Selection</p>', unsafe_allow_html=True)
        frameworks = st.multiselect("Active Logic", ["AIDA", "PAS", "BAB", "4Ps"], default=["AIDA", "PAS"])
    
    if st.button("EXECUTE STRATEGY MATRIX"):
        if topic:
            with st.spinner("Processing Strategy Matrix..."):
                master_prompt = f"""
                Act as a Senior Creative Director & Marketing Architect.
                Brand: {brand} (Luxury). Topic: {topic}. Objective: {objective}.
                Tone: Elegant, Persuasive, Professional.
                Language: Myanmar (Natural, High-end vocabulary).

                Output MUST follow this structure:
                [AIDA_SECTION]
                Write professional AIDA copy.
                [PAS_SECTION]
                Write professional PAS copy.
                [SCRIPT_SECTION]
                Write a 20-sec Video Script (Hook, Body, CTA).
                [VISUAL_SECTION]
                Write a high-end Midjourney Photography Prompt in English.
                """
                response = model.generate_content(master_prompt)
                st.session_state['full_res'] = response.text
                st.session_state['ready'] = True
        else:
            st.warning("Campaign Topic is required.")
    st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    if st.session_state.get('ready'):
        res = st.session_state['full_res']
        
        def parse(tag, text):
            match = re.search(f"\[{tag}\](.*?)(?=\[|$)", text, re.DOTALL)
            return match.group(1).strip() if match else "Data not found."

        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Strategic Output Matrix</p>', unsafe_allow_html=True)
        
        t1, t2, t3 = st.tabs(["📄 CONTENT DECK", "🎬 MEDIA BRIEF", "🎨 VISUAL PROMPTS"])
        
        with t1:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**Angle: AIDA**")
                st.markdown(f"<div class='matrix-box'>{parse('AIDA_SECTION', raw=res)}</div>", unsafe_allow_html=True)
            with c2:
                st.markdown("**Angle: PAS**")
                st.markdown(f"<div class='matrix-box'>{parse('PAS_SECTION', raw=res)}</div>", unsafe_allow_html=True)
        
        with t2:
            st.markdown("**Video Production Script**")
            st.markdown(f"<div class='matrix-box'>{parse('SCRIPT_SECTION', raw=res)}</div>", unsafe_allow_html=True)
            
        with t3:
            st.markdown("**Art Direction (AI Prompt)**")
            st.code(parse("VISUAL_SECTION", raw=res), language="bash")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="border: 2px dashed #30363d; padding: 120px; text-align: center; border-radius: 12px; background: #161b22; color: #8b949e;">
                <p style="font-size: 20px;">Mission Control Ready</p>
                <small>Define campaign parameters and click Execute.</small>
            </div>
        """, unsafe_allow_html=True)
