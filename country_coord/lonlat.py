# country_coordinates/__init__.py


import os 
import json


def _load_coordinates(filepath: str = os.path.join(os.path.dirname(__file__), "coordinates.json")) -> dict:
    """
    Load the coordinate data from a JSON file.

    Parameters:
        filepath (str): Path to the JSON file containing coordinate data.

    Returns:
        dict: A dictionary containing the coordinate data.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If the JSON file cannot be decoded.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Coordinates file not found: {filepath}")
    with open(filepath, "r") as file:
        return json.load(file)
    


# Load the coordinates once so it's available for get_coordinates.
_COORDINATES = _load_coordinates()

def get_coordinates(country: str) -> tuple:
    """
    Retrieve the longitude and latitude boundaries for the specified country.

    Parameters:
        country (str): The country name to retrieve coordinates for.

    Returns:
        tuple: A tuple of two elements:
            - longitude (tuple): (min_longitude, max_longitude)
            - latitude (tuple): (min_latitude, max_latitude)

    Raises:
        ValueError: If the country is not found in the coordinate database.
    """
    try:
        country_data = _COORDINATES[country]
        # Convert lists from JSON to tuples.
        lon = tuple(country_data['longitude'])
        lat = tuple(country_data['latitude'])
        return lon, lat
    except KeyError:
        raise ValueError(f"Coordinates for country '{country}' not found")
