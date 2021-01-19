import random

import discord
from discord.ext import commands

from dashboard.models import (
    MonsterHunterDatabase, SeriesMonster, SeriesWeapon, AdditionalProperties)


class MHDatabaseError(IndexError):
    pass


class WeaponError(IndexError):
    pass


class MonsterError(IndexError):
    pass


def random_choice(data):
    data_len = data.count()
    _list = [i for i in range(data_len)]

    for _ in range(data_len):
        random.shuffle(_list)

    return data[random.choice(_list)]


class RouletteHunt(commands.Cog, name="roulette-hunt"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="rng")
    async def rng_quest(self, ctx):
        """Generate random monster dan weapon untuk quest"""
        channel = ctx.message.channel

        try:
            async with ctx.typing():
                suggestion = self.generate_data(channel)
            embed = discord.Embed(
                title="Pesanan Quest", description="Hasil pencarian pesanan quest kali ini",
                color=discord.Color.dark_blue())
            if suggestion["series"]:
                embed.add_field(name="Game", value=suggestion["series"], inline=False)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/798908288778633287/800092481411612672/mh_crest.png")
            embed.add_field(name="Monster", value=suggestion["monster"], inline=True)
            embed.add_field(name="Weapon", value=suggestion["weapon"], inline=True)
            if suggestion["additional"]:
                for i in suggestion["additional"]:
                    text = "{}\n{}".format(
                        i["value"]["name"], i["value"]["description"])
                    embed.add_field(name=i["label"], value=text, inline=False)
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
        others = [
            {"label": i[1], "field": i[0]}
            for i in AdditionalProperties.GROUPING
        ]

        for d in others:
            additional = AdditionalProperties.objects.filter(
                group=group, prop_grouping=d["field"]).values(
                    "name", "description")
            if additional.count() > 0:
                d.update({"value": random_choice(additional)})
        
        if weapons.count() == 0:
            raise WeaponError("Data Weapon untuk seri {} belum ada".format(group))

        if monsters.count() == 0:
            raise MonsterError("Data Monster untuk seri {} belum ada".format(group))

        return {
            "weapon": random_choice(weapons),
            "monster": random_choice(monsters),
            "series": group.series.aliases,
            "additional": [i for i in others if "value" in i]
        }


def setup(bot):
    bot.add_cog(RouletteHunt(bot))