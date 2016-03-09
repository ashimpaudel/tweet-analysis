#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "gSg0l33RA7pIw0s2Oz2dij97X"
consumer_secret = "SlmtoRBot9tUwTQFOsCDDq5MKd0d4MEdVP2LNScj1rrCa7QGTU"
access_key = "327357336-EsvXQ8FYWYAzdSnQLaf2maLsW1vm67FLqdxUP3Gd"
access_secret = "YWavqT6PXGpEGB5rbwcf9siTCeDxTeibgy7ild0oM88W1"


def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200,include_rts=False)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest, include_rts=False)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["text"])
		writer.writerows(outtweets)
	
	pass
get_all_tweets('taylorswift13')


if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets("J_tsar")
