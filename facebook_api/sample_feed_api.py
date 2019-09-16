import facebook
import urllib3
import json

import pprint

token='EAAJ3Jw24uAEBADFXDI2ZCZASolC1Ot083owmanqMqHHZAz4wUWW5jloGPGUvimN1kacxOVZCsQHc32XRVffSiDqONRkGvNtTvc3LLXC3jL2vrmLkxHdIJu86dDjt3TL6WyRMcBbw03OQ6Th4ZAC7HsQjiCCRRx1ETnC8r24boXAZDZD'

graph_api = facebook.GraphAPI(access_token=token, version="3.1")

# Obtendo dados do próprio usuário
me = graph_api.get_object('me')

pprint.pprint(me)

# Busca por páginas sobre games
search_results = graph_api.request("search",  {'q':'games', 'type':'page'})

# Obtendo o feed da página da Coca-Cola
try:
    coke_id = '40796308305'
    coke_feed = graph_api.get_connections(coke_id, 'feed')
    pprint.pprint(coke_feed)
except:
    pass

# Obtendo o meu próprio feed
my_feed = graph_api.get_connections(me['id'], 'feed')
pprint.pprint(my_feed)



# Obtendo o meu próprio feed
my_likes = graph_api.get_connections(me['id'], 'likes')
pprint.pprint(my_likes)
while 'paging' in my_likes.keys() and 'next' in my_likes['paging'].keys():
    try:
        http = urllib3.PoolManager()
        my_likes = http.request('GET', my_likes['paging']['next'])
        my_likes = json.loads(my_likes.data)
        pprint.pprint(my_likes)
    except Exception as ex:
        pprint.pprint(ex)
        break


# Obtendo amigos
my_friends = graph_api.get_connections(me['id'], 'friends')['data']
pprint.pprint(my_friends)

# Obtendo eventos
my_events = graph_api.get_connections(me['id'], 'events')['data']
pprint.pprint(my_friends)