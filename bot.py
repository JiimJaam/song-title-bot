import tweepy
import sys
import time

from generate_phrase import gen

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

INTERVAL = 30 * 60  # 30 minutes

while True:
    print("Phrase incoming")
    lyric = gen()
    api.update_status(lyric)
    time.sleep(INTERVAL)
