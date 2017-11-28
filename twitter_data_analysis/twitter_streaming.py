#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API 
access_token = "183944935-xYBZt9wxfSXgdqdvQwcDk6PfFAEZzrO2Pb2Yp7Yx"
access_token_secret = "eXS2BLlOOAax9HEcul1u0g1ykQQOhISoaBy5ArkMkPMou"
consumer_key = "5DmRscVMxZ0oB4T7C7DBWuTLM"
consumer_secret = "8U9dbGkPj0yycZ8MbOwSft7X756zFxjdh7JcHgq4QQ3MVvaxXB"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print (data)
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['IvankaTrump', 'Trump'])
