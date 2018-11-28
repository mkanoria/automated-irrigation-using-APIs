# import RPi.GPIO as GPIO
import time
# GPIO.setmode(GPIO.BCM)
# GPIO.setwarnings(False)
# GPIO.setup(18,GPIO.OUT)
def turned_off():
    print("Valve Closed")
    # GPIO.output(18,GPIO.LOW)
def turned_on(t):
    print("Valve Open for " + str(t) + " seconds ")
    # GPIO.output(18,GPIO.HIGH)
    time.sleep(t)
    turned_off()
