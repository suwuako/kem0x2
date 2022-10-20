import discord

from discord.ext import commands


class hello_world(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ping", "hello"])
    async def hello_world(self, message):
        await message.send("Hello world!")


def setup(bot):
    bot.add_cog(hello_world(bot))