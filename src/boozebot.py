#!/usr/bin/python3
# boozebot.py
from discord.ext import commands

import os
from os import listdir
from os.path import isfile, join
from dotenv import load_dotenv

# Load api token using dotenv. 
# Secret token taken from developer portal, stored in .env file.
load_dotenv()
api_token = os.getenv("TOKEN")

cogs_dir = "cogs"
bot = commands.Bot(command_prefix='!')

# This is called after the bot has logged in.
# Prints to the terminal, not the server.
@bot.event
async def on_ready():
    print('Connected as:')
    print(bot.user.name)
    print(bot.user.id)

# Bot command to load a cog on the fly. Add error checking.
@bot.command()
async def load(extension_name : str):
    bot.load_extension(extension_name)
    await bot.say("{} loaded.".format(extension_name))

# Bot command to unload a cog on the fly. Add error checking.
@bot.command()
async def unload(extension_name : str):
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))

# This code block is basically the main entry point of the program
for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
    try:
        bot.load_extension(cogs_dir + '.' + extension)
        print(f'Loaded extension: {extension}')
    except Exception as e:
        print(f'Failed to load extension {extension}.')
    # Start the bot and start listening for events
    bot.run(api_token)

# Move to a cog, change to bot api
#    @client.event
#    async def on_message(message):
#        if message.author == client.user:
#            return
#
#        if message.content == 'F':
#            await message.channel.send("F")
#
#        if 'RIP' in message.content:
#            await message.add_reaction("\U0001F1EB")
#
#        if message.content == '!ping':
#            await message.channel.send("pong!")
#
#        if message.content.startswith('!hello'):
#            await message.channel.send('Hello {0.author.mention}'.format(message))