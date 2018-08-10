import discord

# Make sure we're using the correct version of Discord.py
if discord.__author__ != "Rapptz":
    print("Error: Please use the rewrite version of Discord.py.")
    print("Check the README for instructions.")
    exit()

import requests, asyncio, platform
from discord.ext.commands import Bot
# End imports


bot = Bot(command_prefix='!', case_insensitive=True, description='A bot for comparing cryptocurrency values.')

coin_data = requests.get("https://www.cryptocompare.com/api/data/coinlist/").json()['Data']

# User typing is checked against this list of valid symbols
coin_list = list(coin_data.keys())
invalid_coin = "Error: {} is not a valid symbol. Please check your typing."

# Place the token in a file called "token.txt"
# IMPORTANT: Make sure there is no newline at the end!
# You will get cryptic errors.
# Try "tr -d '\n' < token.txt" (*NIX only)
TOKEN = open("token.txt", "r").read()

# So we can have our neat little custom help function
bot.remove_command("help")

# Help strings; sent when a user types "!help {command_here}"
help_strings = {
    "price": "\nExample: Getting the price of a Bitcoin in USD:\n`  !price USD BTC`",
    "image": "\nExample: Getting the Bitcoin logo:\n`   !image BTC`",
    "name":  "\nExample: Finding out what \"ETC\" means:\n`    !name ETC`",
    "algo":  "\nExample: "
}

# Commands / events below

@bot.event
async def on_ready():
    print(
        "Logged in\n"
        + str(bot.user.name) + "\n"
        + str(bot.user.id)
    )

# NOTE: The whole point of the help strings is so that this command is
#       short and readable. Do not change.
@bot.command()
async def help(ctx, cmd=None):

    # Print a list of commands if one is not supplied
    if cmd is None:
        await ctx.send("List of commands:\n")
        for i in help_strings.keys():
            await ctx.send("`!" + i + "`")

    # Make sure the command typed actually exists
    if cmd in help_strings.keys():
        await ctx.send(help_strings[cmd])
    else:
        # Get rid of annoying errors when no command is passed
        if cmd is not None:
            await ctx.send(cmd + ": Command not found")

# TODO: Clean this up at some point, it's a mess.
@bot.command()
async def price(ctx, to_sym, from_sym):
    if to_sym in coin_list or to_sym is "USD" and from_sym in coin_list or from_sym is "USD":
        res = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms="+from_sym+"&tsyms="+to_sym)
        await ctx.send("Price of 1 " + from_sym + ": " + str(res.json()[from_sym][to_sym]) + " " + to_sym)
        await ctx.send("Data from <https://www.cryptocompare.com>")
    else:
        if to_sym not in coin_list:
            await ctx.send("Error: " + to_sym + " is not a valid symbol. Please check your typing.")
        if from_sym not in coin_list:
            await ctx.send("Error: " + from_sym + " is not a valid symbol. Please check your typing.")
        await ctx.send("Please note that USD is the only non-cryptocurrency accepted.")

@bot.command()
async def image(ctx, coin):
    if coin in coin_list:
        await ctx.send("https://www.cryptocompare.com" + coin_data[coin]["ImageUrl"])
    else:
        await ctx.send(invalid_coin.format(coin))

@bot.command()
async def name(ctx, coin):
    if coin in coin_list:
        await ctx.send(coin_data[coin]["FullName"])
    else:
        await ctx.send(invalid_coin.format(coin))

@bot.command()
async def algo(ctx, coin):
    if coin in coin_list:
        await ctx.send(coin_data[coin]["Algorithm"])
    else:
        await ctx.send(invalid_coin.format(coin))

@bot.command()
async def dedede(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/477252163899228160/477273917795467284/image.jpg")

# End commands / events

bot.run(TOKEN)
