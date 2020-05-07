import discord
from discord.ext import commands
import asyncio

class Disboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == 302050872383242240 :
            if "表示順をアップ" in message.embeds[0].description:
                mn = message.author.name
                msg = await message.channel.send(f"{mn}さんBumpを確認しました。\n2時間後に通知します。")
                await asyncio.sleep(10)
                m = 0
                while m < 7201:
                    b = 7200
                    s = b - m
                    await msg.edit(content=f"あと{s}秒後にBumpできます。")
                    await asyncio.sleep(1)
                    m += 1
                await msg.edit(content=f"<@&694401914770554881>{mn}\nBump可能")
            
def setup(bot):
    bot.add_cog(Disboard(bot))
