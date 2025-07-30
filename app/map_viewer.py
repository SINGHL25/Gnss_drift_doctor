# ----------------- app/map_viewer.py -----------------
import streamlit as st
import pydeck as pdk

def show_map(df):
    st.write("GNSS Path Map")
    st.map(df[['latitude', 'longitude']])
    st.pydeck_chart(pdk.Deck(
        map_style='mapbox://styles/mapbox/streets-v11',
        initial_view_state=pdk.ViewState(
            latitude=df['latitude'].mean(),
            longitude=df['longitude'].mean(),
            zoom=12,
            pitch=0,
        ),
        layers=[
            pdk.Layer(
                'ScatterplotLayer',
                data=df,
                get_position='[longitude, latitude]',
                get_color='[200, 30, 0, 160]',
                get_radius=10,
            ),
        ],
    ))
