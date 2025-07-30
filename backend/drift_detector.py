import pandas as pd
from backend.gnss_utils import clean_data

def load_and_process(file) -> pd.DataFrame:
    df = pd.read_csv(file)
    df = clean_data(df)
    return df

def plot_drift(df):
    import plotly.express as px
    df['drift'] = ((df['lat_gnss'] - df['lat_true'])**2 + (df['lon_gnss'] - df['lon_true'])**2)**0.5 * 111139  # convert deg to meters
    fig = px.line(df, x='timestamp', y='drift', title="GNSS Drift Over Time", labels={'drift': 'Drift (meters)'})
    fig.update_traces(line=dict(color="red"))
    return fig

