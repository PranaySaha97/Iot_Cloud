import RPi.GPIO as GPIO
import time
from ubidots import ApiClient

GPIO.setwarnings(False)

trigger = 3
echo = 5

api = ApiClient(token= 'A1E-WLuKlvx6mrCQVf22RF45pLuVlE0yrY')
var = api.get_variable("5c5dcfacc03f9779d3ecf28c")

GPIO.setmode(GPIO.BOARD)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trigger, 0)

while 1:

    GPIO.output(trigger, 1)
    time.sleep(0.00001)
    GPIO.output(trigger, 0)
    time.sleep(0.00001)

    while GPIO.input(echo) == 0:
        start = time.time()

    while GPIO.input(echo) == 1:
        stop = time.time()

    TimeElapsed = stop - start
    distance = TimeElapsed * 34300/2
    print (distance, " cm")
    time.sleep(1)
    response = var.save_value({"value": distance})
