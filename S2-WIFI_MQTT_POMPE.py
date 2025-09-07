# 2025-05-01 : création
# lolin esp32-s2 mini
# port 15 = led interne
# port 39 : port externe GPIO pour pompe eau
# port 3 : port externe GPIO pour ADC1-2, capteur humidité

# port 32 : port externe GPIO pour capteur DHT


from machine import Pin, ADC
import machine

import network  
#import comptes_wifi 
import urequests
import time
from random import randint
import dht
import ConfigWifi  # On importe le fichier configWifi.py qui doit être mis sur la carte ESP32.(il contient ssid et pwd wifi)

pin_led = Pin(15, mode=Pin.OUT)
pin_Pompe = Pin(39, mode=Pin.OUT)
Potentiometer= ADC(Pin(3)) #GPIO Pin 6 defined for input
Potentiometer.atten(ADC.ATTN_11DB) #Full range: 3.3v

# ************Affichage initialisation **********
Led_builtin = Pin(15,Pin.OUT)# RP2 W ou 25 pour RP2
time.sleep(1)
Led_builtin.value(0)
time.sleep(2)
Led_builtin.value(1)

# d = dht.DHT22(machine.Pin(18))


# **********connexion wifi**************
#ssid = comptes_wifi.ssid
#password = comptes_wifi.password
# **************************************
def WifiConnect() :
    station = network.WLAN(network.STA_IF)
    station.active(True)
    if station.isconnected() == False:
        station.connect(config.WIFI_SSID, config.WIFI_PASSWORD)


    #Attendre que l'ESP soit connecté avant de poursuivre
    print("Connexion ESP32 au point d'acces ", ssid)
    while station.isconnected() == False:
        print('.', end = " ")
        time.sleep(1)
        
    print("Connexion réussie")
    print ("ESP32 : Adresse IP, masque, passerelle et DNS", station.ifconfig())


# **********connexion thingspead**************

# **************************************def send_temperature_ThingSpeak(temperature) :
    data_capteur = str(temperature)
    champ = 'field1' #salon
    try : 
        print('https://api.thingspeak.com/update?api_key=KBV8CN9NY3N184SQ&{}={}'.format(champ,data_capteur))
        request = urequests.get('https://api.thingspeak.com/update?api_key=KBV8CN9NY3N184SQ&{}={}'.format(champ,data_capteur))
        request.close()
        print('données envoyées')
    except :
        print("Pb d'envoi")
        affichage_erreur(3)
# **************************************


# *************main*************************
while True : 
    print("lancement de l'application")
    print("Connexion wifi")
#     connexion_wifi_STA(ssid,password)
    print("Mesure capteur")
      
    # Humidité   
    Humide = Potentiometer.read()
    
    print(Humide)
    print("Envoi donnée ThingSpeak")
    # send_temperature_ThingSpeak(Humide)
    # station.disconnect()   
    time.sleep(5) #temps d'affichage avant mise en sommeil


    print('pompe on')
    pin_Pompe.value(1)
    time.sleep(1)
    print('pompe off')
    pin_Pompe.value(0)



    print('mise en sommeil profond') #sommeil profond
    # machine.deepsleep(3*60*60*1000) #3 / heures
    time.sleep(15) #simulation de sommeil
    
    # ****************************************


