import discord 
from discord.ext import commands 
import colorama 
from colorama import Fore
token = "TOKEN" 
prefix = "_"
bot = commands.Bot(commands_prefix=prefix) 

@client.event
async def on_connect():
await bot.change_presence(status=discord.Status.online, activity = discord.Game(f'{prefix}help ║ watching {len(client.guilds)} servers'))

@client.event
async def on_ready():
print(f"Successfully Connected to {client.user}
I am in {len(client.guilds)} Servers")

@client.command()
async def ping(self, ctx):

    embed = discord.Embed(title='Pong <a:ping:920222208306073643>',

                          color=discord.Colour(0x2f3145),

                          description=f'**`{int(self.client.latency * 1000)}`**')

    embed.set_thumbnail(

        url='https://cdn.discordapp.com/emojis/885681753593872455.gif?size=2048'

    )

    await ctx.reply(embed=embed
