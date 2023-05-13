import json
import requests 
import speech_recognition as sr  
import requests
from assistant import*


def get_latest_news(num_articles=2, country="in", api_key="1c15a99a3ef948c6a1a1c4215c0a6051"):
    # API endpoint and parameters
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": country,
        "apiKey": api_key
    }
    
    # Make API request
    response = requests.get(url, params=params)
    
    # Parse response JSON
    data = json.loads(response.text)
    
    # Get the requested number of articles
    articles = []
    for i in range(num_articles):
        article = data["articles"][i]
        headline = article["title"]
        description = article["description"]
        articles.append(f"{headline}. {description}")
    
    print(articles)
    # Return the list of articles
    return articles