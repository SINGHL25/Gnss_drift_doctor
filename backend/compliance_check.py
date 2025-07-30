import pandas as pd
import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate haversine distance between GNSS and true lat/lon.
    Returns distance in meters.
    """
    R = 6371000  # Earth radius in meters
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)

    a = np.sin(dphi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c

def evaluate(df: pd.DataFrame, threshold_meters=2.0) -> dict:
    df['drift'] = haversine_distance(df['lat_gnss'], df['lon_gnss'], df['lat_true'], df['lon_true'])
    rms_error = np.sqrt(np.mean(df['drift'] ** 2))
    passed = rms_error < threshold_meters

    return {
        "RMS Error (m)": round(rms_error, 3),
        "Threshold (m)": threshold_meters,
        "Compliant": passed,
        "Total Records": len(df),
        "Above Threshold": int((df['drift'] > threshold_meters).sum())
    }

