from flask import Flask, render_template, request, redirect, url_for
from utils import fetch_weather_data, fetch_weather_forecast, summarize_forecast

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Weather route (handles POST request from the form)
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form.get('city')
    if city:
        try:
            # Fetch current weather data for the city
            data = fetch_weather_data(city)
            # Fetch the 5-day weather forecast data for the city
            forecast_data = fetch_weather_forecast(city)
            # Summarize the forecast data
            forecast_summary = summarize_forecast(forecast_data)
            
            # Pass the weather data and forecast summary to the results page
            return render_template('results.html', weather_info=data, forecast_info=forecast_summary)
        except Exception as e:
            return render_template('error.html', error=str(e))
    else:
        return render_template('error.html', error="City not provided.")

# Redirect the user if they try to visit /weather directly with a GET request
@app.route('/weather', methods=['GET'])
def weather_get():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
