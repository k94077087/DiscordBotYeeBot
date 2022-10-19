import discord
from discord.ext import commands
from core.classes import Cog_Extension
import datetime
import pytz

class Main(Cog_Extension):
    #顯示機器人延遲
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f"{round(self.bot.latency*1000)} (ms)")

    #顯示機器人資訊
    @commands.command()
    async def info(self,ctx):
        embed=discord.Embed(title="YeeBot", url="https://github.com/k94077087/DiscordBotYeeBot", description="About YeeBot", color=0xedd32c, timestamp=datetime.datetime.now(pytz.timezone('Asia/Taipei')))
        embed.set_author(name="KkOnly", url="https://github.com/k94077087", icon_url="https://cdn.discordapp.com/attachments/1031823034690064485/1032138659425697813/CuteCat.JPG")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1031823034690064485/1032138659425697813/CuteCat.JPG")
        embed.add_field(name="birthday", value="2022/10/17", inline=True)
        embed.add_field(name="Author", value="KkOnly", inline=True)
        embed.set_footer(text="2147483647")
        await ctx.send(embed=embed)

    @commands.command()
    async def sayd(self,ctx,*,msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self,ctx,num:int):
        await ctx.channel.purge(limit = num+1)
        
#cog必加結尾
async def setup(bot):
    await bot.add_cog(Main(bot))