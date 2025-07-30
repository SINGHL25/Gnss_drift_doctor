# ----------------- app/uploader.py -----------------
import streamlit as st
import pandas as pd

def upload_csv():
    return st.file_uploader("Upload GNSS Data CSV", type=["csv"])

def load_data(file):
    return pd.read_csv(file)

