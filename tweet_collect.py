import tweepy
import json
import pprint
import csv

# twitter api key
consumer_key = "your_key"
consumer_secret = "your_secret"
access_token = "your_token"
access_token_secret = "your_token_secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):

	def __init__(self, outoutfile):
		super().__init__()
		self.counter = 0
		self.limit = 100
		self.outoutfile = outoutfile

	def on_data(self, data):
		s_data = json.loads(data)
		if "retweeted_status" not in s_data:
			with open(self.outoutfile, 'a', encoding='utf-8',newline="") as file:
				writer = csv.writer(file)
				writer.writerow([s_data["created_at"], s_data["id"],s_data["text"]])

			print("success")
			print(s_data)
			self.counter +=1
			print(self.counter)

			# disconnect twitter api after getting reasonable amount of tweets
			if self.counter < self.limit:
				return True
			else:
				return False


if __name__ == '__main__':

	myStreamListener = MyStreamListener()
	myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
	# Sample search with keywords
	keyword = ["Sports, Sport", "Basketball, NBA", "American football, football", "Baseball", "Soccer"]

	#Approximate bounding box location for USA
	myStream.filter(track=["baseball, baseballs"],
					languages=["en"]).filter(locations=[-179.1506, 18.9117, -66.9406, 71.4410])

	print("Done")