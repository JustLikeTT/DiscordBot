import time

from package.controllor import get_string

import asyncio
import discord
from discord.ext.commands import Bot
from discord.ext import commands

Client = discord.Client()
bot = Bot(command_prefix="#")

@bot.event
async def on_ready():
    print("Hello")

@bot.event
async def on_message(message):
    if message.content.startswith("#fine"):
        await bot.send_message(message.channel, get_string())

if __name__ == '__main__':

    token = "NDk4NTA5MzQ1ODM1OTc0Njk2.DpvJkA.utbqXg2c0X7IWAvPm1JgYer99hg"
    bot.run(token)