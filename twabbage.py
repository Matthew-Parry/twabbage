import picamera
from time import sleep
from datetime import datetime
import os
import RPi.GPIO as GPIO
import tweepy
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# pin 17 is shutter button
GPIO.setup(17, GPIO.IN, GPIO.PUD_UP)

# pin 18 is LED
GPIO.setup(18, GPIO.OUT)

#while True:

def tweet(filename):
    consumer_key = 'ACNq06IuOaApzHGHzJes4XIfz'
    consumer_secret = '3bzuG0HuyUcEd5iiaM8ifO7PTajilqy0XvDVjoZUqZZF3dGQtL'
    access_token = '2647226370-b4eJ4Inm4dRbRXFpdwDTbYNpjoRgroit4AQL2Hs'
    access_token_secret = 'uLUs6bNRwQtWjhfM8FciROvGTAlPRUGVSF1Yn984id4wu'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    statuses = [
        "Looking Good!",
        "Wow! Nice outfit!",
        "Oh dear, is it a bad hair day?",
        "Stand still silly!",
        "Twit-twoo!",
        "Pi-tastic!",
        "Babbage, babbage not on the wall, who is the fairest of them all?",
        "Pray Mr Babbage, how do I look?",
        "Perhaps you should get an early night this evening?!",
        "STUNNING!",
        "Ada Lovelace would be impressed!",
        "This should be your profile picture!",
    ]

    photo_path =filename
    status = random.choice(statuses) + " #picademy"
    api.update_with_media(photo_path, status)
    print("Tweeted %s"% filename)


with picamera.PiCamera() as camera:
    #camera.vflip = True
    #camera.hflip = True
    camera.start_preview()
    
    #shutter button pressed
    GPIO.wait_for_edge(17, GPIO.FALLING)
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
    os.system("aplay /home/pi/twabbage/twabbage.wav &")

    timenow=datetime.now()
    formatted_time = timenow.strftime("%Y-%m-%d-%H%M%S")
    camera.capture('/home/pi/twabbage/twabbage%s.jpg'% formatted_time)
     
    camera.stop_preview()
    tweet("/home/pi/twabbage/twabbage%s.jpg" % formatted_time)
