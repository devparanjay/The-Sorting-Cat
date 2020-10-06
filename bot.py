import discord, json, os
from discord.ext import commands

TOKEN = os.environ['BOT_TOKEN']
client = discord.Client()
message: discord.Message
user = discord.User
channel = discord.channel
bot = commands.Bot(command_prefix='#',)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name}')
    print(f'With ID: {bot.user.id}')

@bot.command(name="mushi", alias="konnichiwa")
async def mushimushi(msg):
    async with msg.typing():
        author = msg.author
        await msg.send(author.mention + ' Konnichiwa!')
        




# @client.event
# async def on_ready():
#     print(f'Logged in as: {client.user.name}')
#     print(f'With ID: {client.user.id}')

# @bot.event
# async def on_guild_join(guild):
#     print(guild)

# client.run(TOKEN)
bot.run(TOKEN)