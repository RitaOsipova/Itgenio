##########################################################
# OTI0MzIxMjM5NTkyNDk3MTky.Ycc3PA.PINH6ibbq-yapReklTrF4bhFEo8
  

import discord

client = discord.Client()
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name) 
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    channel = message.channel
    if message.content == '!Hello':
        await channel.send('Hello, friend!')

client.run('OTI0MzIxMjM5NTkyNDk3MTky.Ycc3PA.PINH6ibbq-yapReklTrF4bhFEo8')