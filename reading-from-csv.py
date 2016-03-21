#import for regex matching
import re 

# import for reading and writing data from csv files
import csv

# import for text analysis
from textstat.textstat import textstat

#import for command line arguement
import sys


if (len(sys.argv) == 2):
	f = open("./tweets/" + sys.argv[1] + "_cleaned_tweets.txt", 'w')


	original = file("./tweets/" + sys.argv[1] + "_tweets.csv", 'rU')
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
	"""Getting Data for several types of readability tests.
	   Learn more about each test from the link in the comments below."""
	# flesch kincaid: goo.gl/nWMsiL 
	flesch_kincaid_grades = []
	flesch_kincaid_total_grade = 0
	# gunning fog index: goo.gl/K9NzlW
	gunning_fog_grades = []
	gunning_fog_total_grade = 0
	# SMOG index: goo.gl/w3wskV
	smog_index_grades = []
	smog_index_total_grade = 0
	# Automated Readability Index: goo.gl/tI0CdX
	ar_index_grades = []
	ar_index_total_grade = 0
	# Coleman-Liau index: goo.gl/8sE0m1
	cl_index_grades = []
	cl_index_total_grade = 0
	# Linsear Write Formula: goo.gl/GuOZ8B
	lwf_grades = []
	lwf_total_grade = 0
	# Dale-Chall Readability Score: goo.gl/dvmXmx
	dcr_grades = []
	dcr_total_grade = 0		
	
	num_tweets = 0
	for tweet in cleanest_tweets:
			# skipping tweets which are not just contextbased text. 
			if textstat.sentence_count(tweet) < 1:
				continue
			flesch_kincaid_grade = textstat.flesch_kincaid_grade(tweet)	
			flesch_kincaid_grades.append(flesch_kincaid_grade)
			flesch_kincaid_total_grade += flesch_kincaid_grade

			gunning_fog_grade = textstat.gunning_fog(tweet)	
			gunning_fog_grades.append(gunning_fog_grade)
			gunning_fog_total_grade += gunning_fog_grade

			smog_index_grade = textstat.smog_index(tweet)	
			smog_index_grades.append(smog_index_grade)
			smog_index_total_grade += smog_index_grade

			ar_index_grade = textstat.automated_readability_index(tweet)	
			ar_index_grades.append(ar_index_grade)
			ar_index_total_grade += ar_index_grade
			
			cl_index_grade = textstat.coleman_liau_index(tweet)	
			cl_index_grades.append(cl_index_grade)
			cl_index_total_grade += cl_index_grade				

			lwf_grade = textstat.linsear_write_formula(tweet)	
			lwf_grades.append(lwf_grade)
			lwf_total_grade += lwf_grade

			dcr_grade = textstat.dale_chall_readability_score(tweet)	
			dcr_grades.append(dcr_grade)
			dcr_total_grade += dcr_grade

			num_tweets += 1



	#avg grades
	avg_flesch_kincaid_grade = flesch_kincaid_total_grade / num_tweets
	avg_gunning_fog_grade = gunning_fog_total_grade / num_tweets
	avg_smog_index_grade = smog_index_total_grade / num_tweets
	avg_ar_index_grade = ar_index_total_grade / num_tweets
	avg_cl_index_grade = cl_index_total_grade / num_tweets
	avg_lwf_grade = lwf_total_grade / num_tweets		
	avg_dcr_grade = dcr_total_grade / num_tweets		

	#sorting for median
	flesch_kincaid_grades.sort()
	gunning_fog_grades.sort()
	smog_index_grades.sort()
	ar_index_grades.sort()
	cl_index_grades.sort()
	lwf_grades.sort()
	dcr_grades.sort()


	median_index = num_tweets / 2
	# median grade
	flesch_kincaid_median_grade = flesch_kincaid_grades[median_index]
	gunning_fog_median_grade = gunning_fog_grades[median_index]
	smog_index_median_grade = smog_index_grades[median_index]
	ar_index_median_grade = ar_index_grades[median_index]
	cl_index_median_grade = cl_index_grades[median_index]
	lwf_median_grade = lwf_grades[median_index]
	dcr_median_grade = dcr_grades[median_index]

	# Outputing to console.
	print "Data for ", sys.argv[1] + "'s Tweets:\n"

	print "\nNumber of cleaned and evaluated tweets: ", num_tweets
	print "\n\nAverage Flesch-Kincaid grade: ", avg_flesch_kincaid_grade
	print "Median Flesch-Kincaid grade: ", flesch_kincaid_median_grade

	print "\n\nAverage Gunning FOG Formula: ", avg_gunning_fog_grade
	print "Median Gunning FOG Formula: ", gunning_fog_median_grade

	print "\n\nAverage SMOG INDEX: ", avg_smog_index_grade
	print "Median SMOG INDEX: ", smog_index_median_grade

	print "\n\nAverage Automated Readability INDEX: ", avg_ar_index_grade
	print "Median Automated Readability INDEX: ", ar_index_median_grade		

	print "\n\nAverage Automated Readability INDEX: ", avg_ar_index_grade
	print "Median Automated Readability INDEX: ", ar_index_median_grade

	print "\n\nAverage Coleman-Liau INDEX: ", avg_cl_index_grade
	print "Median Coleman-Liau INDEX: ", cl_index_median_grade

	print "\n\nAverage Linsear Write Formula: ", avg_lwf_grade
	print "Median Linsear Write Formula: ", lwf_median_grade

	print "\n\nAverage Dale-Chall Readability Score: ", avg_dcr_grade
	print "Median Dale-Chall Readability Score: ", dcr_median_grade

	#evaluating all tweet history.
	with open(sys.argv[1] + '_cleaned_tweets.txt', 'r') as content_file:
		content = content_file.read()
	
	overall_flesch_kincaid_grade = textstat.flesch_reading_ease(content)
	overall_gunning_fog_grade = textstat.gunning_fog(content)
	overall_smog_index = textstat.smog_index(content)
	overall_ari = textstat.automated_readability_index(content)
	overall_cli = textstat.coleman_liau_index(content)
	overall_lwf = textstat.linsear_write_formula(content)
	overall_dcr = textstat.dale_chall_readability_score(content)

	print "\n\nOverall Flesch-Kincaid Grade across all tweets: ", overall_flesch_kincaid_grade
	print "\nOverall Gunning FOG Formula across all tweets: ", overall_gunning_fog_grade
	print "\nOverall SMOG INDEX across all tweets: ", overall_smog_index
	print "\nOverall Automated Readability INDEX across all tweets: ", overall_ari
	print "\nOverall Coleman-Liau INDEX across all tweets: ", overall_cli
	print "\nOverall Linsear Write Formula across all tweets: ", overall_lwf
	print "\nOverall Dale-Chall Readability Score across all tweets: ", overall_dcr

else:
	print "Please just supply the username of the user you want evaluated.\n"


