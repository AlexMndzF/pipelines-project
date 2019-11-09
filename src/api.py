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
       pass
       # print("We have a github token: ", authToken[0:4])
    diction={
        'Kyoto' : 'Kyoto',
        'Tokyo' : 'Tokyo',
        'Hiroshima' : 'Kamiyacho',
        'Fukuoka' : 'Itoshima',
        'Osaka' : 'Osaka'
    }
    city2 = diction.get(city)
    
    url = " http://api.airvisual.com/v2/city?city={}&state={}&country=Japan&key={}".format(city2,city,authToken)
    #print("Requesting authorized ")
    res = requests.get(url).json()
    return res
tokyo = githubRequestAuthorized('Tokyo')
kyoto = githubRequestAuthorized('Kyoto')
hiroshima = githubRequestAuthorized('Hiroshima')
fukuoka =  githubRequestAuthorized('Fukuoka')
osaka =  githubRequestAuthorized('Osaka')