import yaml
import discord
import time
import asyncio
import datetime
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)
    VERSION = config["version"]
    PREFIX = config["prefix"]


class Utils(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, context):
        start = time.monotonic()
        message = await context.send('Pinging...')
        pingValue = (time.monotonic() - start) * 1000
        pingMsg = f'Latency: {int(pingValue)}ms'
        await message.edit(content=pingMsg)
        print(f'Ping command issued by {context.author.username}, Latency is {int(pingValue)}ms')

    @commands.command(name='shutdown')
    async def shutdown(self, context):
        client = self.client
        if context.author.id == 376857933067321366:
            async with context.typing():
                await asyncio.sleep(1)
            await context.send('Ok, time for bed')
            print(f'{client.user} is shutting down...')
            await client.close()
        else:
            msg = 'You silly goose, that command is bot admin only!'
            error = await context.send('Permission error')
            await asyncio.sleep(4)
            await error.edit(content=msg)

    @commands.command(name='say')
    async def say(self, context, *, args):
        if context.author.id == 376857933067321366:
            argsLength = len(args)
            await asyncio.sleep(0.05)
            await context.message.delete()
            if 0 < argsLength < 10:
                timer = 1
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued by {context.author.username}, jelly-3.0 said: "{args}" with a typing timer of: {timer} seconds')
            elif 10 < argsLength < 20:
                timer = 3
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued by {context.author.username}, jelly-3.0 said: "{args}" with a typing timer of: {timer} seconds')
            elif 20 < argsLength < 40:
                timer = 5
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued by {context.author.username}, jelly-3.0 said: "{args}" with a typing timer of: {timer} seconds')
            elif 40 < argsLength:
                timer = 8
                async with context.typing():
                    await asyncio.sleep(timer)
                await context.send(args)
                print(f'say command issued by {context.author.username}, jelly-3.0 said: "{args}" with a typing timer of: {timer} seconds')
        else:
            await context.message.delete()
            error = await context.send('Permission Error')
            await asyncio.sleep(4)
            await error.delete()

    @commands.command(name='version')
    async def version(self, context):
        await context.send(f'Current version is: v{VERSION}')

    @commands.group(name='help')
    async def help(self, context):
        if context.invoked_subcommand is None:
            x = ''
            helpEmbed = discord.Embed(
                title='Punks 2.0 Help',
                timestamp=datetime.datetime.utcnow(),
                color=discord.Color.gold()
            )
            helpEmbed.add_field(name=f'{PREFIX}ping', value='Pings the bot', inline=False)
            helpEmbed.add_field(name=f'{PREFIX}version', value='Says the current version of the bot', inline=False)
            if context.author.id == 376857933067321366:
                helpEmbed.add_field(name=f'{PREFIX}say', value='Make the bot say something', inline=False)
                helpEmbed.add_field(name=f'{PREFIX}shutdown', value='Shuts down the bot', inline=False)
                x = 'admin '
            await context.send(embed=helpEmbed)
            print(f'command {x}help was issued by {context.author.username}')

    @help.command()
    async def dm(self, context):
        await asyncio.sleep(0.05)
        await context.message.delete()
        x = ''
        helpEmbed = discord.Embed(
            title='Punks 2.0 Help',
            timestamp=datetime.datetime.utcnow(),
            color=discord.Color.gold()
        )
        helpEmbed.add_field(name=f'{PREFIX}ping', value='Pings the bot', inline=False)
        helpEmbed.add_field(name=f'{PREFIX}version', value='Says the current version of the bot', inline=False)
        if context.author.id == 278548721778688010 or context.author.id == 376857933067321366:
            helpEmbed.add_field(name=f'{PREFIX}say', value='Make the bot say something', inline=False)
            helpEmbed.add_field(name=f'{PREFIX}shutdown', value='Shuts down the bot', inline=False)
            x = 'admin '
        await context.author.send(embed=helpEmbed)
        print(f'Command {x}help was issued in DM by {context.author.username}')


def setup(client):
    client.add_cog(Utils(client))
