import discord

from discord.ext import commands

class on_member_update(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        print(before.activities)
        print(after.activities)

def setup(bot):
    bot.add_cog(on_member_update(bot))