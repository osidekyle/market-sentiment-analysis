import tweepy
from creds import *

client = tweepy.Client(bearer_token)

# Search Recent Tweets

# This endpoint/method returns Tweets from the last seven days

response = client.search_recent_tweets("BTC", tweet_fields=["lang"])

tweets = response.data

# Each Tweet object has default ID and text fields
for tweet in tweets:
    if tweet.lang == 'en':
        print("Tweet:\n",tweet.text)
