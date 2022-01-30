from discord.ext import commands
import discord
from riotwatcher import LolWatcher, ApiError
import os
import json
class Lolstat(commands.Cog):
    """Comando para ver info do league of legends."""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def lolstat(self, ctx,*,text):
        emb = discord.Embed(title='Status do league',color=0x9b59b6,description='status do league of legends')
        api_key = 'RGAPI-074783d1-1848-4019-998a-1474b2b69703'
        watcher = LolWatcher(api_key)
        my_region = 'br1'
        me = watcher.summoner.by_name(my_region, text)
        my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
        app_json = json.dumps(my_ranked_stats[0])
        json_object = json. loads(app_json)
        id=json_object["leagueId"]
        tier=json_object["tier"]
        rank=json_object["rank"]
        pontos=str(json_object["leaguePoints"])+"  <:emoji_39:900535357672677376> "
        nome=json_object["summonerName"]
        vitorias=str(json_object["wins"])+"  <:Kermit_AAAAAAHHH:880294491226005595> "
        derrotas=str(json_object["losses"])+"  <:enervy:925781567886987304> "
        tipo=json_object["queueType"]+"  <:kill:900538073094422569> "
        emb.add_field(name='nome', value=nome, inline=False)
        emb.add_field(name='id', value=id, inline=False)
        emb.add_field(name='tier', value=tier, inline=False)
        emb.add_field(name='rank', value=rank, inline=False)
        emb.add_field(name='pontos', value=pontos, inline=False)
        emb.add_field(name='vitorias', value=vitorias, inline=False)
        emb.add_field(name='derrottas', value=derrotas, inline=False)
        emb.add_field(name='tipo', value=tipo, inline=False)
        await ctx.send(embed=emb)

def setup(bot):
    bot.add_cog(Lolstat(bot))
