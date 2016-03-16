#import for regex matching
import re 

# import for reading and writing data from csv files
import csv

# import for text analysis
from textstat.textstat import textstat

#import for command line arguement
import sys


if (len(sys.argv) == 2):
	f = open(sys.argv[1] + '_cleaned_tweets.txt', 'w')


	original = file(sys.argv[1] + '_tweets.csv', 'rU')
	reader = csv.reader(original)

	cleaned_tweets = []

	# get a singel mutli line tweet as array
	for row in reader:
	    #  extracting tweet as string, every row has one string element
	    tweet_str = row[0]

	    # splitting multi line tweets to form single array.
	    multi_line_arr = tweet_str.split("\n")
	   
	    # for multiline tweets, make a single tweet string at index 0.
	    if len(multi_line_arr) > 1:
	        for i in xrange(1, len(multi_line_arr)):
	            multi_line_arr[0] += " " + multi_line_arr[i]
	    
	    # getting an array of words for the tweet
	    tweet_arr = multi_line_arr[0].split(" ") 
	    # set and reset clean_tweet for every row i.e tweet.
	    clean_tweet = ""
	    for word in tweet_arr:
	        # skip some not text characters probably unicode eith len < 1
	        if len(word) < 1:
	            continue
	        # handling #s    
	        if '#' in word:
	            hash_index = word.index('#')
	            clean_word = word[0:hash_index]
	            clean_tweet += clean_word + " "            
	            continue
	        # skipping URLS.
	        # TODO: need a better implementation to catch other URLs.
	        if "https://" in word or "http://" in word:
	            continue
	        # handling @s    
	        if '@' in word:
	            at_index = word.index('@')
	            clean_word = word[1:at_index] + word[at_index+1:len(word)]
	            clean_tweet += clean_word + " "
	        # if none of the case above tweet is clean
	        else:
	            clean_tweet += word + " "

	    if len(clean_tweet) > 0:
	        cleaned_tweets.append(clean_tweet)
	    cleanest_tweets = []

	# removing unicode emoticons using regex, writing tweets to file, and to final array.
	for tweet in cleaned_tweets:
	        tweet = re.sub("[^0-9a-zA-Z!\,;:'-_\.\^\$\*\+\?\s\"\-]", "",tweet)    
	        cleanest_tweets.append(tweet)
	        f.write(tweet)               
	        f.write('\n')
	f.close()

	grades = []
	num_tweets = 0
	total_grade = 0
	for tweet in cleanest_tweets:
			# skipping tweets which are not just contextbased text. 
			if textstat.sentence_count(tweet) < 1:
				continue
			grade = textstat.flesch_kincaid_grade(tweet)	
			grades.append(grade)
			total_grade += grade
			num_tweets += 1

	#sorting for median
	grades.sort()
	#avg grade
	avg_grade = sum(grades) / num_tweets
	# median grade
	median_grade = grades[num_tweets / 2]
	print "Data for ", sys.argv[1] + "'s Tweets:"
	print "\nNumber of cleaned anted evaluated tweets: ", num_tweets
	print "\naverage flesch_kincaid _grade: ", avg_grade
	print "\nmedian flesch_kincaid_grade: ", median_grade
else:
	print "Please just supply the username of the user you want evaluated.\n"
