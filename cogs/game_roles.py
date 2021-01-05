from discord.ext import commands
from utils import is_send_message_allowed


class BaseRoleManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def get_guild_roles(self, ctx):
        return {role.name: role.id for role in ctx.guild.roles}

    def get_member_roles(self, ctx):
        return {role.name: role.id for role in ctx.author.roles}

    async def role_change_message(self, ctx, command, role):
        author_roles = self.get_guild_roles(ctx)
        if command == "set" and role in author_roles:
            await ctx.send("Kamu baru saja terdaftar dalam role {0}".format(role))
        if command == "unset" and role:
            await ctx.send("Kamu baru saja keluar dari role {0}".format(role))


    @is_send_message_allowed
    async def set_role(self, ctx, role_name):
        guild_roles = self.get_guild_roles(ctx)
        role_found = False

        for role in guild_roles:
            if role.lower().replace(" ", "-") == role_name:
                role_found = True
                author_roles = self.get_member_roles(ctx)
                if role not in author_roles and not ctx.author.bot:
                    new_role = ctx.guild.get_role(guild_roles[role])
                    await ctx.author.add_roles(new_role, reason="set platform from bot")
                    await self.role_change_message(ctx, "set", role)
                else:
                    await ctx.send("Maaf {0}, tapi kayaknya kamu udah ngeset "
                                   "role {1} deh".format(ctx.author.name, role_name))
                break

        if not role_found:
            await ctx.send("Role {0} nggak ada nih, tunggu dibikinin sama "
                           "bang adminnya ya".format(role_name))

    @is_send_message_allowed
    async def unset_role(self, ctx, role_name):
        guild_roles = self.get_guild_roles(ctx)
        role_found = False

        for role in guild_roles:
            if role.lower().replace(" ", "-") == role_name:
                role_found = True
                author_roles = self.get_member_roles(ctx)
                if role in author_roles and not ctx.author.bot:
                    role_id = guild_roles[role]
                    role_to_remove = [i for i in ctx.author.roles if i.id == role_id]
                    for r in role_to_remove:
                        await ctx.author.remove_roles(r, reason="unset platform from bot")
                        await self.role_change_message(ctx, "unset", role)
                break


class PlatformRole(BaseRoleManager, name="platform-hunter"):
    """platform yang digunakan oleh hunter.

    set platform ini agar hunter lain tahu dimana kamu berburu
    """
    @commands.group(name="set-platform", aliases=["platform"])
    async def platform(self, ctx):
        """untuk set platform/konsole game yang digunakan"""
        if ctx.invoked_subcommand is none:
            await ctx.send("set-plaform memerlukan paramater nama platform")

    @platform.command(name="n3ds", aliases=["3ds"], case_insensitive=True)
    async def n3ds(self, ctx):
        """nintendo 3ds"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="ps4", case_insensitive=True)
    async def ps4(self, ctx):
        """play station 4"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc", case_insensitive=True)
    async def pc(self, ctx):
        """pc"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-citra", aliases=["citra"], case_insensitive=True)
    async def pc_citra(self, ctx):
        """pc citra"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(
        name="android", aliases=["android-citra", "citra-android"],
        case_insensitive=True)
    async def android_citra(self, ctx):
        """android citra"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(name="pc-pspp", case_insensitive=True)
    async def pc_pspp(self, ctx):
        """pc pspp"""
        await self.set_role(ctx, ctx.command.name)

    @platform.command(
        name="switch", aliases=["nswitch", "nintendo-switch"], case_insensitive=True)
    async def nswitch(self, ctx):
        """nintendo switch"""
        await self.set_role(ctx, ctx.command.name)


class WeaponRole(BaseRoleManager, name='weapon-utama-hunter'):
    """weapon utama yang digunakan hunter

    set senjata utama yang kamu kuasai, biar hunter lain
    tahu kepada siapa mereka mencari bantuan untuk mencari
    material tertentu
    """
    @commands.group(name="set-main-weapon", aliases=["weap"])
    async def set_weapon(self, ctx):
        """untuk set weapon utama game yang digunakan"""
        if ctx.invoked_subcommand is None:
            await ctx.send("set-main-weapon memerlukan paramater weapon")

    @set_weapon.command(
        name="great-sword", aliases=["gs", ":GS:"], case_insensitive=True)
    async def great_sword(self, ctx):
        """Great Sword"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="long-sword", aliases=["ls", ":LS:"], case_insensitive=True)
    async def long_sword(self, ctx):
        """Long Sword"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="sword-and-shield", aliases=["sns", ":SNS:"], case_insensitive=True)
    async def sword_and_shield(self, ctx):
        """Sword & Shield"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="dual-blades", aliases=["db", ":DB:"], case_insensitive=True)
    async def dual_blade(self, ctx):
        """Dual Blade"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="hamer", aliases=["hmr", ":Hammer:"], case_insensitive=True)
    async def hammer(self, ctx):
        """Hammer"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="hunting-horn", aliases=["hh", ":HH:"], case_insensitive=True)
    async def hunting_horn(self, ctx):
        """Hunting Horn"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="lance", aliases=["lc", ":Lance:"], case_insensitive=True)
    async def lance(self, ctx):
        """Lance"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="gunlance", aliases=["gl", ":GL:"], case_insensitive=True)
    async def gunlance(self, ctx):
        """Gunlance"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="insect-glaive", aliases=["ig", ":IG:"], case_insensitive=True)
    async def insect_glaive(self, ctx):
        """Insect Glaive"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="charge-blade", aliases=["cb", ":CB:"], case_insensitive=True)
    async def charge_blade(self, ctx):
        """Charge Blade"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="switch-axe", aliases=["sa", ":SA:"], case_insensitive=True)
    async def switch_axe(self, ctx):
        """Switch Axe"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(name="bow", aliases=["bw", ":BOW:"], case_insensitive=True)
    async def bow(self, ctx):
        """Bow"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="light-bowgun", aliases=["lbg", ":LBG:"], case_insensitive=True)
    async def light_bowgun(self, ctx):
        """Light Bowgun"""
        await self.set_role(ctx, ctx.command.name)

    @set_weapon.command(
        name="heavy-bowgun", aliases=["hbg", ":HBG:"], case_insensitive=True)
    async def heavy_bowgun(self, ctx):
        """Heavy Bowgun"""
        await self.set_role(ctx, ctx.command.name)


class GameTitleRole(BaseRoleManager, name='title-series'):
    """Title / Series Monster Hunter

    Set judul seri game monster hunter yang saat ini
    sedang dimainkan, dengan begini hunter lain lebih
    mudah mencari teman berburu sesuai seri yang dimainkan
    """
    @commands.group(name="set-title-series", aliases=["Game"])
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

    @set_title_series.command(name="mhxx", aliases=["mhxx-3ds"], case_insensitive=True)
    async def mhxx(self, ctx):
        """Monster Hunter XX"""
        await self.set_role(ctx, ctx.command.name)

    @set_title_series.command(
        name="mhgu", aliases=["mhgu-switch"], case_insensitive=True)
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


class SetupRole(BaseRoleManager, name='set-role'):
    """Command for bot [simple edition]
    !help = buat bantuan list command

    untuk mengambil role:

    jika role weapon : !set [nama weapon]
        example -> !set bow

    jika role game : !set [game]
        example -> !set mh4u, !set mhp3rd

    jika role platform : !set [device]
        example -> !set ps4
    """
    @commands.group(name="set")
    async def main_set_role(self, ctx):
        """Untuk mengambil role"""
        if ctx.invoked_subcommand is None:
            await ctx.send("command 'set' memerlukan info yang mau di set")

    @commands.group(name="unset")
    async def main_unset_role(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("command 'unset' memerlukan info yang mau di unset")

    # command for game title specific
    # ex: mhf1, mh4u, mhwi etc
    @main_set_role.command(name="mhf1", case_insensitive=True)
    async def mhf1(self, ctx):
        """Monster Hunter Freedom 1"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhf1", case_insensitive=True)
    async def unset_mhf1(self, ctx):
        await self.unset_role(ctx, ctx.comand.name)

    @main_set_role.command(name="mhfu", case_insensitive=True)
    async def mhfu(self, ctx):
        """Monster Hunter Freedom United"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhfu", case_insensitive=True)
    async def unset_mhfu(self, ctx):
        """Monster Hunter Freedom United"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mhp3rd", case_insensitive=True)
    async def mhp3rd(self, ctx):
        """Monster Hunter Portable 3rd"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhp3rd", case_insensitive=True)
    async def unset_mhp3rd(self, ctx):
        """Monster Hunter Portable 3rd"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mh3u", case_insensitive=True)
    async def mh3u(self, ctx):
        """Monster Hunter 3 Ultimate"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mh3u", case_insensitive=True)
    async def unset_mh3u(self, ctx):
        """Monster Hunter 3 Ultimate"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mh4u", case_insensitive=True)
    async def mh4u(self, ctx):
        """Monster Hunter 4 Ultimate"""
        await self.set_role(ctx, ctx.command.name)
    
    @main_unset_role.command(name="mh4u", case_insensitive=True)
    async def unset_mh4u(self, ctx):
        """Monster Hunter 4 Ultimate"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mhgen", case_insensitive=True)
    async def mhgen(self, ctx):
        """Monster Hunter Generation"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhgen", case_insensitive=True)
    async def unset_mhgen(self, ctx):
        """Monster Hunter Generation"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mhxx", aliases=["mhxx-3ds"], case_insensitive=True)
    async def mhxx(self, ctx):
        """Monster Hunter XX"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhxx", aliases=["mhxx-3ds"], case_insensitive=True)
    async def unset_mhxx(self, ctx):
        """Monster Hunter XX"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="mhgu", aliases=["mhgu-switch"], case_insensitive=True)
    async def mhgu(self, ctx):
        """Monster Hunter Generation Ultimate"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="mhgu", aliases=["mhgu-switch"], case_insensitive=True)
    async def unset_mhgu(self, ctx):
        """Monster Hunter Generation Ultimate"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="mhw", case_insensitive=True)
    async def mhw(self, ctx):
        """Monster Hunter World"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="mhw", case_insensitive=True)
    async def unset_mhw(self, ctx):
        """Monster Hunter World"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="iceborne", case_insensitive=True)
    async def mhwi(self, ctx):
        """Monster Hunter World Iceborne"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="iceborne", case_insensitive=True)
    async def unset_mhwi(self, ctx):
        """Monster Hunter World Iceborne"""
        await self.unset_role(ctx, ctx.command.name)

    # comman for platform role setup
    # ex: PS4, PC etc
    @main_set_role.command(name="n3ds", aliases=["3ds"], case_insensitive=True)
    async def n3ds(self, ctx):
        """nintendo 3ds"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="n3ds", aliases=["3ds"], case_insensitive=True)
    async def unset_n3ds(self, ctx):
        """nintendo 3ds"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="ps4", case_insensitive=True)
    async def ps4(self, ctx):
        """play station 4"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="ps4", case_insensitive=True)
    async def unset_ps4(self, ctx):
        """play station 4"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="pc", case_insensitive=True)
    async def pc(self, ctx):
        """pc"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="pc", case_insensitive=True)
    async def unset_pc(self, ctx):
        """pc"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="pc-citra", aliases=["citra"], case_insensitive=True)
    async def pc_citra(self, ctx):
        """pc citra"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="pc-citra", aliases=["citra"], case_insensitive=True)
    async def unset_pc_citra(self, ctx):
        """pc citra"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="android", aliases=["android-citra", "citra-android"],
        case_insensitive=True)
    async def android_citra(self, ctx):
        """android citra"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="android", aliases=["android-citra", "citra-android"],
        case_insensitive=True)
    async def unset_android_citra(self, ctx):
        """android citra"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="pc-pspp", case_insensitive=True)
    async def pc_pspp(self, ctx):
        """pc pspp"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="pc-pspp", case_insensitive=True)
    async def unset_pc_pspp(self, ctx):
        """pc pspp"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="switch", aliases=["nswitch", "nintendo-switch"], case_insensitive=True)
    async def nswitch(self, ctx):
        """nintendo switch"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="switch", aliases=["nswitch", "nintendo-switch"], case_insensitive=True)
    async def unset_nswitch(self, ctx):
        """nintendo switch"""
        await self.unset_role(ctx, ctx.command.name)

    # command for main weapon setup
    # ex: switch axe, great sword etc
    @main_set_role.command(
        name="great-sword", aliases=["gs", ":GS:"], case_insensitive=True)
    async def great_sword(self, ctx):
        """Great Sword"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="great-sword", aliases=["gs", ":GS:"], case_insensitive=True)
    async def unset_great_sword(self, ctx):
        """Great Sword"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="long-sword", aliases=["ls", ":LS:"], case_insensitive=True)
    async def long_sword(self, ctx):
        """Long Sword"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="long-sword", aliases=["ls", ":LS:"], case_insensitive=True)
    async def unset_long_sword(self, ctx):
        """Long Sword"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="sword-and-shield", aliases=["sns", ":SNS:"], case_insensitive=True)
    async def sword_and_shield(self, ctx):
        """Sword & Shield"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="sword-and-shield", aliases=["sns", ":SNS:"], case_insensitive=True)
    async def unset_sword_and_shield(self, ctx):
        """Sword & Shield"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="dual-blades", aliases=["db", ":DB:"], case_insensitive=True)
    async def dual_blades(self, ctx):
        """Dual Blade"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="dual-blades", aliases=["db", ":DB:"], case_insensitive=True)
    async def unset_dual_blades(self, ctx):
        """Dual Blade"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="hamer", aliases=["hmr", ":Hammer:"], case_insensitive=True)
    async def hammer(self, ctx):
        """Hammer"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="hamer", aliases=["hmr", ":Hammer:"], case_insensitive=True)
    async def unset_hammer(self, ctx):
        """Hammer"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="hunting-horn", aliases=["hh", ":HH:"], case_insensitive=True)
    async def hunting_horn(self, ctx):
        """Hunting Horn"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="hunting-horn", aliases=["hh", ":HH:"], case_insensitive=True)
    async def unset_hunting_horn(self, ctx):
        """Hunting Horn"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="lance", aliases=["lc", ":Lance:"], case_insensitive=True)
    async def lance(self, ctx):
        """Lance"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="lance", aliases=["lc", ":Lance:"], case_insensitive=True)
    async def unset_lance(self, ctx):
        """Lance"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="gunlance", aliases=["gl", ":GL:"], case_insensitive=True)
    async def gunlance(self, ctx):
        """Gunlance"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="gunlance", aliases=["gl", ":GL:"], case_insensitive=True)
    async def unset_gunlance(self, ctx):
        """Gunlance"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="insect-glaive", aliases=["ig", ":IG:"], case_insensitive=True)
    async def insect_glaive(self, ctx):
        """Insect Glaive"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="insect-glaive", aliases=["ig", ":IG:"], case_insensitive=True)
    async def unset_insect_glaive(self, ctx):
        """Insect Glaive"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="charge-blade", aliases=["cb", ":CB:"], case_insensitive=True)
    async def charge_blade(self, ctx):
        """Charge Blade"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="charge-blade", aliases=["cb", ":CB:"], case_insensitive=True)
    async def unset_charge_blade(self, ctx):
        """Charge Blade"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="switch-axe", aliases=["sa", ":SA:"], case_insensitive=True)
    async def switch_axe(self, ctx):
        """Switch Axe"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="switch-axe", aliases=["sa", ":SA:"], case_insensitive=True)
    async def unset_switch_axe(self, ctx):
        """Switch Axe"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(name="bow", aliases=["bw", ":BOW:"], case_insensitive=True)
    async def bow(self, ctx):
        """Bow"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(name="bow", aliases=["bw", ":BOW:"], case_insensitive=True)
    async def unset_bow(self, ctx):
        """Bow"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="light-bowgun", aliases=["lbg", ":LBG:"], case_insensitive=True)
    async def light_bowgun(self, ctx):
        """Light Bowgun"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="light-bowgun", aliases=["lbg", ":LBG:"], case_insensitive=True)
    async def unset_light_bowgun(self, ctx):
        """Light Bowgun"""
        await self.unset_role(ctx, ctx.command.name)

    @main_set_role.command(
        name="heavy-bowgun", aliases=["hbg", ":HBG:"], case_insensitive=True)
    async def heavy_bowgun(self, ctx):
        """Heavy Bowgun"""
        await self.set_role(ctx, ctx.command.name)

    @main_unset_role.command(
        name="heavy-bowgun", aliases=["hbg", ":HBG:"], case_insensitive=True)
    async def unset_heavy_bowgun(self, ctx):
        """Heavy Bowgun"""
        await self.unset_role(ctx, ctx.command.name)


def setup(bot):
    # bot.add_cog(PlatformRole(bot))
    # bot.add_cog(WeaponRole(bot))
    # bot.add_cog(GameTitleRole(bot))
    bot.add_cog(SetupRole(bot))


def teardown(bot):
    # bot.remove_cog('PlatformRole')
    # bot.remove_cog('WeaponRole')
    # bot.remove_cog('GameTitleRole')
    bot.remove_cog('SetupRole')
