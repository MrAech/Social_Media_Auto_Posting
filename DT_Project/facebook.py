'''
import facebook
import sys

def post_to_facebook(face_access_token, post_date, image_path, caption):

    print("Apoligies cannot upload to facebook at the moment")
    
    
    try:
        # Initialize the Graph API client
        graph = facebook.GraphAPI(access_token=face_access_token, version='3.0')

        # Upload photo or video
        with open(image_path, 'rb') as image:
            graph.put_photo(image=image, message=caption)

        print("Posted to Facebook successfully!")
    except Exception as e:
        print(f"Facebook post failed: {e}")
        

# Check if the script is run from the command line
if __name__ == "__main__":
    # Check if enough arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python facebook.py <access_token> <post_date> <image_path> <caption>")
        sys.exit(1)

    face_access_token = sys.argv[1]
    post_date = sys.argv[2]
    image_path = sys.argv[3]
    caption = sys.argv[4]
    
if __name__ == "__main__":
    # Call the post_to_facebook function with provided arguments: face_access_token, post_date, image_path, caption
    post_to_facebook()
'''
