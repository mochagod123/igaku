# igaku
discord.pyとdiscord.py-selfのデバッグツール

discord.py<br>
main.py
```
import discord
from discord.ext import commands

intent = discord.Intents.all()
# intent.members = True
# intent.message_content = True
intent.typing = False

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="*",
            help_command=None,
            intents=intent
        )
        self.igaku_user = [UserIds]
        print("InitDone")

bot = Bot()

@bot.event
async def on_ready():
    print("起動しました。")

@bot.event
async def setup_hook():
    await bot.load_extension("cog")
    await bot.load_extension("igaku-self")

bot.run("Token")
```
にする<br>

discord.py-self<br>
main.py
```
import discord
from discord.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="*",
            help_command=None,
        )
        self.igaku_user = [UserIds]
        print("InitDone")

bot = Bot()

@bot.event
async def on_ready():
    print("起動しました。")

@bot.event
async def setup_hook():
    await bot.load_extension("cog")
    await bot.load_extension("igaku-self")

bot.run("Token")
```
にする