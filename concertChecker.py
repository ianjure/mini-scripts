import os
import requests

seatgeek_secret = os.environ["SEATGEEK_SECRET"]
seatgeek_clientID = os.environ["SEATGEEK_CLIENT_ID"]

URL_SEATGEEK = 'https://api.seatgeek.com/2/events'

API_KEY = '814db86ef343e43d2f8d27eafccefff1'
URL_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'

city = input('Enter a city: ')
request_url_weather = f'{URL_WEATHER}?appid={API_KEY}&q={city}'
response_weather = requests.get(request_url_weather)

if response_weather.status_code == 200:
    data_weather = response_weather.json()

    coordlon = data_weather['coord']['lon']
    coordlat = data_weather['coord']['lat']

    cln = str(coordlon)
    clt = str(coordlat)

request_url_seatgeek = f'{URL_SEATGEEK}?client_id={seatgeek_clientID}&geoip=true&lat={clt}&lon={cln}'
response_seatgeek = requests.get(request_url_seatgeek)

if response_seatgeek.status_code == 200:
    data = response_seatgeek.json()

    for x in range(0, len(data['events'])):

        print(' ')
        print('Name:', data['events'][x]['performers'][0]['name'])
        print('Type:', data['events'][x]['type'])
        print('Location:', data['events'][x]['venue']['display_location'])
        print('Venue:', data['events'][x]['venue']['name'])
        print('Date:', data['events'][x]['datetime_utc'])

else:
    print('An error occured.')
