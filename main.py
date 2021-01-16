import os
import sys

import discord
from discord.ext import commands
from discord.ext.commands.help import DefaultHelpCommand


import config
from guildmarm.settings import BASE_DIR


sys.path.append(BASE_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "guildmarm.settings")
import django
django.setup()


TOKEN = os.getenv("BOT_TOKEN")
ECO = config.GUILD_ECOSYSTEM
EXTENSIONS = [
    'cogs.greetings',
    'cogs.systems',
    'cogs.game_roles'
]


class HelpCommand(DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)

    def get_ending_note(self):
        """Returns help command's ending note.
        This is overrided version on i18n purposes."""
        command_name = self.invoked_with
        return "Ketik {0}{1} <command> untuk info lebih lanjut.\n" \
               "Kamu juga bisa ketik {0}{1} <category> untuk info category.".format(
                   self.clean_prefix, command_name)

    def command_not_found(self, string):
        return "Command {} tidak ada".format(string)

    def subcommand_not_found(self, command, string):
        if isinstance(command, discord.core.Group) and len(command.all_commands) > 0:
            return 'Command "{0.qualified_name}" tidak punya subcommand {1}'.format(
                        command, string)
        return 'Command "{0.qualified_name}" tidak punya subcommand'.format(command)


class GuildMarm(commands.Bot):
    async def on_ready(self):
        print("Logged to guild {0}".format(self.user.name))
        for guild in self.guilds:
            if guild.name in ECO:
                for channel in guild.channels:
                    if channel.name in ECO[guild.name]["allowed_channel"]:
                        await channel.send(
                            content="Halo salam hunter!!!, selamat berburu"
                                    ":grinning::clap:")
                        break
                break


if __name__ == "__main__":
    help_command = HelpCommand(command_attrs={'help': 'Tampilkan pesan ini'})
    guildmarm = GuildMarm(
        command_prefix=config.COMMAN_PREFIX,
        owner_id=config.OWNER_ID,
        help_command=help_command)

    for ext in EXTENSIONS:
        guildmarm.load_extension(ext)

    try:
        guildmarm.run(TOKEN)
    except Exception as e:
        print(e)
