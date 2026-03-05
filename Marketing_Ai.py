"""
╔══════════════════════════════════════════════════════════════╗
║     Sayar Gyi's AI Command Center — Python / Streamlit       ║
║     pip install streamlit plotly anthropic                   ║
║     streamlit run app.py                                     ║
╚══════════════════════════════════════════════════════════════╝
"""

import streamlit as st
import plotly.graph_objects as go
import math
import json
import random
from anthropic import Anthropic

# ─────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────

C_FB     = "#6366f1"
C_TT     = "#ec4899"
C_YT     = "#ef4444"
C_GREEN  = "#10b981"
C_AMBER  = "#f59e0b"
C_BLUE   = "#3b82f6"
C_PURPLE = "#8b5cf6"
C_TEAL   = "#14b8a6"

CLIENTS = [
    "All Clients", "Real Estate Co.", "Fashion Brand",
    "Restaurant Chain", "Tech Startup", "Beauty Studio",
]

WK = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
MO = ["W1", "W2", "W3", "W4"]
YR = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ─────────────────────────────────────────────────────────────────
# DATA HELPERS
# ─────────────────────────────────────────────────────────────────

def gen_series(key, mn, mx, labels, off=0):
    result = []
    for i, name in enumerate(labels):
        val = (mn + (mx - mn) * 0.4
               + math.sin((i + off) * 0.9) * ((mx - mn) * 0.28)
               + random.uniform(0, (mx - mn) * 0.24))
        result.append({"name": name, key: max(mn, round(val))})
    return result


def mk_data(key, mn, mx):
    return {
        "Weekly":  {"cur": gen_series(key, mn, mx, WK, 0),
                    "prev": gen_series(key, round(mn*.78), round(mx*.84), WK, 3)},
        "Monthly": {"cur": gen_series(key, mn*4, mx*4, MO, 0),
                    "prev": gen_series(key, round(mn*3.1), round(mx*3.4), MO, 2)},
        "Yearly":  {"cur": gen_series(key, mn*50, mx*50, YR, 0),
                    "prev": gen_series(key, round(mn*40), round(mx*43), YR, 4)},
        "Custom":  {"cur": gen_series(key, mn*3, mx*3, MO, 1),
                    "prev": gen_series(key, round(mn*2.5), round(mx*2.7), MO, 3)},
    }


def sum_s(arr, key):
    return sum(r.get(key, 0) for r in arr)


def fmt(n):
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(round(n))

# ─────────────────────────────────────────────────────────────────
# PLATFORM DEFINITIONS
# ─────────────────────────────────────────────────────────────────

PLATFORMS = {
    "Facebook": {
        "color": C_FB,
        "metrics": [
            [
                {"key": "reach",    "label": "Reach",            "prefix": "",  "suffix": "",  "color": C_FB,     "data": mk_data("reach",    18_000,  95_000)},
                {"key": "impr",     "label": "Impressions",      "prefix": "",  "suffix": "",  "color": C_PURPLE, "data": mk_data("impr",     50_000, 250_000)},
            ],
            [
                {"key": "engRate",  "label": "Engagement Rate",  "prefix": "",  "suffix": "%", "color": C_TEAL,   "data": mk_data("engRate",      3,      12)},
                {"key": "clicks",   "label": "Post Clicks",      "prefix": "",  "suffix": "",  "color": C_BLUE,   "data": mk_data("clicks",    2_000,  14_000)},
            ],
            [
                {"key": "vidViews", "label": "Video Views",      "prefix": "",  "suffix": "",  "color": C_GREEN,  "data": mk_data("vidViews", 40_000, 200_000)},
                {"key": "follows",  "label": "Page Follows",     "prefix": "",  "suffix": "",  "color": C_AMBER,  "data": mk_data("follows",      80,     600)},
            ],
        ],
    },
    "TikTok": {
        "color": C_TT,
        "metrics": [
            [
                {"key": "views",    "label": "Video Views",      "prefix": "",  "suffix": "",  "color": C_TT,     "data": mk_data("views",    80_000, 400_000)},
                {"key": "profile",  "label": "Profile Visits",   "prefix": "",  "suffix": "",  "color": C_PURPLE, "data": mk_data("profile",   4_000,  40_000)},
            ],
            [
                {"key": "likes",    "label": "Likes",            "prefix": "",  "suffix": "",  "color": "#f472b6","data": mk_data("likes",     8_000,  80_000)},
                {"key": "shares",   "label": "Shares",           "prefix": "",  "suffix": "",  "color": C_BLUE,   "data": mk_data("shares",    2_000,  20_000)},
            ],
            [
                {"key": "follows",  "label": "Followers Gained", "prefix": "",  "suffix": "",  "color": C_GREEN,  "data": mk_data("follows",     400,   3_000)},
                {"key": "watch",    "label": "Watch Time (hrs)", "prefix": "",  "suffix": "",  "color": C_TEAL,   "data": mk_data("watch",     2_000,  20_000)},
            ],
        ],
    },
    "YouTube": {
        "color": C_YT,
        "metrics": [
            [
                {"key": "views",    "label": "Views",            "prefix": "",  "suffix": "",  "color": C_YT,     "data": mk_data("views",    20_000, 150_000)},
                {"key": "impr",     "label": "Impressions",      "prefix": "",  "suffix": "",  "color": C_PURPLE, "data": mk_data("impr",     60_000, 500_000)},
            ],
            [
                {"key": "watch",    "label": "Watch Time (hrs)", "prefix": "",  "suffix": "",  "color": C_AMBER,  "data": mk_data("watch",       800,   9_000)},
                {"key": "ctr",      "label": "CTR",              "prefix": "",  "suffix": "%", "color": C_BLUE,   "data": mk_data("ctr",           2,       8)},
            ],
            [
                {"key": "subs",     "label": "Subscribers",      "prefix": "+", "suffix": "",  "color": C_GREEN,  "data": mk_data("subs",         60,     600)},
                {"key": "revenue",  "label": "Est. Revenue",     "prefix": "$", "suffix": "",  "color": C_TEAL,   "data": mk_data("revenue",      40,     400)},
            ],
        ],
    },
}

# ─────────────────────────────────────────────────────────────────
# STATUS DATA
# ─────────────────────────────────────────────────────────────────

def mk_status(p, d, s, pub):
    return {
        "Pending":   {"count": p,   "items": [f"Content item #{i+1}" for i in range(p)]},
        "Drafting":  {"count": d,   "items": [f"Draft #{i+1}"        for i in range(d)]},
        "Scheduled": {"count": s,   "items": [f"Scheduled #{i+1}"    for i in range(s)]},
        "Published": {"count": pub, "items": [f"Published #{i+1}"    for i in range(pub)]},
    }

STATUS_DATA = {
    "All Clients":     {"Facebook": mk_status(8,5,6,19), "TikTok": mk_status(5,3,4,12), "YouTube": mk_status(3,2,3,8),  "All": mk_status(16,10,13,39)},
    "Real Estate Co.": {"Facebook": mk_status(3,2,2,7),  "TikTok": mk_status(1,1,1,3),  "YouTube": mk_status(1,0,1,2),  "All": mk_status(5,3,4,12)},
    "Fashion Brand":   {"Facebook": mk_status(2,1,2,5),  "TikTok": mk_status(2,1,2,5),  "YouTube": mk_status(0,1,1,3),  "All": mk_status(4,3,5,13)},
    "Restaurant Chain":{"Facebook": mk_status(1,1,1,4),  "TikTok": mk_status(1,0,1,2),  "YouTube": mk_status(0,0,0,1),  "All": mk_status(2,1,2,7)},
    "Tech Startup":    {"Facebook": mk_status(1,0,1,2),  "TikTok": mk_status(1,1,0,1),  "YouTube": mk_status(1,1,1,2),  "All": mk_status(3,2,2,5)},
    "Beauty Studio":   {"Facebook": mk_status(1,1,0,1),  "TikTok": mk_status(0,0,0,1),  "YouTube": mk_status(1,0,0,0),  "All": mk_status(2,1,0,2)},
}

STATUS_META = [
    {"key": "Pending",   "color": C_AMBER, "icon": "⏳"},
    {"key": "Drafting",  "color": C_FB,    "icon": "✍️"},
    {"key": "Scheduled", "color": C_BLUE,  "icon": "📅"},
    {"key": "Published", "color": C_GREEN, "icon": "✅"},
]

# ─────────────────────────────────────────────────────────────────
# NEWS DATA
# ─────────────────────────────────────────────────────────────────

TAG_C = {
    "AI": "#6366f1", "Marketing": "#f59e0b", "TikTok": "#ec4899",
    "YouTube": "#ef4444", "Myanmar": "#10b981", "Trend": "#3b82f6",
    "Analysis": "#8b5cf6", "Report": "#14b8a6",
}

NEWS = {
    "Global News": [
        {"tag": "AI",        "time": "2h ago", "title": "OpenAI launches GPT-5 with real-time video understanding",           "src": "TechCrunch"},
        {"tag": "Marketing", "time": "4h ago", "title": "Meta rolls out AI-generated ad creatives to all advertisers",        "src": "AdWeek"},
        {"tag": "TikTok",    "time": "6h ago", "title": "TikTok Shop surpasses $1B in weekly GMV globally",                   "src": "Bloomberg"},
        {"tag": "YouTube",   "time": "8h ago", "title": "YouTube Shorts monetization expands to 100+ countries",              "src": "YouTube Blog"},
    ],
    "Local News": [
        {"tag": "Myanmar",   "time": "1h ago", "title": "Facebook remains #1 digital marketing channel in Myanmar",           "src": "MMDigital"},
        {"tag": "Trend",     "time": "3h ago", "title": "Short-form video ads see 3x higher CTR in SEA markets",              "src": "SEA Report"},
        {"tag": "Myanmar",   "time": "5h ago", "title": "Mobile-first content drives 78% of brand discovery locally",        "src": "LocalInsight"},
    ],
    "Deep Insight": [
        {"tag": "Analysis",  "time": "Today",     "title": "Why Faceless content is outperforming branded content in 2025",  "src": "Strategy Weekly"},
        {"tag": "Trend",     "time": "Yesterday", "title": "The rise of AI agents in performance marketing workflows",         "src": "MarTech Report"},
    ],
    "Weekly Report": [
        {"tag": "Report",    "time": "This Week", "title": "Top 10 viral content formats — Week 9, 2026",                    "src": "AI Command Center"},
        {"tag": "Report",    "time": "This Week", "title": "Myanmar market trend summary: Feb 23 – Mar 1",                   "src": "AI Command Center"},
    ],
}

# ─────────────────────────────────────────────────────────────────
# BRAND DNA DATA
# ─────────────────────────────────────────────────────────────────

EMPTY_BRAND = {
    "name": "", "industry": "", "audience": "", "usp": "", "mission": "", "promise": "",
    "tagline": "", "elevator": "", "tone": "", "archetype": "",
    "fbTone": "", "tiktokTone": "", "ytTone": "",
    "dos": "", "donts": "", "pillars": ["", "", ""],
    "painPoints": "", "topicIdeas": "", "logoDesc": "", "moodboard": "",
    "colors": ["#6366f1", "#ec4899", "#10b981", "#f59e0b"],
    "font": "Modern Sans", "competitors": [],
}

SAMPLE_BRANDS = {
    "Real Estate Co.": {
        "name": "Real Estate Co.", "industry": "Real Estate & Property",
        "audience": "Home buyers 28-50, urban professionals in Yangon",
        "usp": "Trusted property solutions with AI-powered market insights",
        "mission": "Helping families find their dream home with confidence",
        "promise": "Full transparency in every property transaction — guaranteed",
        "tagline": "Your Trusted Home, Our Trusted Guidance",
        "elevator": "We help Yangon families find verified properties with zero stress using AI-powered matching and transparent pricing.",
        "tone": "Professional", "archetype": "Sage",
        "fbTone": "Informative and data-driven with market highlights",
        "tiktokTone": "Short property tour clips with surprising price reveals",
        "ytTone": "In-depth area guides and investment explainers",
        "dos": "Use data, cite sources, share client testimonials, stay formal",
        "donts": "No slang, no unverified claims, no emotional oversell",
        "pillars": ["Market Insights & Trends", "Property Investment Tips", "Client Success Stories"],
        "painPoints": "Buyers fear fraud, unclear pricing, and finding trustworthy agents",
        "topicIdeas": "Property price comparisons, neighborhood guides, buyer mistake series, investment ROI breakdowns",
        "logoDesc": "Clean geometric house icon with modern sans-serif wordmark in navy blue",
        "moodboard": "trustworthy, modern, clean, premium, urban",
        "colors": ["#1e40af", "#0ea5e9", "#f8fafc", "#1e293b"],
        "font": "Modern Sans",
        "competitors": [{"name": "Property Guru", "note": "Strong SEO, weak social"}, {"name": "iProperty", "note": "Good listings, no content strategy"}],
    },
    "Fashion Brand": {
        "name": "Fashion Brand", "industry": "Fashion & Lifestyle",
        "audience": "Trendy women 18-35, style-conscious millennials Myanmar",
        "usp": "Affordable luxury streetwear celebrating SEA identity",
        "mission": "Making fashion a form of self-expression for every woman",
        "promise": "You'll always turn heads — or your money back",
        "tagline": "Wear Bold. Be You.",
        "elevator": "Fashion Brand makes premium streetwear affordable for Myanmar's bold generation — where your outfit tells your story.",
        "tone": "Trendy", "archetype": "Creator",
        "fbTone": "Aspirational lifestyle posts with strong visual hooks",
        "tiktokTone": "Viral try-on hauls, GRWM, trending sounds",
        "ytTone": "Mini fashion documentaries and style transformation videos",
        "dos": "Use vivid visuals, trending audio, bold CTAs, influencer collabs",
        "donts": "No boring flat lays, no formal language, no outdated aesthetics",
        "pillars": ["New Arrivals & Lookbooks", "Style Tips & Outfit Ideas", "Behind the Brand Stories"],
        "painPoints": "Can't afford luxury brands, local fashion feels outdated, no style identity",
        "topicIdeas": "Get the look for less, Myanmar street style features, behind-the-design stories, seasonal trend forecasts",
        "logoDesc": "Abstract letter mark with bold italic font, hot pink gradient",
        "moodboard": "bold, edgy, colorful, rebellious, youthful, maximalist",
        "colors": ["#ec4899", "#f472b6", "#fdf2f8", "#1a1a2e"],
        "font": "Display Serif",
        "competitors": [{"name": "Pomelo Fashion", "note": "Strong IG, high price point"}, {"name": "Zara SEA", "note": "Big brand, no local relevance"}],
    },
    "Restaurant Chain": {
        "name": "Restaurant Chain", "industry": "F&B / Restaurant",
        "audience": "Food lovers 22-45, families & couples in Myanmar",
        "usp": "Authentic Myanmar flavors reimagined for modern dining",
        "mission": "Bringing communities together through the joy of shared meals",
        "promise": "Every visit feels like dining at grandma's — with a modern twist",
        "tagline": "Where Every Meal Tells a Story",
        "elevator": "We serve Myanmar's favorite flavors in a warm, modern setting that makes every meal feel like a family reunion.",
        "tone": "Friendly", "archetype": "Everyman",
        "fbTone": "Warm, storytelling-driven, feature customer moments",
        "tiktokTone": "Food reveal videos, chef's secret recipes, ASMR cooking",
        "ytTone": "Full recipe tutorials and restaurant tour vlogs",
        "dos": "Show real food, feature staff, use warm colors, share recipes",
        "donts": "No corporate language, no stock photos, no empty promises",
        "pillars": ["Food Stories & Heritage", "New Menu Highlights", "Customer Moments & UGC"],
        "painPoints": "Missing authentic taste in modern restaurants, overpriced foreign food",
        "topicIdeas": "Dish origin stories, chef behind the scenes, customer 'first bite' reactions, recipe reveals",
        "logoDesc": "Friendly bowl icon with hand-lettered script font in warm amber",
        "moodboard": "warm, homey, authentic, appetizing, community-driven",
        "colors": ["#d97706", "#fbbf24", "#fff7ed", "#1c1917"],
        "font": "Rounded",
        "competitors": [{"name": "Local Chains", "note": "Traditional menu, zero digital presence"}, {"name": "KFC Myanmar", "note": "Strong brand but not authentic"}],
    },
    "Tech Startup": {
        "name": "Tech Startup", "industry": "Technology / SaaS",
        "audience": "SME owners 25-45, entrepreneurs Myanmar & SEA",
        "usp": "AI-powered business tools that save 10+ hours per week",
        "mission": "Democratizing powerful technology for every business owner",
        "promise": "Save time in 30 days or full refund",
        "tagline": "Work Smarter. Grow Faster.",
        "elevator": "We build simple AI tools that give Myanmar SMEs the same edge as Fortune 500 companies — at a fraction of the cost.",
        "tone": "Authoritative", "archetype": "Magician",
        "fbTone": "Educational with clear ROI stats and before/after results",
        "tiktokTone": "30-second productivity hacks and tool demos",
        "ytTone": "Deep-dive tutorials and founder story documentaries",
        "dos": "Lead with ROI data, use case studies, explain simply",
        "donts": "No heavy jargon, no vague promises, no feature-dumping",
        "pillars": ["Productivity & Automation Tips", "Customer Case Studies", "Industry AI Trends"],
        "painPoints": "SMEs waste hours on manual tasks, can't afford enterprise software",
        "topicIdeas": "AI tool demos, time-saved testimonials, small business automation tips, ROI calculators",
        "logoDesc": "Abstract circuit/brain hybrid icon with bold modern sans-serif in electric indigo",
        "moodboard": "cutting-edge, clean, intelligent, minimal, futuristic",
        "colors": ["#6366f1", "#8b5cf6", "#f5f3ff", "#0f172a"],
        "font": "Modern Sans",
        "competitors": [{"name": "Local Dev Agencies", "note": "Slow, expensive, no AI"}, {"name": "Freelancers", "note": "Cheap but inconsistent"}],
    },
    "Beauty Studio": {
        "name": "Beauty Studio", "industry": "Beauty & Wellness",
        "audience": "Women 20-40, beauty enthusiasts Myanmar",
        "usp": "Personalized treatments with premium Korean skincare",
        "mission": "Enhancing every woman's natural beauty with science and care",
        "promise": "You'll leave glowing — or your next treatment is free",
        "tagline": "Your Glow, Perfected.",
        "elevator": "We combine Korean beauty science with personalized care to give every Myanmar woman the skin she deserves.",
        "tone": "Elegant", "archetype": "Lover",
        "fbTone": "Educational skincare tips with elegant visuals and gentle CTAs",
        "tiktokTone": "Satisfying treatment videos, product reviews, glow-up reveals",
        "ytTone": "Full skincare routine guides and ingredient deep-dives",
        "dos": "Show real results, soft aesthetics, educate on ingredients",
        "donts": "No harsh lighting, no fake before/afters, no aggressive sales",
        "pillars": ["Skincare Education & Tips", "Before & After Transformations", "Product Spotlights"],
        "painPoints": "Generic treatments that don't suit Asian skin, overpriced imports",
        "topicIdeas": "Ingredient explainers, skin type quizzes, seasonal skincare routines, client transformation stories",
        "logoDesc": "Delicate floral monogram with thin serif font in blush and deep rose",
        "moodboard": "feminine, luxurious, soft, glowing, serene, premium, pastel",
        "colors": ["#f9a8d4", "#fbcfe8", "#fdf2f8", "#4a0e2e"],
        "font": "Display Serif",
        "competitors": [{"name": "Local Salons", "note": "No branding, no content strategy"}, {"name": "Beauty chains", "note": "Standardized, not personalized"}],
    },
}

TONE_OPTIONS = [
    {"key": "Professional",  "desc": "Trustworthy, formal, expert",     "icon": "💼"},
    {"key": "Friendly",      "desc": "Warm, approachable, casual",      "icon": "😊"},
    {"key": "Trendy",        "desc": "Bold, modern, youth-focused",     "icon": "🔥"},
    {"key": "Authoritative", "desc": "Confident, data-driven, leader",  "icon": "📊"},
    {"key": "Elegant",       "desc": "Refined, premium, sophisticated", "icon": "✨"},
    {"key": "Playful",       "desc": "Fun, creative, energetic",        "icon": "🎨"},
]

ARCHETYPE_OPTIONS = [
    "Hero", "Creator", "Sage", "Jester", "Caregiver", "Explorer",
    "Ruler", "Lover", "Innocent", "Everyman", "Outlaw", "Magician",
]

# ═════════════════════════════════════════════════════════════════
# CHART HELPER
# ═════════════════════════════════════════════════════════════════

def make_chart(cur_data, prev_data, data_key, color, chart_type="Area", compare=False):
    names     = [r["name"]            for r in cur_data]
    cur_vals  = [r.get(data_key, 0)   for r in cur_data]
    prev_vals = [r.get(data_key, 0)   for r in prev_data]
    prev_col  = color + "88"          # semi-transparent

    fig = go.Figure()
    layout = dict(
        height=90,
        margin=dict(l=0, r=0, t=4, b=0),
        plot_bgcolor="#111827",
        paper_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False),
    )

    if chart_type == "Bar":
        if compare:
            fig.add_trace(go.Bar(x=names, y=prev_vals, name="Prev",    marker_color=prev_col, opacity=0.5))
        fig.add_trace(    go.Bar(x=names, y=cur_vals,  name="Current", marker_color=color,    opacity=0.85))

    elif chart_type == "Line":
        if compare:
            fig.add_trace(go.Scatter(x=names, y=prev_vals, name="Prev",
                                     line=dict(color=prev_col, width=1.2, dash="dash"), mode="lines"))
        fig.add_trace(go.Scatter(x=names, y=cur_vals, name="Current",
                                 line=dict(color=color, width=2), mode="lines"))

    else:  # Area
        if compare:
            fig.add_trace(go.Scatter(x=names, y=prev_vals, name="Prev",
                                     fill="tozeroy", fillcolor=prev_col+"44",
                                     line=dict(color=prev_col, width=1.2, dash="dash"), mode="lines"))
        fig.add_trace(go.Scatter(x=names, y=cur_vals, name="Current",
                                 fill="tozeroy", fillcolor=color + "44",
                                 line=dict(color=color, width=2), mode="lines"))

    fig.update_layout(**layout)
    return fig

# ═════════════════════════════════════════════════════════════════
# PAGE: DASHBOARD
# ═════════════════════════════════════════════════════════════════

def dashboard_page():
    client = st.session_state.get("client", "All Clients")

    # ── Status Section ────────────────────────────────────────────
    st.markdown("### ✍️ Content Creation Status")
    st.caption("Click any card to expand items")

    col_ctrl1, col_ctrl2 = st.columns([3, 1])
    with col_ctrl1:
        s_plat = st.radio(
            "Filter Platform", ["All", "Facebook", "TikTok", "YouTube"],
            horizontal=True, key="s_plat", label_visibility="collapsed"
        )
    with col_ctrl2:
        s_tf = st.selectbox(
            "Timeframe", ["Weekly", "Monthly", "Yearly", "Custom"],
            key="s_tf", label_visibility="collapsed"
        )

    if s_tf == "Custom":
        c1, c2 = st.columns(2)
        with c1: st.date_input("From", key="s_from")
        with c2: st.date_input("To",   key="s_to")

    client_data = STATUS_DATA.get(client, STATUS_DATA["All Clients"])
    status_src  = client_data.get(s_plat if s_plat != "All" else "All",
                                  client_data["All"])

    cols = st.columns(4)
    for i, meta in enumerate(STATUS_META):
        d = status_src.get(meta["key"], {"count": 0, "items": []})
        with cols[i]:
            st.metric(label=f"{meta['icon']} {meta['key']}", value=d["count"])
            with st.expander("Items"):
                for item in d["items"]:
                    st.markdown(f"• {item}")

    # Workflow summary bar
    flow = " → ".join(
        f"**{m['icon']} {m['key']}** `{status_src.get(m['key'],{}).get('count',0)}`"
        for m in STATUS_META
    )
    st.markdown(flow)
    st.divider()

    # ── Platform Performance ──────────────────────────────────────
    st.markdown("### 📈 Platform Performance")

    pc1, pc2, pc3, pc4 = st.columns(4)
    with pc1:
        platform = st.selectbox("Platform", ["Facebook", "TikTok", "YouTube"], key="perf_plat")
    with pc2:
        tf = st.selectbox("Timeframe", ["Weekly", "Monthly", "Yearly", "Custom"], key="perf_tf")
    with pc3:
        chart_type = st.selectbox("Chart Type", ["Area", "Line", "Bar"], key="chart_type")
    with pc4:
        compare = st.checkbox("⇄ Compare Period", key="compare")

    if tf == "Custom":
        cc1, cc2 = st.columns(2)
        with cc1: st.date_input("From", key="p_from")
        with cc2: st.date_input("To",   key="p_to")

    if compare:
        tf_label = {"Weekly": "vs Last Week", "Monthly": "vs Last Month",
                    "Yearly": "vs Last Year", "Custom": "vs Previous Period"}
        st.info(f"⇄ {tf_label.get(tf, '')}")

    plat_data = PLATFORMS[platform]

    for row in plat_data["metrics"]:
        left, right = st.columns(2)
        for col_obj, m in zip([left, right], row):
            with col_obj:
                d    = m["data"].get(tf, m["data"]["Weekly"])
                cur  = sum_s(d["cur"],  m["key"])
                prev = sum_s(d["prev"], m["key"])
                diff = cur - prev
                pct  = (diff / prev * 100) if prev > 0 else 0
                fv   = lambda v, pfx=m["prefix"], sfx=m["suffix"]: pfx + fmt(v) + sfx

                st.metric(
                    label=m["label"],
                    value=fv(cur),
                    delta=f"{pct:+.1f}%",
                )
                if compare:
                    c1, c2, c3 = st.columns(3)
                    c1.metric("This",  fv(cur),              label_visibility="collapsed")
                    c2.metric("Prev",  fv(prev),             label_visibility="collapsed")
                    c3.metric("Diff",  f"{'+' if diff>=0 else ''}{fmt(abs(diff))}", label_visibility="collapsed")

                fig = make_chart(d["cur"], d["prev"], m["key"], m["color"], chart_type, compare)
                st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})

# ═════════════════════════════════════════════════════════════════
# PAGE: NEWS
# ═════════════════════════════════════════════════════════════════

def news_page():
    st.markdown("## 📡 Industry News & Trend Analysis")
    st.caption("Real-time AI & Marketing intelligence.")

    tabs = st.tabs(["🌐 Global News", "🇲🇲 Local News", "🔬 Deep Insight", "📋 Weekly Report"])
    tab_keys = ["Global News", "Local News", "Deep Insight", "Weekly Report"]

    for tab, key in zip(tabs, tab_keys):
        with tab:
            for item in NEWS.get(key, []):
                with st.container():
                    c1, c2 = st.columns([5, 1])
                    with c1:
                        tag_color = TAG_C.get(item["tag"], "#6b7280")
                        st.markdown(
                            f'<span style="background:{tag_color}22;color:{tag_color};'
                            f'padding:2px 9px;border-radius:99px;font-size:11px;font-weight:700">'
                            f'{item["tag"]}</span>',
                            unsafe_allow_html=True,
                        )
                        st.markdown(f"**{item['title']}**")
                        st.caption(f"Source: {item['src']}")
                    with c2:
                        st.caption(item["time"])
                st.divider()

# ═════════════════════════════════════════════════════════════════
# PAGE: BRAND DNA
# ═════════════════════════════════════════════════════════════════

def brand_page():
    client = st.session_state.get("client", "All Clients")
    st.markdown("## 🧬 Brand DNA")

    if client == "All Clients":
        st.info("👈 Sidebar မှ Client တစ်ဦးကို ရွေးချယ်ပြီး Brand DNA Configure လုပ်ပါ")
        return

    brand = dict(SAMPLE_BRANDS.get(client, EMPTY_BRAND))

    # Profile completion
    req_keys   = ["name", "industry", "audience", "usp", "mission", "promise", "tone", "archetype"]
    completion = round(sum(1 for k in req_keys if brand.get(k)) / len(req_keys) * 100)
    st.progress(completion / 100, text=f"Profile Completion: {completion}%")

    # Mode switcher
    mode = st.radio("Mode", ["✍️ Manual", "🤖 AI Generate"], horizontal=True, key="brand_mode")
    st.divider()

    if mode == "🤖 AI Generate":
        _ai_generate_ui(client)
        return

    # Manual tabs
    tabs = st.tabs(["📋 Brand Core", "🎙️ Voice & Tone", "🏛️ Content Strategy", "🎨 Visual ID", "🏆 Competitors"])

    with tabs[0]:
        c1, c2 = st.columns(2)
        with c1:
            st.text_input("Brand Name ●",   value=brand.get("name", ""),     key="b_name")
            st.text_input("Industry ●",     value=brand.get("industry", ""), key="b_industry")
        with c2:
            st.text_area("Target Audience ●", value=brand.get("audience", ""), key="b_audience", height=68)
        st.text_area("USP (Unique Selling Point) ●", value=brand.get("usp", ""), key="b_usp", height=68)
        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Brand Mission",  value=brand.get("mission", ""),  key="b_mission",  height=80)
            st.text_input("Tagline",       value=brand.get("tagline", ""),  key="b_tagline")
        with c2:
            st.text_area("Brand Promise",  value=brand.get("promise", ""),  key="b_promise",  height=80)
            st.text_area("Elevator Pitch", value=brand.get("elevator", ""), key="b_elevator", height=68)

    with tabs[1]:
        tone_keys = [t["key"] for t in TONE_OPTIONS]
        tone_idx  = tone_keys.index(brand.get("tone", "Professional")) if brand.get("tone") in tone_keys else 0
        c_cols = st.columns(3)
        for i, t in enumerate(TONE_OPTIONS):
            with c_cols[i % 3]:
                active = brand.get("tone") == t["key"]
                st.markdown(
                    f"{'**' if active else ''}{t['icon']} {t['key']}{'**' if active else ''}"
                )
                st.caption(t["desc"])
        selected_tone = st.selectbox("Select Tone", tone_keys, index=tone_idx, key="b_tone")
        st.divider()

        arch_idx = ARCHETYPE_OPTIONS.index(brand.get("archetype", "Sage")) if brand.get("archetype") in ARCHETYPE_OPTIONS else 0
        st.selectbox("Brand Archetype", ARCHETYPE_OPTIONS, index=arch_idx, key="b_archetype")
        st.divider()

        st.text_area("📘 Facebook Tone",  value=brand.get("fbTone", ""),     key="b_fbTone")
        st.text_area("🎵 TikTok Tone",    value=brand.get("tiktokTone", ""), key="b_ttTone")
        st.text_area("▶️ YouTube Tone",   value=brand.get("ytTone", ""),     key="b_ytTone")
        c1, c2 = st.columns(2)
        with c1:
            st.text_area("✅ Do's",  value=brand.get("dos", ""),   key="b_dos",   height=100)
        with c2:
            st.text_area("❌ Don'ts", value=brand.get("donts", ""), key="b_donts", height=100)

    with tabs[2]:
        st.markdown("**Content Pillars (3 Main Topics)**")
        pillars = brand.get("pillars", ["", "", ""])
        for i in range(3):
            st.text_input(f"Pillar {i+1}", value=pillars[i] if i < len(pillars) else "", key=f"b_pillar_{i}")
        st.text_area("Customer Pain Points",  value=brand.get("painPoints", ""),  key="b_pain",   height=80)
        st.text_area("Content Topic Ideas",   value=brand.get("topicIdeas", ""),  key="b_topics", height=90)

    with tabs[3]:
        st.markdown("**Brand Color Palette**")
        colors  = brand.get("colors", ["#6366f1", "#ec4899", "#10b981", "#f59e0b"])
        cc_cols = st.columns(4)
        picked  = []
        for i, col in enumerate(cc_cols):
            with col:
                picked.append(st.color_picker(f"Color {i+1}", value=colors[i] if i < len(colors) else "#6366f1", key=f"b_color_{i}"))

        # Gradient preview
        st.markdown(
            f'<div style="height:32px;border-radius:8px;'
            f'background:linear-gradient(135deg,{picked[0]},{picked[1]},{picked[2]},{picked[3]});'
            f'margin:4px 0 12px"></div>',
            unsafe_allow_html=True,
        )

        font_options = ["Modern Sans", "Display Serif", "Rounded", "Monospace", "Handwritten"]
        font_idx = font_options.index(brand.get("font", "Modern Sans")) if brand.get("font") in font_options else 0
        st.selectbox("Typography", font_options, index=font_idx, key="b_font")

        c1, c2 = st.columns(2)
        with c1:
            st.text_area("Logo Description",   value=brand.get("logoDesc", ""),  key="b_logo",  height=80)
        with c2:
            st.text_area("Moodboard Keywords", value=brand.get("moodboard", ""), key="b_mood",  height=80)

    with tabs[4]:
        competitors = brand.get("competitors", [])
        if competitors:
            for comp in competitors:
                with st.container():
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"🏢 **{comp['name']}**")
                        st.caption(comp.get("note", "No notes"))
                    st.divider()
        else:
            st.info("Competitor မရှိသေး")

        with st.expander("➕ Add Competitor"):
            cn = st.text_input("Competitor Name", key="new_cn")
            nt = st.text_area("Notes (strengths / weaknesses)", key="new_nt", height=60)
            if st.button("Add", key="add_comp"):
                if cn.strip():
                    st.success(f"Added: {cn}")

    st.divider()
    if st.button("💾 Save Brand DNA", type="primary", use_container_width=True):
        st.success("✓ Brand DNA saved successfully!")


def _ai_generate_ui(client):
    """AI Brand DNA Generator sub-panel."""
    st.markdown("### 🤖 AI Brand DNA Generator")
    st.caption("Basic info ၄ ခုသာ ဖြည့်ပါ — AI က Brand DNA အပြည့်အစုံ ထုတ်ပေးမည်")

    # Show what will be auto-generated
    tags = ["USP", "Mission", "Tagline", "Tone", "Archetype", "Content Pillars", "Platform Tones", "Competitors"]
    st.markdown(" ".join(f"`{t}`" for t in tags))
    st.divider()

    default_name = client if client != "All Clients" else ""
    b_name  = st.text_input("Brand Name ●",                  value=default_name, key="ai_name")
    b_ind   = st.text_input("Industry / Niche ●",            key="ai_industry")
    b_aud   = st.text_input("Target Audience (Optional)",    key="ai_audience")
    b_desc  = st.text_area("Brief Description (Optional — More = Better)", key="ai_desc", height=80)
    b_plats = st.multiselect("Target Platforms", ["Facebook", "TikTok", "YouTube"],
                             default=["Facebook", "TikTok", "YouTube"], key="ai_plats")

    if st.button("✨ AI နဲ့ Brand DNA Generate လုပ်မည်", type="primary", use_container_width=True):
        if not b_name.strip() or not b_ind.strip():
            st.error("Brand Name နှင့် Industry ဖြည့်ပေးပါ")
            return

        with st.spinner("🤖 AI သည် Brand DNA ထုတ်လုပ်နေသည် — analyzing Myanmar market..."):
            try:
                ai_client = Anthropic()
                prompt = f"""You are an expert brand strategist for Myanmar's digital marketing market. Generate a complete Brand DNA in JSON format for this business:

Brand Name: {b_name}
Industry: {b_ind}
Target Audience: {b_aud or 'Not specified'}
Brief Description: {b_desc or 'Not specified'}
Platforms: {', '.join(b_plats)}

Return ONLY a valid JSON object (no markdown, no backticks) with these exact keys:
{{
  "name": "", "industry": "", "audience": "", "usp": "", "mission": "", "promise": "",
  "tagline": "", "elevator": "",
  "tone": "(one of: Professional/Friendly/Trendy/Authoritative/Elegant/Playful)",
  "archetype": "(one of: Hero/Creator/Sage/Jester/Caregiver/Explorer/Ruler/Lover/Innocent/Everyman/Outlaw/Magician)",
  "fbTone": "", "tiktokTone": "", "ytTone": "",
  "dos": "", "donts": "",
  "pillars": ["","",""],
  "painPoints": "", "topicIdeas": "",
  "logoDesc": "", "moodboard": "",
  "colors": ["#hex1","#hex2","#hex3","#hex4"],
  "font": "(one of: Modern Sans/Display Serif/Rounded/Monospace/Handwritten)",
  "competitors": [{{"name":"","note":""}},{{"name":"","note":""}}]
}}

Write all content in English. Make it specific, professional, and tailored for Myanmar market."""

                msg = ai_client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=2000,
                    messages=[{"role": "user", "content": prompt}],
                )
                raw     = msg.content[0].text
                clean   = raw.replace("```json", "").replace("```", "").strip()
                gen     = json.loads(clean)

                # Normalise
                if not isinstance(gen.get("pillars"), list):
                    gen["pillars"] = ["", "", ""]
                if not isinstance(gen.get("colors"), list):
                    gen["colors"] = ["#6366f1", "#ec4899", "#10b981", "#f59e0b"]
                if not isinstance(gen.get("competitors"), list):
                    gen["competitors"] = []

                st.success("✅ Brand DNA Successfully Generated!")
                st.balloons()

                # Summary cards
                c1, c2, c3 = st.columns(3)
                c1.metric("Brand Name",  gen.get("name", ""))
                c2.metric("Tone",        gen.get("tone", ""))
                c3.metric("Archetype",   gen.get("archetype", ""))

                c1, c2, c3 = st.columns(3)
                c1.metric("Industry",    gen.get("industry", ""))
                c2.metric("Tagline",     gen.get("tagline", ""))
                c3.metric("Font",        gen.get("font", ""))

                st.markdown("**USP**")
                st.info(gen.get("usp", ""))

                st.markdown("**Elevator Pitch**")
                st.info(f'"{gen.get("elevator", "")}"')

                st.markdown("**Content Pillars**")
                for i, p in enumerate(gen.get("pillars", [])):
                    st.markdown(f"{i+1}. {p}")

                st.markdown("**Color Palette**")
                pal_cols = st.columns(4)
                for i, pc in enumerate(gen.get("colors", [])[:4]):
                    with pal_cols[i]:
                        st.color_picker(f"C{i+1}", value=pc, key=f"gen_c{i}", disabled=True)

                st.markdown("**Do's**");   st.success(gen.get("dos", ""))
                st.markdown("**Don'ts**"); st.error(gen.get("donts", ""))

                st.session_state["generated_brand"] = gen

            except Exception as e:
                st.error(f"AI generation failed: {e}")

# ═════════════════════════════════════════════════════════════════
# PAGE: CONTENT CREATION
# ═════════════════════════════════════════════════════════════════

def content_page():
    st.markdown("## ✍️ Content Creation")
    st.caption("AI-powered pipeline — strategy to publish.")

    steps = [
        {"n": "01", "label": "Strategy",          "desc": "AI analyzes brand + trends",              "icon": "🧠", "status": "Ready"},
        {"n": "02", "label": "Hook Generation",   "desc": "Scroll-stopping hooks per platform",       "icon": "🪝", "status": "Ready"},
        {"n": "03", "label": "Script Writing",    "desc": "Full scripts from strategy",               "icon": "📝", "status": "Ready"},
        {"n": "04", "label": "Visual Direction",  "desc": "Shot list, B-roll, thumbnails",            "icon": "🎨", "status": "Ready"},
        {"n": "05", "label": "Review & Approve",  "desc": "CEO reviews before publishing",            "icon": "✅", "status": "Pending CEO"},
        {"n": "06", "label": "One-Click Publish", "desc": "Auto-post to all platforms",               "icon": "🚀", "status": "Phase 4"},
    ]

    for step in steps:
        c1, c2, c3 = st.columns([0.5, 4, 1.2])
        with c1:
            st.caption(step["n"])
        with c2:
            st.markdown(f"{step['icon']} **{step['label']}**")
            st.caption(step["desc"])
        with c3:
            status_map = {"Ready": "🟢 Ready", "Pending CEO": "🟡 Pending CEO", "Phase 4": "⚫ Phase 4"}
            st.caption(status_map.get(step["status"], step["status"]))
        st.divider()

# ═════════════════════════════════════════════════════════════════
# PAGE: PROJECT ARCHIVE
# ═════════════════════════════════════════════════════════════════

def archive_page():
    st.markdown("## 🗂️ Project Archive")
    st.caption("All client campaigns.")

    projects = [
        {"name": "Project Alpha — Real Estate", "date": "Feb 2026", "platform": "Facebook", "status": "Completed", "posts": 12},
        {"name": "Fashion Brand Launch",         "date": "Mar 2026", "platform": "TikTok",   "status": "Active",    "posts": 6},
        {"name": "Restaurant Chain Weekly",      "date": "Jan 2026", "platform": "Facebook", "status": "Completed", "posts": 28},
    ]

    for p in projects:
        with st.container():
            c1, c2 = st.columns([4, 1])
            with c1:
                st.markdown(f"**{p['name']}**")
                st.caption(f"{p['date']} · {p['platform']} · {p['posts']} posts")
            with c2:
                if p["status"] == "Active":
                    st.success("Active")
                else:
                    st.caption("Completed")
        st.divider()

    if st.button("➕ New Project"):
        st.info("New project creation — coming soon!")

# ═════════════════════════════════════════════════════════════════
# PAGE: ASSETS LIBRARY
# ═════════════════════════════════════════════════════════════════

def assets_page():
    st.markdown("## 🖼️ Assets Library")
    st.caption("Brand assets & generated content.")

    cats = ["All", "Logos", "Images", "Videos", "Templates", "Copy"]
    cat  = st.radio("Category", cats, horizontal=True, key="asset_cat")

    cols = st.columns(4)
    for i in range(6):
        with cols[i % 4]:
            st.markdown(f"📁 **Asset {i+1}**")
            st.caption(cat if cat != "All" else "Uncategorized")

    st.divider()
    uploaded = st.file_uploader("Upload Asset", type=["png", "jpg", "mp4", "pdf", "docx"])
    if uploaded:
        st.success(f"Uploaded: {uploaded.name}")

# ═════════════════════════════════════════════════════════════════
# PAGE: CREATOR MODE
# ═════════════════════════════════════════════════════════════════

def creator_page():
    st.markdown("## 🎬 Creator Mode")
    st.caption("Faceless content engine for passive income.")

    st.info("🤖 AI Topic Generator — Auto-generate faceless content scripts per platform. (Phase 4)")

    plats = [
        {"name": "YouTube",  "icon": "▶️", "desc": "Monetization · Long-form · Faceless"},
        {"name": "TikTok",   "icon": "🎵", "desc": "Viral · Short-form · Trending Sound"},
        {"name": "Facebook", "icon": "📘", "desc": "Reach · Storytelling · Sponsored"},
    ]

    for p in plats:
        c1, c2 = st.columns([4, 1])
        with c1:
            st.markdown(f"{p['icon']} **{p['name']}**")
            st.caption(p["desc"])
        with c2:
            st.button(f"Connect", key=f"conn_{p['name']}")
        st.divider()

# ═════════════════════════════════════════════════════════════════
# PAGE: SYSTEM STATUS
# ═════════════════════════════════════════════════════════════════

def status_page():
    st.markdown("## 🛰️ System Status")
    st.caption("Real-time health of all services.")

    services = [
        {"name": "AI Engine",      "status": "Online",     "ok": True},
        {"name": "Facebook API",   "status": "Connected",  "ok": True},
        {"name": "TikTok API",     "status": "Connected",  "ok": True},
        {"name": "YouTube API",    "status": "Standby",    "ok": False},
        {"name": "Auto-Publish",   "status": "Active",     "ok": True},
        {"name": "News Feed",      "status": "Live",       "ok": True},
    ]

    for svc in services:
        c1, c2 = st.columns([4, 1])
        with c1:
            dot = "🟢" if svc["ok"] else "🟡"
            st.markdown(f"{dot} **{svc['name']}**")
        with c2:
            if svc["ok"]:
                st.success(svc["status"])
            else:
                st.warning(svc["status"])

    st.divider()
    st.success("Last checked: Just now · All core systems operational.")

# ═════════════════════════════════════════════════════════════════
# AI AGENT (Sidebar Chat)
# ═════════════════════════════════════════════════════════════════

NAV_MAP = {
    "dashboard": "dashboard", "main": "dashboard",
    "news": "news", "trend": "news", "သတင်း": "news",
    "brand": "brand", "brand dna": "brand",
    "content": "content",
    "archive": "archive", "project": "archive",
    "assets": "assets",
    "creator": "creator",
    "status": "status",
}

CLIENT_MAP = {
    "real estate": "Real Estate Co.",
    "fashion":     "Fashion Brand",
    "restaurant":  "Restaurant Chain",
    "tech":        "Tech Startup",
    "beauty":      "Beauty Studio",
    "all clients": "All Clients",
    "all":         "All Clients",
}

PLATFORM_MAP = {
    "facebook": "Facebook", "fb": "Facebook",
    "tiktok":   "TikTok",
    "youtube":  "YouTube",  "yt": "YouTube",
}

TIMEFRAME_MAP = {
    "weekly":  "Weekly",
    "monthly": "Monthly",
    "yearly":  "Yearly",
}


def _parse_command(text: str) -> bool:
    """Try to execute navigation commands. Returns True if something was triggered."""
    t = text.lower()
    triggered = False

    for kw, page in NAV_MAP.items():
        if kw in t:
            st.session_state.active_page = page
            triggered = True
            break

    for kw, client in CLIENT_MAP.items():
        if kw in t:
            st.session_state.client = client
            triggered = True
            break

    for kw, plat in PLATFORM_MAP.items():
        if kw in t:
            if "perf_plat" in st.session_state:
                st.session_state.perf_plat = plat
            triggered = True

    for kw, tf in TIMEFRAME_MAP.items():
        if kw in t:
            if "perf_tf" in st.session_state:
                st.session_state.perf_tf = tf
            triggered = True

    return triggered


def ai_agent_sidebar():
    st.sidebar.divider()
    st.sidebar.markdown("### 🤖 AI Command Agent")

    if "agent_msgs" not in st.session_state:
        st.session_state.agent_msgs = [
            {
                "role": "assistant",
                "content": (
                    "မင်္ဂလာပါ Sayar Gyi! 👋\n\n"
                    "Chat ရေးလို့ရသလို Navigation လည်းလုပ်ပေးနိုင်ပါတယ်\n\n"
                    "**ဥပမာများ:**\n"
                    "• `Dashboard ကိုပြပါ`\n"
                    "• `TikTok data ကြည့်ချင်တယ်`\n"
                    "• `Fashion Brand client ကိုဖွင့်`\n"
                    "• `Brand DNA သွားပါ`"
                ),
            }
        ]

    # Show last 4 messages (save sidebar space)
    for msg in st.session_state.agent_msgs[-4:]:
        with st.sidebar.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Quick-command buttons
    quick = st.sidebar.columns(2)
    btn_map = {
        "📊 Dashboard": "Dashboard",
        "🧬 Brand DNA": "Brand DNA",
        "📡 News": "News",
        "🎬 Creator": "Creator",
    }
    for i, (label, cmd) in enumerate(btn_map.items()):
        with quick[i % 2]:
            if st.button(label, key=f"qb_{label}", use_container_width=True):
                _process_agent_message(cmd)
                st.rerun()

    if prompt := st.sidebar.chat_input("ရိုက်ပါ (Enter to send)"):
        _process_agent_message(prompt)
        st.rerun()


def _process_agent_message(text: str):
    st.session_state.agent_msgs.append({"role": "user", "content": text})
    triggered = _parse_command(text)

    try:
        ai_client = Anthropic()
        history   = [{"role": m["role"], "content": m["content"]}
                     for m in st.session_state.agent_msgs]
        note      = " (navigation/client action was triggered)" if triggered else ""
        message   = ai_client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=400,
            system=(
                f"You are an AI Agent inside 'Sayar Gyi's AI Command Center' — "
                f"a Myanmar marketing agency dashboard. Help CEO Sayar Gyi concisely. "
                f"Support Myanmar + English naturally.{note}"
            ),
            messages=history,
        )
        reply = message.content[0].text
    except Exception as e:
        reply = f"⚠️ Error: {e}"

    st.session_state.agent_msgs.append({"role": "assistant", "content": reply})

# ═════════════════════════════════════════════════════════════════
# DARK THEME CSS
# ═════════════════════════════════════════════════════════════════

DARK_CSS = """
<style>
/* ── Base ── */
.stApp { background-color: #030712 !important; color: #e5e7eb !important; }
section[data-testid="stSidebar"] { background-color: #0d1117 !important; border-right: 1px solid #1f2937; }
section[data-testid="stSidebar"] * { color: #e5e7eb; }

/* ── Headings ── */
h1, h2, h3, h4 { color: #f9fafb !important; }
label, .stMarkdown p { color: #e5e7eb; }

/* ── Metric cards ── */
div[data-testid="metric-container"] {
    background-color: #111827;
    border: 1px solid #1f2937;
    border-radius: 10px;
    padding: 10px 14px;
}
div[data-testid="stMetricValue"] { color: #f9fafb !important; }
div[data-testid="stMetricDelta"]  { font-size: 11px; }

/* ── Inputs ── */
.stTextInput input, .stTextArea textarea, .stSelectbox > div > div {
    background-color: #0d1117 !important;
    border-color: #1f2937 !important;
    color: #e5e7eb !important;
    border-radius: 8px;
}
.stMultiSelect > div { background-color: #0d1117 !important; border-color: #1f2937 !important; }

/* ── Buttons ── */
.stButton > button {
    background-color: #1f2937 !important;
    color: #e5e7eb !important;
    border: 1px solid #374151 !important;
    border-radius: 7px;
}
.stButton > button:hover { background-color: #374151 !important; }
.stButton > button[kind="primary"] {
    background: linear-gradient(135deg,#6366f1,#8b5cf6) !important;
    border: none !important;
    color: #fff !important;
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] { background-color: #111827; border-radius: 8px; }
.stTabs [data-baseweb="tab"] { color: #6b7280 !important; }
.stTabs [aria-selected="true"] { background-color: #6366f1 !important; color: #fff !important; border-radius: 6px; }

/* ── Expanders ── */
.streamlit-expanderHeader { background-color: #111827 !important; border-color: #1f2937 !important; color: #e5e7eb !important; }
.streamlit-expanderContent { background-color: #0d1117 !important; border-color: #1f2937 !important; }

/* ── Info / Success / Error ── */
.stAlert { border-radius: 8px; }

/* ── Divider ── */
hr { border-color: #1f2937 !important; }

/* ── Radio ── */
.stRadio label { color: #e5e7eb !important; }
.stRadio div[role="radiogroup"] > label { background-color: #111827; border-radius: 6px; padding: 4px 10px; }

/* ── Checkbox ── */
.stCheckbox label { color: #e5e7eb !important; }

/* ── Progress ── */
.stProgress > div > div { background-color: #6366f1 !important; }

/* ── Chat ── */
div[data-testid="stChatMessageContent"] { background-color: #111827 !important; border-radius: 10px; }
div[data-testid="stChatInput"] textarea { background-color: #0d1117 !important; color: #e5e7eb !important; border-color: #374151 !important; }

/* ── Plotly charts ── */
.js-plotly-plot { border-radius: 8px; }

/* ── Scrollbar ── */
::-webkit-scrollbar { width: 5px; height: 5px; }
::-webkit-scrollbar-track { background: #0d1117; }
::-webkit-scrollbar-thumb { background: #374151; border-radius: 3px; }
</style>
"""

# ═════════════════════════════════════════════════════════════════
# MAIN APP
# ═════════════════════════════════════════════════════════════════

PAGE_MAP = {
    "dashboard": ("📊", "Interactive Dashboard",     dashboard_page),
    "news":      ("📡", "Industry News & Trends",    news_page),
    "brand":     ("🧬", "Brand DNA",                 brand_page),
    "content":   ("✍️", "Content Creation",          content_page),
    "archive":   ("🗂️", "Project Archive",           archive_page),
    "assets":    ("🖼️", "Assets Library",            assets_page),
    "creator":   ("🎬", "Creator Mode",              creator_page),
    "status":    ("🛰️", "System Status",             status_page),
}


def main():
    st.set_page_config(
        page_title="Sayar Gyi's AI Command Center",
        page_icon="⚡",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    st.markdown(DARK_CSS, unsafe_allow_html=True)

    # Session state init
    if "active_page" not in st.session_state:
        st.session_state.active_page = "dashboard"
    if "client" not in st.session_state:
        st.session_state.client = "All Clients"

    # ── Sidebar ──────────────────────────────────────────────────
    with st.sidebar:
        # Logo / title
        st.markdown(
            '<div style="display:flex;align-items:center;gap:8px;padding:4px 0 12px">'
            '<span style="font-size:22px">⚡</span>'
            '<div><div style="font-weight:800;font-size:14px">Sayar Gyi\'s</div>'
            '<div style="font-size:10px;color:#6b7280">AI Command Center</div></div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # Client picker
        client_idx = CLIENTS.index(st.session_state.client)
        new_client = st.selectbox("👤 Client", CLIENTS, index=client_idx, key="client_picker")
        if new_client != st.session_state.client:
            st.session_state.client = new_client
            st.rerun()

        st.divider()
        st.caption("NAVIGATION")

        # News (top-level)
        for page_id in ["news"]:
            icon, label, _ = PAGE_MAP[page_id]
            active = st.session_state.active_page == page_id
            if st.button(f"{icon} {label}", key=f"nav_{page_id}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.active_page = page_id
                st.rerun()

        st.caption("MENU")
        for page_id in ["dashboard", "brand", "content", "archive", "assets"]:
            icon, label, _ = PAGE_MAP[page_id]
            active = st.session_state.active_page == page_id
            if st.button(f"{icon} {label}", key=f"nav_{page_id}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.active_page = page_id
                st.rerun()

        st.divider()
        for page_id in ["creator", "status"]:
            icon, label, _ = PAGE_MAP[page_id]
            active = st.session_state.active_page == page_id
            if st.button(f"{icon} {label}", key=f"nav_{page_id}",
                         use_container_width=True,
                         type="primary" if active else "secondary"):
                st.session_state.active_page = page_id
                st.rerun()

        st.divider()
        st.markdown(
            '<div style="display:flex;align-items:center;gap:8px">'
            '<span>👤</span>'
            '<div><div style="font-weight:600;font-size:12px">Sayar Gyi</div>'
            '<div style="font-size:10px;color:#10b981">● CEO / Admin</div></div>'
            '</div>',
            unsafe_allow_html=True,
        )

        # AI Agent chat
        ai_agent_sidebar()

    # ── Topbar breadcrumb ────────────────────────────────────────
    active_page = st.session_state.active_page
    icon, label, page_fn = PAGE_MAP.get(active_page, PAGE_MAP["dashboard"])

    st.markdown(
        f'<div style="margin-bottom:16px">'
        f'<span style="font-size:11px;color:#6b7280">AI Command Center</span> '
        f'<span style="color:#374151">/</span> '
        f'<span style="font-size:11px;color:#9ca3af;font-weight:600">{label}</span>'
        f'<span style="float:right;font-size:11px;color:#10b981">● {st.session_state.client}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Render page ──────────────────────────────────────────────
    page_fn()


if __name__ == "__main__":
    main()
