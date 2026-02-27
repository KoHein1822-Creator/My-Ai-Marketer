th st.expander("Add New Project"):
        st.text_input("Client Name"); st.date_input("Start Date"); st.button("Save")

# D. ASSET LIBRARY (Database)
elif st.session_state.menu == "Asset Library":
    st.markdown('<h1 class="header-blue">Asset Library</h1>', unsafe_allow_html=True)
    a_tab1, a_tab2, a_tab3 = st.tabs(["Media", "Copywriting", "Legal"])
    with a_tab1:
        st.table(pd.DataFrame({"File": ["Logo.png", "Promo.mp4"], "Type": ["Image", "Video"], "Platform": ["All", "TikTok"]}))
        st.file_uploader("Upload Assets")
    with a_tab2: st.write("Copywriting Templates Store")
    with a_tab3: st.write("Legal & Contract Templates")

# NEWS & CREATOR MODE
elif st.session_state.menu == "Industry News":
    st.title("Industry News")
    if st.button("Back"): st.session_state.menu = "Interactive Dashboard"
elif st.session_state.menu == "Creator Mode":
    st.title("Creator Mode")
    if st.button("Back"): st.session_state.menu = "Interactive Dashboard"
