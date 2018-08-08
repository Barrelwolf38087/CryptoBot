import discord

# Make sure we're using the correct version of Discord.py
if discord.__author__ != "Rapptz":
    print("Error: Please use the rewrite version of Discord.py.")
    print("Check the README for instructions.")
    exit()

import requests, asyncio, platform
from discord.ext.commands import Bot
# End imports


bot = Bot(command_prefix='!', case_insensitive=True, pm_help=True, description='A bot for comparing cryptocurrency values.')

coin_data = requests.get("https://www.cryptocompare.com/api/data/coinlist/").json()['Data']

# User typing is checked against this list of valid tickers
coin_list = coin_data.keys()

# USD is accepted by the API, but is not in the coin list;
# we can add it without any problems
coin_list.append('USD')

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
    "image": "\nExample: Getting the Bitcoin logo: `!image BTC`"
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
        await ctx.send(cmd + ": Command not found.")

# TODO: Clean this up at some point, it's a mess.
@bot.command()
async def price(ctx, to_sym, from_sym):
    if to_sym in coin_list and from_sym in coin_list:
        res = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms="+from_sym+"&tsyms="+to_sym)
        await ctx.send("Price of 1 " + from_sym + ": " + str(res.json()[from_sym][to_sym]) + " " + to_sym)
        await ctx.send("Data from <https://www.cryptocompare.com>")
    else:
        if to_sym not in coin_list:
            await ctx.send("Error: " + to_sym + " is not a valid ticker. Please check your typing.")
        if from_sym not in coin_list:
            await ctx.send("Error: " + from_sym + " is not a valid ticker. Please check your typing.")
        await ctx.send("Please note that USD is the only non-cryptocurrency accepted.")

@bot.command()
async def image(ctx, coin):

    # Make sure an actual coin was passed (not USD)
    if coin in coin_list and coin is not "USD":
        await ctx.send("https://www.cryptocompare.com" + coin_data[coin]["ImageUrl"])
    else:
        await ctx.send("Error: " + coin + " is not a valid ticker. Please check your typing.")

# End commands / events

bot.run(TOKEN)
