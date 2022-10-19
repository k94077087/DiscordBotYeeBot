import discord
from discord.ext import commands
from core.classes import Cog_Extension
import asyncio,json,datetime

with open("setting.json",'r',encoding = 'utf_8') as jFile:
    jData = json.load(jFile)

class Task(Cog_Extension):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        async def interval():
            await self.bot.wait_until_ready()
            self.channel = self.bot.get_channel(int(jData["Test_channel"]))
            while not self.bot.is_closed():
                await self.channel("Hi")
                await asyncio.sleep(5)
        self.bg_task = self.bot.loop.create_task(interval())

    @commands.command()
    async def set_channel(self,ctx,ch:int):
        self.channel = self.bot.get_channel(ch)
        await ctx.send(f"Set channel:{self.channel.mention}")

#cog必加結尾
async def setup(bot):
    await bot.add_cog(Task(bot))