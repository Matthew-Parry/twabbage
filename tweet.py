import tweepy
import random

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
]

photo_path ='/home/pi/twabbage/babbage.jpeg'
status = random.choice(statuses)
api.update_with_media(photo_path, status)
