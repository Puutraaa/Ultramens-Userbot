# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# You can find misc modules, which dont fit in anything xD

import io
import sys
from os import execl
from random import randint
from time import sleep

from userbot import BOTLOG, BOTLOG_CHATID, CMD_HELP, bot
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez
from userbot.utils import time_formatter


@bot.on(geezbot_cmd(outgoing=True, pattern=r"random"))
async def randomise(items):
    itemo = (items.text[8:]).split()
    if len(itemo) < 2:
        return await items.edit(
            "`2 or more items are required! Check .help random for more info.`"
        )
    index = randint(1, len(itemo) - 1)
    await items.edit(
        "**Query: **\n`" + items.text[8:] + "`\n**Output: **\n`" + itemo[index] + "`"
    )


@bot.on(geezbot_cmd(outgoing=True, pattern=r"sleep ([0-9]+)$"))
async def sleepybot(time):
    counter = int(time.pattern_match.group(1))
    await time.edit("`I am sulking and snoozing...`")
    if BOTLOG:
        str_counter = time_formatter(counter)
        await time.client.send_message(
            BOTLOG_CHATID,
            f"You put the bot to sleep for {str_counter}.",
        )
    sleep(counter)
    await time.edit("`OK, I'm awake now.`")


@bot.on(geezbot_cmd(outgoing=True, pattern=r"shutdown$"))
async def killthebot(event):
    await event.edit("`Goodbye...`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#SHUTDOWN \n" "Bot shut down")
    await bot.disconnect()


@bot.on(geezbot_cmd(outgoing=True, pattern=r"restart$"))
async def killdabot(event):
    await event.edit("`*i would be back in a moment*`")
    if BOTLOG:
        await event.client.send_message(BOTLOG_CHATID, "#RESTART \n" "Bot Restarted")
    await bot.disconnect()
    # Spin a new instance of bot
    execl(sys.executable, sys.executable, *sys.argv)
    # Shut the existing one down
    sys.exit()


@bot.on(geezbot_cmd(outgoing=True, pattern=r"readme$"))
async def reedme(e):
    await e.edit(
        "Here's something for you to read:\n"
        "\n[ProjectAlf's README.md file](https://github.com/alfianandaa/ProjectAlf/blob/master/README.md)"
        "\n[Setup Guide - Basic](https://telegra.ph/How-to-host-a-Telegram-Userbot-11-02)"
        "\n[Setup Guide - Google Drive](https://telegra.ph/How-To-Setup-Google-Drive-04-03)"
        "\n[Setup Guide - LastFM Module](https://telegra.ph/How-to-set-up-LastFM-module-for-Paperplane-userbot-11-02)"
        "\n[Video Tutorial - 576p](https://mega.nz/#!ErwCESbJ!1ZvYAKdTEfb6y1FnqqiLhHH9vZg4UB2QZNYL9fbQ9vs)"
        "\n[Video Tutorial - 1080p](https://mega.nz/#!x3JVhYwR!u7Uj0nvD8_CyyARrdKrFqlZEBFTnSVEiqts36HBMr-o)"
        "\n[Special - Note](https://telegra.ph/Special-Note-11-02)"
    )


# Copyright (c) Gegham Zakaryan | 2019
@bot.on(geezbot_cmd(outgoing=True, pattern=r"repeat (.*)"))
async def repeat(rep):
    cnt, txt = rep.pattern_match.group(1).split(" ", 1)
    replyCount = int(cnt)
    toBeRepeated = txt

    replyText = toBeRepeated + "\n"

    for _ in range(replyCount - 1):
        replyText += toBeRepeated + "\n"

    await rep.edit(replyText)


@bot.on(geezbot_cmd(outgoing=True, pattern=r"repo$"))
async def repo_is_here(wannasee):
    """ For .repo command, just returns the repo URL. """
    await wannasee.edit(
        "╭‒─‒──────────‒─‒\n"
        "│                   ʀᴇᴘᴏ\n"
        "│       [⚔️Ultramen-Userbot⚔️](https://github.com/Puutraaa/Ultramens-Userbot)\n"
        "├‒─‒──────────‒\n"
        "│⚔️ **ᴏᴡɴᴇʀ :** [Ultra-men](t.me/EntarSuren)\n"
        "╰‒─‒──────────\n"
        "  𝗟𝗶𝗰𝗲𝗻𝘀𝗲 : [GPL-3.0 License](https://github.com/Puutraaa/Ultramens-Userbot/blob/Ultramen-Userbot/LICENSE)"
    )


@bot.on(geezbot_cmd(outgoing=True, pattern=r"raw$"))
async def raw(event):
    the_real_message = None
    reply_to_id = None
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        the_real_message = previous_message.stringify()
        reply_to_id = event.reply_to_msg_id
    else:
        the_real_message = event.stringify()
        reply_to_id = event.message.id
    with io.BytesIO(str.encode(the_real_message)) as out_file:
        out_file.name = "raw_message_data.txt"
        await event.edit("`Check the userbot log for the decoded message data !!`")
        await event.client.send_file(
            BOTLOG_CHATID,
            out_file,
            force_document=True,
            allow_cache=False,
            reply_to=reply_to_id,
            caption="`Here's the decoded message data !!`",
        )


CMD_HELP.update(
    {
        "random": f">`{geez}random <item1> <item2> ... <itemN>`"
        "\nUsage: Get a random item from the list of items.",
        "sleep": f">`{geez}sleep <seconds>`"
        "\nUsage: Let yours snooze for a few seconds.",
        "shutdown": f">`{geez}shutdown`"
        "\nUsage: Shutdown bot",
        "repo": f">`{geez}repo`"
        "\nUsage: Github Repo of this bot",
        "readme": f">`{geez}readme`"
        "\nUsage: Provide links to setup the userbot and it's modules.",
        "repeat": f">`{geez}repeat <no> <text>`"
        "\nUsage: Repeats the text for a number of times. Don't confuse this with spam tho.",
        "restart": f">`{geez}restart`"
        "\nUsage: Restarts the bot !!",
        "raw": f">`{geez}raw`"
        "\nUsage: Get detailed JSON-like formatted data about replied message.",
    })
