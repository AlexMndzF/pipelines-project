def changetype(data,changetype=0.0083):
    '''
    Funcion para modificar el tipo de cambio y asi obtener el precio en €
    recibe el tipo de cambio yuan-€ y si no se le introduce como parametro por defecto es 0.0083
    '''
    data['Price-Night-€'] = [float(e)*changetype for e in data['Price-Night-€']]
def datafilter(data,city,distance,score):
    '''
    Esta funcion recibe como parametros el dataframe para filtrar y los parametros por los que filtrar:
    -city: un string con el nombre de la ciudad en funcion de la lista de disponibilidad.
    -distance: distancia máxima al centro de la ciudad.
    -score: puntuacion mínima del alojamiento.
    '''
    datafilter = data[data['City']== city]
    datafilter = datafilter[datafilter['Distance-km']<distance]
    datafilter = datafilter[datafilter['Score']>score]
    return datafilter
