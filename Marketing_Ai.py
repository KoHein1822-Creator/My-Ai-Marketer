# UI Visualization conceptually:
col_team1, col_team2, col_team3 = st.columns(3)

with col_team1:
    st.markdown("👤 **Intel Strategist**")
    st.caption("Market Analysis & Strategy")
    st.progress(100) # Researching...

with col_team2:
    st.markdown("🎨 **Creative Architect**")
    st.caption("Content Production (Junior)")
    st.progress(40) # Drafting Content...

with col_team3:
    st.markdown("⚖️ **Executive Auditor**")
    st.caption("Final QA (Senior)")
    st.progress(0) # Waiting for Draft...
