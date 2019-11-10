#! /usr/bin/python3
import sys
import argparse
import subprocess
import pandas as pd
from filters import datafilter, changetype
from api import AirVisualRequestAuthorized as apirequest
from pdf import createPDF
import pandas as pd

def recibeConfig():
    parser = argparse.ArgumentParser(description='Filtrar hostales Japon')
    parser.add_argument('-d','--distance',
                        help='Distancia máxima a la ciudad',
                        default="20"
                        ),
    parser.add_argument('-c','--city',
                        help='''Ciudad a la que vas.
                        Ciudades disponibles:
                        -Kyoto
                        -Tokyo
                        -Hiroshima
                        -Fukuoka
                        -Osaka
                        '''
                        ),
    parser.add_argument('-m','--mail',
                        help='Correo electronico para mandar la informacion'
                        ),
    parser.add_argument('-s','--score',
                        help='Puntuacion del hostal',
                        default = "0"
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
    data = pd.read_csv("../output/Hostel_clean.csv") #Importacion del data set limpio
    data = datafilter(data,args.city,float(args.distance),float(args.score)) #Dataframe filtrado
    dictionary = apirequest(args.city) #Peticion datos a la api
    createPDF(data,args.score,dictionary) #Generador PDF



if __name__=="__main__":
    main()


