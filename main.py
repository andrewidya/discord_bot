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
    guildmarm = GuildMarm(command_prefix="!", owner_id=489318848731021312)

    for ext in EXTENSIONS:
        guildmarm.load_extension(ext)

    try:
        guildmarm.run(TOKEN)
    except Exception as e:
        print(e)
