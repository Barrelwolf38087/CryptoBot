import discord, requests, asyncio, platform
from discord.ext.commands import Bot

coin_list = list(requests.get("https://www.cryptocompare.com/api/data/coinlist/").json()['Data'].keys())
coin_list.append('USD')

# Place your token in a file called "token.txt"
token_file = open("token.txt", "r")
TOKEN = token_file.read()

bot = Bot(command_prefix='!', case_insensitive=True, pm_help=True, description='A bot for comparing cryptocurrency values.')
bot.remove_command("help")

@bot.event
async def on_ready():
    print(
        "Logged in\n"
        + str(bot.user.name) + "\n"
        + str(bot.user.id)
    )

@bot.command()
async def help(ctx):
    await ctx.send(
        "\nExample: Getting the price of a Bitcoin in USD:\n" +
        "`  !price USD BTC`"
    )

@bot.command()
async def price(ctx, to_sym, from_sym):
    if to_sym in coin_list and from_sym in coin_list:
        res = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms="+from_sym+"&tsyms="+to_sym)
        await ctx.send("Price of 1 " + from_sym + ": " + str(res.json()[from_sym][to_sym]) + " " + to_sym)
        await ctx.send("Data from <https://www.cryptocompare.com>")
    else:
        if to_sym not in coin_list:
            await ctx.send("Error: " + to_sym + " not a valid symbol. Please check your typing.")
        if from_sym not in coin_list:
            await ctx.send("Error: " + from_sym + " not a valid symbol. Please check your typing.")
        await ctx.send("Please note that USD is the only non-cryptocurrency accepted.")


bot.run(TOKEN)
