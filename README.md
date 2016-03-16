# tweet-analysis ML Research

Contributors:
- Ashim Paudel
- Nischal Baral
- Roshil Paudyal
- Saurav Keshari Aryal

Current Status: Evaluating the readability of tweets using the Flesch–Kincaid algorithm.

Languages: Python 2.7

Python package dependencies, we recommend pip installing them if needed:
- re
- csv
- textstat
- tweepy

How to run:

1) Run the Tweets_Excluding_Retweets.py by supplying a the username of the twitter user wanted as a commandline arguement.
  Output: a username_tweets.csv file with tweets from Twiiter excluding retweets. 
2) Run reading_from_csv.py by supplying the username of the user you choose to analyze.
  Output: Commandline output of number of tweets analyzed, average, and median Flesch–Kincaid grade scores.
  
  
The program works when tested on Ubuntu 14.04 with Ubuntu, Python 2.7.11, and pip 8.1.0. 

Please make your own keys needed for Twitter.
Then,replace them in theTweets_Excluding_Retweets.py file, if you plan to use this code..
