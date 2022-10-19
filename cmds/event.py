import discord
from discord.ext import commands
from core.classes import Cog_Extension
import json
import random

with open("setting.json",'r',encoding = 'utf_8') as jFile:
    jData = json.load(jFile)

class Event(Cog_Extension):
    #當成員加入時
    @commands.Cog.listener()
    async def on_member_join(self,member):
        print(f"{member} join!")
        channel = self.bot.get_channel(int(jData["Test_channel"]))
        await channel.send(f"{member} join!")

    #當成員離開時
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        print(f"{member} leave!")
        channel = self.bot.get_channel(int(jData["Test_channel"]))
        await channel.send(f"{member} leave!")

    #當成員離開時
    @commands.Cog.listener()
    async def on_message(self,msg):
        if msg.content == "87" and msg.author != self.bot.user:#防止機器人回復自己的訊息
            await msg.channel.send("臭87")

#cog必加結尾
async def setup(bot):
    await bot.add_cog(Event(bot))