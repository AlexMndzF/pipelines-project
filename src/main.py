#! /usr/bin/python3
import sys
import argparse
import subprocess
import pandas as pd
from filters import datafilter, changetype
from api import AirVisualRequestAuthorized as apirequest
from pdf import createPDF
import pandas as pd
from clean import cleanData
from mail import sendemail,checkmail

def validcity(city):
    city = city.capitalize()
    cities=['Kyoto','Tokyo', 'Hiroshima','Fukuoka','Osaka']
    while True:
        if city in cities:
                return city
        else:
            print('Ivalid city, pleas enter a valid one: \nKyoto,\nTokyo, \nHiroshima,\nFukuoka,\nOsaka')
            city = (input('Insert a valid city:')).capitalize()

def validscore(score):
    while True:
        if score <= 10:
            return float(score)
        else:
            print('Invalid score, 0<sore<= 10')
            score = (input('Insert a valid score:')).capitalize()


def recibeConfig():
    parser = argparse.ArgumentParser(description='Filtrar hostales Japon')
    parser.add_argument('-d','--distance',
                        help='Distancia máxima a la ciudad',
                        default="20",
                        type = float
                        ),
    parser.add_argument('-c','--city',
                        help='''Ciudad a la que vas.
                        Ciudades disponibles:
                        -Kyoto
                        -Tokyo
                        -Hiroshima
                        -Fukuoka
                        -Osaka
                        ''',
                        type = validcity
                        ),
    parser.add_argument('-m','--mail',
                        help='Correo electronico para mandar la informacion, si no introduces este parametro el informe se guradara en la carpeta output/pdf'
                        ),
    parser.add_argument('-s','--score',
                        help='Puntuacion del hostal, rango 0-10',
                        default = "0",
                        type = validscore
                        ), 
    #parser.add_argument('-ch','--change',
    #                   help='Tipo de cambio actual YEN-EURO, por defecto 0.0083',
    #                   default = "0.0083"
    #                    )                        
    args = parser.parse_args()
    print(args)
    return args

def main():
    args = recibeConfig()
    data = pd.read_csv(cleanData()) #Importacion del data set limpio
    data = datafilter(data,args.city,args.distance,args.score) #Dataframe filtrado
    dictionary = apirequest(args.city) #Peticion datos a la api
    doc = createPDF(data,args.score,dictionary) #Generador PDF
    print('PDF generated')
    if args.mail != None :
        mail = checkmail(args.mail)
        sendemail(mail,doc)
    else:
        print('You have the report in the path: {}'.format(doc[0]))



if __name__=="__main__":
    main()


