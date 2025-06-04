from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "Enter your API"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    error_message = None

    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            params = {
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            }
            try:
                response = requests.get(BASE_URL, params=params)
                response.raise_for_status()
                data = response.json()

                if data.get("weather") and data.get("main"):
                    weather_data = {
                        'city': f"{data['name']}, {data['sys']['country']}",
                        'temperature': round(data['main']['temp']),
                        'feels_like': round(data['main']['feels_like']),
                        'humidity': data['main']['humidity'],
                        'description': data['weather'][0]['description'].capitalize(),
                        'icon_url': f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
                    }
                else:
                    error_message = data.get("message", "Invalid data received from API.")
            except requests.exceptions.HTTPError as http_err:
                if response.status_code == 401:
                    error_message = "Invalid API Key."
                elif response.status_code == 404:
                    error_message = f"City '{city}' not found."
                else:
                    error_message = f"HTTP Error: {http_err}"
            except requests.exceptions.RequestException as req_err:
                error_message = f"Network error: {req_err}"
            except Exception as e:
                error_message = f"Unexpected error: {e}"
        else:
            error_message = "City name cannot be empty."

    return render_template('index.html', weather_data=weather_data, error_message=error_message)

if __name__ == '__main__':
    app.run(debug=True)
