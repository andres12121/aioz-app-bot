import discord
import json
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import datetime


#----------------------------------
client = commands.Bot(command_prefix='a!') #prefix
token = 'ODM5Njg1OTMwMTY3NDM1MjY1.YJNQdg.czrb4oUeJzh78LTw7EGDk4A5ryk' #Token
client.remove_command('help')

#----------------------------------

@client.command()
async def help(ctx):
    embed1=discord.Embed(title=f"**Comandos de Aioz | 1.0**", description="**⚡|Principales**\n`help` `purge`\n\n**🎮|Free Fire**\n `mapa1` `mapa2`\n", color=0xFEFEFF)
    embed1.timestamp = datetime.datetime.utcnow()
    embed1.set_footer(text='\u200b #Azkeel', icon_url="""https://emoji.gg/assets/emoji/9643-skeleton-vibe.gif""",)
    await ctx.send(embed=embed1)

@client.command()
async def mapa1(ctx):
    embed2=discord.Embed(title=f"**Mapa Bermuda**", color=0xFEFEFF)
    embed2.timestamp = datetime.datetime.utcnow()
    embed2.set_image(url="https://gamingonphone.com/wp-content/uploads/2020/09/bermuda-map_compress35-768x764.jpg")
    embed2.set_footer(text='\u200b #Azkeel', icon_url="""https://emoji.gg/assets/emoji/9643-skeleton-vibe.gif""")
    await ctx.send(embed=embed2)

@client.command()
async def mapa2(ctx):
    embed4=discord.Embed(title=f"", description="**Mapa Purgatorio**", 
    color=0xFEFEFF)
    embed4.set_image(url="https://ligadecracks.com/wp-content/uploads/2020/07/Mapa-purgatorio.jpg")
    embed4.timestamp = datetime.datetime.utcnow()
    embed4.set_footer(text='\u200b #Azkeel', icon_url="""https://emoji.gg/assets/emoji/9643-skeleton-vibe.gif""")
    await ctx.send(embed=embed4)

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, limit: int):
    await ctx.message.delete()
    await asyncio.sleep(1)
    await ctx.channel.purge(limit=limit)
    purge_embed = discord.Embed(title='Purge [!purge]', description=f'Successfully purged {limit} messages. \n Command executed by {ctx.author}.', color=discord.Colour.random())
    purge_embed.set_footer(text='\u200b', icon_url="https://emoji.gg/assets/emoji/9643-skeleton-vibe.gif")
    await ctx.channel.send(embed=purge_embed, delete_after=True)

@client.command()
async def presentacion(ctx):
    embed3=discord.Embed(title=f"Presentacion del Aioz | v1.0", description="Me presento soy el nuevo bot de este servidor.\nPara saber mis comandos usa a!help\nHasta pronto...\n\n-------\nAtt: **Azkeel.**\nPings: @everyone\n-------", color=0xFEFEFF)
    embed3.timestamp = datetime.datetime.utcnow()
    embed3.set_footer(text='\u200b Azkeel', icon_url="""https://emoji.gg/assets/emoji/9643-skeleton-vibe.gif""")
    await ctx.send(embed=embed3)


#----------------------------------
@client.event
async def on_ready():
    activity = discord.Game(name="#Aioz| v 1.0", type=3)
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print('Hello, I am now running')

#----------------------------------
    
    
    
client.run(token)