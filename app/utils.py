import requests
from config import API_KEY, BASE_URL, FORECAST_URL

def fetch_weather_data(city):
    """Fetches current weather data for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(response.json().get("message", "Error fetching weather data."))

def fetch_weather_forecast(city):
    """Fetches a 5-day forecast for a given city."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(FORECAST_URL, params=params)
    if response.status_code == 200:
        return response.json()  # Return the JSON response containing forecast data
    else:
        raise Exception(response.json().get("message", "Error fetching forecast data."))

def summarize_forecast(data):
    """Summarizes the 5-day forecast."""
    
    # Ensure the data contains the 'list' key (which holds the forecast data)
    if 'list' not in data:
        raise ValueError("Forecast data is missing the 'list' key.")
    
    forecast = {}
    
    # Loop through the forecast data, grouping by date
    for item in data["list"]:
        # Extract date (ignore the time part)
        date = item["dt_txt"].split(" ")[0]
        
        if date not in forecast:
            forecast[date] = {
                "temp": [],
                "description": [],
            }
        
        # Add temperature and description for each day
        forecast[date]["temp"].append(item["main"]["temp"])
        forecast[date]["description"].append(item["weather"][0]["description"])

    # Generate a summary for each date
    summary = []
    for date, info in forecast.items():
        # Calculate the average temperature for the day
        avg_temp = sum(info["temp"]) / len(info["temp"])
        
        # Get the most common weather description for the day
        desc = max(set(info["description"]), key=info["description"].count)
        
        # Format the summary for that date
        summary.append(f"{date}: {desc.capitalize()} with an average temperature of {avg_temp:.2f}°C")

    # Return the forecast summary as a string
    return "\n".join(summary)
