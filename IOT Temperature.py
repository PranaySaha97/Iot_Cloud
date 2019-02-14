import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from ubidots import ApiClient

GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11           
pin = 3

api = ApiClient(token= 'A1E-WLuKlvx6mrCQVf22RF45pLuVlE0yrY')
var1 = api.get_variable("5c5de79ec03f97116385a192")
var2 = api.get_variable("5c5de5d6c03f970f89345fff")


try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            response1 = var1.save_value({"value": humidity})
            response2 = var2.save_value({"value": temperature})
        else:
            print('Failed to get reading. Try again!')

except KeyboardInterrupt:                                                              # Reset by pressing CTRL + C
    print("Measurement stopped by User")
    GPIO.cleanup()















