import discord
from bot_logic import gen_pass
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

client = discord.Client(intents=intents)
print(gen_pass(10))
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

bot.run("MTI3ODUwODAxNzkyNjY2ODQzMw.GmBl3o.EccsOGRuLi_ZbO_64CBXlf-phaWzkXn2QvQ9XI")
client.run("MTI3ODUwODAxNzkyNjY2ODQzMw.GmBl3o.EccsOGRuLi_ZbO_64CBXlf-phaWzkXn2QvQ9XI")