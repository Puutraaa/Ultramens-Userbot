from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.sadboy(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("`Pertama-tama kamu cantik`")
    sleep(2)
    await typew.edit("`Kedua kamu manis`")
    sleep(1)
    await typew.edit("`Dan yang terakhir adalah kamu bukan jodohku`")

# Create by myself @localheart


@register(outgoing=True, pattern='^.punten(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Punten**")

# Create by myself @localheart


@register(outgoing=True, pattern='^.pantau(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n┻┳|―-∩`"
                     "`\n┳┻|     ヽ`"
                     "`\n┻┳|    ● |`"
                     "`\n┳┻|▼) _ノ`"
                     "`\n┻┳|￣  )`"
                     "`\n┳ﾐ(￣ ／`"
                     "`\n┻┳T￣|`"
                     "\n**Masih Ku Pantau**")


# Create by myself @localheart


@register(outgoing=True, pattern='^.idiot(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("\n╭╮╱╱╭╮"
                     "\n┃╰╮╭╯┃"
                     "\n╰╮╰╯╭┻━┳╮╭╮"
                     "\n╱╰╮╭┫╭╮┃┃┃┃"
                     "\n╱╱┃┃┃╰╯┃╰╯┃"
                     "\n╱╱╰╯╰━━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮"
                     "\n┃╭━╮┃"
                     "\n┃┃╱┃┣━┳━━╮"
                     "\n┃╰━╯┃╭┫┃━┫"
                     "\n┃╭━╮┃┃┃┃━┫"
                     "\n╰╯╱╰┻╯╰━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╭╮╱╱╱╭╮"
                     "\n┃╭━━╯╱┃┃╱╱╭╯╰╮"
                     "\n┃╰━━┳━╯┣┳━┻╮╭╯"
                     "\n┃╭━━┫╭╮┣┫╭╮┃┃"
                     "\n┃╰━━┫╰╯┃┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻┻━━┻━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━╮╱╭╮"
                     "\n┃┃╰╮┃┃"
                     "\n┃╭╮╰╯┣━━╮"
                     "\n┃┃╰╮┃┃╭╮┃"
                     "\n┃┃╱┃┃┃╰╯┃"
                     "\n╰╯╱╰━┻━━╯"
                     "\nㅤㅤㅤ"
                     "\n╭━━━╮╱╱╱╱╱╭╮╱╭╮"
                     "\n╰╮╭╮┃╱╱╱╱╱┃┃╭╯╰╮"
                     "\n╱┃┃┃┣━━┳╮╭┫╰┻╮╭╯"
                     "\n╱┃┃┃┃╭╮┃┃┃┃╭╮┃┃"
                     "\n╭╯╰╯┃╰╯┃╰╯┃╰╯┃╰╮"
                     "\n╰━━━┻━━┻━━┻━━┻━╯")

@register(outgoing=True, pattern="^.hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("أ‿أ")
        await e.edit("╥﹏╥")
        await e.edit("(;﹏;)")
        await e.edit("(ToT)")
        await e.edit("(┳Д┳)")
        await e.edit("(ಥ﹏ಥ)")
        await e.edit("（；へ：）")
        await e.edit("(T＿T)")
        await e.edit("（πーπ）")
        await e.edit("(Ｔ▽Ｔ)")
        await e.edit("(⋟﹏⋞)")
        await e.edit("（ｉДｉ）")
        await e.edit("(´Д⊂ヽ")
        await e.edit("(;Д;)")
        await e.edit("（>﹏<）")
        await e.edit("(TдT)")
        await e.edit("(つ﹏⊂)")
        await e.edit("༼☯﹏☯༽")
        await e.edit("(ノ﹏ヽ)")
        await e.edit("(ノAヽ)")
        await e.edit("(╥_╥)")
        await e.edit("(T⌓T)")
        await e.edit("(༎ຶ⌑༎ຶ)")
        await e.edit("(☍﹏⁰)｡")
        await e.edit("(ಥ_ʖಥ)")
        await e.edit("(つд⊂)")
        await e.edit("(≖͞_≖̥)")
        await e.edit("(இ﹏இ`｡)")
        await e.edit("༼ಢ_ಢ༽")
        await e.edit("༼ ༎ຶ ෴ ༎ຶ༽")


@register(outgoing=True, pattern="^.fak$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(".                       /¯ )")
        await e.edit(".                       /¯ )\n                      /¯  /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ ")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (")
        await e.edit(".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  ")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />❤️ *Ini Buat Kamu`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n/>💔  *Aku Ambil Lagi`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💔<\\  *Terimakasih`")



@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n />💖 *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(●_●)`"
                     "`\n💖<\\  *Tapi Bo'ong Hiyahiyahiya`")


