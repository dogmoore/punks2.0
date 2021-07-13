import discord
import yaml
import random
import asyncio
from discord.ext import commands

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.FullLoader)


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        client = self.client

        print(f'(Pterodactyl Bot Online)')
        print(f'Username: {client.user.name}')
        print(f'id: {client.user.id}')

    async def on_member_join(self, message):
        await message.channel.send('Welcome to this shitshow')

    async def on_message(self, message):
        client = self.client
#        try:
        if client.user.mentioned_in(message):
            await message.channel.send("Go fuck yourself, there is no need to `@` me")
        oneInMeme = random.randint(1, 69420)
        oneInTen = random.randint(1, 10)

        i = ''
        x = ''

        msg = {'who do you love punks2', 'who do you love punks2.0', 'who do you love punks',
               'who do you love punks 2.0'}
        msg2 = {'how are you doing punks', 'how are you doing punks2.0', 'how are you doing punks2',
                'how are you doing punks 2.0'}

        timer = 2

        # if client.user.mentioned_in(message):
        #     emote = '<a:pinged:807786291710132266>'
        #     emote2 = '<:sanic:807786621197746206>'
        #
        #     PingMsg = await message.channel.send('Why tf was I pinged!')
        #     await PingMsg.add_reaction(str(emote2))

        if message.author.id == 304399110256066571 and oneInMeme == 7:
            print('\'punks is a heathen\' triggered')
            async with message.channel.typing():
                await asyncio.sleep(1)
            await message.reply('DON\'T LISTEN TO THIS HEATHEN, I AM THE REAL PUNKS!', tts=True)
        elif message.content.lower() in msg:
            if oneInTen == 1:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('some gay fuck')
                i = 1
            elif oneInTen == 2:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('DOGMOORE!')
                i = 2
            elif oneInTen == 3:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('some weird chick who says she\'s a cat')
                i = 3
            elif oneInTen == 4:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('a ginger hehe')
                i = 4
            elif oneInTen == 5:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('APaperbot')
                i = 5
            elif oneInTen == 6:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('Brynn!...but she never responds to my texts....D:')
                i = 6
            elif oneInTen == 7:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('MARSHAL')
                i = 7
            elif oneInTen == 8:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('SYLVI!!!!!!')
                i = 8
            elif oneInTen == 9:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('idk, no one?')
                i = 9
            elif oneInTen == 10:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('The one true Queen, Freddie Mercury!')
                i = 10
            print(f'who does Punks 2.0 love issued and returned option: {i}')
        elif message.content.lower() in msg2:
            if oneInTen == 1:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('fucking dreadful')
                x = 1
            elif oneInTen == 2:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('I\'m doing alright')
                x = 2
            elif oneInTen == 3:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('real question is, how are you doing?')
                x = 3
            elif oneInTen == 4:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('sorta feel like using a forbidden bath bomb')
                x = 4
            elif oneInTen == 5:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('horny')
                x = 5
            elif oneInTen == 6:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('really horny')
                x = 6
            elif oneInTen == 7:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('eh, alive')
                x = 7
            elif oneInTen == 8:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 8
            elif oneInTen == 9:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('Like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 9
            elif oneInTen == 10:
                async with message.channel.typing():
                    await asyncio.sleep(timer)
                await message.channel.send('like I\'m trapped in someone\'s computer.....its cold here......*help*')
                x = 10
            print(f'How is Punks 2.0 feeling issued and returned option: {x}')


def setup(client):
    client.add_cog(Events(client))
