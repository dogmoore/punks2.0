# bot.py
import os
import yaml
import logging
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    bot = yaml.load(ymlfile, Loader=yaml.FullLoader)
    TOKEN = bot["token"]
    PREFIX = bot["prefix"]
    VERSION = bot["version"]

intents = discord.Intents.default()
intents.members = True
activity = discord.Activity(name='with Max\'s head', type=discord.ActivityType.playing)
client = Bot(command_prefix=PREFIX, help_command=None, activity=activity, intents=intents)


@client.event
async def on_ready():
    print(f'{client.user} v{VERSION} has connected to Discord!')
    print(f'(Pterodactyl Bot Online)')

dontLoad = []

if __name__ == '__main__':
    for i in os.listdir('Cogs'):
        if i.endswith('.py') and i not in dontLoad:
            try:
                client.load_extension(f'Cogs.{i[:-3]}')
                print(f'{i[:-3]} loaded.')

            except Exception as error:
                print(f'{i[:-3]} cannot be loaded. [{error}]')

client.run(TOKEN)
