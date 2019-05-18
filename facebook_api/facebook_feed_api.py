import facebook

import pprint

token='EAAJ3Jw24uAEBAA3FX0qAdd5rWJ0IFPH70jSZB6ZB4mFbNv4ZBQZCvXsjBKnkzbO45SyyZA5FF74NnxRZAbTt8A10KOJXdRqP3bpWZAGni3uUz3MeNzroJ9uBZA7iZCmj0Q1QphtSttPlTfgfTvkrW4OrSgkBkedXHOliJlDF7NcVvnMI6SKL33jRaQ0o7lVhdZCmQZD'

graph_api = facebook.GraphAPI(access_token=token,
                              version='3.1')

me = graph_api.get_object('me')

pprint.pprint(me)

#====================

#results = graph_api.request('search', {'q':'games', 'type': 'page'})

#pprint.pprint(results)

my_feed = graph_api.get_connections(me['id'], 'feed')
pprint.pprint(my_feed)

my_likes = graph_api.get_connections(me['id'], 'likes')
pprint.pprint(my_likes)

import urllib3
import json

while 'paging' in my_likes.keys() and \
        'next' in my_likes['paging'].keys():
    http = urllib3.PoolManager()
    my_likes = http.request('GET', my_likes['paging']['next'])
    my_likes = json.loads(my_likes.data)
    pprint.pprint(my_likes)








#test = graph_api.get_object(1412270155739022)
#pprint.pprint(test)
















