# -*- coding: utf-8 -*-
from discord.ext import commands
import discord
import asyncio,json
from discord.ext.commands import clean_content

class Ping(commands.Cog):
    """comando para testar se o bot esta funcionando"""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self, ctx):
    	await ctx.send("pong")
  
    
def setup(bot):
    bot.add_cog(Ping(bot))
