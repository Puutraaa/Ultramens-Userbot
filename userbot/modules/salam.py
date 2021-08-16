from time import sleep
from platform import uname
from userbot import bot, ALIVE_NAME, CMD_HELP
from userbot.events import geezbot_cmd


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@bot.on(geezbot_cmd(outgoing=True, pattern='P(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Assalamualaikum.....`")
# Owner @Si_Dian


@bot.on(geezbot_cmd(outgoing=True, pattern='p(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)  
    await typew.edit("`P WR WB.....`")
# Owner @Si_Dian

@bot.on(geezbot_cmd(outgoing=True, pattern='L(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Walaikumsalam......`")
# Owner @Si_Dian


@bot.on(geezbot_cmd(outgoing=True, pattern='l(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Walaikumshalom.....`")
# Owner @Si_Dian

@bot.on(geezbot_cmd(outgoing=True, pattern='d(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("DIEM,NGENTOD GW LAGI COLI")
# Owner @pikyus1
CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
