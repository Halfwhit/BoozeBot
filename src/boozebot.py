#!/usr/bin/python3
# boozebot.py
import discord

# Token taken from developer portal. Should move this to another file.
api_token = "NDk3NDMxMzkyNzg4MTUyMzUw.XmU2TA.gVf7WBjiXMCSIzZH5cUNp8cKz7U"

# Setup the client (A client is a low level bot, so basically initialise the bot)
client = discord.Client()

# Event callbacks the bot will use
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'F':
        await message.channel.send("F")

    if 'RIP' in message.content:
        await message.add_reaction("\U0001F1EB")

    if message.content == '!ping':
        await message.channel.send("pong!")

    if message.content.startswith('!hello'):
        await message.channel.send('Hello {0.author.mention}'.format(message))

# Start the bot and start listening for events
client.run(api_token)
