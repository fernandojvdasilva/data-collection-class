import tweepy
import pprint

CONSUMER_KEY = 'sUotdtsMfNECbiIlESbg1gkOS'
CONSUMER_SECRET = "yXQkSA4DTZ55z3aBKeYKXpK1Aro2C9jNJtzMLagcTaT3RygdpA"

OAUTH_TOKEN = "1795037040-xto2FmaXa84Q0JnjEYiwx4X53cng48WSnnHEKoe"
OAUTH_TOKEN_SECRET = "UftjJDUQJpkPVAqR7wnu0TAkMfKErNWUxqVREfuQEKT2B"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

users = api.lookup_users(screen_names=['potus'])
pprint.pprint(users[0]._json)

friends = api.friends(users[0].id)
pprint.pprint(friends)

followers = api.followers(users[0].id)
print(len(followers))