import discord
from discord.ext import commands, tasks
import random
import music
from random import choice
from keep_alive import keep_alive
from reddit import reddit
import requests
import json


def AiResponse(message, apikey):
    url = "https://random-stuff-api.p.rapidapi.com/ai"
    querystring = {"msg":message,"bot_name":"monkebot","bot_gender":"genderless","bot_master":"Pratyaksh","bot_age":"0","bot_location":"India","bot_build":"Public","bot_birth_year":"2022 ","bot_birth_date":"29 January, 2022 ","bot_birth_place":"India","bot_favorite_color":"Black","bot_favorite_book":"Kafka on the shore","bot_favorite_band":"Radiohead","bot_favorite_artist":"Kanye West","bot_favorite_actress":"Isabelle Huppert","bot_favorite_actor":"Robert De Niro","id":"For customised response for each user"}
    headers = {'authorization': 'm1MPzlzvGeqV','x-rapidapi-host': "random-stuff-api.p.rapidapi.com",'x-rapidapi-key': "d958b17d86mshbd4f046a540c7a4p1b3850jsna601db35108d"}
    response = requests.request("GET", url, headers=headers, params=querystring)
    return json.loads(response.text)["AIResponse"]
    

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())


@client.command()
async def ai(ctx, *, msg):
    Response = AiResponse(msg, "m1MPzlzvGeqV")
    embed = discord.Embed(title=Response)
    await ctx.send(embed=embed)
    print(Response)



vcbot=[music]

status = ['vibin', 'funee monke gif', 'eating banana','loving monke','Ai Chatbot']



@client.event
async def on_ready():
  print("ready")



@client.command()
async def cute(ctx,subred="aww"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)

  name = randomsub.title
  url = randomsub.url
  em=discord.Embed(title = name)
  em.set_image(url = url)
  await ctx.send(embed= em)


@client.command()
async def memes(ctx,subred="dankmemes"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)

  name = randomsub.title
  url = randomsub.url
  em=discord.Embed(title = name)
  em.set_image(url = url)
  await ctx.send(embed= em)

@client.command()
async def news(ctx,subred="news"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)
  url = randomsub.url
  await ctx.send(url)

@client.command()
async def pics(ctx,subred="pics"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)

  name = randomsub.title
  url = randomsub.url
  em=discord.Embed(title = name)
  em.set_image(url = url)
  await ctx.send(embed= em)

@client.command()
async def gifs(ctx,subred="gifs"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)

  name = randomsub.title
  url = randomsub.url
  em=discord.Embed(title = name)
  em.set_image(url = url)
  await ctx.send(name)
  await ctx.send(url)

  
@client.command()
async def cats(ctx,subred="cats"):
  subreddit = reddit.subreddit(subred)
  allsubs = []
  hot = subreddit.hot(limit=50)
  for submission in hot:
    allsubs.append(submission)
  randomsub=random.choice(allsubs)

  name = randomsub.title
  url = randomsub.url
  em=discord.Embed(title = name)
  em.set_image(url = url)
  await ctx.send(name)
  await ctx.send(url)

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

for i in vcbot:
  i.setup(client)

@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

keep_alive()

client.run('REDACTED')