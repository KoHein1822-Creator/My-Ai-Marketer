import streamlit as st
import google.generativeai as genai
import time
import re

# --- 1. CORE CONFIGURATION ---
st.set_page_config(page_title="Mission Control | Ultimate", layout="wide", page_icon="🚀")

# Gemini API Connection
try:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
    model = genai.GenerativeModel('gemini-1.5-flash')
except:
    st.error("Authentication Error: Connect your API Key in Secrets.")

# --- 2. THE MASTER UI STYLING (GLASSMORPHISM) ---
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: #adbac7; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #30363d; }
    
    /* Global Card Style */
    .mc-card { 
        background: #161b22; padding: 20px; border-radius: 12px; 
        border: 1px solid #30363d; margin-bottom: 20px; 
    }
    .label-sm { font-size: 10px; font-weight: bold; color: #58a6ff; text-transform: uppercase; letter-spacing: 1.5px; margin-bottom: 8px; }
    
    /* Metrics Styling */
    .metric-value { font-size: 24px; font-weight: bold; color: #ffffff; }
    .status-active { color: #3fb950; font-size: 12px; }
    
    /* Button Styling */
    .stButton>button { 
        background: linear-gradient(135deg, #1f6feb 0%, #238636 100%) !important; 
        border: none !important; color: white !important; font-weight: bold; height: 48px; width: 100%; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: NAVIGATION & BRAIN STATUS ---
with st.sidebar:
    st.markdown("<h2 style='color:white;'>M-Control <span style='color:#58a6ff;'>Pro</span></h2>", unsafe_allow_html=True)
    st.caption("Enterprise AI OS | v10.0 Final UI")
    st.divider()
    
    st.markdown('<p class="label-sm">Control Modules</p>', unsafe_allow_html=True)
    menu = st.radio("Navigation", ["🛸 Command Center", "📊 Analytics Hub", "🧬 Audience Engine", "⚙️ Settings"], label_visibility="collapsed")
    
    st.divider()
    st.markdown('<p class="label-sm">The Brain (Aung Gyee)</p>', unsafe_allow_html=True)
    st.markdown("<p class='status-active'>● Online & Synchronized</p>", unsafe_allow_html=True)
    st.progress(100) # Efficiency meter

# --- 4. MAIN COMMAND CENTER ---
if menu == "🛸 Command Center":
    # Dashboard Grid
    col_config, col_main, col_insight = st.columns([1, 2, 1], gap="medium")

    # --- ZONE 1: CONFIGURATION ---
    with col_config:
        st.markdown('<div class="mc-card">', unsafe_allow_html=True)
        st.markdown('<p class="label-sm">Mission Parameters</p>', unsafe_allow_html=True)
        topic = st.text_input("Campaign Topic", placeholder="e.g. Rare Jewelry")
        strategy = st.selectbox("Logic Framework", ["AIDA (Attention-Interest)", "PAS (Problem-Agitate)", "Storytelling (Emotional)"])
        tone = st.select_slider("Brand Voice", options=["Soft", "Professional", "Bold"])
        
        st.markdown('<p class="label-sm" style="margin-top:15px;">Target Channel</p>', unsafe_allow_html=True)
        channels = st.multiselect("Publishing to", ["Facebook", "Instagram", "TikTok"], default="Facebook")
        
        execute = st.button("EXECUTE MISSION")
        st.markdown('</div>', unsafe_allow_html=True)

    # --- ZONE 2: EXECUTION & OUTPUT ---
    with col_main:
        if execute and topic:
            # Agent Thought Simulation
            status_box = st.empty()
            with status_box.container():
                st.markdown('<div class="mc-card">', unsafe_allow_html=True)
                st.markdown('<p class="label-sm">Agent Reasoning (Aung Gyee)</p>', unsafe_allow_html=True)
                steps = ["Analyzing Market Trends...", "Segmenting Audience Interests...", "Constructing Strategic Copy...", "Optimizing for Luxury Tone..."]
                for step in steps:
                    st.write(f"⚡ {step}")
                    time.sleep(0.6)
                st.markdown('</div>', unsafe_allow_html=True)
            status_box.empty()

            # AI Content Generation
            with st.spinner("AI Generating Final Assets..."):
                prompt = f"""
                Act as a Master Marketing Architect. 
                Topic: {topic}. Strategy: {strategy}. Tone: {tone}.
                Language: Myanmar (Natural & Elegant).
                Structure your output with tags: [AIDA], [PAS], [SCRIPT], [IMAGE_PROMPT]
                """
                response = model.generate_content(prompt)
                res_text = response.text

                # Parsing
                def get_part(tag, text):
                    match = re.search(f"\[{tag}\](.*?)(?=\[|$)", text, re.DOTALL)
                    return match.group(1).strip() if match else "Preparing content..."

                st.markdown('<div class="mc-card">', unsafe_allow_html=True)
                st.markdown('<p class="label-sm">Strategy Matrix Output</p>', unsafe_allow_html=True)
                
                t1, t2, t3 = st.tabs(["📄 Strategic Copy", "🎥 Video Script", "🎨 Visual Prompt"])
                with t1:
                    st.markdown("**Core Frameworks**")
                    st.write(get_part("AIDA", res_text))
                    st.divider()
                    st.write(get_part("PAS", res_text))
                with t2:
                    st.write(get_part("SCRIPT", res_text))
                with t3:
                    st.code(get_part("IMAGE_PROMPT", res_text), language="bash")
                
                st.divider()
                st.download_button("Export Mission Report", res_text, file_name="mission_report.txt")
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            # Placeholder State
            st.markdown("""
                <div style="height: 500px; display: flex; flex-direction: column; align-items: center; justify-content: center; border: 2px dashed #30363d; border-radius:12px; color:#484f58;">
                    <img src="https://cdn-icons-png.flaticon.com/512/2592/2592201.png" width="80" style="opacity: 0.2; margin-bottom: 20px;">
                    <p>Ready for Mission Command. Enter a topic to begin.</p>
                </div>
            """, unsafe_allow_html=True)

    # --- ZONE 3: INSIGHTS & PREVIEW ---
    with col_insight:
        st.markdown('<div class="mc-card">', unsafe_allow_html=True)
        st.markdown('<p class="label-sm">Predictive Analytics</p>', unsafe_allow_html=True)
        st.write("Engagement Probability")
        st.progress(88)
        st.write("Conversion Index")
        st.progress(72)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="mc-card">', unsafe_allow_html=True)
        st.markdown('<p class="label-sm">Multi-Channel Preview</p>', unsafe_allow_html=True)
        st.caption("Visualizing content for Desktop & Mobile...")
        st.image("https://via.placeholder.com/300x200/0d1117/58a6ff?text=Social+Media+Preview", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

else:
    st.info(f"The {menu} module is fully designed. Integration with backend database will follow.")
