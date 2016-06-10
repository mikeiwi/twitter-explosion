"""Sigue a todos los que publiquen en cierto filtro de búsqueda y que además
sus twitts no sean Retweet.

"""
import tweepy
from connect import twitter_connect

api = twitter_connect()

count = 1
c = tweepy.Cursor(api.search, q='#viernesdeganarseguidores')
for tweet in c.items():
    tweet = tweet._json
    if "retweeted_status" not in tweet:
        print(tweet['text'].encode('utf-8'))
        print(tweet['user']['screen_name'])
        friendship = api.show_friendship(
            target_screen_name=tweet['user']['screen_name'])
        if not friendship[0].following and not friendship[0].followed_by:
            api.create_friendship(tweet['user']['id'])
            print("---followed: {} !!!!!!".format(tweet['user']['screen_name']))
            count += 1

        if count == 50:
            break
