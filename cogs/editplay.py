# -*- coding: utf-8 -*-
from discord.ext import commands
import discord
import asyncio,json
from discord.ext.commands import clean_content

class Editplay(commands.Cog):
    """edita descricao jogando do bot."""

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def editplay(self, ctx,*,text):
        await self.bot.change_presence(activity=discord.Game(name=text))
        await ctx.send("descricao editada")
  
    
def setup(bot):
    bot.add_cog(Editplay(bot))