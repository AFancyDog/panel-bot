import json
import threading
from tkinter import *
import discord
from discord.ext import commands
import asyncio

# Load the token from a JSON file
var = json.load(open("var.json"))
TOKEN = var["token"]

# Set up intents
intents = discord.Intents.default()
intents.messages = True  # Ensure the bot can send messages
bot = commands.Bot(command_prefix='PanelRequest>', intents=intents)

# Flag to check if the bot is ready
bot_ready = False

@bot.event
async def on_ready():
    global bot_ready
    bot_ready = True
    print(f'Logged in as {bot.user} and ready!')

async def send(sendload, channelinput):
    if not bot_ready:
        print("Bot is not ready yet!")
        return

    channel = bot.get_channel(channelinput)  # Get the channel by ID
    if channel:
        await channel.send(sendload)  # Send the message
    else:
        print("Channel not found!")




def rundiscordbot():
    bot.run(TOKEN)

def panel():
    root = Tk()
    root.geometry("375x125")
    root.title("PanelBot")
    root.config(bg="black")
    
    def SendTxt():
        try:
            channel_id = int(ChannelInput.get())
            print(f"Attempting to send to Channel ID: {channel_id}")
            asyncio.run_coroutine_threadsafe(send(TextInput.get(), channel_id), bot.loop)
        except ValueError:
            print("Please enter a valid integer ID for the channel.")

    MessageSender = Label(text="Sending Messages",fg="white",bg="black")
    MessageSender.grid(column=1,row=1)
    ChannelInput = Entry(bg="black", fg="white")
    ChannelInput.grid(column=1, row=2)
    ChannelLabel = Label(text="<-Put your channel ID here", fg="white", bg="black")
    ChannelLabel.grid(column=2, row=2)
    TextInput = Entry(bg="black", fg="white")
    TextInput.grid(column=1, row=3)
    TextSendBtn = Button(text="<- Send Message", fg="white", bg="black", command=SendTxt)
    TextSendBtn.grid(column=2, row=3)

    root.mainloop()

# Start the Discord bot in a separate thread
discord_thread = threading.Thread(target=rundiscordbot)
discord_thread.start()
panel()