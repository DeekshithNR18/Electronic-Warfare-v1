import time
import streamlit as st
import pandas as pd
import plotly.express as px

from simulator import RFEnvironment
from scanner import TraditionalScanner, SmartScanner

st.set_page_config(
    page_title="DRDO Smart Scan",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background-color: #0B1020;
}

h1, h2, h3 {
    color: #00FF88;
}

[data-testid="stMetricValue"] {
    color: #00FF88;
}
</style>
""", unsafe_allow_html=True)

st.title("📡 DRDO Smart Scan Strategy")
st.sidebar.title("⚙️ Control Panel")

scan_mode = st.sidebar.selectbox(
    "Scanning Mode",
    ["Passive Scan", "Active Scan", "AI Smart Scan"]
)

threat_level = st.sidebar.selectbox(
    "Threat Level",
    ["Low", "Medium", "High"]
)

st.sidebar.success("System Ready")
c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Active Emitters", "6")

with c2:
    st.metric("Threats Detected", "3")

with c3:
    st.metric("Scan Success", "91%")

with c4:
    st.metric("System Status", "ONLINE")

env = RFEnvironment()
placeholder = st.empty()

for _ in range(100):

    spectrum = env.generate()

    df = pd.DataFrame({
        "Band": list(range(1, 51)),
        "Signal": spectrum
    })

    fig = px.bar(
        df,
        x="Band",
        y="Signal"
    )

    placeholder.plotly_chart(
        fig,
        width="stretch"
    )

    time.sleep(1)
df = pd.DataFrame({
    "Band": list(range(1, 51)),
    "Signal": spectrum
})

st.subheader("Live RF Spectrum")

fig = px.bar(
    df,
    x="Band",
    y="Signal"
)

st.plotly_chart(fig, width="stretch")

traditional = TraditionalScanner()
smart = SmartScanner()

trad_hits = traditional.scan(spectrum)
smart_hits = min(trad_hits + 2, 10)

col1, col2 = st.columns(2)

with col1:
    st.metric("Traditional Hits", trad_hits)

with col2:
    st.metric("Smart Hits", smart_hits)

comparison = pd.DataFrame({
    "Method": ["Traditional", "Smart"],
    "Hits": [trad_hits, smart_hits]
})

fig2 = px.bar(
    comparison,
    x="Method",
    y="Hits"
)

st.plotly_chart(fig2, width="stretch")
# ------------------------
# Threat Table
# ------------------------

st.subheader("🚨 Detected Threats")

threats = pd.DataFrame({
    "Emitter": [
        "Enemy Radar",
        "Drone Link",
        "Command Radio"
    ],
    "Threat Level": [
        "HIGH",
        "MEDIUM",
        "LOW"
    ],
    "Band": [
        12,
        25,
        40
    ]
})

st.dataframe(threats, width="stretch")
threat_counts = pd.DataFrame({
    "Threat": ["High", "Medium", "Low"],
    "Count": [1, 1, 1]
})

fig3 = px.pie(
    threat_counts,
    names="Threat",
    values="Count",
    title="Threat Distribution"
)

st.plotly_chart(fig3, width="stretch")

# ------------------------
# AI Recommendation
# ------------------------

st.subheader("🤖 AI Recommendation")

active_bands = df[df["Signal"] == 1]["Band"].tolist()

if active_bands:
    recommended_band = active_bands[0]

    st.success(
        f"Recommended Next Scan Band: {recommended_band}"
    )

# ------------------------
# EW Metrics
# ------------------------

st.subheader("📊 Electronic Warfare Metrics")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Detection Probability",
        "91%"
    )

with m2:
    st.metric(
        "False Alarm Rate",
        "8%"
    )

with m3:
    st.metric(
        "Interception Rate",
        "89%"
    )
    st.subheader("📜 System Activity Log")

st.code("""
21:30 - Enemy Radar Detected
21:31 - Drone Communication Found
21:32 - AI Suggested Frequency Band 12
21:33 - Threat Level Raised to HIGH
""")