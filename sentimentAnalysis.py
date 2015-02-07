#!/usr/bin/python

import nltk
import json
import csv
from sys import stdin
import re
import codecs

# json_data=open('twitDB.csv')

# data = json.loads(json_data)

listOfTweets = list()
count = 0
#with open('twitDB.csv', 'r') as tweetsFile:

lines = open('twitDB.csv').read().splitlines()
for line in lines:
	if line == "" or json.loads(line)['lang'] != "en":
		pass
	else:
		listOfTweets.append(json.loads(line)['text'])

labelledTweets = codecs.open('labelledTweets.csv', 'a', 'utf-8')



for tweet in listOfTweets[458:-1]:
	print tweet

	#Convert to lower case
	tweet = tweet.lower()
	#Convert www.* or https?://* to URL
	tweet = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',tweet)
	#Convert @username to AT_USER
	tweet = re.sub('@[^\s]+','AT_USER',tweet)
	tweet = re.sub('[\s]+', ' ', tweet)
	#Replace #word with word
	tweet = re.sub(r'#([^\s]+)', r'\1', tweet)
	#trim
	tweet = re.sub(u"(\u2018|\u2019|\u2026|\u20ac)", "'", tweet)
	tweet = re.sub(r'[^\x00-\x7F]',' ', tweet)

	print '\n\tType p = pos, n = neg, d = neutral'
	label = raw_input()


	csvString = str(label) + "," + str(tweet) + "\n"
	print csvString
	labelledTweets.write(csvString)

	count += 1
	print "Added " + str(count) + " tweets"

saveFile.close()


    # content = content_file.read()
    # print json.dumps(content)
    # array = []
    # reader = csv.reader(content_file)
    # for row in reader:
    # 	array.append(json.dumps(row))
    # for item in array:
    # 	if item == '[]':
    # 		array.remove(item)
    # 	print item['text']


# json_data.close()
