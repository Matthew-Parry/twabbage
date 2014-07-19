import picamera
from time import sleep
from datetime import datetime
import os
import RPi.GPIO as GPIO
import tweepy
import random

consumer_key = 'ACNq06IuOaApzHGHzJes4XIfz'
consumer_secret = '3bzuG0HuyUcEd5iiaM8ifO7PTajilqy0XvDVjoZUqZZF3dGQtL'
access_token = '2647226370-b4eJ4Inm4dRbRXFpdwDTbYNpjoRgroit4AQL2Hs'
access_token_secret = 'uLUs6bNRwQtWjhfM8FciROvGTAlPRUGVSF1Yn984id4wu'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

mentions = api.mentions_timeline()

for mention in mentions:
    os.system('espeak -a 200 "%s. %s"' % (mention.user.name, mention.text))
    break
