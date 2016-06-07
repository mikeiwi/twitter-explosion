"""Sigue a todos los que publiquen en cierto filtro de búsqueda y que además
sus twitts no sean Retweet.

"""
import tweepy
from connect import twitter_connect

api = twitter_connect()

c = tweepy.Cursor(api.search, q='#SIGUEMEYTESIGO')
for tweet in c.items():
    tweet = tweet._json
    if "retweeted_status" not in tweet:
        print(tweet['text'].encode('utf-8'))
        print(tweet['user']['id'])
        print(tweet['user']['screen_name'])
        break
        #api.create_friendship(tweet['user']['id'])
