# ----------------- app/drift_analysis.py -----------------
import matplotlib.pyplot as plt
import streamlit as st

def plot_drift(df):
    fig, ax = plt.subplots()
    ax.plot(df['timestamp'], df['hdop'], label='HDOP Drift', color='orange')
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("HDOP")
    ax.set_title("GNSS Accuracy Drift Over Time")
    ax.legend()
    st.pyplot(fig)
