# Pipelines-project
<p align="center"> <img  src="/src/readme_files/Enjoy Japan!.png"></p>

Para este proyecto he utilizado un data set de [kaagel](https://www.kaggle.com/koki25ando/hostel-world-dataset), en el que se recoge informacion de hostales de cinco ciudades de Japon:

 * __Kyoto__
 * __Tokyo__
 * __Hiroshima__
 * __Fukuoka__
 * __Osaka__

He conectado este data frame con dos apis:

 * __AirVisual__: Devuelve datos del clima en tempo real y la calidad del aire.
 * __Exchangerate__: Devuelve el tipo de cambio EUR a JPY en el momento.

## Estructura proyecto
 
 * __Input__: Directorio en el que se encuentra el fichero de entrada.
 * __Output__: Directorio en el que están todos los archivos de salida:
    * __pdf__: Directorio donde se almacenan los reportes en pdf.
    * __csv__: Directorio donde se guardan los dataframes limpios en formato CSV.
 * __src__: Directorio en el que se encuentra el programa:
    * __main.py__: Ejecutable principal del programa.
    * __api.py__: Archivo con funciones de llamada a las apis.
    * __clean.py__: Archivo con funcin de limpieza del dataframe.
    * __filters.py__: Archivo con funciones de filtrado del dataframe.
    * __mail.py__: Archivo con funciones para enviar email.
    * __pdf.py__: Archivo con funciones para generar el PDF.

## Objetivo:
El objetivo del proyecto era crear un buscador que le pases varios parámetros,genere un PDF y lo envie por mail.
### Parametros:
 * __Distance__: Distancia máxima del hostal al centro de la ciudad.
 * __City: Ciudad__ elegida para la búsqueda.
 * __Mail__: Correo electrónico al que enviar el informe.
 * __Score__: Puntuación mínima de los hostales.
### Informe:
Cuando se ejecuta la aplicación, el primer paso que se hace es limpiar el data frame, para ello se hace una llamada a la api de cambio de moneda y se hace el tipo de cambio.
Una vez está hecho el tipo de cambio, se filtra el dataset por los diferentes parámetros introducidos en la función.
El siguiente paso es la generación del informe, para lo que la función de pdf se conecta con la api de AirVisual para obtener los datos climatológico y así completar los campos de temperatura, humedad, presión atmosférica, velocidad del viento, dirección del viento y calidad de aire. también actualiza el icono del tiempo.
Para poder interpretar los datos de calidad del aire, se puede recurrir a la siguiente tabla:
<p align="center"> <img  src="/src/readme_files/tabla-aqi.png"></p>

