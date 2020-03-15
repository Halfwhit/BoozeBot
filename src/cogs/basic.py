from discord.ext import commands

@commands.command()
async def add(bot, left: int, right: int):
    await bot.send(left + right)

def setup(bot):
    bot.add_command(add)
