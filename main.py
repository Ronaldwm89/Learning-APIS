import requests
import datetime as dt
import smtplib
import time

MY_LAT = -20.822731
MY_LONG = -58.092879
E_MAIL = "my_email@gmail.com"
PASSWORD = "mypassword"

#obtengo los datos requests de la ISS mediante la API
def get_iss_position():
    response_iss = requests.get("http://api.open-notify.org/iss-now.json")
    data_response = response_iss.json()

    #filtro la latitud y longitud de la ISS
    iss_latitude = data_response["iss_position"]["latitude"]
    iss_longitude = data_response["iss_position"]["longitude"]

    #comparo si la latitud y longitud de la ISS esta cerca de la latitud y longitud de la persona
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG +5:
        return True
    

#envio un correo de notificacion de que la ISS esta pasando
def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(E_MAIL, PASSWORD)
        connection.sendemail(E_MAIL, "youremail@yahoo.com", f"Subject:ISS POSITION\n\n El ISS esta pasando por tu posicion y es de noche, podrias verlo si sales ahora, CORRE!!\n\n Your Name")

#obtengo los datos de sunrise y sunset desde la api utilizando los parametros de latitud y longitud de una ubicacion conocida para saber si la iss va a pasar por la zona de dia o de noche y asi poder saber si es visible o no
def get_sunrise_sunset():
    response_sun = requests.get("https://api.sunrise-sunset.org/json?lat=-20.822731&lng=--58.092879&formatted=0")
    data = response_sun.json()

    #obtengo la hora de sunrise y sunset para saber cuando es de dia y de noche
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
   
    return sunrise, sunset 

#comparo si la hora actual esta entre sunrise y sunset y si la posicion de la ISS es igual a la posicion de la persona para enviar un correo de notificacion de que la ISS esta pasando por su ubicacion y es de noche
def conditionals_true():
    while True:
        time.sleep(60)#espero 60 segundos para verificar de nuevo
                 
    #obtengo la hora actual para comparar con sunrise y sunset y saber si es de noche
        hour_now = int(dt.datetime.now().hour)
        sunrise = get_sunrise_sunset()[0]
        sunset = get_sunrise_sunset()[1]
        
        if hour_now <= sunrise and hour_now >= sunset: 
            if get_iss_position():
                send_email()

            
conditionals_true()

#Si la diferencia de latitud es menor que un rango como 0.5 grados, podrías decir que están cerca. Lo mismo aplica para la longitud