#!/usr/bin/python

import nltk
import json
import csv

posDictionary = dict()
neutDictionary = dict()
negDictionary = dict()

def handleWord(word, label):
	if label == "p":
		print word
		if posDictionary.has_key(word):
			posDictionary[word] = str(int(posDictionary[word]) + 1)
		else: 
			posDictionary[word] = str(1)
		
	elif label == "n":
		print word
		if neutDictionary.has_key(word):
			neutDictionary[word] = str(int(posDictionary[word]) + 1)
		else: 
			neutDictionary[word] = str(1)

	elif label == "d":
		print word
		if negDictionary.has_key(word):
			negDictionary[word] = str(int(posDictionary[word]) + 1)
		else: 
			negDictionary[word] = str(1)

def classifyTweet(tweet):
	words = tweet.split(' ')
	size = len(words)
	print 'size is ' + str(size)
	positive = 0.0
	neutral = 0.0
	negative = 0.0

	for word in words:
		if posDictionary.has_key(word):
			positive += int(posDictionary[word])	

		if neutDictionary.has_key(word):
			neutral += int(neutDictionary[word]) 

		if negDictionary.has_key(word):
			negative += int(negDictionary[word])
			
	positive /= size
	neutral /= size
	negative /= size

	print '\tpositive ' + str(positive)
	print '\tneutral ' + str(neutral)
	print '\tnegative ' + str(negative)

def replaceTwoOrMore(s):
    pattern = re.compile(r"(.)\1{1,}", re.DOTALL)
    return pattern.sub(r"\1\1", s)

def getStopWordList(stopWordListFileName):
    stopWords = []
    stopWords.append('AT_USER')
    stopWords.append('URL')

    fp = open(stopWordListFileName, 'r')
    line = fp.readline()
    while line:
        word = line.strip()
        stopWords.append(word)
        line = fp.readline()
    fp.close()
    return stopWords

# Train Classifier

lines = open('test.csv').read().splitlines()
for line in lines:
	print line
	lineArray = line.split(',')
	label = lineArray[0]
	text = lineArray[1]

	words = line.split(' ')
	for word in words:
		handleWord(word, label)



for item in posDictionary:
	print item 


lines = open('twitDB.csv').read().splitlines()
for line in lines:
	if line == "":
		pass
	else:
		text = json.loads(line)['text']
		classifyTweet(text)
		print text







# Run Classifier