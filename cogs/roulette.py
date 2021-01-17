from random import randint

import discord
from discord.ext import commands

from dashboard.models import MonsterHunterDatabase, SeriesMonster, SeriesWeapon


class MHDatabaseError(IndexError):
    pass


class WeaponError(IndexError):
    pass


class MonsterError(IndexError):
    pass


class RouletteHunt(commands.Cog, name="roulette-hunt"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rng")
    async def rng_quest(self, ctx):
        """Generate random monster dan weapon untuk quest"""
        channel = ctx.message.channel

        try:
            suggestion = self.generate_data(channel)
            embed = discord.Embed(
                title="Pesanan Quest", description="Hasil pencarian pesanan quest kali ini",
                color=discord.Color.dark_blue())
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/798908288778633287/800092481411612672/mh_crest.png")
            embed.add_field(name="Monster", value=suggestion["monster"], inline=True)
            embed.add_field(name="Weapon", value=suggestion["weapon"], inline=True)
            embed.set_footer(text="Happy Hunting!!!")
            await ctx.send(embed=embed)
        except IndexError as e:
            await ctx.send(e)        

    def generate_data(self, channel):
        group = MonsterHunterDatabase.objects.filter(discord_channel=channel.name)
        if group.count() == 0:
            raise MHDatabaseError(
                "Database untuk series sesuai channel {} belum ada".format(channel.mention))
        else:
            group = group[0]
        
        weapons = SeriesWeapon.objects.filter(
            group=group).values_list("weapon__name", flat=True)
        monsters = SeriesMonster.objects.filter(
            group=group).values_list("monster__name", flat=True)
        
        if weapons.count() == 0:
            raise WeaponError("Data Weapon untuk seri {} belum ada".format(group))

        if monsters.count() == 0:
            raise MonsterError("Data Monster untuk seri {} belum ada".format(group))

        return {
            "weapon": weapons[randint(0, weapons.count() - 1)],
            "monster": monsters[randint(0, monsters.count() - 1)]
        }


def setup(bot):
    bot.add_cog(RouletteHunt(bot))