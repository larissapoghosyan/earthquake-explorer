import json
from cached_path import cached_path
import reverse_geocode
from datetime import datetime
from typing import List


class DataSet:
    def __init__(self):
        self.processed_data = {
            "lons": [],
            "lats": [],
            "depth_km": [],
            "mag": [],
            "location": [],
        }

    @classmethod
    def load_data(cls, url: str):
        path = cached_path(url)
        with open(path) as f:
            data = json.load(f)
        return data

    @classmethod
    def get_location_by_coordinates(cld, lats, lons):
        coordinates = []
        for i, j in zip(lats, lons):
            coordinates.append((i, j))
        return reverse_geocode.search(coordinates)

    @classmethod
    def classify_earthquakes(cls, magnitutes: List[float]):
        earthquake_classification = {
            "Minor": {"Lower": 0.0, "Upper": 2.9},
            "Light": {"Lower": 3.0, "Upper": 3.9},
            "Moderate": {"Lower": 4.0, "Upper": 4.9},
            "Strong": {"Lower": 5.0, "Upper": 5.9},
            "Major": {"Lower": 6.0, "Upper": 6.9},
            "Great": {"Lower": 7.0, "Upper": float('inf')},
        }
        classification = []
        magnitutes = [round(num, 1) for num in magnitutes]
        for mgnt in magnitutes:
            for category, bounds in earthquake_classification.items():
                if bounds["Lower"] <= mgnt <= bounds["Upper"]:
                    classification.append(category)
        return classification

    @classmethod
    def date_of_earthquake(cls, timestamps: List[int]):
        date_obj = []
        for timestamp in timestamps:
            date = datetime.fromtimestamp(timestamp / 1000)
            formatted_date = date.strftime("%Y-%m-%d %H:%M:%S")
            date_obj.append(formatted_date)
        return date_obj

    def retrieve_processed_data(self, url: str):
        data = self.load_data(url)
        timestamps = []
        from tqdm import tqdm

        for dat in tqdm(data["features"]):
            mgnt = dat["properties"]["mag"]
            timestamp = dat["properties"]["time"]
            lon, lat, depth = dat["geometry"]["coordinates"]

            if mgnt >= 0:
                self.processed_data["lons"].append(lon)
                self.processed_data["lats"].append(lat)
                self.processed_data["depth_km"].append(depth)
                self.processed_data["mag"].append(mgnt)
                timestamps.append(timestamp)

        location = self.get_location_by_coordinates(self.processed_data["lats"], self.processed_data["lons"])
        for loc in location:
            self.processed_data["location"].append((loc["country"], loc["city"]))

        classification = self.classify_earthquakes(self.processed_data["mag"])
        self.processed_data['classification'] = classification

        self.processed_data["date"] = self.date_of_earthquake(timestamps)

        return self.processed_data
