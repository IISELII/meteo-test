from weather_fonction import get_weather
import requests

def test_get_weather(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        'city': {'coord': {'lat': 48.8566, 'lon': 2.3522}},
        'list': [{'main': {'temp': 20}}] + [{'main': {'temp': 21}}] * 8 + [{'main': {'temp': 22}}] * 8
    }
    mocker.patch.object(requests, 'get', return_value=mock_response)

    API_KEY = '4ad9f7e8f81acbf1697cbb1860bac9c1'
    city = "Paris"
    coords, today, tomorrow, day_after_tomorrow = get_weather(city, API_KEY)

    assert coords['lat'] == 48.8566
    assert coords['lon'] == 2.3522
    assert today == 20
    assert tomorrow == 21
    assert day_after_tomorrow == 22