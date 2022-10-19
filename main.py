import asyncio
import discord

import src.cogs as cogs

from src.lib import json_methods
from discord.ext import commands

class main:
    def __init__(self):
        secret = json_methods.read_json(r"json/secret.json")

        self.token = secret["token"]
        self.log_channel = secret["log_channel"]
        self.alert_list = secret["alert_list"]



    def load_cogs(self):
        bot.load_extension("src.cogs.hello_world")

    def run(self):
        self.load_cogs()
        bot.run(self.token)

if __name__ == "__main__":
    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix='!', intents=intents)
    bot.remove_command('help')

    main = main()
    main.run()