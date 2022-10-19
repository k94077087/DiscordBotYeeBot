import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("discord_bot_YeeBot\setting.json",'r',encoding = 'utf_8') as jFile:
    jData = json.load(jFile)

class React(Cog_Extension):
    #可愛貓貓
    @commands.command()
    async def CuteCat(self,ctx):
        pic = discord.File(jData["PicPath"][0])
        await ctx.send(file = pic)

    #本地隨機圖片
    @commands.command()
    async def Rpic(self,ctx):
        random_pic = random.choice(jData["PicPath"])
        pic = discord.File(random_pic)
        await ctx.send(file = pic)

    #網路圖片
    @commands.command()
    async def RCat(self,ctx):
        random_pic = random.choice(jData["url_pic"])
        await ctx.send(random_pic)

#cog必加結尾
async def setup(bot):
    await bot.add_cog(React(bot))