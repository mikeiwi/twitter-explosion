"""Crea una conexión a twitter mediante tweepy, con los tokens necesarios."""
import tweepy

CONSUMER_KEY = "V8zyjPWvSQnKUr6SdS2uwY2Kg"
CONSUMER_SECRET = "X29Ibxwg1AWjQKBRnlXfFI1CAhD0TUU2gpEgjIctiR8Jw32qpF"

ACCESS_TOKEN = "86767825-Dq6HB3WKGGabo5xffRGAWmbcbW9pMht6X7ZnEeGT4"
ACCESS_TOKEN_SECRET = "sXdwyTAtowyz6BH7Z4W8WfiCNpFQjaT5pQluYhBzAdtgC"

def twitter_connect():
    """Crea una conexión con los datos de acceso y retorna un objeto api de
    tweepy.

    """
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    return tweepy.API(auth)
