import tkinter as tk
from tkinter import messagebox
from utils import fetch_weather_data, fetch_weekly_forecast, summarize_forecast

def display_weather():
    city = city_entry.get()
    try:
        data = fetch_weather_data(city)
        weather_label.config(
            text=f"Weather: {data['weather'][0]['description'].capitalize()}"
        )
        temp_label.config(text=f"Temperature: {data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {data['main']['humidity']}%")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def display_forecast():
    city = city_entry.get()
    try:
        data = fetch_weekly_forecast(city)
        forecast = summarize_forecast(data)
        forecast_label.config(text=forecast)
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title("Weather App")
app.geometry("500x400")

# Input field
city_entry = tk.Entry(app, width=30)
city_entry.pack(pady=10)

# Buttons
current_weather_button = tk.Button(
    app, text="Get Current Weather", command=display_weather
)
current_weather_button.pack(pady=5)

forecast_button = tk.Button(app, text="Get Weekly Forecast", command=display_forecast)
forecast_button.pack(pady=5)

# Output labels
weather_label = tk.Label(app, text="Weather: --", font=("Arial", 12))
weather_label.pack(pady=5)

temp_label = tk.Label(app, text="Temperature: --", font=("Arial", 12))
temp_label.pack(pady=5)

humidity_label = tk.Label(app, text="Humidity: --", font=("Arial", 12))
humidity_label.pack(pady=5)

forecast_label = tk.Label(
    app, text="Weekly Forecast:\n--", font=("Arial", 12), justify="left"
)
forecast_label.pack(pady=10)

app.mainloop()
