import shutil
from os.path import join
import os
import time
import sys
import discord
import discord.ext
from discord.ext import commands
import subprocess
with open("config.txt", "r") as config:
   TOKEN = config.readline().strip('\n')



intents = discord.Intents.default()
intents.message_content = True
print("start")

client = commands.Bot(command_prefix='.', intents=intents)


profanityRep = 0
global banstorage
channels = [1308241606649974847]

banstorage = []
triggered = bool(False)


@client.event
async def on_ready():
    print('bot ready')


@client.event
async def on_message(message):
    channel = client.get_channel(message.channel.id)
    words = message.content.split(" ")
    for x in words:
      if 'kill' in x:
         connector = open("commands.txt", "a")
         connector.write("kill\n")
         connector.close()
      if 'tp' in x:
         connector = open("commands.txt", "a")
         connector.write("tp\n")
         connector.close()
      if 'stone' in x:
         connector = open("commands.txt", "a")
         connector.write("stone\n")
         connector.close()
      if 'tnt' in x:
         connector = open("commands.txt", "a")
         connector.write("tnt\n")
         connector.close()
      if 'kick' in x:
         connector = open("commands.txt", "a")
         connector.write("kick\n")
         connector.close()
      if 'keepinventory' in x:
         connector = open("commands.txt", "a")
         connector.write("keepinventory\n")
         connector.close()
      if 'water' in x:
         connector = open("commands.txt", "a")
         connector.write("water\n")
         connector.close()
      if 'hole' in x:
         connector = open("commands.txt", "a")
         connector.write("hole\n")
         connector.close()
      if 'fling' in x:
         connector = open("commands.txt", "a")
         connector.write("fling\n")
         connector.close()
      if 'tick' in x:
         connector = open("commands.txt", "a")
         connector.write("tick\n")
         connector.close()
      if 'world' in x:
         connector = open("commands.txt", "a")
         connector.write("world\n")
         connector.close()
client.run(TOKEN)
#server integration
#add a random command option
#heal instant


