import requests
import json

def get_weather_data(location):
    api_key = '7cd8f95a86c199b3b4573e54fd747e41'
    base_url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'

    # Make the API request to retrieve weather data
    response = requests.get(base_url)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            weather_data = response.json()
            return weather_data
        except json.decoder.JSONDecodeError as e:
            print("Error: Failed to parse JSON response.")
            print("Error details:", str(e))
    else:
        print("Error: Failed to retrieve weather data.")
    return None


def display_weather(weather_data):
    if weather_data is not None:
        # Extract relevant weather information
        temperature_kelvin = weather_data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']
        description = weather_data['weather'][0]['description']

        # Display the weather information
        print("Temperature:", temperature_celsius, "°C")
        print("Humidity:", humidity, "%")
        print("Wind Speed:", wind_speed, "m/s")
        print("Description:", description)
    else:
        print("No weather data to display.")

def main():
    # Prompt the user to enter the name of a city or a zip code
    location = input("Enter a city name or zip code: ")

    # Get the weather data for the specified location
    weather_data = get_weather_data(location)

    # Display the weather information
    display_weather(weather_data)

# Run the main function
if __name__ == '__main__':
    main()
