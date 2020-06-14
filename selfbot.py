import os
from os import system, name
import discord
from discord.role import Role
from discord.utils import get
from discord.voice_client import VoiceClient
from discord.ext import commands

token = os.environ["TOKEN"]

client = commands.Bot(command_prefix='!', self_bot=True)

def cls():
	if name == "nt":
		_ = system("cls")
	else:
		_ = system("clear")

spam = True

cls()

@client.event
async def on_ready():
    print('Logged in as: ', client.user)
    activity = discord.Game(name="( ͡° ͜ʖ ͡°)")
    await client.change_presence(status=discord.Status.online, activity=activity)

@client.command()
async def spam(ctx, arg):
    spam = True
    print("Spamming ", arg)
    while spam:
    	await ctx.send(arg)
	
client.run(token, bot=False)
