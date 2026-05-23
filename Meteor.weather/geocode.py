import requests


def geocode_city(city: str):
    if not city:
        return (41.8781, -87.6298)

    try:
        r = requests.get(
            "https://nominatim.openstreetmap.org/search",
            params={"q": city, "format": "json", "limit": 1},
            headers={"User-Agent": "Meteor.weather"},
            timeout=10
        )

        data = r.json()
        if not data:
            return (41.8781, -87.6298)

        return float(data[0]["lat"]), float(data[0]["lon"])

    except Exception:
        return (41.8781, -87.6298)