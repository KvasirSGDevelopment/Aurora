import sys
sys.path.append('/home/pi/KvasirDevelopment/Aurora/')
from src import Commands
import os
from discord.ext import commands
from config.auth import User

modulePath = os.getcwd() + "\modules"

bot = commands.Bot(command_prefix=commands.when_mentioned_or('§'), description='AuroraV2 DevBuild PreAlpha')
Commands.load_all_modules(modulePath, bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(User.Token)
