import discord
token = 'MTE3OTAzMTIwNzcxMTg3NTEzNA.G9fFaK.AcFEP8IuYrmYYNtLYggcfAqFqm1_HzcY00RoJU'
channel_id = 1140897051970904189
image_path = "D:\discord test\Screenshot 2023-10-28 223408.png"
def send_image_sync(channel_id, image_path, token):
    intents = discord.Intents.default()
    
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"We have logged in as {client.user}")

        channel = client.get_channel(channel_id)
        if channel:
            try:
                with open(image_path, 'rb') as file:
                    image = discord.File(file)
                    await channel.send(file=image)
            except FileNotFoundError:
                print("File not found!")
            except discord.HTTPException:
                print("Failed to send the image")

        await client.close()

    client.run(token)

send_image_sync(channel_id, image_path, token)
