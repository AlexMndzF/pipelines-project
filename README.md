# Pipelines-project

Para este proyecto he utilizado un data set de kaagel (https://www.kaggle.com/koki25ando/hostel-world-dataset), en el que se recoge informacion de hostales de cinco ciudades de Japon:

 • Kyoto
 • Tokyo
 • Hiroshima
 • Fukuoka
 • Osaka

He conectado este data frame con dos apis:

 • AirVisual: Devuelve datos del clima en tempo real y la calidad del aire.
 • Exchangerate: Devuelve el tipo de cambio EUR a JPY en el momento.
## Objetivo:
El objetivo del proyecto era crear un buscador que le pases varios parametros,genere un PDF y lo envie por mail.
### Parametros:
 • Distance: Distancia máxima del hostal al centro de la ciudad.
 • City: Ciudad elegida para la busqueda.
 • Mail: Correo electronico al que enviar el informe.
 • Score: Puntuacion mínima de los hostales.
### Informe:
Cuando se ejecuta la aplicacion, el primer paso que se hace es limpiar el data frame, para ello se hace una llamada a la api de cambio de moneda y se hace el tipo de cambio.
Una vez esta hecho el tipo de cambio, se filtra el dataset por los diferentes parametros introducidos en la funcion.
El siguiente paso es la generacion del informe, para lo que la funcion de pdf se conecta con la api de AirVisual para obtener los datos climatologico y asi completar los campos de temperatura, humedad, presion atmosferica, velocidad del viento, direccion del viento y calidad de aire. tambien actualiza el icono del tiempo.
Para poder interpretar los datos de calidad del aire, se puede recurrir a la siguiente tabla:
<p align="center"> <img  src="/src/readme_files/tabla-aqi.png"></p>

