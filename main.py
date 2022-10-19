import asyncio
import discord

import src.cogs as cogs

from discord.ext import commands

class main:
    def __init__(self):
        pass

    def load_cogs(self):
        bot.load_extension("cogs.hello_world")

    def run(self):
        self.load_cogs()
        bot.run(self.token)

if __name__ == "__main__":
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.remove_command('help')

    main = main()
    main.run()