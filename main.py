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
        response = 'Tommy correctly predicted Alex Trebek would be the first under 90 pick to pass and has won 1 beer from all the bois.'
    elif category == 'u40':
        response = helpers.pretty_print(constants.picks['under40'])
    elif category == 'pick3':
        response = helpers.pretty_print(constants.picks['pick3'])
    await ctx.send(response)


@bot.command(name="contribute", brief="Link to GitHub repo. Now accepting PRs")
async def on_contribute(ctx):
    helpers.command_logger(ctx.author, 'CONTRIBUTE')
    embed = discord.Embed(title="GitHub Repository", description="Now accepting PRs!",
                          url="https://github.com/chabermehl/DeathPoolBot")
    await ctx.send("https://github.com/chabermehl/DeathPoolBot", embed=embed)

bot.run(TOKEN)
