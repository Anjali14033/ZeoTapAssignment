document.addEventListener('DOMContentLoaded', function() {
    // Function to fetch and display real-time weather data
    function fetchWeatherData() {
        fetch('/weather_data')
            .then(response => response.json())
            .then(data => {
                const weatherContainer = document.getElementById('real-time-weather');
                if (weatherContainer) {
                    weatherContainer.innerHTML = '';
                    data.forEach(item => {
                        const weatherCard = document.createElement('div');
                        weatherCard.className = 'weather-card';
                        weatherCard.innerHTML = `
                            <h3>${item.city}</h3>
                            <p>Temperature: ${item.temperature}°C</p>
                            <p>Feels Like: ${item.feels_like}°C</p>
                            <p>Condition: ${item.condition}</p>
                            <p>Last Updated: ${item.timestamp}</p>
                        `;
                        weatherContainer.appendChild(weatherCard);
                    });
                } else {
                    console.error("Element with ID 'real-time-weather' not found.");
                }
            })
            .catch(error => console.error('Error fetching weather data:', error));
    }

    // Function to fetch and display daily summary data
    function fetchDailySummary() {
        fetch('/daily_summary')
            .then(response => response.json())
            .then(data => {
                const summaryContainer = document.getElementById('weather-summary');
                if (summaryContainer) {
                    summaryContainer.innerHTML = '';
                    data.forEach(item => {
                        const summaryCard = document.createElement('div');
                        summaryCard.className = 'summary-card';
                        summaryCard.innerHTML = `
                            <h3>${item.city} - ${item.date}</h3>
                            <p>Average Temperature: ${item.avg_temp}°C</p>
                            <p>Max Temperature: ${item.max_temp}°C</p>
                            <p>Min Temperature: ${item.min_temp}°C</p>
                            <p>Dominant Condition: ${item.dominant_condition}</p>
                        `;
                        summaryContainer.appendChild(summaryCard);
                    });
                } else {
                    console.error("Element with ID 'weather-summary' not found.");
                }
            })
            .catch(error => console.error('Error fetching daily summary data:', error));
    }

    // Fetch real-time weather data every 1 min (or adjust as needed)
    setInterval(fetchWeatherData, 60000);
    // Fetch the daily summary data once when the page loads
    fetchWeatherData();
    fetchDailySummary();
});
