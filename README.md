# ----------------- README.md -----------------
# 🌎 GNSS Drift Doctor

A Streamlit app to monitor GNSS accuracy drift and compliance for field-deployed devices such as Tolling ETC units, CAV sensors, or survey hardware.

## Features
- Upload GNSS logs (CSV)
- Visualize HDOP drift over time
- Identify out-of-compliance events
- Map GNSS drift path

## Run Locally
```bash
git clone https://github.com/yourusername/gnss-drift-doctor.git
cd gnss-drift-doctor
pip install -r requirements.txt
streamlit run app/main.py
