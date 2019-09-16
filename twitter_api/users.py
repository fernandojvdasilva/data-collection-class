import tweepy
import pprint

CONSUMER_KEY = ''
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)

users = api.lookup_users(screen_names=['potus'])
pprint.pprint(users[0]._json)

friends = api.friends(users[0].id)
pprint.pprint(friends)

followers = api.followers(users[0].id)
print(len(followers))