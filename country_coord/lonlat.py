# country_coordinates/__init__.py

def get_coordinates(country):
    coordinates = {
        "Ghana": {
            "longitude": (-3.5, 1.2),
            "latitude": (4, 11.5)
        },
        # Add more countries here
    }
    
    country_data = coordinates.get(country)
    if country_data:
        return country_data['longitude'], country_data['latitude']
    else:
        return None, None
