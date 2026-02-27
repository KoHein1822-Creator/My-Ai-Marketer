import streamlit as st
import pandas as pd
import numpy as np

def render_executive_telemetry():
    # --- AUTONOMOUS STATUS HEADER ---
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: center; background: #0d1117; border-bottom: 1px solid #30363d; padding-bottom: 15px; margin-bottom: 20px;">
            <div>
                <h1 style="font-size: 28px; color: #ffffff; margin: 0;">🛰️ Executive Telemetry</h1>
                <p style="color: #8b949e; font-size: 12px; margin: 0;">Fully Autonomous Mode: <span style="color: #3fb950;">ENGAGED</span></p>
            </div>
            <div style="text-align: right;">
                <div style="display: inline-block; width: 10px; height: 10px; background-color: #3fb950; border-radius: 50%; box-shadow: 0 0 10px #3fb950; animation: pulse 2s infinite;"></div>
                <span style="color: #3fb950; font-weight: 700; font-size: 13px; margin-left: 8px;">SYSTEMS LIVE</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # --- ROW 1: THE BOTTOM LINE (MACRO METRICS) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1.5px; text-transform:uppercase;">Business Health Overview</p>', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("AI-Generated Revenue", "4.2M MMK", "+18.5%")
    m2.metric("Net Audience Growth", "12.4K", "+2.1K")
    m3.metric("Global Sentiment", "92% Positive", "+4%")
    m4.metric("Active AI Campaigns", "8", "Running smoothly")

    st.write("")

    # --- ROW 2: AUTONOMOUS NEURAL NETWORK (LIVE FEED) ---
    feed_col, chart_col = st.columns([1.2, 1])

    with feed_col:
        st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1.5px; text-transform:uppercase;">Live Autonomous Actions (Agent Feed)</p>', unsafe_allow_html=True)
        # Terminal-style Live Feed Box
        st.markdown("""
            <div style="background: #010409; border: 1px solid #30363d; padding: 15px; border-radius: 8px; height: 250px; overflow-y: hidden; font-family: monospace; font-size: 12px;">
                <p style="color: #8b949e; margin: 5px 0;">[10:42 AM] <span style="color: #58a6ff;">[Data Agent]</span> Detected 15% drop in Facebook Reach.</p>
                <p style="color: #8b949e; margin: 5px 0;">[10:43 AM] <span style="color: #58a6ff;">[Data Agent]</span> Identifying cause: Outdated creative assets.</p>
                <p style="color: #e1e4e8; margin: 5px 0;">[10:43 AM] <span style="color: #a371f7;">[Data Agent -> Content Agent]</span> Brief sent: Requesting 3 new engaging Reels.</p>
                <p style="color: #8b949e; margin: 5px 0;">[10:50 AM] <span style="color: #3fb950;">[Content Agent]</span> Generation complete. A/B testing variations.</p>
                <p style="color: #8b949e; margin: 5px 0;">[11:05 AM] <span style="color: #d29922;">[Ads Agent]</span> Reallocating $20 budget to winning variation.</p>
                <div style="border-top: 1px dashed #30363d; margin: 10px 0; padding-top: 10px;">
                    <span style="color: #3fb950;">> AI Network is optimizing continuously...</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

    with chart_col:
        st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1.5px; text-transform:uppercase;">Engagement Velocity</p>', unsafe_allow_html=True)
        # Area chart showing "Live Flow" of engagement
        chart_data = pd.DataFrame(
            np.random.randn(20, 2) * 10 + [50, 40],
            columns=["Organic Traffic", "AI-Driven Traffic"]
        )
        st.area_chart(chart_data, color=["#3fb950", "#58a6ff"], height=250)

    st.write("")

    # --- ROW 3: CRITICAL RADAR (OPPORTUNITIES & THREATS) ---
    st.markdown('<p style="font-size:11px; font-weight:700; color:#58a6ff; letter-spacing:1.5px; text-transform:uppercase;">Intelligence Radar</p>', unsafe_allow_html=True)
    r1, r2 = st.columns(2)
    
    with r1:
        st.markdown("""
            <div style="border-left: 4px solid #3fb950; background: rgba(63, 185, 80, 0.05); padding: 15px; border-radius: 4px;">
                <h4 style="color: #3fb950; margin-top: 0; font-size: 14px;">🎯 High Opportunity Detected</h4>
                <p style="color: #c9d1d9; font-size: 12px; margin-bottom: 0;">Competitor "Brand X" is receiving negative reviews on customer service. <b>AI Content Agent</b> has automatically scheduled a post highlighting our 24/7 support.</p>
            </div>
        """, unsafe_allow_html=True)

    with r2:
        st.markdown("""
            <div style="border-left: 4px solid #d29922; background: rgba(210, 153, 34, 0.05); padding: 15px; border-radius: 4px;">
                <h4 style="color: #d29922; margin-top: 0; font-size: 14px;">⚠️ Algorithm Shift Alert</h4>
                <p style="color: #c9d1d9; font-size: 12px; margin-bottom: 0;">TikTok algorithm is currently favoring 15-second videos over 60-second ones. <b>AI Content Agent</b> is adjusting video lengths for tomorrow's batch.</p>
            </div>
        """, unsafe_allow_html=True)

# To Test in Streamlit
if __name__ == "__main__":
    render_executive_telemetry()
