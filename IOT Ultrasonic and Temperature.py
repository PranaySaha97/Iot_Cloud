import RPi.GPIO as GPIO
import time
import Adafruit_DHT
from ubidots import ApiClient

GPIO.setwarnings(False)

sensor = Adafruit_DHT.DHT11           
pin = 2
trigger = 3
echo = 4

api = ApiClient(token= 'A1E-WLuKlvx6mrCQVf22RF45pLuVlE0yrY')
var1 = api.get_variable("5c5de79ec03f97116385a192")
var2 = api.get_variable("5c5de5d6c03f970f89345fff")
var = api.get_variable("5c5dcfacc03f9779d3ecf28c")

GPIO.setmode(GPIO.BCM)
GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trigger, 0)

try:
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

        if humidity is not None and temperature is not None:
            print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
            response1 = var1.save_value({"value": humidity})
            response2 = var2.save_value({"value": temperature})
        else:
            print('Failed to get reading. Try again!')
        
        #ultra sonic
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

except KeyboardInterrupt:                                                              # Reset by pressing CTRL + C
    print("Measurement stopped by User")
    GPIO.cleanup()
