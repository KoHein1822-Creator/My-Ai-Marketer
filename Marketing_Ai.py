import streamlit as st
import google.generativeai as genai

# --- CONFIGURATION ---
st.set_page_config(page_title="Elite AI Marketer Pro", layout="wide", page_icon="💎")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 8px; height: 3.2em; background-color: #4F46E5; color: white; border: none; font-weight: bold; }
    .res-box { padding: 25px; border-radius: 15px; background-color: white; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .sidebar-label { font-weight: bold; color: #1e293b; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# --- HYBRID PERSONA MAPPING ---
def get_hybrid_role(niche, mode):
    # လုပ်ငန်းအလိုက် ကျွမ်းကျင်မှု နှင့် Copywriting Skill ကို ပေါင်းစပ်ခြင်း
    roles = {
        "Jewelry": "Senior Luxury Brand Storyteller and Gemology Expert",
        "Cosmetics": "Professional Beauty Consultant and Consumer Psychology Specialist",
        "Tech": "Innovation-focused Copywriter and Tech Solutions Expert",
        "Food": "Mouth-watering Food Stylist and Content Marketer",
        "Real Estate": "Trust-based Investment Advisor and Lifestyle Strategist",
        "Online Shop": "High-Conversion E-commerce Specialist and Direct Response Copywriter"
    }
    base_role = roles.get(niche, "Senior Marketing Consultant")
    
    if mode == "Brand Awareness":
        return f"Act as a {base_role} focusing on Branding and Storytelling."
    elif mode == "Sales Conversion":
        return f"Act as a {base_role} specializing in Sales Psychology and Conversions."
    else:
        return f"Act as a {base_role} specializing in Viral Video Scripts and Engagement."

# --- AI CORE ENGINE ---
def generate_content(api_key, dna, mode, niche, topic, target, tone, formula=None):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        role_instruction = get_hybrid_role(niche, mode)
        style_dna = f"Strictly follow this writing style: {dna}" if dna else "Use natural, modern Burmese."
        
        # Dynamic Prompt Building
        prompt = f"""
        {role_instruction}
        
        TASK: Write a {mode} about {topic}.
        NICHE: {niche}
        TARGET AUDIENCE: {target}
        DESIRED TONE: {tone}
        {f"FRAMEWORK: Use {formula} structure." if formula else ""}
        
        CONSTRAINTS:
        - Use NATURAL SPOKEN BURMESE (No bookish/formal language).
        - Start with a massive HOOK.
        - Style DNA: {style_dna}
        - Include relevant emojis and a clear Call to Action (CTA).
        - Use line breaks for readability.
        """
        
        response = model.generate_content(prompt)
        return response.text, None
    except Exception as e:
        return None, str(e)

# --- UI LAYOUT ---
st.title("💎 Elite AI Marketer Pro")
st.markdown("##### Hybrid Persona & Professional Marketing Engine")
st.divider()

# --- SIDEBAR (Settings & DNA) ---
with st.sidebar:
    st.header("⚙️ Configuration")
    user_key = st.text_input("Gemini API Key", type="password")
    st.divider()
    st.markdown("<div class='sidebar-label'>🧬 STYLE DNA</div>", unsafe_allow_html=True)
    user_dna = st.text_area("သင့်ရဲ့ အကောင်းဆုံး Post နမူနာများကို ထည့်ပါ", height=250, 
                            placeholder="AI က သင့်လေသံကို အတုယူပါလိမ့်မယ်...")

# --- MAIN ENGINE ---
col_in, col_out = st.columns([1, 1.3], gap="large")

with col_in:
    st.subheader("🛠️ Strategy Input")
    st.markdown('<div class="res-box">', unsafe_allow_html=True)
    
    # Mode Selector
    mode_in = st.selectbox("🎯 Objective (Mode)", ["Sales Conversion", "Brand Awareness", "Video Script"])
    
    # Dynamic Framework Selector (Only for Sales)
    formula_in = None
    if mode_in == "Sales Conversion":
        formula_in = st.radio("Framework", ["AIDA", "PAS", "BAB"], horizontal=True)
    
    # Business Details
    niche_in = st.selectbox("🏢 Niche (လုပ်ငန်းအမျိုးအစား)", ["Jewelry", "Cosmetics", "Tech", "Food", "Real Estate", "Online Shop"])
    topic_in = st.text_input("💡 Topic / Product Name", placeholder="ဥပမာ- ရွှေဖြူဆွဲကြိုး လက်ရာသစ်")
    target_in = st.text_input("👥 Target Audience", placeholder="ဥပမာ- လူငယ်စုံတွဲများ")
    tone_in = st.select_slider("🎭 Tone", options=["Casual", "Friendly", "Professional", "Hard Sell"])
    
    if st.button("Generate Magic ✨"):
        if not user_key or not topic_in:
            st.error("API Key နှင့် Topic ကို ဖြည့်သွင်းပေးပါ။")
        else:
            with st.spinner("Creating your professional content..."):
                res, err = generate_content(user_key, user_dna, mode_in, niche_in, topic_in, target_in, tone_in, formula_in)
                if err: st.error(err)
                else: st.session_state['pro_result'] = res
    st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    st.subheader("🚀 Output Preview")
    if 'pro_result' in st.session_state:
        st.markdown('<div class="res-box">', unsafe_allow_html=True)
        final_draft = st.text_area("AI Copywriter", st.session_state['pro_result'], height=480)
        
        # Utility Buttons
        c1, c2, c3 = st.columns(3)
        with c1: st.button("📋 Copy to Clipboard")
        with c2: st.download_button("📥 Download TXT", final_draft)
        with c3: 
            if st.button("✂️ Make Shorter"):
                # Quick tweak logic
                with st.spinner("Refining..."):
                    res, _ = generate_content(user_key, user_dna, mode_in, niche_in, f"Shorten this: {final_draft}", target_in, tone_in, formula_in)
                    st.session_state['pro_result'] = res
                    st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("အချက်အလက်များ ဖြည့်သွင်းပြီး 'Generate' ကို နှိပ်ပါဗျာ။")

st.divider()
st.caption("© 2026 AI Marketer Pro | Built for Professional Burmese Freelancers")
