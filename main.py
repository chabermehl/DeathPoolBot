import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

import constants
import helpers

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.command(name="standings", brief="Shows current standings", description=constants.description)
async def on_message(ctx, category: str):
    helpers.command_logger(ctx.author, f'STANDINGS {category}')
    if category == 'u90':
        response = helpers.pretty_print(constants.picks['under90'])
    elif category == 'u40':
        response = helpers.pretty_print(constants.picks['under40'])
    elif category == 'pick3':
        response = helpers.pretty_print(constants.picks['pick3'])
    await ctx.send(response)

bot.run(TOKEN)