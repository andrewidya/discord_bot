import os
import asyncio

import discord
from discord.ext import commands


class Maintenance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.NotOwner):
            await ctx.send("Hayoo, perintah ini cuman buat abang teknisi")

    @commands.group(name="system-config")
    @commands.is_owner()
    async def system_config(self, ctx):
        """Untuk config dan manage bot"""
        if ctx.invoked_subcommand is None:
            await ctx.send("sytem memerlukan parameter perintah")

    @system_config.command(name="reload")
    async def reload_cogs(self, ctx):
        """Reload semua cogs yang ada
        
        Bisa digunakan untuk hot reload cogs baru, biasanya
        diperlukan ketika menguji cogs tanpa harus restart bot
        """
        async with ctx.typing():
            embed = discord.Embed(
                title="Reloading all cogs", timestamp=ctx.message.created_at)
            
            for ext in os.listdir('cogs/'):
                if ext.endswith(".py") and not ext.startswith("_") and ext != 'systems.py':
                    try:
                        self.bot.reload_extension("cogs.{}".format(ext[:-3]))
                        embed.add_field(
                            name="Reloading 'cogs.{}'".format(ext[:-3]),
                            value="\uFEFF",
                            inline=False)
                    except Exception as e:
                        embed.add_field(
                            name="Error to reload 'cogs.{}'".format(ext[:-3]),
                            value=e,
                            inline=False)
                    
                    await asyncio.sleep(0.5)
            
            await ctx.send(embed=embed)
    
    @system_config.command(name="refresh")
    async def refresh_bot(self, ctx):
        """Refreshing bot"""
        async with ctx.typing():
            bot_name = self.bot.user.name
            embed = discord.Embed(
                title="Refresing {}".format(bot_name),
                timestamp=ctx.message.created_at)
            
            try:
                self.bot.clear()
                embed.add_field(
                    name="Refreshing {} successfull".format(bot_name),
                    value="\uFEFF",
                    inline=False)
            except Exception as e:
                embed.add_field(
                    name="Failed to refresh {}".format(bot_name),
                    value="\uFEFF",
                    inline=False)

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Maintenance(bot))


def teardown(bot):
    bot.remove_cog(Maintenance(bot))
