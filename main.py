##########################################################
# 
  

# import discord

# client = discord.Client()
# @client.event
# async def on_ready():
#     print('Logged in as')
#     print(client.user.name) 
#     print(client.user.id)
#     print('------')


# @client.event
# async def on_message(message):
#     channel = message.channel
#     if message.content == '!Hello' or '!Hi':
#         await channel.send('Hello, friend!')

# client.run('DISCORD_KEY')

n = int(input())
i = 1

faktoren = []              
z = n                       

while z > 1:
  p = 2
  while p != 0:
    i += 1
    p = z % i
  faktoren.append(i)
  z = z // i

print(faktoren)