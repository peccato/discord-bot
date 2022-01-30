from discord.ext import commands
import discord
class Say(commands.Cog):
    """Commands for providing tips about using the bot."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(hidden=True)
    async def say(self, ctx,channel : discord.TextChannel, *,text):
       """Faz o bot falar a mensagem"""
       message = ctx.message
       await channel.send(text)
       
def setup(bot):
    bot.add_cog(Say(bot))
