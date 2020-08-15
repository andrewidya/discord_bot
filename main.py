import os

import discord
from discord.ext import commands
from discord.ext.commands.help import DefaultHelpCommand


TOKEN = os.getenv("BOT_TOKEN")
EXTENSIONS = [
    'cogs.greetings',
    'cogs.systems',
    'cogs.game_roles'
]

class HelpCommand(DefaultHelpCommand):
    def __init__(self, **options):
        super().__init__(**options)

    def get_ending_note(self):
        """Returns help command's ending note. This is overrided version on i18n purposes."""
        command_name = self.invoked_with
        return "Ketik {0}{1} <command> untuk info lebih lanjut.\n" \
               "Kamu juga bisa ketik {0}{1} <category> untuk info category.".format(
                   self.clean_prefix, command_name)


class GuildMarm(commands.Bot):
    async def on_ready(self):
        print("Logged to guild {0}".format(self.user.name))
        for guild in self.guilds:
            if guild.name == "andre_bot_dev":
                for channel in guild.channels:
                    if channel.name == "general":
                        await channel.send(
                            content="Halo salam hunter!!!, selamat berburu :grinning::clap:")
                        break
                break

if __name__ == "__main__":
    help_command = HelpCommand(command_attrs={'help': 'Tampilkan pesan ini'})
    guildmarm = GuildMarm(
        command_prefix="!",
        owner_id=489318848731021312,
        help_command=help_command)
        
    for ext in EXTENSIONS:
        guildmarm.load_extension(ext)

    try:
        guildmarm.run(TOKEN)
    except Exception as e:
        print(e)
