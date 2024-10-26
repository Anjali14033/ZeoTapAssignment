from flask import jsonify
from app.models import WeatherData, DailySummary
from flask import Blueprint, render_template
from datetime import datetime, timedelta

# Define the blueprint for main
main = Blueprint('main', __name__)

# Root route to render index.html
@main.route('/')
def index():
    # Get the latest daily summaries for the past 7 days
    summaries = DailySummary.query.order_by(DailySummary.date.desc()).limit(7).all()
    
    # Get the latest real-time weather data for each city (last fetched data)
    cities = WeatherData.query.with_entities(WeatherData.city).distinct().all()
    latest_weather_data = []
    
    for city in cities:
        latest_data = (
            WeatherData.query.filter_by(city=city.city)
            .order_by(WeatherData.timestamp.desc())
            .first()
        )
        if latest_data:
            latest_weather_data.append(latest_data)
    
    return render_template('index.html')


@main.route('/weather_data')
def weather_data():
    # Fetch the latest weather data from the database
    weather_data = WeatherData.query.order_by(WeatherData.timestamp.desc()).all()

    # Convert the data into a format suitable for JSON response
    data = [
        {
            'city': w.city,
            'temperature': w.temperature,
            'feels_like': w.feels_like,
            'condition': w.condition,
            'timestamp': w.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        } for w in weather_data
    ]
    return jsonify(data)
    # return render_template('./templates/static/js/index.html', data=data)
    # return render_template('./templates/static/js/index.html', data=jsonify(data))

@main.route('/daily_summary')
def daily_summary():
    # Fetch the latest daily summaries for the past 7 days
    # summaries = DailySummary.query.order_by(DailySummary.date.desc()).limit(7).all()
    # Get the current time and calculate 10 minutes prior
    # Fetch the latest daily summaries for the past 7 days
    seven_days_ago = datetime.utcnow() - timedelta(days=7)
    
    # Fetch only the last 7 days of data in descending order by date
    recent_data = DailySummary.query.filter(
        DailySummary.date >= seven_days_ago
    ).order_by(DailySummary.date.desc()).all()

    # Convert the summaries to a JSON-compatible format
    data = [
        {
            'city': summary.city,
            'date': summary.date.strftime('%Y-%m-%d') if summary.date else None,
            'avg_temp': summary.avg_temp,
            'max_temp': summary.max_temp,
            'min_temp': summary.min_temp,
            'dominant_condition': summary.dominant_condition
        }
        for summary in recent_data
    ]
    return jsonify(data)
