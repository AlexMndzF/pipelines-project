from fpdf import FPDF
from api import changetypeapi
#Funcion que crea el pdf con imagen del tiempo.
def createPDF(data,score,dictionary):
    '''
    En los parametros de entrada estan:
    Data => DataFrame sobre el que se hara el PDF (ya filtrado)
    Score => Puntuacion minima de los hostales.
    Dictionary => Resultado de la api que obtendra los parametros que necesitamos.
    '''
    change = changetypeapi()
    city = (dictionary.get('data')).get('city')
    temp = ((((dictionary.get('data')).get('current')).get('weather')).get('tp'))
    icon = ((((dictionary.get('data')).get('current')).get('weather')).get('ic'))
    press = ((((dictionary.get('data')).get('current')).get('weather')).get('pr'))
    hum = ((((dictionary.get('data')).get('current')).get('weather')).get('hu'))
    windspeed = ((((dictionary.get('data')).get('current')).get('weather')).get('ws'))
    winddirect = ((((dictionary.get('data')).get('current')).get('weather')).get('wd'))
    aqi = ((((dictionary.get('data')).get('current')).get('pollution')).get('aqius'))
    pdf =  FPDF()
    pdf.add_page()
    pdf.set_font('times', 'B', 20)
    pdf.cell(0,20, 'Hostels in {}, whit score greater than {}'.format(city, score),align = 'C')
    pdf.set_font('times', '', 7)
    pdf.ln(12)
    pdf.cell(0,7, 'The document display the first 20, Current change type: 1EUR = {}JPY'.format(change),align = 'C')
    pdf.set_font('times', 'B', 10)
    pdf.ln(10)
    pdf.cell(100, 7, 'Name', align='C', border = 1)
    pdf.cell(10, 7, 'City', align='C', border = 1)
    pdf.cell(30, 7, 'Price-Night-Euro', align='C', border = 1)
    pdf.cell(25, 7, 'Distance-km', align='C', border = 1)
    pdf.cell(10, 7, 'Score', align='C', border = 1)
    pdf.cell(20, 7, 'Rating', align='C', border = 1)
    pdf.ln(7)
    pdf.set_font('times', '', 10)
    for i in range(len(data['Name'])):        
        name = data['Name'].iloc[i]
        city = data['City'].iloc[i]
        price = data['Price-Night'].iloc[i]
        distance = data['Distance-km'].iloc[i]
        score = str(data['Score'].iloc[i])
        rating = str(data['Rating'].iloc[i])
        pdf.cell(100, 7, '%s' % (name), align='L', border = 1)
        pdf.cell(10, 7, '%s' % (city), align='C', border = 1)
        pdf.cell(30, 7, '%s' % (price), align='C', border = 1)
        pdf.cell(25, 7, '%s' % (distance), align='C', border = 1)
        pdf.cell(10, 7, '%s' % (score), align='C', border = 1)
        pdf.cell(20, 7, '%s' % (rating), align='C', border = 1)
        pdf.ln(7)
        if i == 20:
            break
    pdf.set_font('times', 'B', 20)
    pdf.cell(0,10, 'Clima',align='C')
    pdf.ln(10)
    pdf.set_font('times', '', 10)
    pdf.image('../src/icons/{}.png'.format(icon),90,w=30,h=30)
    pdf.cell(0,10, 'Temperature: {}ºC'.format(temp),align='C')
    pdf.ln(5)
    pdf.cell(0,10, 'Atmospheric pressure: {}hPa'.format(press),align='C')
    pdf.ln(5)
    pdf.cell(0,10, 'Humdity: {}%'.format(hum),align='C')
    pdf.ln(5)
    pdf.cell(0,10, 'Wind speed: {}m/s'.format(windspeed),align='C')
    pdf.ln(5)
    pdf.cell(0,10, 'Wind direccion: {}º'.format(winddirect),align='C')
    pdf.ln(5)
    pdf.cell(0,10, 'Air quality: {}aqi'.format(aqi),align ='C')
    pdf.output('../output/pdf/Search_city-{}_score-{}'.format(city,score), 'F')