# Intermediate Task 3: API Integration

import requests


def get_weather(city_name, api_key):
    try:
        # API endpoint
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

        # Send a GET request to the API
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            # Extract weather information
            city = data['name']
            temperature = data['main']['temp']
            description = data['weather'][0]['description']
            humidity = data['main']['humidity']

            # Display the weather details
            print(f"Weather in {city}:")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
            print(f"Humidity: {humidity}%")
        else:
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    city_name = input("Enter the city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city_name, api_key)