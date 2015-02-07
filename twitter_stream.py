from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey = 'uOCEGlJx8Fati0XRvJN3vWfQy'
csecret = 'jmXV3j1UEkefOBlOaj93XVKEr35igEXzkyNeA6rlBy5HERDeHJ'
atoken = '238928383-WFlMFWImuNtU8Hhb7GYTaZxxZ58AumH6FdoWES2X'
asecret = 'gse3jCt9XvUE8u78kLGjs37FtzeDV19ZUR5VhsLhXcg5B'

class TwitterStream(StreamListener):

	def on_data(self, data):
		try:
			print data
			saveFile = open('twitDB.csv', 'a')
			saveFile.write(data)
			saveFile.write('\n')
			saveFile.close()
			return True
		except BaseException, e:
			print 'failed ondata,',str(e)

	def on_error(self, status):
		print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, TwitterStream())
twitterStream.filter(track=["netflix"])