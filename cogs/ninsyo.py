from discord.ext import commands
import discord
import datetime
import r
import os

main_guild_id=689263691669176426
role_name="認証済み"

class Ninsyo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="agree")
    async def _ninsyo(self, ctx):
        if ctx.guild.id!=main_guild_id:
            return
        command_time=datetime.datetime.now()
        command_minute=command_time.minute
        members=ctx.author.id
        #データベース読み込み(値をjtに)
        conn=r.connect()
        jt=conn.get(members)
        jt=str(jt)
        x=command_minute-jt
        if x<0:
            x+=60
        if x>4:
            members=self.bot.get_user(members)
            role = discord.utils.get(ctx.guild.roles,name=role_name)
            await members.add_roles(role)
            await ctx.send("登録しました")
            p=conn.delete(members)
            print(p)
        else:
            x=5-x
            await ctx.send(f"後{x}分後に登録できます")

def setup(bot):
    bot.add_cog(Ninsyo(bot))
