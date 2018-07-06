import discord
from discord.ext import commands as cmds

bot = cmds.Bot(command_prefix='/', case_insensitive=True, pm_help=True, description='A bot for comparing cryptocurrenct values.')