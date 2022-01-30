import discord
import sys
import random
import os
import sqlite3
from cogwatch import Watcher
from discord.ext import commands
con = sqlite3.connect('database.db')
cur = con.cursor()
cur.execute('Select * FROM status')
stat =cur.fetchall()
status=random.choice(stat)
pref=cur.execute('Select value FROM config WHERE key=="prefix"')
prefix=pref.fetchone()
bot = commands.Bot(command_prefix=prefix[0])
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=status[0]))
    print(f"bot   {bot.user.name} ligado com sucesso")
    watcher = Watcher(bot, path="cogs", preload=True)
    await watcher.start()

def run():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('Select value FROM config WHERE key=="token"')
    result = cur.fetchone()
    if result == "":
        raise ValueError("token not found")
        print(result);
        sys.exit(1)
    bot.run(result[0])

