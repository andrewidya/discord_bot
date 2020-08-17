import inspect

import discord

import config

def is_send_message_allowed(func):
    async def decorator(*args, **kwargs):
        ctx = args[1]
        is_allowed = False
        guild = config.GUILD_ECOSYSTEM[ctx.guild.name] if ctx.guild.name in config.GUILD_ECOSYSTEM else None
        channels = guild["allowed_channel"] if guild["allowed_channel"] else None

        try:
            if guild:
                if ctx.channel.name in channels:
                    is_allowed = True
                    await func(*args, **kwargs)
            
            if not is_allowed:
                channel_info = [ i.mention for i in ctx.guild.channels if i.name in channels ]
                await ctx.send(
                    "Saya hanya boleh menjawab di channel {}".format(", ".join(channel_info)),
                    allowed_mentions=discord.AllowedMentions()
                    )
        except Exception as e:
            print(e)

    return decorator