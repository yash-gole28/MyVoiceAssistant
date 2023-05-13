import requests

def get_weather_info(api_key, city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    # make a GET request to the OpenWeatherMap API
    response = requests.get(url)
    
    # parse the JSON response
    data = response.json()
    
    # check if the API returned any results
    if data['cod'] != 200:
        return "Sorry, I couldn't retrieve weather information. Please try again later."
    
    # extract the weather information from the JSON response
    city_name = data['name']
    temperature = data['main']['temp']
    weather_description = data['weather'][0]['description']
    return(f"Current weather in {city_name}: {temperature}°C and {weather_description}")
    