import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime
import math

# --- ၁။ Configuration & Styling ---
st.set_page_config(page_title="AI Command Center", layout="wide", initial_sidebar_state="expanded")

# UI Colors (React C constants)
C = {
    "fb": "#6366f1", "tt": "#ec4899", "yt": "#ef4444",
    "green": "#10b981", "amber": "#f59e0b", "blue": "#3b82f6", 
    "purple": "#8b5cf6", "teal": "#14b8a6",
    "bg": "#030712", "card": "#111827", "border": "#1f2937",
    "muted": "#6b7280", "dim": "#4b5563", "text": "#e5e7eb", "head": "#f9fafb"
}

# CSS for styling
st.markdown(f"""
    <style>
    .main {{ background-color: {C['bg']}; color: {C['text']}; }}
    [data-testid="stMetricValue"] {{ color: {C['head']}; font-weight: 800; }}
    .status-card {{
        background-color: {C['card']};
        border: 1px solid {C['border']};
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
    }}
    .news-card {{
        background-color: {C['card']};
        padding: 10px;
        border-radius: 8px;
        border-left: 4px solid {C['fb']};
        margin-bottom: 8px;
    }}
    </style>
""", unsafe_allow_html=True)

# --- ၂။ Data Generation Logic (Python Version) ---
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

def mk_data(min_val, max_val):
    return {
        "Weekly": {"cur": gen_s(min_val, max_val, WK), "prev": gen_s(min_val*0.8, max_val*0.8, WK, 3)},
        "Monthly": {"cur": gen_s(min_val*4, max_val*4, MO),
