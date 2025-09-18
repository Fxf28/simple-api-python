# Making a GET request to the Open Notify API to get the current location of the ISS

# Importing the requests library to make an API call
import requests

# Create a variable called response to store the response from the API call
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Check if the request was successful
response.raise_for_status()

# Create a variable called data to store the JSON data from the response
data = response.json()

# Extract the longitude and latitude of the ISS from the data
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

# Create a tuple called iss_position to store the longitude and latitude
iss_position = (longitude, latitude)

# Print the current location of the ISS
print(f"The ISS is currently at longitude {longitude} and latitude {latitude}.")
print(iss_position)