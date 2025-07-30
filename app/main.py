# ----------------- app/main.py -----------------
import streamlit as st
from app import uploader, drift_analysis, compliance_check, map_viewer

st.set_page_config(page_title="GNSS Drift Doctor", layout="wide")
st.title("🌎 GNSS Drift Doctor – Accuracy & Compliance Tracker")

uploaded_file = uploader.upload_csv()

if uploaded_file is not None:
    data = uploader.load_data(uploaded_file)
    st.success("GNSS data loaded successfully!")

    with st.expander("GNSS Drift Visualization"):
        drift_analysis.plot_drift(data)

    with st.expander("Compliance Check"):
        compliance_check.check_accuracy(data)

    with st.expander("Map View"):
        map_viewer.show_map(data)
