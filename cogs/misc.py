import discord
from discord.ext import commands

class Misc(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot
        
    @discord.user_command()
    async def avatar(self, ctx, member: discord.Member):
        if member.display_avatar == None:
            await ctx.respond("User has no avatar")
        else:
            await ctx.respond(member.display_avatar)

def setup(bot):
    bot.add_cog(Misc(bot))