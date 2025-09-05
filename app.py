from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Your WeatherAPI key
API_KEY = "1246a31f7fe341c3abb61141250509"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None
    
    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
            response = requests.get(url)
            data = response.json()
            
            if "error" in data:
                error = data["error"]["message"]
            else:
                weather_data = {
                    "city": data["location"]["name"],
                    "country": data["location"]["country"],
                    "time": data["location"]["localtime"],
                    "temp": data["current"]["temp_c"],
                    "condition": data["current"]["condition"]["text"],
                    "icon": data["current"]["condition"]["icon"],
                    "wind": data["current"]["wind_kph"],
                    "humidity": data["current"]["humidity"]
                }

    return render_template("index.html", weather=weather_data, error=error)

# For Vercel, no need for app.run()
app = app


