import requests

API_KEY = "5a62e938741dd2211d4f4f1d5cfad4ef"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    params = {
        "q": city_name,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"\nWeather in {city_name.capitalize()}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s\n")

    except requests.exceptions.HTTPError:
        print("City not found or invalid API key.")
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")
    except KeyError:
        print("Unexpected response format.")

def main():
    print("=== Weather Application ===")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == "exit":
            print("Exiting the app.")
            break
        get_weather(city)

if __name__ == "__main__":
    main()