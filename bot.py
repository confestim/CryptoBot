
from config import *


from random import randint
import base64
import subprocess
import time
import discord
from discord.ext import commands


description = '''CryptoBot'''
bot = commands.Bot(command_prefix='c!', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(game=discord.Game(name="c!help"))


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


@bot.command()
async def caesar(text):
    """ encodes clear text to the caesar cipher """
    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
    I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    key = 3
    plaintext = str(plaintext)

    # encipher
    ciphertext = ""
    for c in plaintext.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
        else: ciphertext += c

        # decipher
        plaintext2 = ""
        for c in ciphertext.upper():
            if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
            else: plaintext2 += c

            await bot.say(plaintext)
            await bot.say(ciphertext)
            await bot.say(plaintext2)



bot.run(TOKEN)
