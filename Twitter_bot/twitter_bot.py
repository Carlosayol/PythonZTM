import tweepy
import time

auth = tweepy.OAuthHandler("bIs4oceQFUyV5JQ0hUmnoJHya","lCBMyOGLIOaSijTNqArcqXXJUwbjpzUfR4Xc9KXP2RrdXvBt3U")
auth.set_access_token("3307744882-b4RcB5yQlPJp1BnNtigSoLiznWPDG8crbnRAGOE","340tfEhUx6YdajRNaPxmmOzOcnxNMT1HZe1AuohWH15vp")

api = tweepy.API(auth)

user = api.me()

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(300)

search_string = 'Carlos Ayala'
numberOfTweets = 5

# for tweet in limit_handler(tweepy.Cursor(api.search, search_string).items(numberOfTweets)):
#     try:
#         tweet.favorite()
#         print('I liked that tweet')
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

#Generous_bot
for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    #if follower.name == "Ojala tuviera un follower :c":
    follower.follow()
    break


