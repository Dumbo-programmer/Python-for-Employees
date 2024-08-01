#Weather Forecast
import requests

def get_weather():
    print("Welcome to the Weather Forecast Script!")
    city = input("Enter the city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"Weather in {city}: {data['weather'][0]['description']}")
        print(f"Temperature: {data['main']['temp']}K")
    else:
        print("Failed to retrieve weather data.", data)

if __name__ == "__main__":
    get_weather()
