import discord
from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            message = "Selamat datang {0.mention}," \
                " selamat berbelanja".format(member)
            await channel.send(message)


def setup(bot):
    bot.add_cog(Greeting(bot))