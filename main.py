import schedule
import time
from weather_data.weather_monitor import WeatherMonitor

def main():
    weather_monitor = WeatherMonitor(api_key='YOUR_API_KEY')
    schedule.every(5).minutes.do(weather_monitor.retrieve_weather_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    main()
