import discord
import sys
import traceback
import logging
from discord.ext import commands


class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.add_listener(self.on_command_error, "on_command_error")

    async def on_command_error(self, ctx, error):
        if hasattr(ctx.command, "on_error"):
            return  # Don't interfere with custom error handlers

        error = getattr(error, "original", error)  # get original error

        if isinstance(error, commands.CommandNotFound):
            return await ctx.send(
                f"Este comando nao existe. use `{self.bot.command_prefix}help` para ver a lista de comandos."
            )

        if isinstance(error, commands.CommandError):
            return await ctx.send(
                f"Error executing command `{ctx.command.name}`: {str(error)}")

        await ctx.send(
            "um erro inespeado ocorreu ao rodar esse comando.")
        logging.warn("Ignoring exception in command {}:".format(ctx.command))
        logging.warn("\n" + "".join(
            traceback.format_exception(
                type(error), error, error.__traceback__)))

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))