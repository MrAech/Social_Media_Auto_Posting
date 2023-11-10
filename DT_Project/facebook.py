import facebook
import schedule
import time
import os

def post_to_facebook():
    # Initialize the Graph API client
    graph = facebook.GraphAPI(access_token='face_access_token', version='3.0')

    # Upload photo or video
    graph.put_photo(image=open('image', 'rb'), message='Caption')

    # Delete photo or video after posting (optional)
    os.remove('image')

# Set the date and time for the post
post_date = 'get_time'

# Schedule the post at the specified date and time
schedule.every().day.at(post_date).do(post_to_facebook)

# Keep running the script to check for scheduled tasks
while True:
    schedule.run_pending()
    time.sleep(1)