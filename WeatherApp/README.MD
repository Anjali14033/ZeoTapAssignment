# WeatherApp

## Overview
WeatherApp is a real-time weather monitoring application that retrieves and displays current weather data for user-selected locations. It utilizes a Flask-based backend server, HTML and JavaScript frontend, and integrates with external weather APIs to fetch data.

## Requirements
- Python 3.x
- Required Python libraries listed in `requirements.txt`

## Setup and Installation

1. **Navigate to the WeatherApp Directory**: 
   - Open a terminal and change the directory to where `WeatherApp` is located.
   ```bash
   cd path/to/WeatherApp
   ```
2. **Install Dependencies:**
    Install all the required Python libraries from requirements.txt.
    ```bash
    pip install -r requirements.txt
    ```
3. **How to Run the Application**

    Run the Flask Server:
    Start the application by running run.py.
    ```bash
    python run.py
    ```
    Execute Weather Fetching Script:

    In a new terminal, execute weather_fetcher.py to initiate data fetching from the weather API.
    ```bash
    python weather_fetcher.py
    ```
    Access the Application:
    Open a web browser and go to http://localhost:5000 to access the WeatherApp interface.
4. **File Structure**
        WeatherApp/
    ├── templates/
    │   ├── index.html           # Homepage template
    ├── static/
    │   ├── style.css            # CSS for styling
    ├── run.py                   # Main application file
    ├── weather_fetcher.py       # Weather data fetching script
    └── requirements.txt         # Python library requirements
    |__ .env                     # This env file stores the secret Weather API key and DB secret key

