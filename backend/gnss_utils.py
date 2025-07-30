import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    expected_cols = ['timestamp', 'lat_gnss', 'lon_gnss', 'lat_true', 'lon_true']
    missing_cols = [col for col in expected_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing columns: {missing_cols}")
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df.dropna(subset=['timestamp', 'lat_gnss', 'lon_gnss', 'lat_true', 'lon_true'], inplace=True)
    return df.sort_values(by='timestamp')

