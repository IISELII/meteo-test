import streamlit as st
import pydeck as pdk
import requests

# Configuration de l'API météo
# API_KEY = st.secrets["API_KEY"]
API_KEY = '4ad9f7e8f81acbf1697cbb1860bac9c1'
BASE_URL = "http://api.openweathermap.org/data/2.5/forecast"

def get_weather(city):
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


st.title("Mon application Streamlit")

# Partie Gauche
with st.sidebar:
    st.write("Recherche météo")
    city = st.text_input("Entrez une ville :")
    if st.button("Recherche"):
        try:
            coords, today, tomorrow, day_after_tomorrow = get_weather(city)
            st.write(f"Aujourd'hui : {today}°C")
            st.write(f"Demain : {tomorrow}°C")
            st.write(f"Après Demain : {day_after_tomorrow}°C")
            
            # Centrer la carte sur les coordonnées de la ville
            view_state = pdk.ViewState(
                latitude=coords['lat'],
                longitude=coords['lon'],
                zoom=10
            )
            
            # Ajouter une ScatterplotLayer pour indiquer l'emplacement de la ville
            scatter_layer = pdk.Layer(
                "ScatterplotLayer",
                data=[{
                    'position': [coords['lon'], coords['lat']],
                    'color': [255, 0, 0, 255],
                    'radius': 1000
                }],
                get_position='position',
                get_radius='radius',
                get_fill_color='color',
                pickable=True,
                filled=True
            )

            deck = pdk.Deck(layers=[scatter_layer],
                            map_style='mapbox://styles/mapbox/light-v9',
                            initial_view_state=view_state)
            st.pydeck_chart(deck)
            
        except:
            st.write("Veuillez entrer une ville valide ou vérifier votre clé API.")

# Partie Droite
france_coordinates = [2.2137, 46.603354]
view_state = pdk.ViewState(
    latitude=france_coordinates[1],
    longitude=france_coordinates[0],
    zoom=5
)

deck = pdk.Deck(map_style='mapbox://styles/mapbox/light-v9',
                initial_view_state=view_state)
st.pydeck_chart(deck)
