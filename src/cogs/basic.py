from discord.ext import commands


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, left: int, right: int):
        await ctx.send(left + right)


def setup(bot):
    bot.add_cog(Basic(bot))
