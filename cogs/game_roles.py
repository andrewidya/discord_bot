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

    @platform.command(name="n3ds", case_insensitive=True)
    async def n3ds(self, ctx):
        """Nintendo 3ds"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="ps4", case_insensitive=True)
    async def ps4(self, ctx):
        """Play Station 4"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc", case_insensitive=True)
    async def pc(self, ctx):
        """PC"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-citra", case_insensitive=True)
    async def ps4(self, ctx):
        """PC Citra"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-pspp", case_insensitive=True)
    async def ps4(self, ctx):
        """PC PSPP"""
        await self.set_role(ctx, ctx.command.name)  

    @platform.command(name="switch", case_insensitive=True)
    async def nswitch(self, ctx):
        """Nintendo Switch"""
        await self.set_role(ctx, ctx.command.name)


class WeaponRole(BaseRoleManager, name='weapon-utama-hunter'):
    """Weapon utama yang digunakan hunter

    Set senjata utama yang kamu kuasai, biar hunter lain
    tahu kepada siapa mereka mencari bantuan untuk mencari
    material tertentu
    """
    @commands.group(name="set-main-weapon")
    async def set_weapon(self, ctx):
        """Untuk set weapon utama game yang digunakan"""
        if ctx.invoked_subcommand is None:
            await ctx.send("set-main-weapon memerlukan paramater weapon")

    @set_weapon.command(name="great-sword", aliases=["gs",], case_insensitive=True)
    async def great_sword(self, ctx):
        """Great Sword"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="long-sword", aliases=["ls",], case_insensitive=True)
    async def long_sword(self, ctx):
        """Long Sword"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="sword-and-shield", aliases=["sns",], case_insensitive=True)
    async def sword_and_shield(self, ctx):
        """Sword & Shield"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="dual-blade", aliases=["db",], case_insensitive=True)
    async def dual_blade(self, ctx):
        """Dual Blade"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="hamer", aliases=["hmr",], case_insensitive=True)
    async def hammer(self, ctx):
        """Hammer"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="hunting-horn", aliases=["hh",], case_insensitive=True)
    async def hunting_horn(self, ctx):
        """Hunting Horn"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="lance", aliases=["lc",], case_insensitive=True)
    async def lance(self, ctx):
        """Lance"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="gunlance", aliases=["gl",], case_insensitive=True)
    async def gunlance(self, ctx):
        """Gunlance"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="insect-glaive", aliases=["ig",], case_insensitive=True)
    async def insect_glaive(self, ctx):
        """Insect Glaive"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="charge-blade", aliases=["cb",], case_insensitive=True)
    async def charge_blade(self, ctx):
        """Charge Blade"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="switch-axe", aliases=["sa",], case_insensitive=True)
    async def switch_axe(self, ctx):
        """Switch Axe"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="bow", aliases=["bw",], case_insensitive=True)
    async def bow(self, ctx):
        """Bow"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="light-bowgun", aliases=["lbg",], case_insensitive=True)
    async def light_bowgun(self, ctx):
        """Light Bowgun"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="heavy-bowgun", aliases=["hbg",], case_insensitive=True)
    async def heavy_bowgun(self, ctx):
        """Heavy Bowgun"""
        await self.set_role(ctx, ctx.command.name)


class GameTitleRole(BaseRoleManager, name='title-series'):
    """Title / Series Monster Hunter

    Set judul seri game monster hunter yang saat ini
    sedang dimainkan, dengan begini hunter lain lebih
    mudah mencari teman berburu sesuai seri yang dimainkan    
    """
    @commands.group(name="set-title-series")
    async def set_title_series(self, ctx):
        """Untuk set judul seri game yang sedang dimainkan"""
        if ctx.invoked_subcommand is None:
            await ctx.send("set-title-series memerlukan paramater judul seri game")
    
    @set_title_series.command(name="mhf1", case_insensitive=True)
    async def mhf1(self, ctx):
        """Monster Hunter Freedom 1"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhfu", case_insensitive=True)
    async def mhfu(self, ctx):
        """Monster Hunter Freedom United"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhp3rd", case_insensitive=True)
    async def mhp3rd(self, ctx):
        """Monster Hunter Portable 3rd"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mh3u", case_insensitive=True)
    async def mh3u(self, ctx):
        """Monster Hunter 3 Ultimate"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mh4u", case_insensitive=True)
    async def mh4u(self, ctx):
        """Monster Hunter 4 Ultimate"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhgen", case_insensitive=True)
    async def mhgen(self, ctx):
        """Monster Hunter Generation"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhxx", case_insensitive=True)
    async def mhxx(self, ctx):
        """Monster Hunter XX"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhgu", case_insensitive=True)
    async def mhgu(self, ctx):
        """Monster Hunter Generation Ultimate"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="mhw", case_insensitive=True)
    async def mhw(self, ctx):
        """Monster Hunter World"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(name="iceborne", case_insensitive=True)
    async def mhwi(self, ctx):
        """Monster Hunter World Iceborne"""
        await self.set_role(ctx, ctx.command.name)


def setup(bot):
    bot.add_cog(PlatformRole(bot))
    bot.add_cog(WeaponRole(bot))
    bot.add_cog(GameTitleRole(bot))


def teardown(bot):
    bot.remove_cog('PlatformRole')
    bot.remove_cog('WeaponRole')
    bot.remove_cog('GameTitleRole')
