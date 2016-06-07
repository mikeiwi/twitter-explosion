import tweepy

auth = tweepy.OAuthHandler("V8zyjPWvSQnKUr6SdS2uwY2Kg", "X29Ibxwg1AWjQKBRnlXfFI1CAhD0TUU2gpEgjIctiR8Jw32qpF")
auth.set_access_token("86767825-Dq6HB3WKGGabo5xffRGAWmbcbW9pMht6X7ZnEeGT4", "sXdwyTAtowyz6BH7Z4W8WfiCNpFQjaT5pQluYhBzAdtgC")

api = tweepy.API(auth)

c = tweepy.Cursor(api.search, q='#SIGUEMEYTESIGO')
for tweet in c.items():
	tweet = tweet._json
	if "retweeted_status" not in tweet:
		print(tweet['text'].encode('utf-8'))
		print(tweet['user']['id'])
		print(tweet['user']['screen_name'])
		api.create_friendship(tweet['user']['id'])
	#from pprint import pprint
	#pprint(tweet)