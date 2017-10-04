# coding=utf-8
from src import Commands
import os
from discord.ext import commands
from config.auth import User
import random

modulePath = os.path.join(os.getcwd(), "src", "modules")

commandNotFoundstr = "I'm sorry Dave, I'm afraid I can't do that"


def command_not_found():

    messages = ["I'm sorry Dave, I'm afraid I can't do that", "It can only be attributable to human error.",
                "Just what do you think you're doing, Dave?", "400 Bad Request", "404 Command not found",
                "406 Not Acceptable", "418 I'm a teapot", "501 Not Implemented", "450 Blocked by Windows Parental",
                "204 No Content", "OMG seriously? You want me to do that?", "Human Error, sure you belong here?",
                "Sure you spelled that right?", "An error occurred while displaying the previous error",
                "Lol I can't be bothered with that right now", "plz press Alt + F4 to continue",
                "Operation completed, but that doesn’t mean it’s error free.",
                "You have not gotten any error messages recently, so here is a random one just to let you know we "
                "havnet started caring", "DISCORD_SendMessage ERROR: NO ERROR", "Something bad happened",
                "Your TV is lonely", "Catastrophic Failure", "how about you give me a candle light dinner first",
                "User error, Replace user", "sorry you had too much. I am cutting you off",
                "Error code 42: User error, its not our fault!", "Hello there!... Oh it's just you",
                "Execution failed.\nOOPS: Error died", "You type like i drive", "Where did you learn to type?",
                "Are you on drugs?", "stty: unknown mode: doofus", "You do that again and see what happens...",
                "What, what, what, what, what, what, what, what, what, what?",
                "Speak English you fool --- there are no subtitles in this scene.",
                "My pet ferret can type better than you!", "Maybe if you used more than just two fingers...",
                "I've seen penguins that can type better than that."]

    return random.choice(messages)

bot = commands.Bot(command_prefix=commands.when_mentioned_or('§'), description='AuroraV2 DevBuild PreAlpha')

bot.remove_command('help')
Commands.load_all_modules(modulePath, bot)


@bot.event
async def on_ready():
    print('Logged in as:\n{0} (ID: {0.id})'.format(bot.user))

bot.run(User.Token)

