import tweepy

CONSUMER_KEY = ''
CONSUMER_SECRET = ""

OAUTH_TOKEN = ""
OAUTH_TOKEN_SECRET = ""

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
api = tweepy.API(auth)
import pprint
from datetime import date, timedelta
last_month=date.today() - timedelta(days=30)

tweets = tweepy.Cursor(api.search,
                       q='facens',
                       since=last_month.strftime('%Y-%m-%d'),
                       until=date.today().strftime('%Y-%m-%d'),
                       include_entities=True,
                       lang='pt').items()
for t in tweets:
    pprint.pprint(t._json)