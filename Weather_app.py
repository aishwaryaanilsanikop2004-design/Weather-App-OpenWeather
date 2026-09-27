import requests

API_KEY = "e9fb4bf0ec14dd661c7f3eaf0ed430e5"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print("\n===== WEATHER INFORMATION =====")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])
    print("Wind Speed:", data["wind"]["speed"], "m/s")
    print("===============================")

elif response.status_code == 401:
    print("Invalid API key.")

elif response.status_code == 404:
    print("City not found.")

else:
    print("Error:", response.status_code)