# Databricks notebook source
# MAGIC %sh pip install tweepy

# COMMAND ----------

dbutils.fs.ls("/FileStore/justin/")

# COMMAND ----------

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
#access_token = "your token"
#access_token_secret = "your token secret"
#consumer_key = "your key"
#consumer_secret = "your key secret"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        file = open("/dbfs/FileStore/justin/twitterdata.txt","a")
        #https://demo.cloud.databricks.com/files/justin/twitterdata.txt
        file.write(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=['databricks', 'Databricks', '#databricks', '#Databricks', 'Azure', '#Azure'])
