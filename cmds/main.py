import discord
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    #顯示機器人延遲
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

#cog必加結尾
async def setup(bot):
    await bot.add_cog(Main(bot))