import discord
import os
from dotenv import load_dotenv

 # load all the variables from the env file
load_dotenv()
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f"{bot.user} is ready and online!")
    await bot.change_presence(activity=discord.Game(name="https://github.com/Zckyy"))
    
# Array of cogs
cogs_list = [
    'greetings',
    'games',
    'misc',
]

#Loading all cogs in Array
for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

#Run bot
bot.run(os.getenv('TOKEN'))