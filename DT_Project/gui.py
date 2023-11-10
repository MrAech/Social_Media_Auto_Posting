import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
import stlye
from stlye import set_styles, create_header_frame
import subprocess

def execute_facebook_script(face_access_token, post_date):
    try:
        result = subprocess.check_output(['python', 'facebook.py', face_access_token, post_date], text=True)
        messagebox.showinfo("Script Execution", f"Facebook script executed successfully. Result: {result}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Facebook script execution failed: {e}")

def execute_twitter_script(tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret):
    try:
        result = subprocess.check_output(['python', 'twitter.py', tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret], text=True)
        messagebox.showinfo("Script Execution", f"Twitter script executed successfully. Result: {result}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Error", f"Twitter script execution failed: {e}")

def on_execute_button_click():
    # Get input values from entry fields
    face_access_token = face_access_token_entry.get()
    post_date = post_date_entry.get()

    tweet_consumer_key = tweet_consumer_key_entry.get()
    tweet_consumer_secret = tweet_consumer_secret_entry.get()
    tweet_access_token = tweet_access_token_entry.get()
    tweet_access_token_secret = tweet_access_token_secret_entry.get()

    # Check if any of the fields is empty
    if not face_access_token or not post_date or not tweet_consumer_key or not tweet_consumer_secret or not tweet_access_token or not tweet_access_token_secret:
        messagebox.showerror("Error", "Please enter values for all variables.")
        return

    # Execute the Facebook script with input values
    execute_facebook_script(face_access_token, post_date)

    # Execute the Twitter script with input values
    execute_twitter_script(tweet_consumer_key, tweet_consumer_secret, tweet_access_token, tweet_access_token_secret)

window = tk.Tk()
window.title("Social Media Post Scheduler")

# Set styles
set_styles()

# Create header frame
create_header_frame(window, "Social Media Post Scheduler")

# Create and place entry fields for Facebook
tk.Label(window, text="Facebook Access Token:").grid(row=1, column=0, pady=(10, 5))
face_access_token_entry = ttk.Entry(window)
face_access_token_entry.grid(row=1, column=1, pady=(10, 5))

tk.Label(window, text="Facebook Post Date (HH:MM):").grid(row=2, column=0, pady=(10, 5))
post_date_entry = ttk.Entry(window)
post_date_entry.grid(row=2, column=1, pady=(10, 5))

# Create and place entry fields for Twitter
tk.Label(window, text="Twitter Consumer Key:").grid(row=3, column=0, pady=(10, 5))
tweet_consumer_key_entry = ttk.Entry(window)
tweet_consumer_key_entry.grid(row=3, column=1, pady=(10, 5))

tk.Label(window, text="Twitter Consumer Secret:").grid(row=4, column=0, pady=(10, 5))
tweet_consumer_secret_entry = ttk.Entry(window)
tweet_consumer_secret_entry.grid(row=4, column=1, pady=(10, 5))

tk.Label(window, text="Twitter Access Token:").grid(row=5, column=0, pady=(10, 5))
tweet_access_token_entry = ttk.Entry(window)
tweet_access_token_entry.grid(row=5, column=1, pady=(10, 5))

tk.Label(window, text="Twitter Access Token Secret:").grid(row=6, column=0, pady=(10, 5))
tweet_access_token_secret_entry = ttk.Entry(window)
tweet_access_token_secret_entry.grid(row=6, column=1, pady=(10, 5))

# Create and place execute button
execute_button = ttk.Button(window, text="Schedule Posts", command=on_execute_button_click)
execute_button.grid(row=7, column=0, columnspan=2, pady=(15, 10))

# Start the GUI event loop
window.mainloop()