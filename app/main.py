import streamlit as st
from components import uploader
from backend import drift_detector, compliance_check

st.set_page_config(page_title="GNSS Drift Doctor", layout="wide")

st.title("🛰️ GNSS Drift Doctor")
st.subheader("Real-time drift visualization and compliance checker")

# Upload GNSS file
uploaded_file = uploader.upload_csv()

if uploaded_file:
    df = drift_detector.load_and_process(uploaded_file)
    st.success("Data uploaded and processed.")

    st.plotly_chart(drift_detector.plot_drift(df), use_container_width=True)

    compliance_report = compliance_check.evaluate(df)
    st.write(compliance_report)

