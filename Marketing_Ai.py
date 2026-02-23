import streamlit as st

st.title("API Key Connection Test")

# Secrets ထဲမှာ Key ရှိ၊ မရှိ စစ်ဆေးခြင်း
if "GEMINI_API_KEY" in st.secrets:
    st.success("✅ အောင်မြင်ပါတယ်! Streamlit က သင့်ရဲ့ API Key ကို ရှာတွေ့ထားပါတယ်။")
    
    # Key ရဲ့ ပထမစာလုံး ၄ လုံးလောက်ကိုပဲ ပြပြီး စစ်ဆေးမယ် (လုံခြုံရေးအရ အကုန်မပြပါ)
    key_preview = st.secrets["GEMINI_API_KEY"][:4]
    st.write(f"Key Preview: {key_preview}****")
else:
    st.error("❌ မအောင်မြင်သေးပါ! Secrets ထဲမှာ GEMINI_API_KEY ကို ရှာမတွေ့သေးပါဘူး။")
