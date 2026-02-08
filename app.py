import streamlit as st
import json
import os
from main import process_thread

# ---------- FIXED PATH HANDLING ----------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SAMPLE_PATH = os.path.join(BASE_DIR, "sample_emails.json")
# ---------------------------------------

st.set_page_config(page_title="Email Triage Assistant")

st.title("📧 Email Triage Assistant")
st.write("Paste email thread JSON or use sample data")

option = st.radio(
    "Choose input type:",
    ["Use Sample Emails", "Paste Email JSON"]
)

threads = []

# ---------- LOAD SAMPLE EMAILS SAFELY ----------
if option == "Use Sample Emails":
    try:
        with open(SAMPLE_PATH, "r") as f:
            threads = json.load(f)
    except FileNotFoundError:
        st.error("❌ sample_emails.json not found in project folder")

# ---------- USER INPUT JSON ----------
elif option == "Paste Email JSON":
    user_input = st.text_area("Paste email thread JSON here")

    if user_input:
        try:
            threads = [json.loads(user_input)]
        except json.JSONDecodeError:
            st.error("❌ Invalid JSON format")

# ---------- PROCESS ----------
if st.button("Process Emails"):
    if not threads:
        st.warning("⚠️ No emails to process")
    else:
        for thread in threads:
            result = process_thread(thread)

            st.subheader(f"Thread ID: {result['thread_id']}")
            st.write("**Summary:**", result["summary"])
            st.write("**Category:**", result["category"])
            st.write("**Action:**", result["action"])
            st.write("**Suggested Reply:**", result["reply"])
            st.divider()
