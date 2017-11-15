# coding=utf-8
from src import Commands
import os
from discord.ext import commands
from config.auth import User
import random

__author__ = "Luke"
__version__ = "0.0.1"

modulePath = os.path.join(os.getcwd(), "src", "modules")

bot = commands.Bot(command_prefix=commands.when_mentioned_or('§'), description='AuroraV2 DevBuild PreAlpha')

bot.remove_command('help')
Commands.load_all_modules(modulePath, bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(User.Token)
