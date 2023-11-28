import tweepy

def post_to_twitter(tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret, image_path, caption):
    try:
        auth = tweepy.OAuthHandler(tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret)
        auth.set_access_token(tweet_access_token, tweet_access_token_secret)
        api = tweepy.API(auth)
        
        media = api.media_upload(image_path, chunked=True)
        media_ids = [media]

        api.simple_upload(media_ids)

        print("Posted to Twitter successfully!")
    except Exception as e:
        print(f"Twitter post failed: {e}")
