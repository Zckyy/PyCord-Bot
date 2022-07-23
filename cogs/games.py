import discord
import random
from discord.ext import commands

class Games(commands.Cog): # create a class for our cog that inherits from commands.Cog
    # this class is used to create a cog, which is a module that can be added to the bot

    def __init__(self, bot): # this is a special method that is called when the cog is loaded
        self.bot = bot

    #Coinflip
    @discord.slash_command()
    async def coinflip(self, ctx):
        """Flip a coin, see what you land on."""

        coin = ["Heads","Tails"]
        coinflip = random.choice(coin)
        await ctx.respond(f"{coinflip}!")
    
    #Get-the-Number
    @discord.command()
    async def gtn(self, ctx, guess):
        """Guess a number between 1 and 10."""
        
        correctAnswer = random.randint(0,10)
        print(f"The generated correct answer is: {correctAnswer}")
        
        if int(guess) == correctAnswer:
            await ctx.send('You guessed it!')
        else:
            await ctx.send('Nope, try again.')
    
    #Gaydar
    @discord.user_command()
    async def gaydar(self, ctx, member: discord.Member):
        gayValue = random.randint(0,100)
        await ctx.respond(f'{member.mention} is {gayValue}% gay!')
              
def setup(bot):
    bot.add_cog(Games(bot))