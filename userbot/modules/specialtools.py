from time import sleep
from platform import uname
from userbot import ALIVE_NAME, WEATHER_DEFCITY, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(f"**JAKA SEMBUNG BAWA GOLOK**")
    sleep(3)
    await typew.edit("**NIMBRUNG GOBLOKK!!!**")
# Pantun


@register(outgoing=True, pattern='^.p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Salam Dulu Biar Sopan...`")
    sleep(2)
    await typew.edit("`السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Salam


@register(outgoing=True, pattern='^.l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`Kalo Orang Salam Itu Dijawab...`")
    sleep(2)
    await typew.edit("`وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ`")
# Menjawab Salam


@register(outgoing=True, pattern="^.kenalin(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Kek Gila`")
    sleep(2)
    await typew.edit("✅ `Kek Gila`")
    sleep(1)
    await typew.edit("☑️ `Askar Stress`")
    sleep(2)
    await typew.edit("✅ `Askar Stress`")
    sleep(1)
    await typew.edit("☑️ `Duta Gajelas`")
    sleep(2)
    await typew.edit("✅ `Duta Gajelas`")
    sleep(1)
    await typew.edit("☑️ `Skyzuu Wibu Sangean`")
    sleep(2)
    await typew.edit("✅ `Skzuu Wibu Sangean`")
    sleep(1)
    await typew.edit("☑️ `Izyy Autis`")
    sleep(2)
    await typew.edit("✅ `Izzy Autis`")
    sleep(1)
    await typew.edit("`⚡ Cuma Ultramen Yang Paling Waras, Baik Hati, Dan Tidak Sombong :v`")
# King Userbot Support


@register(outgoing=True, pattern="^.la(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("☑️ `Askar Owner Sadis`")
    sleep(1)
    await typew.edit("✅ `Askar Owner Sadis`")
    sleep(2)
    await typew.edit("☑️ `Kek Gila`")
    sleep(1)
    await typew.edit("✅ `Kek Gila`")
    sleep(2)
    await typew.edit("☑️ `Duta Babi`")
    sleep(1)
    await typew.edit("✅ `Duta Babi`")
    sleep(2)
    await typew.edit("☑️ `Ken Bapak Tukang Coli`")
    sleep(1)
    await typew.edit("✅ `Ken Bapak Tukang Coli`")
    sleep(2)
    await typew.edit("☑️ `Izzy Gaje`")
    sleep(1)
    await typew.edit("✅ `Izzy Gaje`")
    sleep(2)
    await typew.edit("✨ `Cuma Ultrmen Yang Paling Sopan, Baik Hati, Dan Tidak Sombong :v`")
# Luar Angkasa


@register(outgoing=True, pattern="^.istigfar(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Heh Kamu Gaboleh Begitu...`")
    sleep(2)
    await event.edit("`اَسْتَغْفِرُاللهَ الْعَظِيْم`")
# Istigfar


@register(outgoing=True, pattern="^.perkenalan(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`Hai Guys , Perkenalkan Nama Gw {DEFAULTUSER}`")
    sleep(2)
    await event.edit(f"`Gw Tinggal Di {WEATHER_DEFCITY}`")
    sleep(2)
    await event.edit("`Salam Kenal...`")
    sleep(2)
    await event.edit("`Udah Gitu Aja :v`")
# Perkenalan
