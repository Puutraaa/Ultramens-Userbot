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
    await typew.edit("DIEM NGENTOD!!")
# Owner @pikyus1

@bot.on(geezbot_cmd(outgoing=True, pattern='gj.(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("GAK,JANGAN MAKSA")

@bot.on(geezbot_cmd(outgoing=True, pattern='g(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("BABI LU GOBLOK!!GANTENGAN JUGA GUA HAHAHAHA")

@bot.on(geezbot_cmd(outgoing=True, pattern='c(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("BABI LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA")

@bot.on(geezbot_cmd(outgoing=True, pattern='bct(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!")

@bot.on(geezbot_cmd(outgoing=True, pattern='K(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("KONTOL UDAH ITEM BENGKOK PULA,SOSOAN MAU PAP!!")

@bot.on(geezbot_cmd(outgoing=True, pattern='a(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
sleep(1)
    await typew.edit("Ehh Lu Mau Tau Gak?")
    sleep(1)
    await typew.edit("Sih Adel Kan Mukanya Kaya Bagong😂")
    sleep(1)
    await typew.edit("Ehh Gak Bercanda Deh😁")
    sleep(1)
    await typew.edit("Emang Bener Adel Mukanya Kaya BAGONG🙈")
    sleep(1)
    await typew.edit("Ehh Engga Deh,Adel Kan Cantik Kaya Artis Korea😄")
    sleep(1)
    await typew.edit("Tapi Boong😂")
    sleep(1)
    await typew.edit("HAHAHAHAHAHAHA")
    sleep(1)
    await typew.edit("Udah Ahh Takut Adel Nangis Minta Permen😂")
    sleep(1)
    await typew.edit("Maaf Ya Adel Cantik Bercanda💖")
    sleep(1)
    await typew.edit("Tapi Bo'ong Hiyahiyahiya")
# Create by myself @localheart

CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
