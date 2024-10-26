import os
import schedule
import time
from app.utils import fetch_weather_data, calculate_daily_summary, monitor_alerts
from app import create_app, db
from dotenv import load_dotenv

load_dotenv()
app = create_app()

# Set your API key here
OPEN_WEATHER_API_KEY = os.environ.get('OPEN_WEATHER_API_KEY')


def fetch_data():
    with app.app_context():
        cities = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
        for city in cities:
            fetch_weather_data(city, OPEN_WEATHER_API_KEY)
        monitor_alerts(threshold=35.0)  # Check for alerts after each fetch

def daily_rollup():
    with app.app_context():
        calculate_daily_summary()

# Fetch weather data at set interval
schedule.every(1).minutes.do(fetch_data)
# Run daily summary calculation at midnight
# schedule.every().day.at("00:00").do(daily_rollup)
schedule.every(1).minutes.do(daily_rollup)

while True:
    schedule.run_pending()

