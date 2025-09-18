# Demonstrates how to pass parameters to an API endpoint and process the JSON response.

# Import necessary libraries
import requests
from datetime import datetime

# Define your latitude and longitude into constants
MY_LAT = -7.552330
MY_LNG = 110.820709

# Define parameters for the API request
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # ISO format (UTC)
}

# Make the API request
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, timeout=5)
response.raise_for_status()
data = response.json()

# Extract sunrise and sunset times from the response
sunrise_str = data["results"]["sunrise"]
sunset_str = data["results"]["sunset"]

# Convert to datetime objects (UTC)
sunrise_utc = datetime.fromisoformat(sunrise_str)
sunset_utc = datetime.fromisoformat(sunset_str)

# Convert to local timezone
sunrise_local = sunrise_utc.astimezone()
sunset_local = sunset_utc.astimezone()
time_now = datetime.now().astimezone()

# Format to 12-hour clock with AM/PM
sunrise_fmt = sunrise_local.strftime("%I:%M %p")
sunset_fmt = sunset_local.strftime("%I:%M %p")
time_now_fmt = time_now.strftime("%I:%M %p")

print(f"Sunrise (UTC):   {sunrise_utc}")
print(f"Sunset  (UTC):   {sunset_utc}")
print(f"Sunrise (Local): {sunrise_local} -> {sunrise_fmt}")
print(f"Sunset  (Local): {sunset_local} -> {sunset_fmt}")
print(f"Time now:        {time_now} -> {time_now_fmt}")
