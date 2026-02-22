import streamlit as st
import google.generativeai as genai
import pandas as pd
from io import BytesIO

# --- CONFIGURATION ---
st.set_page_config(page_title="Elite AI Marketer Pro v2", layout="wide", page_icon="💎")

# --- ADVANCED CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pyidaungsu&display=swap');
    body { font-family: 'Pyidaungsu', sans-serif; background-color: #f1f5f9; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; transition: 0.3s; }
    .main-btn > button { background-color: #4F46E5 !important; color: white !important; height: 3.5em; font-size: 18px !important; }
    .refine-btn > button { background-color: #f8fafc !important; color: #475569 !important; border: 1px solid #e2e8f0 !important; font-size: 12px !important; }
    .res-box { padding: 25px; border-radius: 12px; background-color: white; border: 1px solid #e2e8f0; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); }
    .sidebar-card { padding: 15px; background-color: #1e293b; border-radius: 10px; color: white; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

# --- ENGINE FUNCTIONS ---
def call_gemini(api_key, full_prompt):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(full_prompt)
        return response.text, None
    except Exception as e:
        return None, str(e)

# --- UI HEADER ---
st.markdown("## 💎 Elite AI Marketer Pro <span style='font-size: 15px; color: #64748b;'>v2.0 Premium</span>", unsafe_allow_html=True)

# --- SIDEBAR CONTROL ---
with st.sidebar:
    st.markdown("<div class='sidebar-card'>⚙️ <b>SYSTEM ACCESS</b></div>", unsafe_allow_html=True)
    user_api_key = st.text_input("Gemini API Key", type="password")
    
    st.divider()
    st.markdown("<div class='sidebar-card'>🧬 <b>STYLE DNA BANK</b></div>", unsafe_allow_html=True)
    dna_input = st.text_area("ကိုယ့်ရဲ့ လေသံနမူနာများ (Writing Samples)", height=250, 
                             placeholder="သင်ရေးဖူးတဲ့ အကောင်းဆုံး Post ၃-၅ ပုဒ် ထည့်ပါ။ AI က သင့်အရည်အချင်းကို ကူးယူပါလိမ့်မယ်။")
    
    st.divider()
    st.info("💡 Tip: DNA ထည့်လေ AI က သင်နဲ့တူလေ ဖြစ်မှာပါ။")

# --- MAIN INTERFACE ---
col_in, col_out = st.columns([1, 1.2], gap="large")

with col_in:
    st.subheader("🛠️ Strategy & Input")
    with st.container():
        st.markdown('<div class="res-box">', unsafe_allow_html=True)
        
        task = st.selectbox("🎯 ဘာလုပ်ချင်လဲ?", 
                          ["Social Media Post", "30-Day Content Plan (Excel)", "Short Video Script", "Sales Copywriting"])
        
        topic_in = st.text_input("💡 Topic / Product", placeholder="ဥပမာ- ရွှေဖြူဆွဲကြိုး အသစ်ရောက်တာ")
        
        c1, c2 = st.columns(2)
        with c1:
            niche_in = st.selectbox("🏢 Niche", ["Jewelry", "Beauty", "Fashion", "Real Estate", "Tech", "Food"])
        with c2:
            audience_in = st.selectbox("👥 Target", ["General", "Young Adults", "Housewives", "High-end Clients"])
            
        tone_in = st.select_slider("🎭 Tone", options=["Casual", "Friendly", "Professional", "Hard Sell"])
        
        st.markdown('<div class="main-btn">', unsafe_allow_html=True)
        generate = st.button("Generate Magic ✨")
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with col_out:
    st.subheader("🚀 Result Engine")
    
    if generate:
        if not user_api_key or not topic_in:
            st.error("⚠️ API Key နဲ့ Topic ထည့်ပေးဖို့ လိုပါတယ်ဗျာ။")
        else:
            with st.spinner("AI is thinking like a Pro..."):
                # PROMPT BUILDING
                identity = f"You are a world-class Burmese Marketer. Style DNA: {dna_input if dna_input else 'Engaging and modern'}. "
                
                if task == "30-Day Content Plan (Excel)":
                    prompt = f"{identity} Create a 30-day content calendar for {niche_in} about {topic_in}. Provide ONLY a CSV-formatted table with columns: Date, Topic, Hook, Goal. Language: Burmese."
                else:
                    prompt = f"{identity} Write a {task} about {topic_in}. Target: {audience_in}. Tone: {tone_in}. Use natural spoken Burmese, catchy hooks, and emojis."
                
                res, err = call_gemini(user_api_key, prompt)
                if err: st.error(err)
                else: st.session_state['master_output'] = res

    if 'master_output' in st.session_state:
        st.markdown('<div class="res-box">', unsafe_allow_html=True)
        
        # DISPLAY LOGIC
        final_text = st.text_area("AI Final Draft:", st.session_state['master_output'], height=400)
        
        # REFINE TOOLS
        st.markdown("##### ⚡ Quick Refine")
        r1, r2, r3 = st.columns(3)
        with r1:
            st.markdown('<div class="refine-btn">', unsafe_allow_html=True)
            if st.button("✂️ ပိုတိုပေးပါ"):
                new_res, _ = call_gemini(user_api_key, f"Make this shorter and punchier: {final_text}")
                st.session_state['master_output'] = new_res
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with r2:
            st.markdown('<div class="refine-btn">', unsafe_allow_html=True)
            if st.button("🤣 ပိုရယ်ရအောင်"):
                new_res, _ = call_gemini(user_api_key, f"Make this more humorous and witty in Burmese: {final_text}")
                st.session_state['master_output'] = new_res
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        with r3:
            st.markdown('<div class="refine-btn">', unsafe_allow_html=True)
            if st.button("🔥 ပိုရောင်းရအောင်"):
                new_res, _ = call_gemini(user_api_key, f"Add more urgency and strong Call to Action (Hard Sell) in Burmese: {final_text}")
                st.session_state['master_output'] = new_res
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)

        st.divider()
        
        # EXPORT TOOLS
        ex1, ex2 = st.columns(2)
        with ex1:
            st.download_button("📥 Download as TXT", final_text, file_name="ai_content.txt")
        with ex2:
            # Excel/CSV Export Logic
            if "Date," in final_text or "Topic," in final_text:
                st.download_button("📊 Export as CSV/Excel", final_text, file_name="content_plan.csv")
            else:
                st.button("📋 Copy to Clipboard (Ctrl+C)")
        
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.info("စောင့်ဆိုင်းနေပါသည်... အချက်အလက်ဖြည့်ပြီး Generate ကိုနှိပ်ပါ။")

st.divider()
st.caption("Developed by Gemini for Elite Freelance Marketers | © 2026")
