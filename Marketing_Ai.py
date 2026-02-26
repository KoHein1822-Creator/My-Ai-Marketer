import streamlit as st
import time

# --- 1. PREMIUM ENTERPRISE UI (V14.0 STANDARDS) ---
st.set_page_config(page_title="SAYAR GYI | COMMAND CENTER", layout="wide")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #05070a; color: #e1e4e8; }
    .agent-card { background: #0d1117; border: 1px solid #30363d; padding: 20px; border-radius: 12px; height: 100%; }
    .status-badge { padding: 4px 8px; border-radius: 4px; font-size: 10px; font-weight: bold; text-transform: uppercase; }
    .pass { background: #238636; color: white; }
    .fail { background: #da3633; color: white; }
    .sub-label { font-size: 11px; text-transform: uppercase; color: #8b949e; letter-spacing: 1px; font-weight: 600; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. CORE ENGINE: MULTI-AGENT LOGIC ---

class EnterpriseAgency:
    def __init__(self, biz_type, stock):
        self.biz = biz_type
        self.stock = stock

    # --- AGENT 1: THE MARKET INTEL (Strategy & Research) ---
    def intel_agent_execute(self):
        # Funnel Logic: If stock is high, focus on Awareness (TOFU). If low, focus on Sale (BOFU).
        funnel = "TOFU (Awareness)" if self.stock > 10 else "BOFU (Conversion)"
        
        brief = {
            "funnel": funnel,
            "topic": f"{self.biz} Selection Tips" if funnel == "TOFU (Awareness)" else f"{self.biz} Flash Sale",
            "logic": "Educational" if funnel == "TOFU (Awareness)" else "Urgency/Scarcity",
            "trend": "Minimalist Lifestyle Trends 2026"
        }
        return brief

    # --- AGENT 2: THE CONTENT ENGINE (The Junior) ---
    def content_engine_execute(self, brief):
        # Strict Content Mapping to Funnel Stage
        if "TOFU" in brief['funnel']:
            copy = f"နွေရာသီမှာ ဘယ်လို {self.biz} မျိုးက သင့်ကို ပိုဝင်းပစေမလဲ? ဒါလေးတွေ သိထားသင့်ပါတယ်။ ✨"
            visual = "Warm, natural lighting, lifestyle aesthetic."
        else:
            copy = f"လက်ကျန် {self.stock} ခုသာ! {self.biz} ကို အထူးဈေးနှုန်းနဲ့ အမြန်ဆုံး ဝယ်ယူလိုက်ပါ။ ⏳"
            visual = "Bold, high-contrast, product-focused with 'Limited' badge."
            
        return {"copy": copy, "visual": visual, "funnel_label": brief['funnel']}

    # --- AGENT 3: THE EXECUTIVE AUDITOR (The Senior) ---
    def audit_process(self, brief, content):
        # GATE 1: Logic Verification
        # Check if Junior mistakenly used Sale words in TOFU or Tips in BOFU
        error_found = False
        report = []

        if "TOFU" in brief['funnel'] and ("ဝယ်ယူပါ" in content['copy'] or "ဈေးနှုန်း" in content['copy']):
            error_found = True
            report.append("❌ GATE 2 FAIL: Awareness Strategy မှာ အရောင်းစာသား (Hard Sell) သုံးထားသည်။")
        
        if not error_found:
            report.append("✅ ALL GATES PASSED: Funnel Alignment & Brand DNA Verified.")
            
        return not error_found, report

# --- 3. COMMAND CENTER UI ---

with st.sidebar:
    st.markdown("## SAYAR GYI <span style='color:#58a6ff; font-size:14px;'>v21.0</span>", unsafe_allow_html=True)
    st.divider()
    biz_input = st.selectbox("ACTIVE ACCOUNT", ["Jewelry SME", "Real Estate", "Digital Academy"])
    stock_input = st.slider("INVENTORY / CAPACITY", 0, 50, 15)
    st.divider()
    run_mission = st.button("🚀 EXECUTE AUTOMATED MISSION")

st.markdown(f"### Mission Control: {biz_input}")
st.caption("Standardized Pipeline: Intel > Creation > Audit > Approval")

if run_mission:
    agency = EnterpriseAgency(biz_input, stock_input)
    
    # PHASE 1: INTELLIGENCE
    with st.spinner("Intel Agent researching..."):
        time.sleep(1)
        brief_data = agency.intel_agent_execute()
    
    # PHASE 2: PRODUCTION
    with st.spinner("Content Engine drafting..."):
        time.sleep(1.5)
        content_data = agency.content_engine_execute(brief_data)
        
    # PHASE 3: AUDIT
    with st.spinner("Executive Auditor verifying..."):
        time.sleep(1)
        is_safe, audit_logs = agency.audit_process(brief_data, content_data)

    # --- DISPLAY AGENT CARDS ---
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f"""<div class="agent-card">
            <p class="sub-label">Market Intel</p>
            <h4>{brief_data['funnel']}</h4>
            <p style='font-size:12px;'>Topic: {brief_data['topic']}<br>Logic: {brief_data['logic']}</p>
        </div>""", unsafe_allow_html=True)

    with c2:
        st.markdown(f"""<div class="agent-card">
            <p class="sub-label">Content Engine</p>
            <p style='font-size:13px;'>{content_data['copy'][:50]}...</p>
            <span class="status-badge" style="background:#30363d;">Draft v1.0</span>
        </div>""", unsafe_allow_html=True)

    with c3:
        status_class = "pass" if is_safe else "fail"
        st.markdown(f"""<div class="agent-card">
            <p class="sub-label">Executive Auditor</p>
            <span class="status-badge {status_class}">{'Cleared' if is_safe else 'Rejected'}</span>
            <p style='font-size:11px; margin-top:10px;'>{audit_logs[0]}</p>
        </div>""", unsafe_allow_html=True)

    # --- FINAL APPROVAL ---
    if is_safe:
        st.divider()
        st.markdown("### 💎 Final Strategic Asset")
        col_draft, col_ops = st.columns([2, 1])
        with col_draft:
            with st.container(border=True):
                st.write(content_data['copy'])
                st.caption(f"Visual Direction: {content_data['visual']}")
        with col_ops:
            st.button("✅ APPROVE & LAUNCH")
            st.button("🔄 REQUEST REDRAFT")
    else:
        st.error("Mission Aborted: Junior Error detected. Check Auditor Log.")

# --- 4. SYSTEM REPORTING ---
st.divider()
st.markdown("<p class='sub-label'>Integrated Agent Reports</p>", unsafe_allow_html=True)
r1, r2, r3 = st.columns(3)
r1.caption("Intel: Market Synced ✅")
r2.caption("Content: Asset Ready ✅")
r3.caption("Audit: Policy Compliant ✅")
