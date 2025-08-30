import requests

# Function to fetch weather data from OpenWeatherMap API
def get_weather(city, unit="metric"):
    api_key = "6e51cb12fd423037b17bc818e14e5078"  # 🔑 Replace with your OpenWeatherMap API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": city,
        "appid": api_key,
        "units": unit  # "metric" for Celsius, "imperial" for Fahrenheit
    }
    
    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            feels_like = data["main"]["feels_like"]
            desc = data["weather"][0]["description"].capitalize()
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            unit_symbol = "°C" if unit == "metric" else "°F"
            speed_unit = "m/s" if unit == "metric" else "mph"

            return (f" Weather in {city}:\n"
                    f" Temperature: {temp}{unit_symbol}\n"
                    f" Feels like: {feels_like}{unit_symbol}\n"
                    f" Condition: {desc}\n"
                    f" Humidity: {humidity}%\n"
                    f" Wind Speed: {wind} {speed_unit}")
        else:
            return f" Error: {data.get('message', 'Unable to fetch weather')}"
    
    except requests.exceptions.RequestException as e:
        return f" Network Error: {e}"

# Main program
if __name__ == "__main__":
    print("===  Weather App ===")
    city = input("Enter city name: ").strip()

    if not city:
        print(" Please enter a valid city name.")
    else:
        unit_choice = input("Choose unit (C for Celsius, F for Fahrenheit): ").strip().lower()
        unit = "metric" if unit_choice == "c" else "imperial"

        weather_report = get_weather(city, unit)
        print("\n" + weather_report)
