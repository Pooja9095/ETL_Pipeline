import pandas as pd
from sqlalchemy import create_engine
import requests

# Configuration
API_KEY = '34f15e62b004325e61228ce04b9189fb'
CITY = 'London'
API_URL = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}'
DATABASE_URL = 'sqlite:///C:/Users\mailp\Desktop\ETL_Pipeline\data\weather_data.db'

def extract_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return pd.json_normalize(data)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame()

def transform_data(df):
    # Convert temperature from Kelvin to Celsius
    if not df.empty and 'main.temp' in df:
        df['main.temp'] = df['main.temp'].apply(lambda x: x - 273.15)

    # Simplify the data structure for database storage
    if not df.empty:
        weather_description = df['weather'].iloc[0][0]['description'] if df['weather'].any() else None
        df = df[['main.temp', 'main.humidity', 'main.pressure', 'wind.speed']].copy()
        df['Weather_Description'] = weather_description
        df.columns = ['Temperature_Celsius', 'Humidity', 'Pressure', 'Wind_Speed', 'Weather_Description']
        # Insert the city name as the first column
        df.insert(0, 'City', CITY)
    return df

def load_data(df):
    if not df.empty:
        engine = create_engine(DATABASE_URL)
        df.to_sql('weather_data', engine, index=False, if_exists='replace')

if __name__ == '__main__':
    df = extract_data()
    if not df.empty:
        df = transform_data(df)
        load_data(df)
