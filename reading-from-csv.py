import re 
import csv


f = open('workfileTrump.txt', 'w')


original = file('taylorswift13_tweets.csv', 'rU')
reader = csv.reader(original)

cleaned_tweets = []

# get a singel mutli line tweet as array
for row in reader:
    #  extracting tweet as string, every row has one string element
    tweet_str = row[0]

    # splitting multi line tweets to form single array.
    multi_line_arr = tweet_str.split("\n")
   
    # for multiline tweets, make asingel tweet string at index 0.
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
        # skipping URLS
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

for tweet in cleaned_tweets:
        tweet = re.sub("[^0-9a-zA-Z!\,;:'-_\.\^\$\*\+\?\s\"\-]", "",tweet)    
        f.write(tweet)               
        f.write('\n')
f.close()
