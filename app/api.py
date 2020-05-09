"""
    filename: api.py

    author: Joseph Villegas

    abstract: a python file holding functions 
              to perform API calls to get user/city location
              and weather information
"""

import requests
import configure
from pyconverter import *

def get_user_location():
    """

    Makes use of an API to get location information 
    based off of the users external IP address

    API: IP Geolocation API

    No API Key required

    Base Path: http://ip-api.com/json/{query}

    {query} can be a single IPv4/IPv6 address or a domain name
    If you don't supply a query the current IP address will be used

    """
    
    # API endpoint
    url = 'http://ip-api.com/json/'

    # API call
    response = requests.get(url)

    # Collect response in json format
    data = response.json()

    # Return data gathered
    if data['status'] == 'success':
        return {
            'success': data['status'] == 'success', # Should exaluate to True
            'city': data['city'],
            'state': data['regionName'],
            'ip_coordinates': str(data['lat']) + ', ' + str(data['lon']),
            'lat': data['lat'],
            'lon': data['lon'],
            'ip_address': data['query']
        }
    else:
        return {
        'success': data['status'] == 'success', # Should exaluate to False
        'ip_address': data['query']
        }

def get_city(zip_code):
    """

    Makes use of an API to get location information 
    based off of a provided zip code

    API: Zipcode API

    API Key required, sign up at https://www.zipcodeapi.com

    Base Path: https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees
   
    Returns information required to use the weather API, 
    the city and state name but most importantly the longetude and latitude

    """

    # API key, retrieved from configure.py
    api_key = configure.ZIP_KEY

    # API endpoint
    url = f'https://www.zipcodeapi.com/rest/{api_key}/info.json/{zip_code}/degrees'

    # API call
    response = requests.get(url)

    # Collect response in json format
    data = response.json()

    if 'error_code' in data or 'error_msg' in data:
        return {
            'success': False,
            'query': zip_code
        }

    else:
        return {
        'success': True,
        'query': data['zip_code'],
        'city': data['city'],
        'state': data['state'],
        'lat': data['lat'],
        'lon': data['lng']
        }

def get_weather(lat, lon):
    """

    Makes use of an API to get current and daily weather

    API: Weather API

    API Key required, sign up at https://openweathermap.org/api

    Base Path: https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}

    Returns current and daily weather information in two separate dictionaries

    """

    # API key, retrieved from configure.py
    api_key = configure.WEATHER_KEY

    # API endpoint
    url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&appid={api_key}'

    # API call
    response = requests.get(url)

    # Collect response in json format
    weather = response.json()

    # Interpret Current Weather
    current_weather = weather['current']

    # By default, the API returns all requested times in unix format
    current_weather['dt'] = epoch_to_human_readable_date(current_weather['dt'])
    current_weather['sunrise'] = epoch_to_human_readable_date(current_weather['sunrise'])
    current_weather['sunset'] = epoch_to_human_readable_date(current_weather['sunset'])

    # By default, the API returns all temperature values in Kelvin
    current_weather['dew_point'] = {'kelvin': current_weather['dew_point'], 
                                    'fahrenheit': round(kelvin_to_fahrenheit(current_weather['dew_point']), 2),
                                    'celsius': round(kelvin_to_celsius(current_weather['dew_point']), 2)}

    current_weather['feels_like'] = {'kelvin': current_weather['feels_like'], 
                                     'fahrenheit': round(kelvin_to_fahrenheit(current_weather['feels_like']), 2),
                                     'celsius': round(kelvin_to_celsius(current_weather['feels_like']), 2)}

    current_weather['temp'] = {'kelvin': current_weather['temp'], 
                               'fahrenheit': round(kelvin_to_fahrenheit(current_weather['temp']), 2),
                               'celsius': round(kelvin_to_celsius(current_weather['temp']), 2)}

    # Change icon value to image url to be used in html img tag as src
    current_weather['weather'][0]['icon'] = 'http://openweathermap.org/img/wn/' + current_weather['weather'][0]['icon'] + '@2x.png'

    # Interpret Daily Weather
    daily_forcast = weather['daily']

    for day in daily_forcast:
        # Get readable dates and times
        day['dt'] = epoch_to_human_readable_date(day['dt'])
        day['sunrise'] = epoch_to_human_readable_date(day['sunrise'])
        day['sunset'] = epoch_to_human_readable_date(day['sunset'])

         # Change icon value to image url to be used in html img tag as src
        day['weather'][0]['icon'] = 'http://openweathermap.org/img/wn/' + day['weather'][0]['icon'] + '@2x.png'


        # Convert temperatures in 'feels_like' dictionary from Kelvin to Fahrenheit and Celsius

        for temp in day['feels_like']:
            day['feels_like'][temp] = {'kelvin': day['feels_like'][temp], 
                                       'fahrenheit': round(kelvin_to_fahrenheit(day['feels_like'][temp]), 2),
                                       'celsius': round(kelvin_to_celsius(day['feels_like'][temp]), 2)}


        # Convert temperatures in 'temp' dictionary from Kelvin to Fahrenheit

        for temp in day['temp']:
            day['temp'][temp] = {'kelvin': day['temp'][temp], 
                                 'fahrenheit': round(kelvin_to_fahrenheit(day['temp'][temp]), 2),
                                 'celsius': round(kelvin_to_celsius(day['temp'][temp]), 2)}

    # Interpret Hourly Weather
    hourly_weather = weather['hourly']

    # Only manipulating data for hours of the current date, rest will be ommitted

    curr_date = epoch_to_human_readable_date(hourly_weather[0]['dt']).split(",", 1)[1][:3]

    last_hour = 0

    for index, hour in enumerate(hourly_weather):
        # Get date in relation to the hour
        date = epoch_to_human_readable_date(hour['dt']).split(",", 1)[1][:3]
        if date != curr_date:
            last_hour = index
            break
            
        # Convert temperatures in 'dew_point' dictionary from Kelvin to Fahrenheit and Celsius
        hour['dew_point'] = {'Kelvin':hour['dew_point'],
                             'fahrenheit': round(kelvin_to_fahrenheit(hour['dew_point']), 2),
                             'celsius': round(kelvin_to_celsius(hour['dew_point']), 2)}

        # Get readable dates and times
        hour['dt'] = epoch_to_human_readable_date(hour['dt'])

        # Convert temperatures in 'feels_like' dictionary from Kelvin to Fahrenheit and Celsius
        hour['feels_like'] = {'kelvin': hour['feels_like'], 
                              'fahrenheit': round(kelvin_to_fahrenheit(hour['feels_like']), 2),
                              'celsius': round(kelvin_to_celsius(hour['feels_like']), 2)}

        # Convert temperatures in 'temp' dictionary from Kelvin to Fahrenheit
        hour['temp'] = {'kelvin': hour['temp'], 
                        'fahrenheit': round(kelvin_to_fahrenheit(hour['temp']), 2),
                        'celsius': round(kelvin_to_celsius(hour['temp']), 2)}

        hour['weather'][0]['icon'] = 'http://openweathermap.org/img/wn/' + hour['weather'][0]['icon'] + '@2x.png'


    return current_weather, daily_forcast, hourly_weather[:last_hour]