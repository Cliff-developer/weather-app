# WeatherWise - Your Smart Weather Companion

WeatherWise is a web-based weather application that allows users to get real-time weather updates and 5-day weather forecasts. With an intuitive and user-friendly interface, it provides essential weather information, such as temperature, weather description, humidity, and more.

## Features

- **Current Weather:** Get the latest weather information for any city.
- **5-Day Forecast:** Access detailed weather forecasts for the upcoming days.
- **Error Handling:** Displays appropriate error messages when data fetching fails or when the city name is invalid.
- **Professional Design:** The app features a clean, responsive design for an optimal user experience.

## Future Advancements

1. **Voice Commands:** Add voice recognition to allow users to get weather updates and forecasts using speech commands. This will provide a more interactive and hands-free experience.
2. **Predictive Weather Analysis with Machine Learning:** Integrate machine learning algorithms to predict future weather patterns based on historical data, improving forecasting accuracy.
3. **Severe Weather Alerts:** Incorporate severe weather warnings and alerts (e.g., storms, floods, hurricanes) to help users stay informed of dangerous weather events.

## Requirements

Before running the app, ensure that you have the following:

- **Python 3.x** installed on your computer.
- **Flask** for creating the web application.
- **Requests** library for making API calls.
- **OpenWeatherMap API Key** for fetching weather data.

### Required Libraries

To install the necessary dependencies, run the following command:

```bash
pip install -r requirements.txt


Setup Instructions
1. Clone the repository
Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/yourusername/WeatherWise.git
2. Configure the API Key
Go to OpenWeatherMap and sign up for an API key.
Save your API key in the config.py file.
python
Copy code
# config.py
API_KEY = "your_openweathermap_api_key"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"
3. Run the Application
Navigate to the project directory and run the Flask application using the following command:

bash
Copy code
python web.py
The application will start running on http://127.0.0.1:5000/.

4. Open the Application
Open your web browser and go to http://127.0.0.1:5000/ to start using the WeatherWise app.

5. Interact with the App
Enter a city name in the form provided.
Get the current weather and the 5-day weather forecast for the specified city.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
We welcome contributions to improve the app! Feel free to fork the repository, make your changes, and submit a pull request.