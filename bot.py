import discord, json
from discord.ext import commands

TOKEN = 'process.env.BOT_TOKEN'
client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command()
async def mushimushi(ctx):
    await ctx.send('Konnichiwa!')


# @client.event
# async def on_ready():
#     print(f'Logged in as: {client.user.name}')
#     print(f'With ID: {client.user.id}')

# @bot.event
# async def on_guild_join(guild):
#     print(guild)

# client.run(TOKEN)
bot.run(TOKEN)