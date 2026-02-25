import streamlit as st
import google.generativeai as genai
import re

# --- 1. CORE SETUP ---
st.set_page_config(page_title="AI Marketer Pro | Mission Control", layout="wide", page_icon="🚀")

# --- 2. THE MISSION CONTROL CSS (ADVANCED) ---
st.markdown("""
    <style>
    /* Dark Theme Base */
    .stApp { background-color: #0d1117; color: #c9d1d9; font-family: 'Inter', sans-serif; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #161b22 !important; border-right: 1px solid #30363d; }
    
    /* Modular Cards (Glassmorphism effect) */
    .module-card { 
        background: #161b22; padding: 20px; border-radius: 12px; 
        border: 1px solid #30363d; margin-bottom: 20px;
        transition: 0.3s;
    }
    .module-card:hover { border-color: #58a6ff; box-shadow: 0 0 15px rgba(88,166,255,0.1); }
    
    /* Section Labels */
    .label { font-size: 10px; font-weight: 800; color: #8b949e; text-transform: uppercase; letter-spacing: 2px; }
    .status-online { color: #3fb950; font-size: 11px; }
    
    /* Custom Tabs */
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: #21262d !important; border-radius: 8px 8px 0 0 !important; 
        padding: 10px 20px !important; color: #c9d1d9 !important;
    }
    
    /* Social Icons Placeholder Style */
    .social-bar { display: flex; gap: 15px; margin-top: 10px; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: CONTENT CREATOR PROFILE ---
with st.sidebar:
    # Creator Profile (Based on Image top-left)
    st.markdown("""
        <div style='text-align: center; padding: 10px;'>
            <img src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png' width='80' style='border-radius: 50%; border: 2px solid #58a6ff;'>
            <h3 style='margin-bottom:0;'>Aung Kyaw</h3>
            <p style='font-size: 12px; color: #8b949e;'>Content Architect</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Navigation Modules
    st.markdown('<p class="label">Navigation</p>', unsafe_allow_html=True)
    menu = st.radio("Control Panel", 
                    ["🛸 Command Center", "📊 Analytics", "📅 Schedule", "🧬 Audience"], 
                    label_visibility="collapsed")
    
    st.divider()
    st.markdown('<p class="label">System</p>', unsafe_allow_html=True)
    st.markdown("<p class='status-online'>● AI Neural Engine Active</p>", unsafe_allow_html=True)

# --- 4. MAIN INTERFACE: COMMAND CENTER ---
if menu == "🛸 Command Center":
    st.markdown("<h2 style='color:white;'>AI Command Center</h2>", unsafe_allow_html=True)
    st.caption("Central Orchestration for Multi-Channel Content")

    # TOP ROW: TREND ANALYSIS (Based on Image top-center)
    with st.container():
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        col_t1, col_t2 = st.columns([1, 2])
        with col_t1:
            st.markdown('<p class="label">Trend Analysis</p>', unsafe_allow_html=True)
            st.write("Current Hot Topics: #LuxuryJewelry, #Investing2026")
        with col_t2:
            st.progress(85, text="Market Engagement Prediction")
        st.markdown('</div>', unsafe_allow_html=True)

    # MIDDLE ROW: CORE GENERATOR & PREVIEW
    col_input, col_preview = st.columns([1, 1.5], gap="medium")

    with col_input:
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown('<p class="label">Automated Generation</p>', unsafe_allow_html=True)
        topic = st.text_input("Campaign Focus", placeholder="e.g. Diamond Collection")
        objective = st.selectbox("Goal", ["Conversion", "Awareness", "Engagement"])
        st.button("GENERATE ASSETS")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Audience Segment (Based on Image right-side)
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown('<p class="label">Target Persona</p>', unsafe_allow_html=True)
        st.multiselect("Audience Segments", ["VIP Clients", "New Millenials", "Investors"], default="VIP Clients")
        st.markdown('</div>', unsafe_allow_html=True)

    with col_preview:
        st.markdown('<div class="module-card">', unsafe_allow_html=True)
        st.markdown('<p class="label">Content Output Matrix</p>', unsafe_allow_html=True)
        
        tab1, tab2, tab3 = st.tabs(["📝 Copywriting", "🎥 Video Brief", "🎨 Visuals"])
        with tab1:
            st.info("Awaiting Generation... Results will appear here in AIDA/PAS format.")
        with tab2:
            st.info("Video Hooks and Scripts will be displayed here.")
        with tab3:
            st.info("AI Art Prompts and Color Palettes.")
        
        st.divider()
        st.markdown('<p class="label">Publishing Channels</p>', unsafe_allow_html=True)
        st.markdown("""
            <div class="social-bar">
                🔵 Facebook | 📸 Instagram | 🎵 TikTok | 📺 YouTube
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# --- 5. PLACEHOLDERS FOR OTHER PAGES ---
elif menu == "📊 Analytics":
    st.header("Performance Monitoring")
    st.image("https://via.placeholder.com/800x400/161b22/ffffff?text=Engagement+Analytics+Dashboard") # Placeholder for Image
    st.caption("Tracking Like, Share, and Feedback Loops")

elif menu == "📅 Schedule":
    st.header("Content Scheduling")
    st.info("Predicting best times to post across channels")

elif menu == "🧬 Audience":
    st.header("Content Personalization")
    st.write("Analyzing Audience Preferences")
