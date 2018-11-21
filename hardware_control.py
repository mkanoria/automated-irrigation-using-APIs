
#hard ware control- replace led with valve; GPIO pins may vary
#import script
#x=generate_value
import RPi.GPIO as GPIO
import time
from script import generate_value  

def turned_on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    #print("LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(10)
   
def turned_off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    #print("LED off")
    GPIO.output(18,GPIO.LOW)
    time.sleep(10)

while (True):
    if generate_value():
        turned_on()
    else:
        turned_off()
