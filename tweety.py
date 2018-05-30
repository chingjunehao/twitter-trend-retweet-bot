import re
import tweepy
from time import sleep
import tkinter # For python 3.6
from tkinter import *

consumer_key = 'key from your acc'
consumer_secret = 'key from your acc'
access_token = 'key from your acc'
access_token_secret = 'key from your acc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print(user.name) # Your screen name

# Loop through everyone that followed by you
for following in tweepy.Cursor(api.friends).items():
	print (following.screen_name) # To see name of the people that followed by you

# Follow people that are following you
for follower in tweepy.Cursor(api.followers).items():
    follower.follow()


# Retweet specified keywords
retweet = "machine learning%20OR%20computer science%20OR%20durian"
numOfreTweets = 2

for tweet in tweepy.Cursor(api.search, retweet).items(numOfreTweets):
	try:
		tweet.retweet()
		print('Retweeted the tweet.')
		sleep(45) # Sleep for 45seconds so we will not be banned by Twitter.. lol
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

# Favorite specified keywords
favorite = '%23durian%20OR%20%23mangosteen'
numOffavTweets = 2
for tweet in tweepy.Cursor(api.search, favorite).items(numOffavTweets):
	try:
		tweet.favorite() 
		print('Favorite-ed the tweet.')
		sleep(45) # Sleep for 45seconds so we will not be banned by Twitter.. lol
	except tweepy.TweepError as e:
		print(e.reason)
	except StopIteration:
		break

# Retweet the keywords in trend
trendsPlace = api.trends_place(1154781) # id for Malaysia, view more here: https://codebeautify.org/jsonviewer/f83352
data = trendsPlace[0] 
trends = data['trends']
# Get the name from each trend
names = [trend['name'] for trend in trends]

for name in names:
	for tweet in tweepy.Cursor(api.search, name).items(1):
		try:
			if (not tweet.retweeted) and ('RT @' not in tweet.text): # This is to prevent dupicating retweets
				tweet.retweet()
				print('Retweeted the tweet.')
				sleep(45) # Sleep for 45seconds so we will not be banned by Twitter.. lol
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break

