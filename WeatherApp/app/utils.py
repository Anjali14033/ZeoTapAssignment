import requests
from app.models import WeatherData, DailySummary, db
from datetime import datetime, timedelta
from sqlalchemy import func
from flask import current_app

def fetch_weather_data(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    data = response.json()

    # Process the weather data
    temp_kelvin = data['main']['temp']
    temp_celsius = temp_kelvin - 273.15
    feels_like_celsius = data['main']['feels_like'] - 273.15
    condition = data['weather'][0]['main']

    # Store the data in the database
    weather_data = WeatherData(
        city=city,
        timestamp=datetime.fromtimestamp(data['dt']),
        temperature=round(temp_celsius, 2),
        feels_like=feels_like_celsius,
        condition=condition
    )
    db.session.add(weather_data)
    db.session.commit()

def calculate_daily_summary():
    cities = db.session.query(WeatherData.city).distinct().all()
    for city in cities:
        city_name = city[0]
        
        # Get all weather data for the current date
        today = datetime.utcnow().date()
        data_today = WeatherData.query.filter(
            WeatherData.city == city_name,
            WeatherData.timestamp >= today,
            WeatherData.timestamp < today + timedelta(days=1)
        ).all()
        
        if data_today:
            # Calculate aggregates
            avg_temp = sum(d.temperature for d in data_today) / len(data_today)
            max_temp = max(d.temperature for d in data_today)
            min_temp = min(d.temperature for d in data_today)
            
            # Determine dominant condition by frequency
            conditions = [d.condition for d in data_today]
            dominant_condition = max(set(conditions), key=conditions.count)
            
            # Save to DailySummary table
            daily_summary = DailySummary(
                city=city_name,
                date=today,
                avg_temp=avg_temp,
                max_temp=max_temp,
                min_temp=min_temp,
                dominant_condition=dominant_condition
            )
            db.session.add(daily_summary)
    db.session.commit()

def monitor_alerts(threshold=35.0):
    cities = db.session.query(WeatherData.city).distinct().all()
    for city in cities:
        city_name = city[0]
        
        # Get last two records for the city
        recent_data = WeatherData.query.filter_by(city=city_name).order_by(WeatherData.timestamp.desc()).limit(2).all()
        
        if len(recent_data) == 2:
            if recent_data[0].temperature > threshold and recent_data[1].temperature > threshold:
                # Trigger an alert
                print(f"ALERT: Temperature in {city_name} has exceeded {threshold}°C for two consecutive updates.")

