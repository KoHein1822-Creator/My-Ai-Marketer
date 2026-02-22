import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime

# ၁။ AI Configuration & Troubleshooter
def setup_ai(api_key):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_choice)
        # Key မှန်မမှန် စမ်းသပ်ခြင်း
        model.generate_content("test")
        return model, None
    except Exception as e:
        return None, f"❌ API Key မှာ ပြဿနာရှိနေပါတယ်: {str(e)}"

# ၂။ UI အလှဆင်ခြင်း
st.set_page_config(page_title="Pro Marketer AI", layout="wide")
st.title("🚀 All-in-One AI Marketing Platform")

# Sidebar - Settings
with st.sidebar:
    model_choice = st.selectbox("Select AI Model", ["gemini-flash-lite-latest","gemini-flash-latest"])
    st.header("⚙️ Settings")
    user_api_key = st.text_input("Enter your Gemini API Key", type="password")
    
    st.divider()
    client_name = st.text_input("Client Name", "Client A")
    business_type = st.selectbox("Niche", ["Jewelry", "Cosmetics", "FMCG", "Online Shop", "Other"])
    target_audience = st.radio("Targeting", ["B2C", "B2B"])

# ၃။ AI အား စစ်ဆေးခြင်း
model = None
if user_api_key:
    model, error_msg = setup_ai(user_api_key)
    if error_msg:
        st.error(error_msg)
    else:
        st.success("✅ AI Connected!")

# ၄။ Tabs ခွဲခြင်း (Features များ)
tab1, tab2, tab3 = st.tabs(["✍️ Single Post", "📅 Monthly Plan", "📊 Dashboard"])

# --- Tab 1: Single Post / Script / Copy ---
with tab1:
    col1, col2 = st.columns(2)
    with col1:
        mode = st.selectbox("Format", ["FB Content", "Copywriting (AIDA)", "Short Script"])
        topic = st.text_area("Topic/Idea")
        if st.button("Generate Now"):
            if model:
                prompt = f"You are an expert marketer for {business_type}. Create {mode} for {target_audience} about {topic} in Burmese."
                res = model.generate_content(prompt)
                st.session_state['last_result'] = res.text
            else:
                st.warning("Please connect API first.")
    
    with col2:
        st.subheader("Output")
        if 'last_result' in st.session_state:
            st.text_area("Result", st.session_state['last_result'], height=300)

# --- Tab 2: Monthly Strategy (သင်တောင်းဆိုထားသော Feature) ---
with tab2:
    st.subheader("📅 Content Strategy & 30-Day Plan")
    if st.button("Generate 30-Day Calendar"):
        if model:
            with st.spinner("Calculating Strategy..."):
                prompt = f"Create a 30-day content calendar for a {business_type} business targeting {target_audience}. Output in a table format with Date, Topic, and Goal. Language: Burmese."
                res = model.generate_content(prompt)
                st.markdown(res.text)
        else:
            st.warning("Please connect API first.")

# --- Tab 3: Simple Dashboard ---
with tab3:
    st.subheader("📊 Your Activity Status")

    st.info("ဤအပိုင်းတွင် သင်ထုတ်ထားသော စာရင်းများကို Excel ထုတ်ယူနိုင်ရန် နောက်အဆင့်တွင် ထပ်တိုးပါမည်။")




