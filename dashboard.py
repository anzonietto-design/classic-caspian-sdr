import streamlit as st
import os

st.set_page_config(page_title="Classic Caspian SDR", page_icon="🐟", layout="wide")

# Try to load secrets for Streamlit Cloud
try:
      AIRTABLE_KEY = st.secrets["airtable"]["api_key"]
  except:
    AIRTABLE_KEY = ""

SEGMENTS = {
      "fine_dining": "🍽️ Fine Dining",
      "hotels": "🏨 Luxury Hotels", 
      "yacht": "🛥️ Yacht & Marine",
      "catering": "👨‍🍳 Catering",
      "golf": "⛳ Golf Clubs",
      "beach": "🏖️ Beach Clubs",
      "banks": "🏦 Private Banks",
      "airlines": "✈️ Airlines",
}

LOCATIONS = {
      "Riviera": ["Monaco", "Nice", "Cannes"],
      "Switzerland": ["Geneva", "Zurich"],
      "UK": ["London"],
      "Middle East": ["Dubai"],
}

# Sidebar
with st.sidebar:
      st.title("🐟 Classic Caspian")
      st.caption("AI Sales Agent")
      st.divider()
      page = st.radio("Menu", ["🎯 Campaign", "📊 Dashboard", "⚙️ Settings"])

# Campaign Setup
if page == "🎯 Campaign":
      st.header("🎯 Campaign Setup")

    st.subheader("📍 Target Location")
    region = st.selectbox("Select region:", list(LOCATIONS.keys()))
    cities = st.multiselect("Cities:", LOCATIONS[region], default=LOCATIONS[region])
    st.success(f"Targeting: {', '.join(cities)}")

    st.divider()
    st.subheader("🏢 Market Segments")

    cols = st.columns(2)
    active = []
    for i, (k, v) in enumerate(SEGMENTS.items()):
              with cols[i % 2]:
                            if st.checkbox(v, value=True, key=k):
                                              active.append(k)

                    st.divider()
    c1, c2 = st.columns(2)
    with c1:
              if st.button("💾 Save Config", type="primary", use_container_width=True):
                            st.success("Configuration saved!")
                    with c2:
                              if st.button("🚀 Launch Campaign", use_container_width=True):
                                            st.balloons()
                                            st.success("Campaign launched!")

                      # Dashboard
elif page == "📊 Dashboard":
    st.header("📊 Campaign Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Leads", "0")
    c2.metric("Emails Sent", "0", "0 today")
    c3.metric("Replies", "0")
    c4.metric("Meetings", "0")

    st.divider()
    st.info("Launch a campaign to see leads here!")

# Settings
else:
    st.header("⚙️ Settings")

    st.subheader("🔑 API Status")
    st.write("✅ Connected" if AIRTABLE_KEY else "❌ Not configured")

    st.divider()
    st.subheader("📧 Email Settings")
    st.number_input("Daily email limit:", value=50, min_value=1)
    st.number_input("Emails per hour:", value=10, min_value=1)

st.divider()
st.caption("Classic Caspian SDR • Powered by Streamlit")
