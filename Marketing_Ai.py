import streamlit as st

# 1. ပထမဆုံးအနေနဲ့ UI ပုံစံကို Standard ဖြစ်အောင် ပြန်ညှိပါတယ်
st.set_page_config(page_title="AI Marketer Suite", layout="wide")

# 2. Sidebar ကို အရင်တည်ဆောက်ပါမယ်
with st.sidebar:
    st.title("💎 AI Marketer")
    st.divider()
    selected_brand = st.selectbox("Select Project", ["Jewelry Client A", "Tech Startup X"])
    st.write("---")
    st.success("Elite Agency Plan - Active")

# 3. Main Header
st.title("🚀 AI Marketer Command Center")
st.info(f"လက်ရှိစီမံနေသော Project: {selected_brand}")

# 4. Layout ကို ဘယ်/ညာ (၂) ခြမ်း ခွဲပါမယ်
col_left, col_right = st.columns([1, 1.5], gap="large")

with col_left:
    st.subheader("🎯 Campaign Design")
    
    # ရွေးချယ်စရာများကို ရှင်းလင်းစွာ ထားရှိခြင်း
    app_mode = st.radio("System Engine Mode", ["Smart Mode", "Architect Mode"])
    
    marketing_topic = st.text_input("Marketing Topic", placeholder="ဥပမာ - ရွှေဖြူဆွဲကြိုး")
    
    if app_mode == "Smart Mode":
        goal = st.selectbox("Goal", ["အရောင်းမြှင့်တင်ရန်", "အသိပညာပေးရန်", "Brand Story"])
    else:
        frameworks = st.multiselect("Frameworks", ["AIDA", "PAS", "BAB"], default=["AIDA"])
        creativity = st.select_slider("Creativity Level", ["Low", "Medium", "High"])

    if st.button("EXECUTE CAMPAIGN", type="primary"):
        st.session_state['run_process'] = True

with col_right:
    if st.session_state.get('run_process'):
        st.subheader("🔥 Result Matrix")
        
        # ရလဒ်များကို Tab များဖြင့် ခွဲပြခြင်း
        tab1, tab2, tab3 = st.tabs(["📝 Ad Copies", "🎬 Video Scripts", "🎨 Image Prompts"])
        
        with tab1:
            st.write("### Sales Copy (AIDA)")
            st.code("AI က ထုတ်ပေးမည့် စာသားများ ဤနေရာတွင် ပေါ်လာမည်...", language=None)
            
        with tab2:
            st.write("### Video Script")
            st.code("Hook: ... \nBody: ...", language=None)
            
        with tab3:
            st.write("### Midjourney Prompt")
            st.code("/imagine prompt: high-end jewelry...")
    else:
        # ဘာမှမလုပ်ရသေးခင် ပြမည့် အကွက်လေး
        st.warning("👈 ဘယ်ဘက်ခြမ်းတွင် အချက်အလက်များ ဖြည့်သွင်းပေးပါ။")

# 5. Footer (Optional)
st.divider()
st.caption("AI Marketer Suite v2.0 - Optimized for Visibility")
