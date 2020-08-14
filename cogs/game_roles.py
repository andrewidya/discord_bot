import discord
from discord.ext import commands


class BaseRoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_guild_roles(self, ctx):
        return { role.name: role.id for role in ctx.guild.roles }

    def get_member_roles(self, ctx):
        return { role.name: role.id for role in ctx.author.roles }

    async def set_role(self, ctx, role_name):
        guild_roles = self.get_guild_roles(ctx)
        if role_name in guild_roles and not ctx.author.bot:
            author_roles = self.get_member_roles(ctx)
            if role_name not in author_roles:
                role = ctx.guild.get_role(guild_roles[role_name])
                await ctx.author.add_roles(role, reason="set platform from bot")
            else:
                await ctx.send("Maaf {0}, tapi kayaknya kamu udah ngeset "\
                        "role {1} deh".format(ctx.author.name, role_name))
        else:
            await ctx.send("Role {0} nggak ada nih, tunggu dibikinin sama "\
                    "bang adminnya ya".format(role_name))


class PlatformRole(BaseRoleManager, name="platform-hunter"):
    """Platform yang digunakan oleh hunter.
    
    Set platform ini agar hunter lain tahu dimana kamu berburu
    """   
    @commands.group(name="set-platform")
    async def platform(self, ctx):
        """Untuk set platform/konsole game yang digunakan"""
        if ctx.invoked_subcommand is None:
            await ctx.send("set-plaform memerlukan paramater nama platform")

    @platform.command(name="n3ds")
    async def n3ds(self, ctx):
        """Nintendo 3ds"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="ps4")
    async def ps4(self, ctx):
        """Play Station 4"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc")
    async def pc(self, ctx):
        """PC"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-citra")
    async def ps4(self, ctx):
        """PC Citra"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-pspp")
    async def ps4(self, ctx):
        """PC PSPP"""
        await self.set_role(ctx, ctx.command.name)  

    @platform.command(name="switch")
    async def nswitch(self, ctx):
        """Nintendo Switch"""
        await self.set_role(ctx, ctx.command.name)


def setup(bot):
    bot.add_cog(PlatformRole(bot))
