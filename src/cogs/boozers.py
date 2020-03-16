from discord.ext import commands


class Boozers(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("pong!")

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member):
        await ctx.send(f'Hello {member.display_name}')

    @commands.Cog.listener()
    async def on_message(self, ctx, message):

        if message.author == self.user:  # Abort if the message was ours
            return

        if message.content == 'F':
            await message.channel.send("F")

        if 'RIP' in message.content:
            await message.add_reaction("\U0001F1EB")


def setup(bot):
    bot.add_cog(Boozers(bot))
