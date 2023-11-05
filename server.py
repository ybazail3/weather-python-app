# Importing modules flask, weather, and waitress.
# Flask = Helps create web applications for Python
# render_template = is used to generate output from a file
# request =  Allows you to send HTTP requests using Python, Syntax: requests.methodname(params).
# weather = We are calling the function get weather from our file weather.py
# waitress = WSGI (web Server Gateway Interface) server it has no dependies only the ones that live in the standard Python library. It supports HTTP.
from flask import Flask, render_template, request
from weather import get_weather
from waitress import serve

# Creating a Flask application object --app--
app = Flask(__name__)

# app routing to a specific URL
# app routing to the index.html file


@app.route('/')
@app.route('/index')
# Created a function name index()
def index():
    # render_template is used to generate output from file index.html
    return render_template('index.html')

# app routing to the weather.html file


@app.route('/weather')
# Creating a function named get_current_weather()
def get_current_weather():
    # Creating an object named city and getting the argument city
    city = request.args.get('city')

    # Check for empty string or string with only spaces. If the string is empty or has only spaces by default show San Diego.
    if not bool(city.strip()):
        city = "San Diego"

    # Creating an object name weather_data and using the get_weather function to pass through the city name.
    weather_data = get_weather(city)

    # City is not found by API
    if not weather_data['cod'] == 200:
        # render_template is used to generate output from file city-not-found.html
        return render_template('city-not-found.html')

    # render_template is used to generate output from file weather.html
    return render_template(
        "weather.html",
        # We are using the format method to extract data from our weather API. The name of the city, description, temperature, and what the temperature feels like.
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )


# if the name of the file is main run the application on localserver:8000. This can be don eon your browser.
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
