import discord
import requests
import json
from datetime import date

today = date.today()
todays_date = today.strftime("%B %d, %Y")
client = discord.Client()
bad_words = ['fuck','shit','bitch','asshole','whore']

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('logged in as {0.user}'
  .format(client))

@client.event
async def on_message(message):
  msg = message.content
  sendername = message.author
  msg.lower()
  if message.author == client.user:
    return
  if msg.startswith('$hello'):
    await message.channel.send(f'Hey there {sendername}')
  elif msg.startswith('$quote'):
    quote = get_quote();
    await message.channel.send(quote)
  elif any(word in msg for word in bad_words):
    await message.delete()
    await message.channel.send(f'Watch your language {sendername}')
  elif msg.startswith('$date'):
    await message.channel.send(f'Today is {todays_date}')
  elif msg.startswith('$src-Code'):
    await message.channel.send("Here is a link to my code on github: ")

client.run('TOKEN')
