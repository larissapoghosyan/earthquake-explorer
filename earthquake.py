import pandas as pd
import streamlit as st
import plotly.express as px
from dataset import DataSet


class Earthquake:
    def __init__(self, url: str):
        ds = DataSet()
        self.processed_data = ds.retrieve_processed_data(url)
        self.geojson: dict = ds.load_data(url)

    def world_map(self):
        dataset = pd.DataFrame(self.processed_data)
        (
            minLongitude,
            minLatitude,
            minDepth,
            maxLongitude,
            maxLatitude,
            maxDepth,
        ) = self.geojson["bbox"]

        centerLongitude = (minLongitude + maxLongitude) / 2
        centerLatitude = (minLatitude + maxLatitude) / 2

        color_gradient = [
            "#ff0000",
            "#df1b1b",
            "#f84c0b",
            "#ff5a00",
            "#ff9a00",
            "#FFAE42",
            "#ffce00",
            "#f0ff00",
        ]
        fig = px.density_mapbox(
            dataset,
            lat="lats",
            lon="lons",
            z="mag",
            radius=10,
            center=dict(lat=-20, lon=180),
            zoom=0,
            mapbox_style="open-street-map",
            width=1600,
            height=800,
            hover_name="location",
            hover_data=dict(
                lats=False,
                lons=False,
            ),
            color_continuous_scale=color_gradient,
        )
        fig.update_layout(
            margin=dict(r=0, t=0, l=0, b=0),
            uirevision=True,
            mapbox_style="carto-darkmatter",
            legend=dict(yanchor="top", y=0.5, xanchor="left", x=0.01),
            coloraxis_colorbar=dict(
                yanchor="top",
                y=1.0,
                xanchor="left",
                x=0.01,
                orientation="h",
                ticks="outside",
                dtick=1,
                len=400,
                lenmode="pixels",
                thicknessmode="pixels",
                thickness=26,
                title="Magnitude",
            ),
        )

        return fig


def app(url):
    earthquake = Earthquake(url)
    fig = earthquake.world_map()

    st.plotly_chart(fig)
    st.markdown(
        """<style>
        .block-container {
            padding: 0;
            overflow: hidden;
        }
        .stApp > header {
            background: transparent;
        }
    </style>""",
        unsafe_allow_html=True,
    )
