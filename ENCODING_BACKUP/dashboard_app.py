import sys

try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass
import streamlit as st


st.set_page_config(
    page_title="IOTEC COMMAND CENTER",
    layout="wide"
)

st.title("IOTEC GLOBAL EXPERIENCE")

st.subheader("COMMAND CENTER")

st.success("CORE ONLINE")

st.metric(
    "ACTIVE MODULES",
    4
)

st.metric(
    "MONTHLY REVENUE",
    "$3700"
)

st.metric(
    "SYSTEM STATUS",
    "STABLE"
)

st.markdown("---")

st.write("Premium ecosystem operational.")



