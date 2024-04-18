# Earthquake Explorer
[Application Demo](https://earthquake-explorer.streamlit.app/)
## Overview
Earthquake Explorer is a Python-based web application that offers real-time,
comprehensive visualizations of global earthquake activities. Through the use
of GeoJSON data, the tool highlights seismic events on a dynamic world map,
classifies earthquakes by magnitude, and identifies the most active seismic zones.

<img src="https://github.com/larissapoghosyan/earthquake-explorer/assets/43134338/082f70cd-f195-4245-ba29-f6633cdbe1cd">


## Features
- **Real-Time Seismic Activity Map**: Presents a detailed world map visualizing near real-time earthquake data. The data ranges from an hour to a month's worth of seismic events, offering a comprehensive view of global earthquake activity.
- **Geographical Classification**: The tool provides city and country level data for each recorded earthquake. By utilizing reverse geocoding techniques, it links each seismic event to its specific geographical location.
- **Earthquake Classification**: Based on their magnitudes, seismic events are categorized into classes such as 'Minor', 'Light', 'Moderate', 'Strong', 'Major', and 'Great'.
- **Seismic Data Analysis**: Earthquake Explorer features an analysis module to identify the strongest earthquakes and the most seismic zones.
- **Flexible Time Range Selection**: Users can set a specific time range for viewing earthquake data, which can range from an hour to an entire month.

<img src="https://github.com/larissapoghosyan/earthquake-explorer/assets/43134338/dbb70881-aad3-4d72-b2b5-bedc95465def">
<img src="https://github.com/larissapoghosyan/earthquake-explorer/assets/43134338/2d9ca2a4-d754-4b61-8058-36fead41e8f1">


## Installation

1. Clone this repository:<br />
```sh
git clone git@github.com:larissapoghosyan/earthquake-explorer.git
```
2. Install requirements:<br />
```sh
pip install -r requirements.txt
```


## Running the Application

```sh
streamlit run main.py
```
