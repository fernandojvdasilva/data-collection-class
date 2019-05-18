import tweepy

CONSUMER_KEY = 'sUotdtsMfNECbiIlESbg1gkOS'
CONSUMER_SECRET = "yXQkSA4DTZ55z3aBKeYKXpK1Aro2C9jNJtzMLagcTaT3RygdpA"

OAUTH_TOKEN = "1795037040-xto2FmaXa84Q0JnjEYiwx4X53cng48WSnnHEKoe"
OAUTH_TOKEN_SECRET = "UftjJDUQJpkPVAqR7wnu0TAkMfKErNWUxqVREfuQEKT2B"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        print(status.text)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth,
                         listener=myStreamListener)

myStream.filter(track=['watford'],
                is_async=True)














