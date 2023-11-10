import twitter
import os
import schedule
import time

def post_to_twitter():
    # Authenticate with Twitter API
    api = twitter.Api(consumer_key='tweet_consumer_key',
                      consumer_secret='tweet_consumer_secret',
                      access_token_key='tweet_access_token',
                      access_token_secret='tweet_access_token_secret')

    # Upload media and create tweet
    with open('image', 'rb') as file:
        media = api.UploadMediaSimple(file)
        
    tweet = 'Caption'
    status = api.PostUpdate(status=tweet, media=[media.media_id])

    # Delete media file after posting (optional)
    os.remove('image')

# Schedule the tweet
schedule.every().day.at("12:00").do(post_to_twitter)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)