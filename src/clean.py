import pandas as pd
import matplotlib.pyplot as plt
import requests
import json
from filters import changetype
#cracion data frame:
data = pd.read_csv("./input/Hostel.csv")
#Eliminacion de columnas no relevantes y cambio de nombre:
data = data[['hostel.name', 'City', 'price.from', 'Distance','summary.score','rating.band']]
data.columns = ['Name', 'City', 'Price-Night-€', 'Distance-km','Score', 'Rating']
#modificacion en la columna distancias para poder usarlo como filtro:
distances = []
for e in data['Distance-km']:
    e = e.split(' ')
    dist = e[0][:-2]
    distances.append(float(dist))
data['Distance-km'] = distances
changetype(data)
data.to_csv("output/Hostel_clean.csv",index = None)