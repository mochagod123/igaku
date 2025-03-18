from discord.ext import commands
import discord

class Igaku(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Welcome to Igaku!!!")
        print("Created by Neko.")

    @commands.group(name="igaku")
    async def igaku(self, ctx: commands.Context):
        return

    @igaku.command(name="eval")
    async def igaku_eval(self, ctx: commands.Context, *, command: str):
        if ctx.author.id in self.bot.igaku_user:
            message = eval(command)
            if self.bot.ws.token in f"{message}":
                return await ctx.reply("TOKENが含まれるため、送信できません。")
            await ctx.reply(f"{message}")
        
    @igaku.command(name="owner_list")
    async def igaku_owner_list(self, ctx: commands.Context):
        if ctx.author.id in self.bot.igaku_user:
            await ctx.reply(f"オーナーリスト\n{self.bot.igaku_user}")

async def setup(bot):
    await bot.add_cog(Igaku(bot))