from telethon.tl.functions.phone import JoinGroupCallRequest as joinvc
from telethon.tl.functions.phone import LeaveGroupCallRequest as leavevc
from userbot import ALIVE_NAME, CMD_HELP, API_KEY, API_HASH, telethn
from userbot.events import register
from telethon.tl.types import DataJSON
from telethon.sync import TelegramClient
from telethon import functions, types

with TelegramClient(TelegramClient(MemorySession(), API_KEY, API_HASH) as client:
    result = client(functions.phone.JoinGroupCallRequest(
        call=types.InputGroupCall(
            id=API_KEY,
            access_hash=API_HASH
        ),
        join_as=ALIVE_NAME,
        params=types.DataJSON(
            data='telethn'
        ),
        muted=True,
        video_stopped=True,
        invite_hash='telethn'
    ))
    print(result.stringify())


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call

@register(outgoing=True, groups_only=True, pattern=r"^\.joinvc$")
async def join_voice(c):
    chat = await c.get_chat

try:
        await c.client(joinvc(await get_call(c), users=client))
        await c.edit("`Joined...`")
    except Exception as ex:
        await c.edit(f"**ERROR:** `{ex}`")
