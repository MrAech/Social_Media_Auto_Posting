import tkinter as tk
from PIL import Image, ImageTk
import tweepy
import discord
from facebook import GraphAPI
from tkinter import simpledialog, messagebox, filedialog

def send_to_discord(message, image_path, token, channel_id):
    intents = discord.Intents.default()
    intents.messages = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(int(channel_id))
        await channel.send(message, file=discord.File(image_path))

    client.run(token)

def send_to_twitter(message, image_path, consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    api.update_with_media(image_path, status=message)

def send_to_facebook(message, image_path, access_token):
    graph = GraphAPI(access_token)
    graph.put_photo(image=open(image_path, 'rb'), message=message)

def get_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        try:
            img = Image.open(file_path)
            img.thumbnail((300, 300))  # Resize the image without antialiasing
            photo = ImageTk.PhotoImage(img)
            image_label.config(image=photo)
            image_label.image = photo
            global selected_image_path
            selected_image_path = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Error opening image: {e}")

def send():
    message = message_entry.get()
    
    if discord_var.get():
        channel_id = simpledialog.askstring("Discord Channel ID", "Enter Discord Channel ID:")
        discord_token = simpledialog.askstring("Discord Token", "Enter Discord Bot Token:")
        send_to_discord(message, selected_image_path, discord_token, channel_id)
    if twitter_var.get():
        consumer_key = simpledialog.askstring("Twitter API", "Enter Twitter Consumer Key:")
        consumer_secret = simpledialog.askstring("Twitter API", "Enter Twitter Consumer Secret:")
        access_token = simpledialog.askstring("Twitter API", "Enter Twitter Access Token:")
        access_token_secret = simpledialog.askstring("Twitter API", "Enter Twitter Access Token Secret:")
        send_to_twitter(message, selected_image_path, consumer_key, consumer_secret, access_token, access_token_secret)
    if facebook_var.get():
        facebook_token = simpledialog.askstring("Facebook Access Token", "Enter Facebook Access Token:")
        send_to_facebook(message, selected_image_path, facebook_token)
    status_label.config(text="Message Sent!")

# Create GUI
root = tk.Tk()
root.title("Social Media Sender")
heading_label = tk.Label(root, text="Social Media Sender", font=("Arial", 20, "bold"))
heading_label.grid(row=0, column=0, columnspan=2, pady=20)

selected_image_path = ""

discord_var = tk.BooleanVar()
twitter_var = tk.BooleanVar()
facebook_var = tk.BooleanVar()

# Label for Message
message_label = tk.Label(root, text="Message:")
message_label.grid(row=1, column=0, sticky="w")
message_entry = tk.Entry(root)
message_entry.grid(row=1, column=1)


# Select Image Button
select_image_button = tk.Button(root, text="Select Image", command=get_image)
select_image_button.grid(row=3, column=0, columnspan=2, pady=10)

# Image Display
image_label = tk.Label(root)
image_label.grid(row=4, column=0, columnspan=2)

# Send to Label
send_label = tk.Label(root, text="Send to:")
send_label.grid(row=5, column=0, sticky="w")

# Checkboxes for platforms
discord_check = tk.Checkbutton(root, text="Discord", variable=discord_var)
discord_check.grid(row=6, column=1, sticky="w")
twitter_check = tk.Checkbutton(root, text="Twitter", variable=twitter_var)
twitter_check.grid(row=7, column=1, sticky="w")
facebook_check = tk.Checkbutton(root, text="Facebook", variable=facebook_var)
facebook_check.grid(row=8, column=1, sticky="w")

# Send Button
send_button = tk.Button(root, text="Send", command=send)
send_button.grid(row=9, column=0, columnspan=2, pady=10)

# Status Label
status_label = tk.Label(root, text="")
status_label.grid(row=10, column=0, columnspan=2)


root.mainloop()
