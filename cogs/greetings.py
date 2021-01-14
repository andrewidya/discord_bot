import discord
from discord.ext import commands


class Greeting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        server_info = '<#798081750831726623>'
        rules = '<#790776530733105214>'
        message = "Halo {0.mention}, welcome to HAN7, silahkan baca \
            {1} dan {2} dulu. jika ada pertanyaan bisa tanyakan admin.".format(
                member, rules, server_info)
        await channel.send(message)


def setup(bot):
    bot.add_cog(Greeting(bot))