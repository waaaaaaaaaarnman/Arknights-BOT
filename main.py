import json
import discord
import dropbox
import asyncio
import traceback
from discord.ext import commands
import os

token = os.environ.get("TOKEN")
prefix = ";"

dbxtoken = "_Qobiq7UxdAAAAAAAAAAUSQMe2MDJyrmNyMWglSKGrfZKrrzGx_ruooafYposH3L"
dbx = dropbox.Dropbox(dbxtoken)
dbx.users_get_current_account()

async def run():
    bot = MyBot()
    try:
        await bot.start(token)
    except KeyboardInterrupt:
        await bot.logout()


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or(prefix), loop=loop)
        self.remove_command('help')

    async def on_ready(self):
        for extension in ["admin", "help", "log", "global_chat", "main_program", "disboard", "limited", "auxiliary", "music", "url", "twapi"]:
            try:
                self.load_extension(f"cogs.{extension}")
            except commands.ExtensionAlreadyLoaded:
                self.reload_extension(f"cogs.{extension}")


        await self.change_presence(activity=discord.Game(name=f"{prefix}help | {len(self.guilds)}guilds"))

    async def on_guild_join(self, _):
        await self.change_presence(activity=discord.Game(name=f"{prefix}help | {len(self.guilds)}guilds"))

    async def on_guild_remove(self, _):
        await self.change_presence(activity=discord.Game(name=f"{prefix}help | {len(self.guilds)}guilds"))

    async def on_command_error(self, ctx, error1):
        if isinstance(error1, (commands.CommandNotFound, commands.CommandInvokeError)):
            return

if __name__ == '__main__':
    try:
        print("Logged in as")
        with open("all_data_arknights_main.db", "wb") as f:
            metadata, res = dbx.files_download(path="/all_data_arknights_main.db")
            f.write(res.content)
        print("データベースのダウンロード完了")

        main_task = loop.create_task(run())
        loop.run_until_complete(main_task)
        loop.close()

    except Exception as error:
        print("エラー情報\n" + traceback.format_exc())
