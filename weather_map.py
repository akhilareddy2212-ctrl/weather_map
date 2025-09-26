import requests
from config import API_KEY   # Import your API key from config.py


# Function to fetch weather from OpenWeatherMap API
def get_weather(city, api_key):
    """
    Fetches weather details for a given city from OpenWeatherMap API.
    Returns a dictionary with city, temperature, humidity, and description.
    """
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        # Check if city is found
        if response.status_code == 200:
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"].capitalize()
            }
            return weather
        else:
            # If API returns error (e.g., city not found)
            print(f"Error: {data.get('message', 'Unable to fetch weather data')}")
            return None

    except Exception as e:
        print("An error occurred while fetching weather:", e)
        return None


# Function to display weather neatly
def view_weather(weather_data):
    """
    Displays the weather information in a readable format.
    """
    if weather_data:
        print("\n===== Weather Report =====")
        print(f"City: {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Description: {weather_data['description']}")
        print("==========================\n")
    else:
        print("No weather data available.\n")


# Menu Function
def menu():
    """
    Displays menu options and handles user input.
    """
    while True:
        print("===== Weather Map Application =====")
        print("1. Get Weather by City")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather = get_weather(city, API_KEY)
            view_weather(weather)

        elif choice == "2":
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")


# Run the application
if __name__ == "__main__":
    menu()
