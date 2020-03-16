import discord
from discord.ext import commands


class Boozers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.display_name}')

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author == self.bot.user:  # Abort if the message was ours
            return

        if message.content == 'F':
            await message.channel.send("F")

        if 'RIP' in message.content:
            await message.add_reaction("\U0001F1EB")


def setup(bot):
    bot.add_cog(Boozers(bot))
