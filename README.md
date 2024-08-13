# Project Name: Weather Data ETL Pipeline

## Overview
This project develops an ETL (Extract, Transform, Load) pipeline that fetches weather data from the OpenWeatherMap API, processes the data, and stores it into a SQLite database. This allows for the efficient storage and retrieval of weather conditions for specified cities.

## Technologies
Python
Pandas
SQLAlchemy
SQLite
Requests

## Features
Fetch weather data using the OpenWeatherMap API.
Transform data by normalizing JSON response and converting temperatures from Kelvin to Celsius.
Load data into a SQLite database for persistent storage.

## How to Use
Ensure Python and required packages (pandas, sqlalchemy, requests) are installed.
Run the script using python etl.py to fetch, process, and store weather data for London.
Data is stored in weather_data.db, which can be queried using any SQLite client.

## Future Improvements
Implement functionality to dynamically change the city via a web interface.
Enhance data visualization and reporting capabilities.
