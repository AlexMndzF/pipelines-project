#! /usr/bin/python3
import sys
import argparse
import subprocess

def recibeConfig():
    parser = argparse.ArgumentParser(description='Filtrar hostales Japon')
    parser.add_argument('-d','--distance',
                        help='distancia máxima de la ciudad',
                        default="20"
                        ),
    parser.add_argument('-c','--city',
                        help='Ciudad a la que vas,\nCiudades disponibles:\n-Kyoto\n-Tokyo\n-Hiroshima\n-Fukuoka\n-Osaka',
                        ),
    parser.add_argument('-m','--mail',
                        help='Correo electronico para mandar la informacion'
                        ),
    parser.add_argument('-s','--score',
                        help='Puntuacion del hostal',
                        default = "0"
                        ), 
    parser.add_argument('-ch','--change',
                        help='Tipo de cambio actual YEN-EURO, por defecto 0.0083',
                        default = "0.0083"
                        )                        
    args = parser.parse_args()
    print(args)
    return args


def main():
    config = recibeConfig()


if __name__=="__main__":
    main()


