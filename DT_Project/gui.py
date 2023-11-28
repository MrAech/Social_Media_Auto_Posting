import tkinter as tk
from tkinter import ttk, filedialog
from tkinter import messagebox
import sys
import subprocess
from style import set_styles, create_header_frame
from twitter import post_to_twitter

selected_image_path = ""  # Variable to store the selected image path
'''
def execute_facebook_script():
    face_access_token = face_access_token_entry.get()
    post_date = post_date_entry.get()
    caption = caption_entry.get()

    try:
        result = subprocess.check_output([sys.executable, 'facebook.py', face_access_token, post_date, selected_image_path, caption], text=True)
        messagebox.showinfo("Script Execution", f"Facebook script executed successfully. Result: {result}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Facebook script execution failed: {e}")
''' 
def execute_twitter_script():
    tweet_consumer_key = tweet_consumer_key_entry.get()
    tweet_consumer_secret = tweet_consumer_secret_entry.get()
    tweet_access_token = tweet_access_token_entry.get()
    tweet_access_token_secret = tweet_access_token_secret_entry.get()
    caption = caption_entry.get()

    try:
        result = post_to_twitter(tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret, selected_image_path, caption)
        messagebox.showinfo("Script Execution", f"Twitter script executed successfully. Result: {result}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Twitter script execution failed: {e}")

def select_image():
    global selected_image_path  # Use the global variable to store the selected image path
    filename = filedialog.askopenfilename(title="Select Image File", filetypes=(("Image Files", "*.png; *.jpg; *.jpeg; *.gif"), ("All Files", "*.*")))
    if filename:  # Check if a file is selected
        selected_image_path = filename
        messagebox.showinfo("Image Selected", f"Selected Image: {filename}")

window = tk.Tk()
window.title("Social Media Post Scheduler")

create_header_frame(window, "Social Media Post Scheduler")

set_styles()

# Create entry fields for Facebook
label_face = ttk.Label(window, text="Facebook Access Token:")
label_face.grid(row=1, column=0, pady=(10, 5))
face_access_token_entry = ttk.Entry(window)
face_access_token_entry.grid(row=1, column=1, pady=(10, 5))

label_date = ttk.Label(window, text="Facebook Post Date (HH:MM):")
label_date.grid(row=2, column=0, pady=(10, 5))
post_date_entry = ttk.Entry(window)
post_date_entry.grid(row=2, column=1, pady=(10, 5))

label_caption = ttk.Label(window, text="Caption:")
label_caption.grid(row=3, column=0, pady=(10, 5))
caption_entry = ttk.Entry(window)
caption_entry.grid(row=3, column=1, pady=(10, 5))

# Upload Image button for selecting image
label_image = ttk.Label(window, text="Image: ")
label_image.grid(row=4, column=0, pady=(10, 5))
upload_image_button = ttk.Button(window, text="Upload Image", command=select_image, style='ImageButton.TButton')
upload_image_button.grid(row=4, column=1, columnspan=2, pady=(10, 5))

# Entry fields for Twitter (if any)
label_consumer_key = ttk.Label(window, text="Twitter Consumer Key:")
label_consumer_key.grid(row=5, column=0, pady=(10, 5))
tweet_consumer_key_entry = ttk.Entry(window)
tweet_consumer_key_entry.grid(row=5, column=1, pady=(10, 5))

label_consumer_secret = ttk.Label(window, text="Twitter Consumer Secret:")
label_consumer_secret.grid(row=6, column=0, pady=(10, 5))
tweet_consumer_secret_entry = ttk.Entry(window)
tweet_consumer_secret_entry.grid(row=6, column=1, pady=(10, 5))

label_access_token = ttk.Label(window, text="Twitter Access Token:")
label_access_token.grid(row=7, column=0, pady=(10, 5))
tweet_access_token_entry = ttk.Entry(window)
tweet_access_token_entry.grid(row=7, column=1, pady=(10, 5))

label_access_token_secret = ttk.Label(window, text="Twitter Access Token Secret:")
label_access_token_secret.grid(row=8, column=0, pady=(10, 5))
tweet_access_token_secret_entry = ttk.Entry(window)
tweet_access_token_secret_entry.grid(row=8, column=1, pady=(10, 5))

# Execute button
def on_execute_button_click():
    '''
    # Check if any field is empty
    if not all(entry.get() for entry in (face_access_token_entry, post_date_entry, caption_entry)):
        messagebox.showerror("Error", "Please enter values for all Facebook variables.")
        return
    '''
    
def on_execute_button_click():
    if not all(entry.get() for entry in (tweet_consumer_key_entry, tweet_consumer_secret_entry, tweet_access_token_entry, tweet_access_token_secret_entry, caption_entry)) or not selected_image_path:
        messagebox.showerror("Error", "Please enter values for all Twitter variables and select an image.")
        return

    # Execute scripts
    #execute_facebook_script()
    execute_twitter_script()

execute_button = ttk.Button(window, text="Schedule Posts", command=on_execute_button_click)
execute_button.grid(row=9, column=0, columnspan=2, pady=(15, 10))

window.mainloop()
