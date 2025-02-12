import requests

api_url = "https://api.openweatheropen.org/data/2.5/weather"
city = "New York"
apikey = "xfhi16veg2SJtmOtSmJTAXrCNakqlCT0"

response = requests.get(f"{api_url}?q={city}&appid={apikey}")

if response.status_code == 200:
    weather_data = response.json()
    print(f"Temperature: {data['main']['temp']}")
    print(f"Weather: {data['weather'][0]['description']}")
else:
    print("Failed to retrieve data")
