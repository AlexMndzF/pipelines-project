import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()
#Funcion que devuelve los datos por ciudad:
def githubRequestAuthorized(city):
    authToken = os.getenv("AIR_VISUAL_TOKEN")
    if not authToken:
        raise ValueError("NECESITAS UN TOKEN")
    else:
        print("We have a github token: ", authToken[0:4])
    diction={
        'Kyoto' : 'Kyoto',
        'Tokyo' : 'Tokyo',
        'Hiroshima' : 'Higashihiroshima',
        'Fukuoka' : 'Itoshima',
        'Osaka' : 'Osaka'
    }
    state = diction.get(city)
    url = " http://api.airvisual.com/v2/city?city={}&state={}&country=Japan&key={}".format(city,state,authToken)
    print("Requesting authorized ")
    res = requests.get(url).json()
    return res
#tokyo = githubRequestAuthorized('Tokyo')
#print(tokyo)