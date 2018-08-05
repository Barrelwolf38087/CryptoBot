import discord, asyncio, platform
from discord.ext.commands import Bot
from discord.ext import commands

TOKEN = "NDY0MTYyMDk3ODI4MzMxNTIx.DkiwIw.PWSRmOKmL07_8LmR1EjzvGlfguw"

#client = discord.Client()

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
