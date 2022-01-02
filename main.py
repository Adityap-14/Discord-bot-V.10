import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from discord.ext import commands


client = discord.Client()
client = commands.Bot(command_prefix="$")

@client.event  # Message when Bot joins a server
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! This is a bot that was created by aditza#5091 to see what I can do, use $Info.')
        break




def get_joke(): # Joke api for jokes 
  response = requests.get(
    'https://v2.jokeapi.dev/joke/Any?blacklistFlags=racist,sexist',
    params={ 
        'action': 'query', 
        'format': 'json', 
        "type": "single",
        
    }).json()
  return(response['joke'])

def get_Iss(): # 
  response = requests.get(
    'http://api.open-notify.org/iss-now.json',
    params={ 
      
        'format': 'json', 
        
        
    }).json()
  return(response['iss_position'])
  




@client.event  # Confirms Bot is connected in the console
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$joke'):  
    joke = get_joke()
    await message.channel.send(joke)

  if msg.startswith('$whereisISS'): 
    Iss = get_Iss()
    await message.channel.send(Iss)  

  
  if msg.startswith('$Info'): #title card to display bot funfunctions 
    embedVar = discord.Embed(title="Aditz Bot", description="Commands for Aditz Bot", color=0x00ff00)
    embedVar.add_field(name="$joke", value="sends you a joke", inline=False)
    embedVar.add_field(name="$whereisISS", value="shows you the latitiude and longitude of the ISS", inline=False)
    embedVar.add_field(name="$ttt", value="shows you the commands for tic tac toe", inline=False)
    embedVar.add_field(name="$imusic", value="shows you the commands for music", inline=False)
    await message.channel.send(embed=embedVar)

  if msg.startswith('$ttt'): #tictactoe functions
    embedVar = discord.Embed(title="Aditz Bot", description="Commands for Aditz Bot Tic Tac Toe", color=0x00ff00)
    embedVar.add_field(name="$tictactoe @user1 @user2", value=" Starts a game of Tic Tac Toe", inline=False)
    embedVar.add_field(name="$place(integer 1-9) ", value=" Starts a game of Tic Tac Toe", inline=False)
    embedVar.add_field(name="$end", value="Ends current game of tic tac toe", inline=False)
    await message.channel.send(embed=embedVar)
    await message.channel.send('https://www.youtube.com/watch?v=46pra8NwhzU')


  if msg.startswith('$imusic'): #displays music functions
    embedVar = discord.Embed(title="Aditz Bot", description="Commands for Aditz Bot Music", color=0x00ff00)
    embedVar.add_field(name="Music Commands that are pretty self explainatory", value="leave, loop, nowplaying, pause, play, playlist,queue, remove, resume, search, shuffle, skip, stop, volume ", inline=False)
    await message.channel.send(embed=embedVar)
    
# Purge Command
@client.command()
async def clear (ctx, amount=5):
  await ctx.channel.purge(limit=amount)
    

keep_alive() #This keeps the bot running 24/7
client.run(os.getenv('TOKEN'))
