import tweepy

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.get_user(id="usuario")
print ("usuario: ",user.screen_name)
print ("segidores: ",user.followers_count)
#numero de publicaciones
print ("publicaciones: ",user.statuses_count)
#print ("likes: ", user.favourites_count)

public_tweets = api.user_timeline(id="usuario")
for i in range(len(public_tweets)):
  print("likes publiccacion",i+1,public_tweets[i].favorite_count)