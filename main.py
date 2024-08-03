import settings
import discord
from discord.ext import commands

def run():
    print(settings.DISCORD_API_SECRET)
    intents = discord.Intents.default()
    
    bot = commands.Bot(command_prefix="!", intents=intents)
    
    @bot.event
    async def on_ready():
        print(bot.user)
        print(bot.user.id)
        print("_____________")
    
    bot.run(settings.DISCORD_API_SECRET)
    
if __name__ == "__main__":
    run()