#!/usr/bin/python

import nltk
import json
import csv

json_data=open('twitDB.csv')

data = json.load(json_data)



with open('twitDB.csv', 'r') as content_file:
    content = content_file.read()
    print content



json_data.close()