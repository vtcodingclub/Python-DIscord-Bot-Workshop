import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    print('Test')
    await client.change_presence(activity=discord.Game(name=""))

@client.listen('on_message')
async def on_message(message):
  if message.content.startswith("Marco"):
    await message.channel.send("Polo")
  if message.content.startswith('Hello!'):
    await message.channel.send(u"\U0001F60D")
  if message.content.startswith("DM"):
    await message.author.send("Here is a DM!")

@client.command()
async def hello(ctx):
    await ctx.send("Hello World!")

@client.command()
async def role(ctx):
     role_name = "TESTONE"
     role = discord.utils.get(ctx.guild.roles, name=role_name)
     if role is not None:
         await ctx.author.add_roles(role)
         await ctx.send("You have been given a role!")

@client.command()
async def embed(ctx):
    my_embed = discord.Embed(
        title = "Hello World",
        description = "This is a description."
    )
    await ctx.send(embed=my_embed)

@client.command()
async def pic(ctx):
  await ctx.send(file=discord.File(''))

@client.command()
async def say(ctx, arg=""):
    await ctx.send(f"{arg}")

@client.command()
async def count(ctx, *args):
    await ctx.send(f"{len(args)}")

client.run('OTU4NDUzMDAwOTQxMjM2Mjc1.YkNi6g.2dxhEN2_CD6xLqbDQLHh0lxaWes')