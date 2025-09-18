import time
import requests
from datetime import datetime
import smtplib
from config import *

def check_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (MY_LNG - 5) <= iss_longitude <= (MY_LNG + 5):
        return True
    else:
        return False
    
def is_night_time():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunrise < time_now.hour < sunset:
        return False
    else:
        return True

def is_overhead_and_night():
    if check_iss_position() and is_night_time():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, 
            to_addrs=EMAIL, 
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky!")
        connection.close()
        return print(True)
    else:
        return print(False)

while True:
    is_overhead_and_night()
    time.sleep(60)


