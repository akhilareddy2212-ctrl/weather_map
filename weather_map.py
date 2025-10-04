import requests
from config import API_KEY

BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
def get_weather(city, api_key=API_KEY):
    """
    Fetch weather details for a given city from OpenWeatherMap API.
    Returns a dictionary with city, temperature, humidity, description.
    """
    url = f"{BASE_URL}?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            return {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"],
            }
        else:
            return {"error": data.get("message", "Unable to fetch weather data.")}
    except Exception as e:
        return {"error": str(e)}


def view_weather(weather_data):
    """
    Display weather data neatly in console.
    """
    if "error" in weather_data:
        print(f"\n Error: {weather_data['error']}\n")
    else:
        print("\n===== Weather Report =====")
        print(f"City       : {weather_data['city']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity   : {weather_data['humidity']}%")
        print(f"Condition  : {weather_data['description'].title()}")
        print("==========================\n")


def menu():
    """
    Display the menu and handle user interaction.
    """
    while True:
        print("\n===== Weather Map Application =====")
        print("1. Get Weather by City")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            city = input("Enter city name: ")
            weather_data = get_weather(city)
            view_weather(weather_data)
        elif choice == "2":
            print("\n Exiting the application. Goodbye!\n")
            break
        else:
            print("\n Invalid choice! select 1 or 2.\n")


if __name__ == "__main__":
    menu()
