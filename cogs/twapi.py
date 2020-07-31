from discord.ext import commands,tasks
import asyncio
import traceback
import tw
import tweepy

print("Twitterの読み込み完了")

api = tw.api

class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.twap.start()

    #検索
    @commands.command()
    async def twitter(self, ctx, id=None):
        if id == None:
            id = 'ArknightsStaff'
        tl = api.user_timeline(id=id,count=1)
        for t in tl:
            embed = discord.Embed(title=f"**{t.user.name}**",description=t.text)                 
        await ch.send(embed=embed)

def setup(bot):
    bot.add_cog(Twitter(bot))