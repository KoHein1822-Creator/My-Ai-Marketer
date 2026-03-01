":
        render_dashboard()
    elif st.session_state.page == "Intelligence":
        st.markdown('<h1 style="font-weight:900; margin:0; font-size:38px;">Sayar Gyi\'s Intelligence</h1>', unsafe_allow_html=True)
        st.divider()
        st.info("Ready for Deep Insights & Weekly Reports Integration...")
    else:
        # အခြား Menu များ (Brand DNA, Project Archive, etc.)
        st.markdown(f'<h1 style="font-weight:900; margin:0; font-size:38px;">{st.session_state.page}</h1>', unsafe_allow_html=True)
        st.write("")
        st.info(f"{st.session_state.page} Module syncing...")
