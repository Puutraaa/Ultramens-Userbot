from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='.mmk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGAAAA MEMEKNYA ANAK INI!!!!**")


@register(outgoing=True, pattern='.ek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**EH KONTOOOLL!!!**")


@register(outgoing=True, pattern='.ya(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAA SAYANG...**")


@register(outgoing=True, pattern='.asn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAH NGENTOOOT!!!**")


@register(outgoing=True, pattern='.suci(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LU LAMA-LAMA JADI KEK ANAK HARAM, KEKNYA HARUS GUA BAPTIS. SINI LU NGENTOT GUA BAPTIS BIAR SUCI JIWA LO YANG HARAM ITU!!!**")


@register(outgoing=True, pattern='.wi(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LARI CUK ADA WIBU!!!**🏃🏃🏃")

@register(outgoing=True, pattern='^.gjt(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("APASI NGENTOT GAJELAS LU TOLOL")

@register(outgoing=True, pattern='^.gjn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas Ngentottt")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yabenarrrrrrr...**")

@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BABI....**")


@register(outgoing=True, pattern='^.gjk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gajelas Kontolll....**")


@register(outgoing=True, pattern='^.gbgn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ga banget, Ngentott!!!**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GA, LO SANGEAN!!!**")


@register(outgoing=True, pattern='^.bsl(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BAU SAWI LO..!!**")


@register(outgoing=True, pattern='^.hai(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Hai, Anak yatim!!**")

@register(outgoing=True, pattern='^.ucp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Lu siapa si ngentooootttt!!!!**")


@register(outgoing=True, pattern='^.hey(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI BOCAH HINA!**")

@register(outgoing=True, pattern='^.mgk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAKANYA GANTENG KONTOL!**")


@register(outgoing=True, pattern='^.loh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GC SAMPAH KAYA GINI, BUBARIN AJA PLIS!!🤣**")

CMD_HELP.update({
    "salam3":
    "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.asn`\
\n↳ : Hmmm.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.mmk`\
\n↳ : Biasalah.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.suci`\
\n↳ : Baptis.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.wibu`\
\n↳ : Pake Bila Ketemu Wibu.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ek`\
\n↳ : Coba Aja Sendiri Kontol.\
\n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ya`\
\n↳ : Yasaja."
})
