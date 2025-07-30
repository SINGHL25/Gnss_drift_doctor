import plotly.express as px

def plot_location_scatter(df):
    fig = px.scatter_mapbox(df, lat="lat_gnss", lon="lon_gnss", zoom=15,
                            mapbox_style="open-street-map",
                            title="GNSS Positions on Map")
    return fig

def plot_truth_vs_gnss(df):
    fig = px.scatter(df, x="lon_gnss", y="lat_gnss", color_discrete_sequence=["blue"], label="GNSS",
                     title="GNSS vs Ground Truth")
    fig.add_scatter(x=df["lon_true"], y=df["lat_true"], mode="markers", name="Ground Truth", marker=dict(color="green"))
    return fig

