import json
import requests
import tweepy
import config

STREAM_RULE_1 = "from:{} -is:retweet -is:reply".format(config.TWITTER_ID_1)
STREAM_RULE_2 = "from:{} -is:retweet -is:reply".format(config.TWITTER_ID_2)

class MySC(tweepy.StreamingClient):

    ENDPOINT = "https://api.telegram.org/bot{}/sendMessage"

    def on_tweet(self, tweet):

        print("[INFO] New tweet received")
        text = tweet.text

        req = self.ENDPOINT.format(config.TELEGRAM_BOT_API_KEY)
        params = {
            'chat_id':config.TELEGRAM_USER_ID,
            'text':text
        }

        requests.get(req,params=params)

        print('[INFO] New tweet sent to Telegram')




def main():
   streaming_client =MySC(config.BEARER_TOKEN)
   print('[INFO] Connected to stream')
   try:
       streaming_client.add_rules(tweepy.StreamRule(value=STREAM_RULE_1))
       streaming_client.add_rules(tweepy.StreamRule(value=STREAM_RULE_2))
       print('[INFO] Stream rule(s) added')
   except:
       print('[ERROR] Rule already exists')


   print('[INFO] Listening...')
   streaming_client.filter()





if __name__ == "__main__":
   main()
