from tweepy import Client, OAuthHandler, API
import os
from log import logger


class TweetClient(object):
    consumer_key = os.environ.get("CONSUMER_KEY")
    consumer_secret = os.environ.get("CONSUMER_SECRET")
    access_token = os.environ.get("ACCESS_TOKEN")
    access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")
    bearer_token = os.environ.get("BEARER_TOKEN")

    def create_v1(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_token_secret)
        return API(auth)

    def create_v2(self):
        return Client(
            consumer_key=self.consumer_key,
            consumer_secret=self.consumer_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def upload_media(self, file_name):
        client = self.create_v1()
        res = client.media_upload(filename=file_name)
        return res.media_id_string

    def create_tweet(self, **kwargs):
        client = self.create_v2()
        resp = client.create_tweet(**kwargs)
        return resp

    def create_media_tweet(self, files, text):
        media_ids = []
        if isinstance(files, list):
            if len(files) > 0:
                for file in files:
                    media_id = self.upload_media(file)
                    media_ids.append(media_id)
        elif isinstance(files, str):
            media_id = self.upload_media(files)
            media_ids.append(media_id)
        else:
            logger.warn("files: %s", files)
        resp = self.create_tweet(text=text, media_ids=media_ids)
        return resp

    def delete_tweet(self, tweet_id):
        client = self.create_v2()
        response = client.delete_tweet(id=tweet_id)
        return response


tweet_client = TweetClient()
