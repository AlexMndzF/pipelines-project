import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
#Funcion que devuelve los datos por ciudad:
def AirVisualRequestAuthorized(city):
    authToken = os.getenv("AIR_VISUAL_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    diction={
        'Kyoto' : 'Kyoto',
        'Tokyo' : 'Tokyo',
        'Hiroshima' : 'Kamiyacho',
        'Fukuoka' : 'Itoshima',
        'Osaka' : 'Osaka'
    }
    city2 = diction.get(city)
    
    url = " http://api.airvisual.com/v2/city?city={}&state={}&country=Japan&key={}".format(city2,city,authToken)
    res = requests.get(url).json()
    return res
def changetypeapi():
    url = 'https://api.exchangerate-api.com/v4/latest/JPY'
    response = requests.get(url)
    data = response.json()
    return float((data.get('rates').get('EUR')))