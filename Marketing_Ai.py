import streamlit as st
import google.generativeai as genai

# ၁။ AI Setup Function
def get_ai_response(api_key, prompt):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-flash-latest')
        response = model.generate_content(prompt)
        return response.text, None
    except Exception as e:
        return None, str(e)

# ၂။ UI Layout
st.set_page_config(page_title="Pro Marketer AI", layout="wide")
st.title("🚀 All-in-One AI Marketing Platform")

with st.sidebar:
    st.header("⚙️ Settings")
    user_api_key = st.text_input("Enter your Gemini API Key", type="password")
    client_name = st.text_input("Client Name", "Client A")
    business_type = st.selectbox("Niche", ["Jewelry", "Cosmetics", "FMCG", "Online Shop", "Other"])
    target_audience = st.radio("Audience", ["B2C", "B2B"])

# ၃။ Tabs ခွဲခြင်း
tab1, tab2, tab3 = st.tabs(["✍️ Content Writer", "📅 30-Day Plan", "📊 Dashboard"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        mode = st.selectbox("Format", ["FB Post", "Sales Copy", "Video Script"])
        topic = st.text_area("ဘာအကြောင်းရေးမလဲ?", key="topic_input")
        
        if st.button("Generate Content"):
            if not user_api_key:
                st.error("🔑 API Key အရင်ထည့်ပေးပါဗျာ။")
            elif not topic:
                st.warning("📝 ရေးချင်တဲ့ အကြောင်းအရာလေး အရင်ရိုက်ပေးပါ။")
            else:
                with st.spinner("AI စာရေးပေးနေပါသည်... ခဏစောင့်ပါ..."):
                    prompt = f"Write a {mode} in Burmese for {business_type} about {topic}. Natural tone."
                    result, error = get_ai_response(user_api_key, prompt)
                    
                    if error:
                        st.error(f"❌ Error တက်သွားပါတယ်: {error}")
                    else:
                        st.session_state['content_output'] = result

    with col2:
        st.subheader("Result Output")
        if 'content_output' in st.session_state:
            st.text_area("AI ရေးပေးထားသောစာ -", st.session_state['content_output'], height=450)
            st.button("Clear Output", on_click=lambda: st.session_state.pop('content_output'))

with tab2:
    st.subheader("📅 Monthly Content Calendar")
    if st.button("Generate 30-Day Strategy"):
        if user_api_key:
            with st.spinner("တစ်လစာ Plan ဆွဲနေပါသည်..."):
                prompt = f"Create a 30-day content calendar for {business_type} in table format (Date, Topic, Goal). Language: Burmese."
                result, error = get_ai_response(user_api_key, prompt)
                if error:
                    st.error(f"❌ Error: {error}")
                else:
                    st.markdown(result)
        else:
            st.error("API Key လိုအပ်ပါသည်။")

with tab3:
    st.info("📊 Dashboard & Export features are coming soon.")

