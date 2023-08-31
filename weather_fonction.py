import requests
import streamlit as st

BASE_URL = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = st.secrets["API_KEY"]

def get_weather(city, API_KEY):
    params = {
        'q': city,
        'units': 'metric',
        'appid': API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()

    coords = data['city']['coord']
    today = data['list'][0]['main']['temp']
    tomorrow = data['list'][8]['main']['temp']
    day_after_tomorrow = data['list'][16]['main']['temp']

    return coords, today, tomorrow, day_after_tomorrow