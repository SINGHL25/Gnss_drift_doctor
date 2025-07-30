# ----------------- README.md -----------------
# 🌎 GNSS Drift Doctor

📱 App Name: GNSS Drift Doctor
🎯 Purpose:
Track, visualize, and diagnose GNSS drift and signal loss for tolling vehicles (especially OBU-based eToll systems using GNSS).

🧱 Architecture Overview:
🔧 1. Data Inputs
Source	Format	Example
GNSS Log	JSON / CSV	Time, Lat, Lon, Speed, HDOP, SNR, Sat Count
Map Matching Engine	API	Route segment data
Device Metadata	JSON	Vehicle ID, Device Model, Firmware

🗺️ 2. Core Modules
A. Data Processor
Parses GNSS logs

Filters noise

Computes:

Average HDOP

Satellite count

Gaps in position

Position error w.r.t. ground truth

B. Map Matching Engine (Optional)
Uses OpenStreetMap or HERE API to compare reported path with actual road path

Identifies drifted segments, off-road jumps

C. AI-based Drift Detector
Flags trip segments with:

Low SNR or HDOP > 3.0

< 4 Satellites

Sudden jumps (>100m/sec)

Signal loss in tunnel zones

D. Visualization UI (Streamlit)
Map of GNSS trace (color-coded by quality)

Satellite strength time-series plot

Drift events timeline

Exportable report (PDF/CSV)

🗃️ Tech Stack
Component	Tech
Frontend	Streamlit
Map	Folium / Leaflet.js
Data Store	SQLite / Firebase
ML/Drift Logic	Python + Pandas + NumPy
Optional Map Matching	OSRM or HERE Maps API






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


