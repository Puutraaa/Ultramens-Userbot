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
    await typew.edit("**Assalamualaikum.....**")
# Owner @Si_Dian


@bot.on(geezbot_cmd(outgoing=True, pattern='p(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)  
    await typew.edit("**P WR WB.....**")
# Owner @Si_Dian

@bot.on(geezbot_cmd(outgoing=True, pattern='L(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Walaikumsalam......**")
# Owner @Si_Dian


@bot.on(geezbot_cmd(outgoing=True, pattern='l(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Walaikumshalom.....**")
# Owner @Si_Dian

@bot.on(geezbot_cmd(outgoing=True, pattern='d(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIEM NGENTOD!!**")
# Owner @pikyus1

@bot.on(geezbot_cmd(outgoing=True, pattern='gjm(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK,JANGAN MAKSA**")

@bot.on(geezbot_cmd(outgoing=True, pattern='g(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!GANTENGAN JUGA GUA HAHAHAHA**")

@bot.on(geezbot_cmd(outgoing=True, pattern='c(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BABI LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA**")

@bot.on(geezbot_cmd(outgoing=True, pattern='bct(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='k(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KONTOL UDAH ITEM BENGKOK PULA,SOSOAN MAU PAP!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='f(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Kek**")
    sleep(1)
    await typew.edit("**Kek Ganteng Banget**")
    sleep(1)
    await typew.edit("**Kan Kek Mukanya Kaya Dugong🤣**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Kek Kan Ganteng Kaya Artis Korea☺️**")
    sleep(1)
    await typew.edit("**Tapi Boong🤣**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Kek Nangis Minta Pap TT🤣**")
    sleep(1)
    await typew.edit("**Pokoknya Kek Ganteng Banget**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")

@bot.on(geezbot_cmd(outgoing=True, pattern='a(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Adel**")
    sleep(1)
    await typew.edit("**Adel Cantik Banget**")
    sleep(1)
    await typew.edit("**Kan Adel Mukanya Kaya Berbi🦄**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Adel Kan Cantik Kaya Artis Korea☺️**")
    sleep(1)
    await typew.edit("**Tapi Boong🤣**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut AdelNangis Minta Permen🍬**")
    sleep(1)
    await typew.edit("**Pokoknya Adel Cantik Banget**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")

@bot.on(geezbot_cmd(outgoing=True, pattern='s(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Askar**")
    sleep(1)
    await typew.edit("**Askar Ganteng Banget**")
    sleep(1)
    await typew.edit("**Kan Askar Mukanya Kaya Monyet🐒**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Askar Kan Ganteng Kaya Artis Korea☺️**")
    sleep(1)
    await typew.edit("**Tapi Boong🤣**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Askar Nangis Minta Pap Memek**")
    sleep(1)
    await typew.edit("**Pokoknya Askar Ganteng Banget**")
    sleep(1)
    await typew.edit("**Tapi Bo'ong Hiyahiyahiya**")

@bot.on(geezbot_cmd(outgoing=True, pattern='t(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Putra**")
    sleep(1)
    await typew.edit("**Putra Ganteng Banget**")
    sleep(1)
    await typew.edit("**Kan Putra Mukanya Kaya Jerfi Nichol**")
    sleep(1)
    await typew.edit("**Ehh Engga Deh,Putra Kan Ganteng Kaya Artis Korea☺️**")
    sleep(1)
    await typew.edit("**Tapi boong 🤣**")
    sleep(1)
    await typew.edit("**HAHAHAHAHAHAHA**")
    sleep(1)
    await typew.edit("**Udah Ahh Takut Putra Nangis Minta Vps**")
    sleep(1)
    await typew.edit("**Pokoknya Putra Ganteng Banget**")
    sleep(1)
    await typew.edit("**Tapi Beneran**")

@bot.on(geezbot_cmd(outgoing=True, pattern='m(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Mandi Dulu**")

@bot.on(geezbot_cmd(outgoing=True, pattern='T(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**EH BOCAH TUA HINA, KALO TUANYA TUA AJA GOBLOK GA COCOK BOCAH TUA KAYA LU MAIN KEK GINIAN TOLOL UDAH BAU TANAH JADINYA GAUSAH BELAGU KONTOL.**")
    sleep(7)
    await typew.edit("**URUSIN AJA BEGO KUBURAN LU ITU BESOK CALON RUMAH LU SEKALI SEKALI YEKAN LU TINGGAL DIRUMAH GA DI RONGSOKAN MULU**")

@bot.on(geezbot_cmd(outgoing=True, pattern='B(?: |$)(.*)'))
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**NI YE GUA KASIH TAU SAMA LU YA BEGO LU BAKAL PUNYA ANAK CUCU LU KASIH TAU AJA KETURUNAN LU TUH KALO UDAH HINA YA HINA BEGO.**")
    sleep(6)
    await typew.edit("**GUA SARANIN JUGA LU SURUH ANAK LU NYEKOLAHIN CUCU LU BESOK BIAR PINTER GA KEK LU DONGO GOBLOK IDIOT YEKAN.ANAK LU SURUH KERJA BIAR PUNYA DUIT BIAR BISA MAKAN JANGAN BERGANTUNG SAMA BANSOS MULU.NIH YA KALO KOSA KATA MASIH NYURI DARI ORANG LAINAPA LAGI COPY PASTE GAUSAH BELAGU KONTOL.MAKANYA OTAKNYA DIPAKE TOLOL JANGAN DITARO DI DENGKUL MULU.**")
    sleep(11)
    await typew.edit("**KEBANYAKAN COLI SIH MAKANYA JADI KOPONG TUH DENGKUL ISI OTAK LU AJA CUMA DEBU SAMA SARANG LABA LABA BEGO**")
    sleep(6)
    await typew.edit("**GA USAH SO MANTEP BEGO KALO LEHER MASIH BEDAKI SELANGKANGAN BEJAMUR KONTOL NANAHAN MAKANYA KALO MANDI PAKE AIR BUKAN PAKE PASIR.**")
    sleep(6)
    await typew.edit("**GUA JAGO GA KAYA LU YG SOSOAN JADI JAGOAN KOSA KATA CUMA 1-10 TERUS DIBALIKIN 10-1 SAMA KAYA HIDUP LU MUNDAR MANDIR SANA SINI CARI PINJEMAN BUAT MAKAN SEHARI HARI YEKAN**")
    sleep(6)
    await typew.edit("**MAU SAMPE KAPAN PUN GUA BAKALAN LADENIN LU GOBLOK, LADENIN MANUSIA PURBA JELEK KEK LU GABAKALAN BERENTI GUA TOLOL NI YE GUA SARANIN MENDING LU APUS TELE DAH KONTOL.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='Y(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**ANDA TAU SEBERAPA BAIKNYA YESUS?**")
    sleep(2)
    await typew.edit("**YESUS TERAMAT TULUS SAMPAI JADI TUKANG PIJIT PLUS PLUS YANG MELAYANI UMATNYA.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='S(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**NI YE GUA KASIH TAU SAMA LU YA BEGO LU BAKAL PUNYA ANAK CUCU LU KASIH TAU AJA KETURUNAN LU TUH KALO UDAH HINA YA HINA BEGO.**")
    sleep(6)
    await typew.edit("**GUA SARANIN JUGA LU SURUH ANAK LU NYEKOLAHIN CUCU LU BESOK BIAR PINTER GA KEK LU DONGO GOBLOK IDIOT YEKAN.ANAK LU SURUH KERJA BIAR PUNYA DUIT BIAR BISA MAKAN JANGAN BERGANTUNG SAMA BANSOS MULU.NIH YA KALO KOSA KATA MASIH NYURI DARI ORANG LAINAPA LAGI COPY PASTE GAUSAH BELAGU KONTOL.MAKANYA OTAKNYA DIPAKE TOLOL JANGAN DITARO DI DENGKUL MULU.**")
    sleep(11)
    await typew.edit("**KEBANYAKAN COLI SIH MAKANYA JADI KOPONG TUH DENGKUL ISI OTAK LU AJA CUMA DEBU SAMA SARANG LABA LABA BEGO**")
    sleep(6)
    await typew.edit("**GA USAH SO MANTEP BEGO KALO LEHER MASIH BEDAKI SELANGKANGAN BEJAMUR KONTOL NANAHAN MAKANYA KALO MANDI PAKE AIR BUKAN PAKE PASIR.**")
    sleep(6)
    await typew.edit("**GUA JAGO GA KAYA LU YG SOSOAN JADI JAGOAN KOSA KATA CUMA 1-10 TERUS DIBALIKIN 10-1 SAMA KAYA HIDUP LU MUNDAR MANDIR SANA SINI CARI PINJEMAN BUAT MAKAN SEHARI HARI YEKAN**")
    sleep(6)
    await typew.edit("**MAU SAMPE KAPAN PUN GUA BAKALAN LADENIN LU GOBLOK, LADENIN MANUSIA PURBA JELEK KEK LU GABAKALAN BERENTI GUA TOLOL NI YE GUA SARANIN MENDING LU APUS TELE DAH KONTOL.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='b(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**LU TAU BUDDHA GA?**")
    sleep(3)
    await typew.edit("**ITU AGAMA ATAU APAAN SI?**")
    sleep(3)
    await typew.edit("**NYEMBAHNYA DEWA.**")
    sleep(3)
    await typew.edit("**DEWA NYA JELEK LAGI, APALAGI YANG WARNA BIRU.**")
    sleep(3)
    await typew.edit("**KEK WARNA TINTA BUAT CAP JARI AJG**")
    sleep(3)
    await typew.edit("**ANEH BANGET DAH TU AGAMA CUIHHH!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='rp(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Woy**")
    sleep(2)
    await typew.edit("**Anak erpe ya?**")
    sleep(3)
    await typew.edit("**Ngapain Sih Pake Foto Orang?**")
    sleep(3)
    await typew.edit("**Malu Ya Karena Muka Lu Burik?**")
    sleep(3)
    await typew.edit("**Daripada Mubadzir Itu Muka Mending Lu Kasih Ke Orang Yang Cari Muka.**")
    sleep(3)
    await typew.edit("**Tuhan Ciptain Lu Sesempurna Mungkin, Eh Lu Malah Mau Pake Muka Orang. Bhaaks!!!**")
    sleep(3)
    await typew.edit("**Eh Maaf Lu Kan Atheis, Jadi Gapercaya Tuhan. Makanya Tolol Kek Gini.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='Bi(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**TAU BIKSU GA?**")
    sleep(3)
    await typew.edit("**KALO GATAU GUA KASIH TAU!**")
    sleep(3)
    await typew.edit("**BIKSU ADALAH TUKANG CORET AL KITAB YANG NYEMBAHNYA SAPI**")
    sleep(3)
    await typew.edit("**BOTAK BIADAB YAHAHAHA WAHYOEEE...**")

@bot.on(geezbot_cmd(outgoing=True, pattern='N(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**HEH LU KONTOL**")
    sleep(2)
    await typew.edit("**LU KENAPA SI NGONTOL BANGET ANJING!**")
    sleep(2)
    await typew.edit("**SUMPAH LU NGONTOL BANGET KONTOLLL!**")
    sleep(2)
    await typew.edit("**DASAR LU KONTOOOOLLLL!!!**")
    sleep(2)
    await typew.edit("**KONTOLLL**")
    sleep(2)
    await typew.edit("**KONTOOOOOLLLLL!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='gj(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**YA AMPUN LU NGOMONG APA? GA NYAMBUNG KONTOL KAYA KEHIDUPAN LU MAKANYA ORG ORG KAYA LU GABAKALN MAJU HIDUPNYA APA LAGI ORG ORG BAWAHAN KAYA LU.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='S(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**SOKAP BANGET LU NAJIS ANJING GAUSAH REP REP CUIHHH!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='W(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**WAR WAR TAI ANJING!!! SOK SOK AN NANTANG WAR, EH KE TRIGGERED MINTA SHARE LOCK. PAS UDAH DI SHARE LOCK NGILANG. MENTAL KEK TAI BHAAAKSSS!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='A(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**APAAN SI LU TOLOOLLLLL!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='PP(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**PASANG PP DULU LU NGENTOT BIAR SEMUA ORANG TAU MUKA LU YANG HINA ITU CUIHHHH!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='BCT(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**BACOT BANGET LU ANJEEEENGGGG!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='ybg(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAIN AJA GOBLOK!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='GK(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**GAK KEREN LU BEGITU GOBLOK, SINI KELUARGA LU GUA LUDAHIN SATU SATU...**")

@bot.on(geezbot_cmd(outgoing=True, pattern='yhh(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**YAHAHA WAHYOOOOEEEEE**")

@bot.on(geezbot_cmd(outgoing=True, pattern='eg(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**EH GOBLOK!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='en(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**EH NGENTOTTT!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='ast(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAHALAZDIM....**")

@bot.on(geezbot_cmd(outgoing=True, pattern='X(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**GRUP SAMPAH KEK GINI MENDING BUBARIN AJA NGENTOT.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='SO(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**SOK KERAS BANGET SI JAMET INI BHAAAKSSSS.**")

@bot.on(geezbot_cmd(outgoing=True, pattern='O(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**JANGAN MAIN BOT MULU ALAY LU GOBLOK NORAK BANGET ANJING CUIHHHHH!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='D(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**HEH LU BABU, HARUS SOPAN SAMA MAJIKAN LU GOBLOK. KERJA YANG BENER BIAR MAK LU KAGAK NGELONTE LAGI BUAT KASIH MAKAN LU TOLOL!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='F(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**BHAAAAAAAAAKKKKKSSSSS**")

@bot.on(geezbot_cmd(outgoing=True, pattern='mmk(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**ASTAGAAAA MEMEKNYA ANAK INI!!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='ek(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**EH KONTOOOLL!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='ya(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**YAUDAH IYAAA SAYANG...**")

@bot.on(geezbot_cmd(outgoing=True, pattern='asn(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**ASTAGFIRULLAH NGENTOOOT!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='suci(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**LU LAMA-LAMA JADI KEK ANAK HARAM, KEKNYA HARUS GUA BAPTIS. SINI LU NGENTOT GUA BAPTIS BIAR SUCI JIWA LO YANG HARAM ITU!!!**")

@bot.on(geezbot_cmd(outgoing=True, pattern='wibu(?: |$)(.*)'))
async def typewriter(typew):
typew.pattern_match.group(1)
    await typew.edit("**LARI CUK ADA WIBU!!!**🏃🏃🏃")

CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
