# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel

from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot, CMD_HELP
from userbot.events import geezbot_cmd
from userbot import CUSTOM_CMD as geez

from asyncio.exceptions import TimeoutError


# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#
# Port to userbot by @MoveAngel


@bot.on(geezbot_cmd(outgoing=True, pattern=r"sg(?: |$)(.*)"))
async def lastname(steal):
    if steal.fwd_from:
        return
    if not steal.reply_to_msg_id:
        await steal.edit("```Reply Ke BaBu```")
        return
    message = await steal.get_reply_message()
    chat = "@SangMataInfo_bot"
    user_id = message.sender.id
    id = f"/search_id {user_id}"
    if message.sender.bot:
        await steal.edit("```Reply Ke Pesan Babu```")
        return
    await steal.edit("```Mohon tunggu Masi proses```")
    try:
        async with bot.conversation(chat) as conv:
            try:
                msg = await conv.send_message(id)
                r = await conv.get_response()
                response = await conv.get_response()
            except YouBlockedUserError:
                await steal.reply(
                    "```@SangMataInfo_bot Sang Mata Jan Di Blockir Tolol```"
                )
                return
            if r.text.startswith("Name"):
                respond = await conv.get_response()
                await steal.edit(f"{r.message}")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id, respond.id]
                )
                return
            if response.text.startswith("No records") or r.text.startswith(
                "No records"
            ):
                await steal.edit("```No records found for this user```")
                await steal.client.delete_messages(
                    conv.chat_id, [msg.id, r.id, response.id]
                )
                return
            else:
                respond = await conv.get_response()
                await steal.edit(f"{response.message}")
            await steal.client.delete_messages(
                conv.chat_id, [msg.id, r.id, response.id, respond.id]
            )
    except TimeoutError:
        return await steal.edit("`Error: `@SangMataInfo_bot` is not responding!.`")


CMD_HELP.update({
    "sangmata":
        f"`{geez}sg`\
          \nUsage: Steal ur or friend name."
})
