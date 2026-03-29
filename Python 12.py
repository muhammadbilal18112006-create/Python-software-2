# QUESTION NO 1

import requests

response = requests.get("https://api.chucknorris.io/jokes/random")
data = response.json()

print(data["value"])


# QUESTION NO 2

import requests

city = input("Enter municipality name: ")
api_key = "YOUR_API_KEY_HERE"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

weather = data["weather"][0]["description"]
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15

# print results
print("Weather:", weather)
print("Temperature:", round(temp_celsius, 1), "°C")