import discord
from discord.ext import commands
import json
import random

with open("setting.json","r", encoding = "utf8") as jfile:
    jdata = json.load(jfile)


bot = commands.Bot(command_prefix = '@')

#Bot 上線指令
@bot.event
async def on_ready():
    print(">>Bot is Online<<")


#Bot 成員加入指令
@bot.event 
async def on_member_join(member):
    channel = bot.get_channel(jdata["Welcome_Channel"])
    await channel.send(f"{member}join!")


#Bot 成員離開指令
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(jdata["Leave_Channel"])
    await channel.send(f"{member}leave!")
    

#Bot Ping指令
@bot.command()
async def ping(ctx):
    await ctx.send(f"{round(bot.latency*1000)} (ms)")

#Bot dice指令
@bot.command()
async def dice(ctx):
    random_pic = random.choice(jdata["dice"])
    pic = discord.File(random_pic)
    await ctx.send(file = pic)

#Bot 網路圖片指令
@bot.command()
async def web(ctx):
    random_pic = random.choice(jdata["url-pic"])
    await ctx.send(random_pic)


bot.run(jdata["TOKEN"])