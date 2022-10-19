from encodings import utf_8
import discord
from discord.ext import commands
import json
import os
import asyncio

#開json檔
with open("setting.json",'r',encoding = 'utf_8') as jFile:
    jData = json.load(jFile)

#discord 1.5 重大更新
intents = discord.Intents.all()
bot = commands.Bot(command_prefix = 'y ',intents = intents)

#開啟bot
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#load所有extensions到bot中
async def load_extensions():
    for Filename in os.listdir("cmds"):
        if Filename.endswith(".py"):
            await bot.load_extension(f"cmds.{Filename[:-3]}")

#load指定的extension
@bot.command()
async def load(ctx,extension):
    await bot.load_extension(f"cmds.{extension}")
    await ctx.send(f"Load {extension} done.")

#unload指定的extension
@bot.command()
async def unload(ctx,extension):
    await bot.unload_extension(f"cmds.{extension}")
    await ctx.send(f"Unload {extension} done.")

#reload指定的extension
@bot.command()
async def reload(ctx,extension):
    await bot.reload_extension(f"cmds.{extension}")
    await ctx.send(f"Reload {extension} done.")


#if __name__ == "__main__":
#    bot.run(jData["TOKEN"])

#上面的改寫版，因應cog的機制需要await，故作此改寫
async def main():
    async with bot:
        await load_extensions()
        await bot.start(jData["TOKEN"])

asyncio.run(main())