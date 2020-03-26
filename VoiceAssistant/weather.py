import requests
from geotext import GeoText
from googletrans import Translator

def check_weather(text):
    city = find_city_in_string(text)
    if city is None:
        country = find_country_instring(text)
        if country is None:
            return None
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + str(country) + '&APPID=caeadda0fd761bace210ea2cd08bf167')
        content = response.text
        print(content)
        return content
    response = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + str(city) +'&APPID=caeadda0fd761bace210ea2cd08bf167')
    content = response.text
    print(content)
    return content


def find_city_in_string(text):
    try:
        print(text)
        translator = Translator()
        translate = translator.translate(text, src='pl', dest='en')
        print(translate.text)
        cities = GeoText(translate.text).cities
        if len(cities) == 0:
            return None
        return cities[0]
    except Exception as e:
        print(e)
        pass

def find_country_instring(text):
    try:
        print(text)
        translator = Translator()
        translate = translator.translate(text, src='pl', dest='en')
        print(translate.text)
        countries = GeoText(translate.text).countries
        if len(countries) == 0:
            return None
        return countries[0]
    except Exception as e:
        print(e)
        pass