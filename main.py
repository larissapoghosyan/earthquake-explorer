import streamlit as st

import earthquake
import analysis

st.set_page_config(
    layout="wide",
    page_title="Recent Earthquakes",
    page_icon="🌍",
)

pages = {
    "Earthquake": earthquake.app,
    "Analysis": analysis.app,
}


def app():
    st.sidebar.title("Navigation")
    st.sidebar.markdown("### Pages")

    page = st.sidebar.radio("page", pages.keys())
    st.sidebar.markdown("---")

    api_provider = (
        "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_{}.geojson"
    )
    timerange = st.sidebar.select_slider(
        "range", ["hour", "day", "week", "month"], value="month"
    )

    url = api_provider.format(timerange)

    pages[page](url)


app()
