import discord
from discord.ext import commands

class Greetings(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    @discord.slash_command()
    async def hello(self, ctx):
        """Say goodbye to the bot."""

        await ctx.respond('Hello!')

    @discord.slash_command()
    async def goodbye(self, ctx):
        """Say hello to the bot."""

        await ctx.respond('Goodbye!')
        
    @discord.user_command()
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')
        
def setup(bot):
    bot.add_cog(Greetings(bot))