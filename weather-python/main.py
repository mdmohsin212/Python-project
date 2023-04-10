import requests

def weather(city):
    API_KEY = "a5218f9a88602bdfdfa82349666c56ab"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        main = data["main"]
        temp = main["temp"] - 273.15
        temp = round(temp, 2)
        weather = data["weather"][0]["main"]
        print(f"Temperature in {city}: {temp}°C")
        print(f"Weather: {weather}")
    else:
        print("Weather information not found.")

city = input("Enter the Name of City -> ")
weather(city)
print("Have a Nice Day!")
