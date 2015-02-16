from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
import ConfigParser

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.twitter

    def on_data(self, data):
        self.db.ukstream.insert(data)
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()

    Config = ConfigParser.ConfigParser()
    Config._interpolation = ConfigParser.ExtendedInterpolation()
    Config.read("twitter.ini")

    section = "TwitterDebug"

    auth = OAuthHandler(Config.get(section, 'consumer_key'), Config.get(section, 'consumer_secret'))
    auth.set_access_token(Config.get(section, 'access_token'), Config.get(section, 'access_token_secret'))

    stream = Stream(auth, l)
    stream.filter(locations=[-11.909180,49.234637,2.373047,61.245799])