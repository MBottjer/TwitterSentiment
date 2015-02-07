#!/usr/bin/python

import nltk
import json
import csv

# json_data=open('twitDB.csv')

# data = json.loads(json_data)



#with open('twitDB.csv', 'r') as tweetsFile:

lines = open('twitDB.csv').read().splitlines()
for line in lines:
	if line == "":
		pass
	else:
		print json.loads(line)['text']

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