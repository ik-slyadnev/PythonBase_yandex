import requests


url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': ''

}

response = requests.get(url, params=weather_parameters)

print(response.text)