import json
import time
import urllib2

currentTimestamp = ""

while(True):
	time.sleep(1)
	print "Getting data"

	url = 'https://api.bitcoinaverage.com/ticker/USD/'
	response = urllib2.urlopen(url).read()
	timestamp = json.loads(response)

	# print timestamp
	

	if str(timestamp['timestamp']) == str(currentTimestamp):
		pass
	else:
		currentTimestamp = timestamp['timestamp']
		print "Got new timestamp"
		print 'currentTimestamp is ' + str(currentTimestamp)
		print 'timestamp is ' + str(timestamp['timestamp'])
		saveFile = open('bitcoin.csv', 'a')
		saveFile.write(response)
		saveFile.write('\n')
		saveFile.close()

	