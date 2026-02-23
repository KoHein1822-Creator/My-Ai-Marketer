import streamlit as st
import google.generativeai as genai
import re

# --- 1. SETUP & THEME ---
st.set_page_config(page_title="AI Marketer Pro | Command Center", layout="wide", page_icon="💎")

# AI Connection
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("API Key not found in Secrets. Please check your configuration.")

# CSS for SaaS Architecture
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #c9d1d9; }
    section[data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    .workspace-card { background: #161b22; padding: 25px; border-radius: 12px; border: 1px solid #30363d; margin-bottom: 20px; }
    .matrix-box { background: #0d1117; padding: 20px; border-radius: 10px; border: 1px solid #30363d; margin-bottom: 15px; }
    .section-label { font-size: 11px; font-weight: 800; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; }
    .main-header { font-size: 28px; font-weight: 800; color: #ffffff; margin-bottom: 5px; }
    .stButton>button { background: linear-gradient(135deg, #238636 0%, #2ea043 100%) !important; color: white !important; font-weight: 700 !important; width: 100%; border-radius: 8px !important; height: 50px; border: none !important; }
    .secondary-btn>button { background: #21262d !important; border: 1px solid #30363d !important; color: #c9d1d9 !important; height: 40px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. SIDEBAR: BRAND VAULT ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>AI Marketer <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.caption("Strategic Intelligence Suite v6.0")
    st.divider()
    
    st.markdown('<p class="section-label">Organization</p>', unsafe_allow_html=True)
    selected_brand = st.selectbox("Current Brand", ["Jewelry Client A", "Luxury Lifestyle X"], label_visibility="collapsed")
    
    with st.expander("🧬 Brand DNA Insights", expanded=True):
        st.markdown("**Niche:** Luxury Jewelry")
        st.markdown("**Tone:** Elegant, Story-driven")
        st.markdown("**Audience:** High-net-worth")
    
    st.divider()
    st.markdown('<p class="section-label">Status</p>', unsafe_allow_html=True)
    st.markdown("<p style='color:#3fb950; font-weight:bold;'>● Elite Agency Active</p>", unsafe_allow_html=True)
    st.caption("45 Days remaining in your plan.")

# --- 3. MAIN INTERFACE ---
st.markdown('<p class="main-header">Strategic Command Center</p>', unsafe_allow_html=True)
st.caption(f"Executing Multi-Channel Strategy for **{selected_brand}**")

col_config, col_result = st.columns([1, 2.2], gap="large")

# LEFT: CONFIGURATION
with col_config:
    st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
    st.markdown('<p class="section-label">Campaign Setup</p>', unsafe_allow_html=True)
    
    engine_mode = st.radio("System Engine Mode", ["Smart Mode", "Architect Mode"], horizontal=True)
    
    topic = st.text_input("Marketing Topic", placeholder="e.g. 18k Rose Gold Diamond Necklace")
    objective = st.selectbox("Objective", ["Sales Conversion", "Brand Awareness", "Direct Engagement"])
    
    if engine_mode == "Architect Mode":
        st.markdown('<p class="section-label">Advanced Controls</p>', unsafe_allow_html=True)
        frameworks = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB", "4Ps"], default=["AIDA", "PAS"])
        creativity = st.slider("Creativity Depth", 0.1, 1.0, 0.7)
    
    if st.button("EXECUTE STRATEGY MATRIX"):
        if topic:
            with st.spinner("Calculating Multi-Angle Content Matrix..."):
                master_prompt = f"""
                You are a Senior Marketing Strategist. Create a high-end campaign for: {topic}.
                Brand Context: {selected_brand} (Luxury). Language: Myanmar (Natural & Professional).
                
                Follow this structure:
                [AIDA_SECTION]
                Write AIDA Ad Copy.
                
                [PAS_SECTION]
                Write PAS Ad Copy.
                
                [SCRIPT_SECTION]
                Write a 20-second Video Script (Hook, Body, CTA).
                
                [VISUAL_SECTION]
                Write a detailed Midjourney AI Prompt in English.
                
                [META_SECTION]
                Provide 5 trending hashtags and targeting keywords.
                """
                response = model.generate_content(master_prompt)
                st.session_state['run'] = True
                st.session_state['raw_data'] = response.text
        else:
            st.warning("Topic အရင်ဖြည့်စွက်ပေးပါ။")
    st.markdown('</div>', unsafe_allow_html=True)

# RIGHT: STRATEGIC MATRIX OUTPUT
with col_result:
    if st.session_state.get('run'):
        raw = st.session_state['raw_data']
        
        def parse(tag, text):
            match = re.search(f"\[{tag}\](.*?)(?=\[|$)", text, re.DOTALL)
            return match.group(1).strip() if match else "Data not found."

        st.markdown('<div class="workspace-card">', unsafe_allow_html=True)
        st.markdown('<p class="section-label">Strategic Result Matrix</p>', unsafe_allow_html=True)
        
        tab_deck, tab_prod, tab_meta = st.tabs(["📝 CONTENT DECK", "🎬 PRODUCTION BRIEF", "📊 TARGETING INFO"])
        
        with tab_deck:
            c1, c2 = st.columns(2)
            with c1:
                st.markdown("**[Angle 1: AIDA]**")
                st.markdown(f"<div class='matrix-box'>{parse('AIDA_SECTION', raw)}</div>", unsafe_allow_html=True)
            with c2:
                st.markdown("**[Angle 2: PAS]**")
                st.markdown(f"<div class='matrix-box'>{parse('PAS_SECTION', raw)}</div>", unsafe_allow_html=True)
            
            # Post-Generation Controls
            st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
            btn_col1, btn_col2, _ = st.columns([1, 1, 2])
            btn_col1.button("🔄 Regenerate")
            btn_col2.button("📥 Export PDF")
            st.markdown('</div>', unsafe_allow_html=True)

        with tab_prod:
            st.markdown("**Video Narrative Script**")
            st.markdown(f"<div class='matrix-box'>{parse('SCRIPT_SECTION', raw)}</div>", unsafe_allow_html=True)
            
            st.markdown("**AI Visual Direction (Prompt)**")
            st.code(parse('VISUAL_SECTION', raw), language="bash")
            st.caption("Copy this to Midjourney or DALL-E to generate visuals.")

        with tab_meta:
            st.markdown("**Metadata & Hashtags**")
            st.markdown(f"<div class='matrix-box'>{parse('META_SECTION', raw)}</div>", unsafe_allow_html=True)
            
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        # Professional Empty State
        st.markdown("""
            <div style="border: 2px dashed #30363d; padding: 120px; text-align: center; border-radius: 12px; background: #161b22; color: #8b949e;">
                <p style="font-size: 18px;">Ready to deploy intelligence.</p>
                <small>ဘယ်ဘက်တွင် Campaign Topic ထည့်သွင်းပြီး <b>Execute</b> ကိုနှိပ်ပါ။</small>
            </div>
        """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color: #484f58; font-size: 11px; margin-top: 30px;'>AI Marketer Pro v6.0 | Enterprise Strategic Environment</p>", unsafe_allow_html=True)
