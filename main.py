import discord
import config
from discord.ext import commands
import requests
import os

bot = commands.Bot(command_prefix='"\"')

@bot.event
async def on_ready():
  print(f'Бот {bot.user} готов к работе!')

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
  if f'<@{bot.user.id}>' in message.content:
    # Send a request to the specified URL
    async with message.channel.typing():
        ss = "{" + '"role"' + ": " '"user"' + ", "  + '"content"' + ': ' + '"' + message.content.replace(f'<@{bot.user.id}>', '').replace(' ', '', 1) + '"' + "}"
        url = f"https://tenon.sryden.com/api/v1/chat/completions?model=tenon7&messages=[{ss}]"
        response = requests.get(url)
        response_json = response.json()
        await message.reply(response_json['message'], file=discord.File('halex.png'))

bot.run(config.token)