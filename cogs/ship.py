from discord.ext import commands
import discord
import random
import asyncio,json
from discord.ext.commands import clean_content

class Ship(commands.Cog):
    """Shippa duas pessoas mencionadas."""
    def __init__(self, bot):
        self.bot = bot

        

    @commands.command()
    async def ship(self, ctx, name1 :discord.Member,name2:discord.Member):
        shipnumber = random.randint(0,100)
        if 0 <= shipnumber <= 10:
            status = "Realmente baixo! {}".format(random.choice(["Friendzone ;(",'Somente "amigos"','"Amigos"', "Pouco ou nenhum amor;(","Quase não há amor ;("]))
            imagem="https://i.imgur.com/pezOkg9.gif";
        elif 10 < shipnumber <= 20:
            status = "Baixo! {}".format(random.choice(["Continua na friendzone","Ainda na friendzone ;(","Não há muito amor aqui... ;("]))
            imagem="https://i.imgur.com/xsyIxxf.gif";
        elif 20 < shipnumber <= 30:
            status = "Normal! {}".format(random.choice(["Parecem irmaos!","Mas há um pouco de amor em algum lugar!","Eu sinto um pouco de amor fraternal!","Parece um pouco de amizade"]))
            imagem="https://c.tenor.com/RLx1QpjOcTEAAAAC/anime-cat-girl.gif";
        elif 30 < shipnumber <= 40:
            status = "Pouco! {}".format(random.choice(["Nao passam de amigos", "Há um pouco de amor aí ...", "Amam mais comida do que um ao outro"]))
            imagem="https://i.imgur.com/zlWBVLG.gif";
        elif 40 < shipnumber <= 60:
            status = "Moderado! {}".format(random.choice(["Mas é muito unilateral OwO", "Parece unilateral!", "Há algum potencial!", "Sinto um pouco de potencial!", "Há um pouco de romance acontecendo aqui!", " Eu sinto que há algum romance progredindo! "," O amor está chegando lá ... "]))
            imagem="https://i.imgur.com/bwg5Vev.gif";
        elif 60 < shipnumber <= 70:
            status = "Bom! {}".format(random.choice(["Sinto o romance progredindo!", "Há um pouco de amor no ar!", "Estou começando a sentir um pouco de amor!"]))
            imagem="https://i.imgur.com/HTQcCLn.gif";
        elif 70 < shipnumber <= 80:
            status = "Excelente! {}".format(random.choice(["Desconfio que estao tendo um caso as escondidas!", "Posso ver que o amor está lá! Em algum lugar ...","Eu definitivamente posso ver que o amor está no ar"]))
            imagem="https://i.imgur.com/uviybrX.gif";
        elif 80 < shipnumber <= 90:
            status = "Acima da média! {}".format(random.choice(["O amor está no ar!", "Eu posso definitivamente sentir o amor", "Eu sinto o amor! Há um sinal de correspondência!", "Há um sinal de correspondência!", "Sinto uma correspondência ! "," Algumas coisas podem ser corrigidas para torná-lo um casamento feito no céu! "]))
            imagem="https://i.imgur.com/FGbRyyB.gif";
        elif 90 < shipnumber <= 100:
            status = "Amor verdadeiro! {}".format(random.choice(["Combinam perfeitamente!", "Se peguem logo carai!", "Quando vai ser o casamento?", "Se ja estiverem namorando escondido eu nao me surpreenderia!"])) 
            imagem="https://c.tenor.com/qEIeZqdgFMcAAAAC/up-wedding.gif";
        if shipnumber <= 33:
            shipColor = 0xE80303
        elif 33 < shipnumber < 66:
            shipColor = 0xff6600
        else:
            shipColor = 0x3be801

        emb = (discord.Embed(color=shipColor, \
                             title="Teste de amor para:", \
                             description="**{0.mention}** e **{1.mention}** {2}".format(name1, name2, random.choice([
                                                                                                        ":sparkling_heart:", 
                                                                                                        ":heart_decoration:", 
                                                                                                        ":heart_exclamation:", 
                                                                                                        ":heartbeat:", 
                                                                                                        ":heartpulse:", 
                                                                                                        ":hearts:", 
                                                                                                        ":blue_heart:", 
                                                                                                        ":green_heart:", 
                                                                                                        ":purple_heart:", 
                                                                                                        ":revolving_hearts:", 
                                                                                                        ":yellow_heart:", 
                                                                                                        ":two_hearts:"]))))
        emb.add_field(name="Resultado:", value=f"{shipnumber}%", inline=True)
        emb.add_field(name="Status:", value=(status), inline=False)
        emb.set_image(url=imagem)
        await ctx.send(embed=emb)
 

def setup(bot):
    bot.add_cog(Ship(bot))