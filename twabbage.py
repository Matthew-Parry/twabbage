import picamera
from time import sleep
from datetime import datetime
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin 17 is shutter button
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

# pin 18 is LED
GPIO.setup(18, GPIO.OUT)

#while True:

def tweet(filename):
    print("Tweeted %s"% filename)


with picamera.PiCamera() as camera:
    #camera.vflip = True
    #camera.hflip = True
    camera.start_preview()
    
    #shutter button pressed
#    GPIO.wait_for_edge(17, GPIO.FALLING)
    #led light in other eye   

    GPIO.output(18, 1)
    sleep(0.2)
    GPIO.output(18, 0)
    sleep(0.2)    
    GPIO.output(18, 1)
    sleep(0.2)
    GPIO.output(18, 0)
    sleep(0.2)    
    GPIO.output(18, 1)
    sleep(0.15)
    GPIO.output(18, 0)
    sleep(0.15)    
    GPIO.output(18, 1)
    sleep(0.15)
    GPIO.output(18, 0)
    sleep(0.15)    
    GPIO.output(18, 1)
    sleep(0.1)
    GPIO.output(18, 0)
    sleep(0.1)    
    GPIO.output(18, 1)
    sleep(0.1)
    GPIO.output(18, 0)
    #shutter sound
    os.system("aplay /home/pi/twabbage.wav")

    timenow=datetime.now()
    formatted_time = timenow.strftime("%Y-%m-%d-%H%M%S")
    camera.capture('/home/pi/twabbage/twabbage%s.jpg'% formatted_time)
     
    camera.stop_preview()
    tweet("/home/pi/twabbage/twabbage%s.jpg" % formatted_time)
