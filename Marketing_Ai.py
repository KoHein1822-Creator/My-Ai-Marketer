import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import math

# --- 1. CONFIGURATION ---
st.set_page_config(page_title="AI Command Center", layout="wide")

# Colors
C = {
    "fb": "#6366f1", "tt": "#ec4899", "yt": "#ef4444",
    "green": "#10b981", "amber": "#f59e0b", "blue": "#3b82f6", 
    "purple": "#8b5cf6", "teal": "#14b8a6",
    "bg": "#030712", "card": "#111827", "border": "#1f2937",
    "muted": "#6b7280", "dim": "#4b5563", "text": "#e5e7eb", "head": "#f9fafb"
}

# --- 2. DATA ENGINE (Phase 3 Logic) ---
WK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MO = ["W1", "W2", "W3", "W4"]
YR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def gen_s(min_val, max_val, labels, off=0):
    data = []
    for i, name in enumerate(labels):
        val = max(min_val, round(min_val + (max_val - min_val) * 0.4 + 
              math.sin((i + off) * 0.9) * ((max_val - min_val) * 0.28) + 
              np.random.random() * (max_val - min_val) * 0.24))
        data.append({"name": name, "value": val})
    return pd.DataFrame(data)

# စောစောက Error တက်ခဲ့တဲ့ အပိုင်းကို သေချာပြန်ပြင်ထားပါတယ်
def mk_data(min_val, max_val):
    return {
        "Weekly": {
            "cur": gen_s(min_val, max_val, WK), 
            "prev": gen_s(min_val*0.8, max_val*0.8, WK, 3)
        },
        "Monthly": {
            "cur": gen_s(min_val*4, max_val*4, MO), 
            "prev": gen_s(min_val*3.5, max_val*3.5, MO, 2)
        },
        "Yearly": {
            "cur": gen_s(min_val*50, max_val*50, YR), 
            "prev": gen_s(min_val*40, max_val*40, YR, 4)
        }
    }

# --- 3. MOCK DATABASE (Phase 3: Integration) ---
PLATFORMS = {
    "Facebook": {"color": C["fb"], "metrics": [
        {"key": "reach", "label": "Reach", "data": mk_data(18000, 95000)},
        {"key": "impr", "label": "Impressions", "data": mk_data(50000, 250000)}
    ]},
    "TikTok": {"color": C["tt"], "metrics": [
        {"key": "views", "label": "Video Views", "data": mk_data(80000, 400000)},
        {"key": "likes", "label": "Likes", "data": mk_data(8000, 80000)}
    ]},
    "YouTube": {"color": C["yt"], "metrics": [
        {"key": "views", "label": "Views", "data": mk_data(20000, 150000)},
        {"key": "watch", "label": "Watch Time (hrs)", "data": mk_data(800, 9000)}
    ]}
}

NEWS_DATA = {
    "Global News": [
        {"tag": "AI", "time": "2h ago", "title": "OpenAI launches GPT-5 with real-time video understanding", "src": "TechCrunch"},
        {"tag": "Marketing", "time": "4h ago", "title": "Meta rolls out AI-generated ad creatives", "src": "AdWeek"}
    ],
    "Myanmar News": [
        {"tag": "Local", "time": "1h ago", "title": "Facebook remains #1 marketing channel in Myanmar", "src": "MMDigital"},
        {"tag": "Trend", "time": "3h ago", "title": "Short-form video ads see 3x higher CTR", "src": "SEA Report"}
    ]
}

# --- 4. UI COMPONENTS ---
def draw_chart(df_cur, df_prev, color):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df_prev['name'], y=df_prev['value'], name='Prev', line=dict(color=C['dim'], width=1, dash='dot')))
    fig.add_trace(go.Scatter(x=df_cur['name'], y=df_cur['value'], name='Cur', line=dict(color=color, width=3), fill='tozeroy'))
    fig.update_layout(margin=dict(l=0,r=0,t=0,b=0), height=120, showlegend=False, 
                      paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                      xaxis=dict(visible=False), yaxis=dict(visible=False))
    return fig

# --- 5. MAIN APP ---
st.title("🚀 AI Command Center")

tab_dash, tab_news = st.tabs(["📊 Dashboard", "📡 Intelligence Hub"])

with tab_dash:
    p_select = st.selectbox("Select Platform", list(PLATFORMS.keys()))
    tf_select = st.radio("Timeframe", ["Weekly", "Monthly", "Yearly"], horizontal=True)
    
    m_cols = st.columns(2)
    metrics = PLATFORMS[p_select]["metrics"]
    
    for idx, m in enumerate(metrics):
        with m_cols[idx % 2]:
            d_cur = m["data"][tf_select]["cur"]
            d_prev = m["data"][tf_select]["prev"]
            cur_val = d_cur['value'].sum()
            
            st.markdown(f"""
                <div style="background:{C['card']
