import discord, asyncio, platform
from discord.ext.commands import Bot
from discord.ext import commands

# Place your token in a file called "token.txt"
token_file = open("token.txt", "r")
TOKEN = token_file.read()

bot = Bot(command_prefix='!', case_insensitive=True, pm_help=True, description='A bot for comparing cryptocurrenct values.')

@bot.event
async def on_ready():
    print(
        "Logged in\n"
        + str(bot.user.name) + "\n"
        + str(bot.user.id)
    )

@bot.command()
async def get(ctx):
    await ctx.send("Nothing to see here yet!")

bot.run(TOKEN)
