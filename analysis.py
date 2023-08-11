import streamlit as st
import pandas as pd
from dataset import DataSet
from typing import Dict, List, Any


class Analysis:
    def __init__(self, url: str):
        ds = DataSet()
        self.processed_data: Dict[str, List[Any]] = ds.retrieve_processed_data(url)
        self.dataset = pd.DataFrame(self.processed_data)

    def strongest_earthquakes(self):
        sorted = self.dataset.sort_values("mag", ascending=False)
        return sorted.head(30)

    def find_seismic_cities(self):
        seismic_cities = (
            self.dataset.groupby("location")["mag"]
            .agg(["count", "mean", "var"])
            .sort_values(by="count", ascending=False)
            .head(30)
        )
        return seismic_cities


def app(url):
    st.sidebar.header("Plotting Demo")
    analysis = Analysis(url)
    # Creating a header
    st.header("The Strongest Earthquakes")

    # Showing the strongest earthquakes
    st.write(analysis.strongest_earthquakes())

    # Showing the most seismic zones
    st.header("The most Seismic Cities")
    st.write(analysis.find_seismic_cities())

    st.header("Header 2")
    st.table(pd.DataFrame({"col1": ["item1", "item2"], "col2": ["item1", "item2"]}))
