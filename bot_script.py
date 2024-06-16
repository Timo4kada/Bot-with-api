from config import TOKEN
from discord import Intents
from discord.ext import commands
from PIL import Image
import requests
from api_script import *
import discord
import time


bot = commands.Bot(command_prefix="!", intents=Intents.all())


@bot.event
async def on_message(message):
    msc = message.content
    user = message.author
    create(msc)
    f = Image.open('image.jpg')
    d = discord.File(f)
    await message.channel.send(file=d, delete_after=60.0)


    
        


bot.run(TOKEN)