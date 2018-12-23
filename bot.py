
from config import *


from random import randint
import base64
import subprocess
import time
import discord
from discord.ext import commands


description = '''CryptoBot'''
bot = commands.Bot(command_prefix='c!', description=description)

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name="c!help"))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    bot.loop.create_task(status_task())


@bot.command()
async def encode_b64(s):
    s = str(s)
    bot.say(base64.b64encode(b'{}'.format(s)))


@bot.command()
async def decode_binary(s):
    """ Decode Binary Code """
    await bot.say(''.join(chr(int(s[i*8:i*8+8],2)) for i in range(len(s)//8)))

@bot.command()
async def encode_binary(st):
   """ Encode Text to Binary Code """
   st = str(st)
   await bot.say(' '.join(format(ord(x), 'b') for x in st))


bot.run(TOKEN)
