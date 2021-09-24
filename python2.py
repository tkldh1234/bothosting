import discord
import asyncio
import random
import time

client = discord.Client()

token = "NzA5MDAxMTcyMDAxNzUxMDgw.XrfizA.lThEwl8quiEyMbTUWKp1zabePjc"

@client.event

async def on_ready():
    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('봇켜짐 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ루삥뽕')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith(':start'):
        value1 = message.content.split(" ")
        mention = value1[1]
        await message.channel.send(f"<@{mention}>")
        await message.channel.send(f"<@{mention}>")
        await message.channel.send(f"<@{mention}>")
        await message.channel.send(f"<@{mention}>")
        await message.channel.send(f"<@{mention}>")
                    
client.run(token)

