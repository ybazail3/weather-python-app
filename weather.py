# Importing modules dotenv, pprint, requests, os
# dotenv = This reads key=value pairs
# pprint = Allows you to print data structured in a readable, pretty way. pretty-print.
# requests = Allows you to send HTTP requests using Python, Syntax: requests.methodname(params).
# os = This moduule interacts with operating systems. This module can read, append, write, create, and delete files.
from dotenv import load_dotenv
from pprint import pprint
import requests
import os
load_dotenv()

# Created a function name get_weather and by default San Diego will be the city if the user does not type in a city


def get_weather(city="San Diego"):

    # Created an object names request_url and passing through the link to connect to the weather API also including our API Key
    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={
        os.getenv("API_KEY")}&q={city}&units=imperial'

    # Created an object names weather_data and requesting the data from the API be passed through in json format
    weather_data = requests.get(request_url).json()

    return weather_data


# If this file name is main output "Please enter city name:" for the user to type in an answer.
if __name__ == "__main__":
    print("\n***Get Current Weather Conditions ***")

    city = input("\nPlease enter a city name: ")

    # Check for empty string or string with only spaces. If there is an empty submission or submission with only space return the city San Diego as default
    if not bool(city.strip()):
        city = "San Diego"

    # Created and object named weather_data and calling the get_weather function and passing through the city (user input)
    weather_data = get_weather(city)

    print("\n")
    # Printing the weather_data in readable json format
    pprint(weather_data)
