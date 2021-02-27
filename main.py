from typing import Counter
import tweepy
import twitter_key

CONSUMER_KEY=twitter_key.consumer_key
CONSUMER_SECRET=twitter_key.consumer_secret
ACCESS_TOKEN=twitter_key.access_token
ACCESS_TOKEN_SECRET=twitter_key.access_token_secret

auth=tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

api=tweepy.API(auth)

tweets=tweepy.Cursor(api.search,q='from:Roro3828_').items()
for i in tweets:
    print('='*100)
    print(i.text)