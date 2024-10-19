import requests
import pandas as pd
from .alerts import AlertSystem

class WeatherMonitor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        self.alert_system = AlertSystem()
        self.weather_data = []

    def retrieve_weather_data(self):
        for city in self.cities:
            response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}')
            data = response.json()
            if response.status_code == 200:
                self.process_weather_data(data)
            else:
                print(f"Error retrieving data for {city}: {data['message']}")

    def process_weather_data(self, data):
        temp_k = data['main']['temp']
        temp_c = temp_k - 273.15 
        feels_like_k = data['main']['feels_like']
        feels_like_c = feels_like_k - 273.15
        main_condition = data['weather'][0]['main']

        self.weather_data.append({
            'city': data['name'],
            'temp': temp_c,
            'feels_like': feels_like_c,
            'condition': main_condition,
            'dt': data['dt']
        })

        
        self.alert_system.check_alerts(temp_c, main_condition)
