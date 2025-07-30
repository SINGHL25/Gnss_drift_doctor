# ----------------- app/compliance_check.py -----------------
import streamlit as st

def check_accuracy(df):
    threshold = st.slider("HDOP Compliance Threshold", 1.0, 5.0, 2.5)
    non_compliant = df[df['hdop'] > threshold]
    st.write(f"Total Non-compliant Records: {len(non_compliant)}")
    st.dataframe(non_compliant)
