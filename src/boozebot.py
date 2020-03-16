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

    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + '.' + extension)
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'Failed to load extension {extension}.')


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


bot.run(api_token)

