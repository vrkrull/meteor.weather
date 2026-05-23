import requests


class WeatherProvider:
    name = "Base"

    def get_weather(self, lat, lon, units="metric"):
        raise NotImplementedError


# ---------------- OPEN-METEO (primary) ----------------
class OpenMeteoProvider(WeatherProvider):
    name = "Open-Meteo"

    def get_weather(self, lat, lon, units="metric"):
        temp_unit = "fahrenheit" if units == "imperial" else "celsius"
        wind_unit = "mph" if units == "imperial" else "kmh"

        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}"
            "&current="
            "temperature_2m,apparent_temperature,wind_speed_10m,"
            "wind_direction_10m,relative_humidity_2m,pressure_msl,"
            "visibility,weather_code"
            "&hourly=temperature_2m"
            "&daily=temperature_2m_max,temperature_2m_min"
            f"&temperature_unit={temp_unit}"
            f"&windspeed_unit={wind_unit}"
            "&timezone=auto"
        )

        d = requests.get(url, timeout=10).json()
        c = d.get("current", {})

        return {
            "current": {
                "temp": c.get("temperature_2m"),
                "feels_like": c.get("apparent_temperature"),
                "wind": c.get("wind_speed_10m"),
                "wind_dir": c.get("wind_direction_10m"),
                "humidity": c.get("relative_humidity_2m"),
                "pressure": c.get("pressure_msl"),
                "visibility": c.get("visibility"),
                "code": c.get("weather_code"),
            },
            "hourly": d.get("hourly", {}),
            "daily": d.get("daily", {})
        }


# ---------------- WTTR fallback ----------------
class WttrProvider(WeatherProvider):
    name = "wttr.in"

    def get_weather(self, lat, lon, units="metric"):
        r = requests.get(f"https://wttr.in/{lat},{lon}?format=j1", timeout=10)
        d = r.json()

        c = d["current_condition"][0]

        return {
            "current": {
                "temp": c["temp_C"] if units == "metric" else c["temp_F"],
                "feels_like": c["FeelsLikeC"],
                "wind": c["windspeedKmph"],
                "humidity": c["humidity"],
                "pressure": c["pressure"],
                "visibility": c["visibility"],
                "desc": c["weatherDesc"][0]["value"]
            },
            "hourly": d["weather"][0]["hourly"],
            "daily": d["weather"]
        }


PROVIDERS = [
    OpenMeteoProvider(),
    WttrProvider()
]