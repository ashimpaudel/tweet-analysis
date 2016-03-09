#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import csv

#http://www.tweepy.org/
import tweepy

#Get your Twitter API credentials and enter them here
consumer_key ='gSg0l33RA7pIw0s2Oz2dij97X'
consumer_secret ='SlmtoRBot9tUwTQFOsCDDq5MKd0d4MEdVP2LNScj1rrCa7QGTU'
access_key ='327357336-EsvXQ8FYWYAzdSnQLaf2maLsW1vm67FLqdxUP3Gd'
access_secret ='YWavqT6PXGpEGB5rbwcf9siTCeDxTeibgy7ild0oM88W1'
#method to get a user's last 100 tweets
def get_tweets(username):

	#http://tweepy.readthedocs.org/en/v3.1.0/getting_started.html#api
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	#set count to however many tweets you want; twitter only allows 200 at once
	number_of_tweets = 100

	#get tweets
	tweets = api.user_timeline(screen_name = username,count = number_of_tweets)

	#create array of tweet information: username, tweet id, date/time, text
	tweets_for_csv = [[username,tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

	#write to a new csv file from the array of tweets
	print "writing to {0}_tweets.csv".format(username)
	with open("{0}_tweets.csv".format(username) , 'w+') as file:
		writer = csv.writer(file, delimiter='|')
		writer.writerows(tweets_for_csv)


def clean_data(username):
	file_name = "{0}_tweets.csv".format(username)
	cleaned_tweets = []
	with open(file_name) as csvfile:
		for row in csvfile:
			current_tweet = ''
			row = row.split('|')
			Is_retweet = False
			if len(row) <= 1:
				continue 
			for i in xrange(2, len(row)):
				text_array = row[i].split(" ")
				print text_array
				print type(text_array)
				for word in text_array:
					print len(word)
					# removes some enocded chars
					if len(word) < 1:
						continue									
					# skips hashtags
					if word == "RT":
						Is_retweet = True
						break
					if word[0] == '#':
						continue	 					
					# simple solution because all the URLs shared are https
					if "https://" in word or "http://" in word:
						continue
					#rmeove @ from every word that beggins with it	
					if word[0] == "@":
						word = word[1:]
					current_tweet += word + " "
				if Is_retweet:
					current_tweet = ""
					break
				if current_tweet != "":	
					current_tweet = current_tweet[0:len(word)-1]
					print current_tweet
					cleaned_tweets.append(current_tweet)
	print cleaned_tweets			



#if we're running this as a script
if __name__ == '__main__':

    #get tweets for username passed at command line
    if len(sys.argv) == 2:
        get_tweets(sys.argv[1])
    else:
        print "Error: enter one username"
    clean_data(sys.argv[1])
    #alternative method: loop through multiple users
	# users = ['user1','user2']
	# Gshankar_Gautam
	# for user in users:
	# 	get_tweets(user)
