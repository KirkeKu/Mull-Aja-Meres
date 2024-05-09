define config.name = ("Mull aja meres")
define fade = Fade(0.4, 0.0, 0.4)
define fastdissolve = Dissolve(0.2)
init python:
    renpy.music.register_channel("mar", "music")
#Tegelased ja nimesildid
define ai = Character("Aisling", color="#FCED8F")
define gl = Character("Glass", color="#333333")
define ca = Character("Carina", color="#e35567")
define ir = Character("Irene", color="#69D9CD")
define xy = Character("Xiao Yun", color="#548643")
define pov = Character("[player_name]", color="#FFFFFF")
define op = Character("Õpetaja", color="#EFBC89")
define kt = Character("Abiline", color="#EFBC89")

define spriteSize = 0.26

#Spraidid ja suurused
image ai neutral = im.FactorScale("aisling_neutral.png", spriteSize)
image ai happy = im.FactorScale("aisling_happy.png", spriteSize)
image gl neutral = im.FactorScale("glass_neutral.png", spriteSize)
image gl sigh = im.FactorScale("glass_sigh.png", spriteSize)
image gl happy = im.FactorScale("glass_happy.png", spriteSize)
image ir neutral = im.FactorScale("irene_neutral.png", spriteSize)
image ir happy = im.FactorScale("irene_happy.png", spriteSize)
image ir sigh = im.FactorScale("irene_sigh.png", spriteSize)
image xy neutral = im.FactorScale("xiao_neutral.png", spriteSize)
image xy happy = im.FactorScale("xiao_happy.png", spriteSize)
image xy sigh = im.FactorScale("xiao_sigh.png", spriteSize)
image ca neutral = im.FactorScale("carina_neutral.png", spriteSize)
image ca sigh = im.FactorScale("carina_sigh.png", spriteSize)
image ca happy = im.FactorScale("carina_happy.png", spriteSize)

#Taustad
image bg classroom = "bg classroom.jpg"
image bg must = "bg must.jpg"
image bg clubroom = "bg clubroom.jpg"
image bg hallway = "bg hallway.jpg"
image bg bedroomn = "bg bedroomn.jpg"
image bg trepid = "bg trepid.jpg"
image bg sookla = "bg sookla.jpg"
image bg livin = "bg livin.jpg"
image bg mets = "bg mets.png"
image bg soo = "bg soo.jpg"
image bg tanav = "bg tanav.jpg"
image bg kohvik = "bg kohvik.jpg"
image bg park = "bg park.jpg"
image bg muusika = im.FactorScale("bg muusika.jpg", 0.5)
image bg library = im.FactorScale("bg library.jpg", 0.5)

#Positsioonid
transform midleft:
    xalign 0.27 yalign 1.0
transform midright:
    xalign 0.73 yalign 1.0
transform jumper:
    ease .04 yoffset -24
    ease .04 yoffset -20
    ease .03 yoffset -16
    ease .02 yoffset -12
    ease .01 yoffset -8
    ease .01 yoffset -4
    ease .01 yoffset 0

#Globaalsed muutujad
init:
     $ aisling = 0
     $ glass = 0
     $ xiaoyun = 0
     $ carina = 0
     $ irene = 0
     $ showstats = False
     $ minigame = 0


########################################## GAME START ######################################
label start:
    #Muusika start
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0

#Mängija nime muutujana salvestamine
    $ player_name = renpy.input("Mis saab olema su nimi?", length=14)
    $ player_name = player_name.strip()
    if not player_name:
        $ player_name = "Mängija"

    scene bg classroom
#Esimene stseen
#Narratsioon
    "Aknast välja vaadates sa näed päikest eredalt säramas."
    "Sa näed linde lendamas üle taeva. Üks varblane maandub aknalaua peale ja vaatab sulle otsa."
    "Sa naeratad talle ja kogu maailm tundub korraga olevat rahulik."
#Tegelaste nimelühendid
    op"[player_name]? [player_name]!"
    pov"Ah, jah, kohal!"
    "Õpetaja vaatab sinu poole ja noogutab kiiresti. Kool alles algas ja tundub, et ta tahab juba koju minna."
    pov"(Väga hea algus päevale [player_name], väga hea.)"
    "Sa vaatad jälle aknast välja, poole kõrvaga kuulates, mida õpetaja räägib."
    op" Olgu, siis vist on kõik kohal. Nii klass, ma selgitan teile paar asja nüüd üle."
    op"Esiteks, ma tuletan meelde nendele, kes seda veel teinud pole, klubidesse registreerimine on juba alanud."
    op"Seega palun valige endale midagi meelepärast. Ütlen ka veel üle, et klubis olemine ja kaasa tegemine annab sulle lõpueksamites lisa punkte, mis võib mõnel kasuks tulla."
    pov"(Ah, õigus, klubid. Need on asjad. Peaks endale ühe leidma, lihtsalt igaksjuhuks. Aga milline oleks parim?)"
    "Neid mõtteid mõlkudes istusid sa tunni lõpuni."

#Stseeni muutus, taustapildiks koridor.
    scene bg hallway
    with fade

    pov"(Mul pole vähimatki aimu kuhu minna.)"
    "Sa kõnnid mööda koridore, vaatad klassidesse sisse ja proovid välja mõelda, milline nendest klubidest oleks piisavalt huvitav, et sa poole aasta pealt ära ei läheks."
    pov"(Olgu, mis on minu valikud?)"

#Menüü valikute kadumine
    $ robootika = True
    $ aiandus = True
    $ keemia = True
label klubid:

    menu:
        "(Olgu, mis on minu valikud?)"
        "Robootikaring" if robootika == True:
            pov"Meil on robootikaring, kuid see tundub nagu liiga palju matemaatilist mõtlemist ja mu aju ei taha selle peale isegi mõelda."
            $ robootika = False
            jump klubid
        "Aianduse klubi" if aiandus == True:
            pov"Aianduse klubi nägi huvitav välja, aga ma hea meelega ei saaks räpaseks mitu korda nädalas ainult selleks, et ilusaid lilli vaadata."
            $ aiandus = False
            jump klubid
        "Keemia klubi" if keemia == True:
            pov"Keemia klubis saaks midagi lõbusat teha, samas mõned inimesed on ilmselt seal ainult selleks, et plahvatusi näha ja see muutuks esimese nädalaga tüütuks."
            $ keemia = False
            jump klubid

    pov"(Kui vaid oleks siin koolis klubi, mis laseks inimestel lihtsalt rahulikus keskkonnas oma loovust väljendada-)"

    "Sa peatud ukse ees mille küljes on väga värviliselt joonistatud silt. Selle peal on kirjas \“Loovuse klubi!\”"
    pov"(Ah. Lahe. See oli lihtne.)"

    scene bg clubroom
    with fade

    "Sa astud tuppa sisse ja näed kolme inimest."
    "Üks istub akna ääres ja kirjutab midagi märkmikusse. Teised kaks räägivad üksteisega, kuni üks nendest, tal olid ilusad punased juuksed, näeb sind ja kõnnib su juurde."

#Spraidi ilmumine
    show ca happy at midleft with dissolve
    ca"Tere, tule edasi!"
    "Ta haarab su käest kinni ja tõmbab su klassi ette."
    show ca neutral at jumper with dissolve
    ca"Tere tulemast loovuse klubisse. Mina olen Carina, olen ka klubi president."
    show ir neutral at midright with dissolve
    "Ta osutab tüdruku poole, kellega ta enne rääkis."
    ca" See on meie asepresident Irene."
    show ir happy with dissolve
    ir"Tere tulemast!"
    hide ir happy with dissolve
    ca"Ja see seal…"
    "Ta osutab nüüd istuvale isikule."
    show xy neutral at midright with dissolve
    ca"On Xiao Yun."
    show xy happy with fastdissolve
    "Xiao vaatab üles, naeratab ja lehvitab. Carina vaatab uuesti sulle otsa."
    hide xy happy  with dissolve
    ca"Ja sina oled?"
    #Mängija peab ise vajutama nuppu ekraanil, et vastata ja dialoogi jätkata. Siin kasutatakse ka muutuja põhjal mängija sisestatud nime.
    menu:
        "Mina olen [player_name].":
            pov"Mina olen [player_name]."
    #Esimene valik, mis punkte annab.
    ca"Meeldiv tutvuda, [player_name]. Väike küsimus, mida mul paluti küsida kõikidelt klubi huvilistelt. Miks sa siia tulla tahad?"
    menu:
        "Miks sa siia tulla tahad?"

        "Loovuse arendamine":
            pov" Ma arvan, et see klubi aitaks mul oma loovust arendada ja teiste kunstide kohta õppida."
            show ca happy
            "Carina naeratab laialt."
            #Carina punktisummale lisatakse 3
            $ carina += 3
            #Tekib teavitus
            $ renpy.notify('Teenisid Carinaga 3 sõpruspunkti')
            #Muutuja jätab siin tehtud valiku meelde ja selle põhjal muutub ka dialoog tulevikus.
            $ irenedialoog1 = 1
            ca"See on väga hea vastus! Peaks selle igaks juhuks meelde jätma."
        "Esimene huvitav klubi":
            pov"See oli esimene huvitav klubi, mis ette tuli."
            $ carina += 1
            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')
            $ irenedialoog1 = 2
            "Carina noogutab."
            ca"Tore teada, et meie idee on huvitav."
            "Irene kergitab ühe kulmu."
            ir"Vähemalt see töötab."
        "Punktide saamine":
            pov"Ausalt öeldes on see enamasti nende eksamite punktide pärast."
            "Carina vaatab sulle otsa paar hetke liiga kaua."
            ca"Noh, vähemalt oled aus."
            "Irene turtsatab."
            ir"Heagi see, et kohale tulid."
            $ irenedialoog1 = 3

    show gl neutral at midright with dissolve
    "Hetk hiljem sa kuuled, kuidas keegi vaikselt ukse avab. Sisse astub üks poiss, kes noogutab ja istub ühe laua äärde maha. Carina mõtleb hetke ja kõnnib tema juurde."
    show ca happy at jumper with dissolve
    ca"Tere tulemast loovuse klubisse! Mina olen president Carina. See on asepresident Irene."
    #Irene sprait tekib ja Carina sprait kaob ekraanilt samaaegselt.
    show ir neutral at midleft
    hide ca happy
    with fastdissolve
    "Irene lehvitab uustulnukale."
    #Irene sprait kaob samaaegselt Carina spraidi uuesti ilmumisega.
    hide ir neutral
    show ca happy at jumper
    with fastdissolve
    ca"Ja need on Xiao ja [player_name]. Mis sinu nimi on?"
    "Tumedate juustega poiss vaatab korraks ringi."
    gl"Glass."
    show ca neutral with dissolve
    "Carina ootab hetke ja saab siis aru, et ei saa temalt enam sõnagi."
    ca"Meeldiv kohtuda, Glass. Kui ma võin küsida, miks sa meie klubiga liituda tahad?"
    "Glass on paar sekundit vait. Sul on tunne, et niimoodi ta räägib kõigiga."
    gl"Ma loodan leida inimesi, kellele meeldib loominguline meedia."
    show ca happy  with dissolve
    "Carina naeratab."
    ca"Siis sa oled tulnud õigesse kohta. See ongi meie peamine plaan."
    hide gl neutral with dissolve
    "Sa kuuled koridoris lähenevaid jooksu samme. Järsku avaneb uks ja üks tüdruk astub hingeldades sisse."

    show ai neutral at midright with fastdissolve
    show ai neutral at jumper
    "Tere. Palun vabandust kui ma hilinen. Üks õpetaja peatas mu."
    show ca neutral  with dissolve
    "Carina, kes oli natuke ehmunud, kõnnib tema ette."
    ca"Eh, ei, sa ei ole hilinenud. Em, tere tulemast loovuse klubisse! Mina olen president Carina."
    #Tihe spraitide vahetamine
    hide ai neutral with fastdissolve
    show ir neutral at midright with fastdissolve
    "Irene astub sammu ette."
    ir"Ma olen Irene, asepresident."
    hide ir neutral with fastdissolve
    show ai neutral at midright with fastdissolve
    ca"Ja need…"
    "Carina näitab käega kõigi poole."
    show ca neutral at left
    show xy neutral
    show gl neutral at midleft
    with fastdissolve
    ca"on Xiao, Glass ja [player_name]."
    hide xy neutral
    hide gl neutral
    with fastdissolve
    show ca neutral at midleft
    show ai happy at midright
    with fastdissolve
    ai"Tere! Mina olen Aisling. Olen siin, et leida uusi sõpru ja õppida teistest loovkunstidest."
    ca"Olgu, aitäh. Ootame veel äkki viis minutit ja kui keegi veel tuleb siis vaatame."
    hide ca neutral
    hide ai happy
    with dissolve
    "Viis minutit mööduvad peaaegu vaikuses."
    "Carina ja Irene räägivad üksteisega mingisugusest ülesandest, Glass pani mingil hetkel kõrvaklapid pähe ja kuulab nüüd muusikat."
    "Xiao kirjutab midagi oma märkmikusse ja Aisling proovib oma hingamist korda saada. Tundub, et ta tõesti jooksis siia."

    show ca neutral at midleft with dissolve
    ca"Olgu, nii. Kõik istuge korraks maha, et ma saaks teile selgitada selle klubi plaane."
    "Carina läheb klassi ette seisma, Irene tema kõrval. Sina ja Aisling, kes olid ainukesed seisjad, istute maha."
    show ca neutral at jumper
    ca"Nii, siis \“Loovuse klubi\” esimene ja peamine idee on erinevate loominguliste kunstide näitamine, õpetamine ja läbi tegemine."
    ca"Praegu on meie plaan selline, kuna meie tunnid teisipäeviti ja reedeti, siis see nädal me teeme lihtsalt väikese kohtumise ja plaani paika panemise nädala."
    ca"Kuid pärast seda, me mõtlesime, et iga tund võiks olla keegi, kes tutvustab oma huvi ja näitab ülejäänutele kuidas seda teostada või midagi."
    ca"Kas see oleks teie arvates tehtav?"
    "Klass on korraks vaikne. Aisling on esimene, kes räägib."
    show ai neutral at midright with fastdissolve
    ai"Ma arvan, et see võib väga tore olla."
    hide ai neutral with fastdissolve
    "Sina, Glass ja Xiao kõik noogutate. "
    show ca happy
    show ir happy at midright
    with fastdissolve
    "Carina ja Irene naeravad kergendatult."
    ir" Väga tore. Kuna tänane plaan oli vaid klubi leida, siis me lasemeid teil kohe minna. Enne aga peame me teid kõiki kirja panema."
    show ir neutral
    "Irene võtab oma kotist paberilehe ja annab selle Xiao kätte, kes oli talle kõige lähemal. Kõik istujad kirjutavad oma nime paberile ja sina, kes olid viimane, annad selle Irene kätte tagasi."
    show ca happy at jumper
    ca"Olgu. Aitäh teile kõigile, et otsustasite liituda \“Loovuse klubiga\”! Kohtume reedel!"
    "Kõik tõusid püsti ja lahkusid klassist, Carina ja Irene jäid klassi. Ilmselt mingi presidentide asi."
    hide ir neutral
    hide ca happy
    with dissolve
    pov"(See oli tore. Ma loodan, et see klubi on seda väärt.)"

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

label tutorial:
    #Sissejuhatus mälumängu
    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    menu:
        "Mis on klubi nimi?"
        "Loovuse klubi":
            #Õige vastus
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti! Näed, said isegi punkti selle eest."

        "Kunsti klubi":
            #vale vastus
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli 'Loovuse klubi'!"

        "Hängimise klass":
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli 'Loovuse klubi'!"

    centered"Mis täna veel juhtus?"
    menu:
        "Mis on punaste juustega tüdruku nimi?"
        "Xiao Yun":
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli Carina!"

        "Carina":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti! Tundub, et nägusid ja nimesid sa tunned."

        "Irene":
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli Carina!"

    centered"Olgu, tundub, et sa saad juba aru, kuidas see väike mäng töötab."
    centered"Siin on kolmas küsimus!"
    menu:
        "Kes tuli kõige hiljem?"
        "Glass":
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli Aisling!"

        "Sina":
            $ renpy.notify('Vale vastus')
            centered"Näed, ongi vaja korrata. Valesti mäletasid. Õige vastus oli Aisling!"

        "Aisling":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti! Mälu on sul hea."

    centered"Vinge, saidki kõik vastatud!"
    centered"Kui sa kõik kolm detaili õigesti mäletasid, saad sa võimaluse õhtul ühele klubikaaslasele helistada!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    #Tulemuste näitamine
    centered"{size=*2}Õigesti: [minigame]{/size}"
    #Skoori lugemine
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            #Iga tegelase unikaalne dialoog telefonile vastamisel
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."
    #Hetkese punktiskoori näitamine
    call screen display_stats

#Teine päev
label day2:
    scene bg must
    with fade
    centered"{size=*2}Reede, esimene klubipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg classroom
    with fade
    "Sa istud oma päeva viimases tunnis ja ootad, et see lõppeks."
    "Tavaliselt sa ootaksid praegu koju minemist, aga täna on esimene ametlik klubipäev, nii et pead veel sellega tegelema."
    "Sa hakkad korraks õpetaja igava juttu pärast uinuma. Õnneks kella helin päästab sind päris magama jäämisest. "
    scene bg clubroom
    with fade
    "Sa astud klassi sisse ja näed teisi juba istumas ja vestlemas."
    show ir neutral at midright
    show ca neutral at midleft
    with fastdissolve
    "Irene ja Carina arutavad mingite paberite üle, võib-olla presidenti kohustused."
    hide ir neutral
    hide ca neutral
    with fastdissolve
    show ai neutral at midleft
    show xy neutral at midright
    with fastdissolve
    show ai neutral at jumper
    "Aisling räägib Xiaole oma päevast ja teine kuulab teda viisakalt."
    hide ai neutral
    hide xy neutral
    with fastdissolve
    show gl neutral at midright
    "Sa istud Glassi kõrvale, kes kuulab muusikat."
    gl"Hommik."
    pov"Pärastlõuna tegelikult."
    "Glass vaatab sind imelikult."
    gl"Ok..."
    hide gl neutral with fastdissolve
    "Carina ja Irene seisavad jälle klassi ees. "
    show ir neutral at midright
    show ca neutral at midleft
    with fastdissolve

    ca"Tere jälle. Tänane plaan on siis panna paika järjekord meie huvide tutvustamisest ja siis natuke põhjalikum tutvumine ka üksteisega."
    ir"Tore oleks teada saada, kellega me iga teisipäev ja reede kokku peame saama."
    ca"Täpselt. Nii siis, järjekord. Ma arvan, et kõige parem oleks, kui mina ja Irene alustama, et teie kõik saaksite enda korra jaoks paremini aru, mida teha."
    show ir neutral at jumper
    ir"Ma võin kõige esimesena teha. Mul läheb ettevalmistus kiirelt."
    "Carina võtab oma kotist ühe paberi ja paneb midagi sinna kirja."
    show ca neutral at jumper
    ca"Ma lähen siis teisena. Kas keegi läheb vabatahtlikult kolmandana?"
    hide ir neutral
    show ai neutral at midright
    with fastdissolve
    "Aisling tõstab käe."
    ai"Ma võin, tundub lõbus."
    "Carina kirjutab selle oma paberile."
    hide ai neutral with fastdissolve
    ca"Kes tahab peale Aislingi minna?"
    show xy neutral at midright with fastdissolve
    xy"Ma läheks."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    gl"Ma tahaks pärast teda minna."
    "Carina paneb selle kirja."
    hide gl neutral with fastdissolve
    ca"Siis on [player_name] viimane. Kas sobib?"
    pov"(Ah.)"
    pov"Em, jah sobib, aga mul pole tegelikult sellist nagu hobi, mida ma saaksin näidata."
    "Carina mõtleb paar hetke. Enne kui ta rääkima saab hakata, Aisling võtab sõna."
    show ai neutral at midright with fastdissolve
    ai"Sa võiksid meie tundidest kokkuvõte teha. Me saaks sulle vajalikku infot anda ja siis pärast vaatame koos üle kõike, mida teinud oleme."
    "Carina noogutab."
    show ca neutral at jumper
    ca"Ma arvan, et see on aus. Mida sa arvad, [player_name]?"
    menu:
        ca"Mida sa arvad, [player_name]?"

        "Väga hea idee.":
            pov"Ma arvan, et see on väga hea idee. Mulle meeldiks seda teha."
            show ca happy
            show ai happy
            with fastdissolve
            "Carina, Irene ja Aisling naeravad selle peale. Xiao ja Glass noogutavad."
            show ca happy at jumper
            ca"Väga tore"
            hide ai happy with fastdissolve

        "Ma ei tea...":
            pov"Ma ei tea. See kõlab väga keeruliselt."
            hide ai neutral
            show ir neutral at midright
            with fastdissolve
            ir" Sa saad hakkama. Pluss oleks see ebaaus kui kõik teevad midagi ja sina ainult kuulad pealt."
            pov"Seda küll. Ma teen selle ära."
            hide ir neutral with fastdissolve

        "Mulle ei meeldi.":
            pov"Mulle ei meeldi see idee. Ma ei viitsi seda teha."
            hide ai neutral
            show ca unhappy
            show ir unhappy at midright
            with fastdissolve
            "Irene jõllitab sind kurjalt. Aisling ja Carina näevad kurvad välja. Xiao ja Glass ei liiguta."
            ir"Noh kurb. Sa teed selle ära."
            hide ir unhappy with fastdissolve

    show ca neutral with fastdissolve
    ca"Igatahes, nüüd kui see on tehtud ma usun, et nüüd oleks aeg igaühega kohtuda. Võtame äkki paaridesse ja ma olen välja mõelnud paar küsimust millele vastata."
    ca"Esiteks: Millega sa tegeled või mis on sinu hobid?"
    ca"Teiseks: Kust sa pärit oled?"
    ca"Ja kolmandaks: Miks sa siia klubisse tulla tahtsid?"
    hide ca neutral with fastdissolve
    pov"(Kellega ma peaks esimesena rääkima?)"
#Viiest valikust saab valida ainult 3
    $ menuchoices = 0
    $ cad1 = True
    $ ird1 = True
    $ aid1 = True
    $ xyd1 = True
    $ gld1 = True
label day1:
    if menuchoices == 3:
        jump day1end
    else:
        menu:
            "(Kellega ma peaks rääkima?)"

            "Carina" if cad1 == True:
                pov"(Carina on klubi president, temaga võiks rääkida küll.)"
                show ca neutral with fastdissolve
                "Carina istub õpetaja laua taha ja näeb kuidas sa lähened. Sa võtad endale ühe tooli ja istud ta kõrvale."
                ca"Tere jälle, [player_name]! Ma olen väga õnnelik, et saame lähemalt kohtuda. Sa võid mult esimesena küsimusi küsida."
                $ hobi = True
                $ parit = True
                $ klubi = True
                label carinaday1:
                    menu:
                        "Millega sa tegeled/Mis on sinu hobid?" if hobi == True:
                            pov"Mis sinu hobiks siis on?"
                            ca"Ma tegelen cosplayga. Teen kostüüme tegelastest."
                            pov"Ise teed?"
                            show ca happy at jumper
                            ca"Ikka. Noh, neid saab juba valmis kujul osta ka, aga mulle meeldib ise meistertada."
                            pov "Äge."
                            show ca neutral with fastdissolve
                            $ hobi = False
                            $ carina += 1
                            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')
                            jump carinaday1

                        "Kust sa pärit oled?" if parit == True:
                            pov"Kust sa siis tulnud oled?"
                            show ca neutral at jumper
                            ca"Norrast kolisin siia. Koos perega ikka."
                            pov"Tore teada."
                            $ parit = False
                            $ carina += 1
                            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')
                            jump carinaday1

                        "Miks sa klubi asutasid?" if klubi == True:
                            pov"Miks sa selle klubi siis üldse ette võtsid?"
                            ca"Ma tahtsin oma vanematele tõestada, et sarnaste huvidega inimesi on veel ja et ma pole üksi."
                            pov"Ah, arusaadav."
                            $ klubi = False
                            $ carina += 1
                            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')
                            jump carinaday1
                    ca"Ma usun, et nüüd on minu kord küsida."
                    "Carina küsib sinult küsimusi ja kuulab su vastuseid tähelepanelikult. Ta noogutab, siis kui lõpetad. "
                    ca"See on päris huvitav. Mul on hea meel, et liitusid mu klubiga. See on tähtis meile."
                    pov"Sina ja Irene alustasite selle, eks? Kas ma võin küsida miks?"
                    "Carina vaatab sind hetke, mõtleb ja vastab:"
                    ca"Noh, jällegi, ma tahtsin teisi inimesi kohata, kellel on minuga samad huvid. Kuid tegelikult ka lihtsalt, et Irene-ga aega veeta."
                    ca"Me oleme päris head sõbrad. Igatahes, meil on vaja veel teistega rääkida."
                    pov"Õigus. Oli tore jutustada."
                    show ca happy with fastdissolve
                    ca"Sinuga ka!"
                    hide ca happy with fastdissolve
                    $ cad1 = False
                    $ menuchoices += 1
                    jump day1

            "Irene" if ird1 == True:
                pov"(Irene tundus lõbus olevat, ma räägin temaga.)"
                show ir neutral with fastdissolve
                "Irene toetub seinale ühe akna juures. Sa seisad tema kõrvale ja toetud läheval olevale lauale."
                ir"Hei. Tore sind jälle näha."
                if irenedialoog1 == 1:
                    ir"Carina ütles mulle, et oled siin, et oma loovust arendada. Sinu õnneks on see mingis mõttes selle klubi üleüldine mõte."
                    pov"Ma loodaks küll. Miks muide selline nimi, eks?"
                    ir"Mhm."
                elif irenedialoog1 == 2:
                    ir"Sa vist ütlesid esimesel päeval, et meie klubi oli esimene, mis oli tegelikult huvitav? Aitäh, vist."
                    pov"Palun?"
                else:
                    ir"Sa oled siin, et punkte saada? Ausus on hea asi, aga tegelt sa pead ka tegelikult üritama, et need punktid kätte saada."
                    pov"Jah, muidugi. Kui siin olla siis vähemalt võiks lõbus olla. Ma luban, et üritan."
                    ir"Väga hea."
                $ hobi = True
                $ parit = True
                $ klubi = True
                label ireneday1:
                    menu:
                        #Veel üks näide vastusevariantide kadumisest
                        "Millega sa tegeled/Mis on sinu hobid?" if hobi == True:
                            pov"Mis sinu hobiks siis on?"
                            ir"Programmeerin ise mänge ja muid asju. Enamus inimesi arvab, et see on jube keeruline, aga see on sama nagu uue keele õppimine."
                            pov"Kuidas uue keele?"
                            ir"Arvutite keele. Programmeerimise keele. Kui sa seda piisavalt vahid, õpid lõpuks lugema ka."
                            pov"Naljakas viis sellest mõelda, aga samas kõlab täitsa ägedalt."
                            show ir happy at jumper
                            ir"Onju?"
                            show ir neutral with fastdissolve
                            $ hobi = False
                            $ irene += 1
                            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')
                            jump ireneday1

                        "Kust sa pärit oled?" if parit == True:
                            pov"Kust sa siis tulnud oled?"
                            ir"Tulin Ameerikast koos oma isaga, ema töötab ikka Ameerikas."
                            show ir happy at jumper
                            ir"Suvel saame tal külas käia."
                            pov"Kuidas seal Ameerikas siis oli?"
                            show ir neutral with fastdissolve
                            ir"Soe. Liiga soe, isegi. Mulle meeldib Eesti kliima rohkem."
                            $ parit = False
                            $ irene += 1
                            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')
                            jump ireneday1

                        "Miks sa klubiga liitusid?" if klubi == True:
                            pov"Miks sa selle klubi siis üldse ette võtsid?"
                            ir"Otsin teisi arvutimängude ja programmeerimise huvilisi. Neid on üllatavalt raske niisama leida."
                            pov"Usun."
                            $ klubi = False
                            $ irene += 1
                            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')
                            jump ireneday1
                    ir"Ma küsin siis sinult ka. "
                    "Irene küsib sinult samu küsimusi ja sa vastad nendele."
                    ir"Mm, lahe. Aitäh jälle, et otsustasid klubiga liituda. Alati on hea kui on inimesi."
                    pov"Aitäh, et selle klubi tegite. Sina ja Carina sobite hästi presidentidena. Vähemalt minu arvates."
                    "Irene naeratab iseendale."
                    hide ir neutral with fastdissolve
                    $ ird1 = False
                    $ menuchoices += 1
                    jump day1

            "Aisling" if aid1 == True:
                pov"(Mulle tundus, et Aisling on energiline. Ta võib huvitav olla.)"
                show ai happy with fastdissolve
                "Aisling istub uksele kõige lähemal pingil ja ümiseb endamisi. Ta näeb, kuidas sa tema kõrvale maha istub ja naeratab."
                ai"Tere! Sa oled [player_name], eks? Ma nägin sind esimesel päeval. Mäletad mind?"
                pov"Jah, vist. Sa jäid hiljaks, kui ma õigesti mäletan."
                "Aisling naerab närviliselt."
                ai"Haha, jah, see oli mina. Üks õpetaja tahtis minuga rääkida. Mingisugune kunstikonkurss."
                show ai happy at jumper
                ai"Kas ma võin sinult esimesena küsida? Ma olen elevil ja tahan kõigi kohta teadmisi saada."
                pov"Jah, võid ikka."
                "Aisling küsib sinult küsimusi, vahepeal ta küsib ka täpsustavaid küsimusi."
                ai"Okei, sinu kord!"
                $ hobi = True
                $ parit = True
                $ klubi = True
                label aislingday1:
                    menu:
                        "Millega sa tegeled/Mis on sinu hobid?" if hobi == True:
                            pov"Mis sinu hobiks siis on?"
                            show ai happy with fastdissolve
                            ai"Mulle meeldib kunst! Tegelen joonistamisega ja vahel maalin ka."
                            pov"Kõlab uhkelt."
                            show ai neutral with fastdissolve
                            $ hobi = False
                            $ aisling += 1
                            $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
                            jump aislingday1

                        "Kust sa pärit oled?" if parit == True:
                            pov"Kust sa siis tulnud oled?"
                            show ai neutral with fastdissolve
                            ai"Kolisin paar aastat tagasi oma perega Eestisse, enne seda hüppasime Portugali ja Iirimaa vahet."
                            pov"Hüppasite Portugali ja Iirimaa vahet?"
                            ai"Nojah. Meil oli mõlemas riigis kodu olemas seega me käisime kahe vahet koguaeg."
                            ai"Mu vanemad töötavad kodust, seega neil pole vahet kus nad on."
                            pov"Hmm. Kõlab täitsa hästi."
                            show ai happy at jumper
                            ai"Nõus!"
                            $ parit = False
                            $ aisling += 1
                            $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
                            jump aislingday1

                        "Miks sa klubiga liitusid?" if klubi == True:
                            pov"Miks sa selle klubiga üldse liitusid?"
                            ai"Tahtsin teiste hobidega ka tutvuda ja uusi sõpru leida."
                            ai"Ma arvan, et seni vist isegi tuleb välja."
                            ai"Kõik on jube toredad. Peale Glassi, võib-olla."
                            ai"Ta on jube vaikne. Aga ma saan aru, ega kõik ei saagi kogu aeg lobiseda."
                            $ klubi = False
                            $ aisling += 1
                            $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
                            jump aislingday1
                    ai"Igatahes, nüüd on küsitud. Sinuga oli väga tore tutvuda!"
                    ai"Räägime teine kord jälle!"
                    pov"Muidugi."
                    hide ai happy with fastdissolve
                    $ aid1 = False
                    $ menuchoices += 1
                    jump day1

            "Xiao Yun" if xyd1 == True:
                pov" (Xiao Yun oli teisipäeval üks esimesi kohal. Äkki räägin temaga.)"
                show xy neutral with fastdissolve
                "Xiao istub ühe akna kõrval ja vaatab sellest välja. Ta käsi on märkmiku peal, nagu ta tahaks midagi kirjutada. Sa istud tema kõrvale pingile."
                pov"Tere."
                xy"Tere. [player_name], eks? Me kohtusime teisipäeval."
                pov"Seda tõesti. Ma küsin sinult siis need küsimused."
                xy"Lase aga käia."
                $ hobi = True
                $ parit = True
                $ klubi = True
                label xiaoyunday1:
                    menu:
                        "Millega sa tegeled/Mis on sinu hobid?" if hobi == True:
                            pov"Millega sa vabal ajal siis tegeled?"
                            xy"Ma luuletan vahel. Loen ka."
                            pov"Kas sa teed riimiga luuletusi või haikusid, või mis?"
                            show xy happy with fastdissolve
                            xy"Natuke kõike. Vahepeal proovin teisi stiile ikka ka."
                            show xy neutral with fastdissolve
                            $ hobi = False
                            $ xiaoyun += 1
                            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
                            jump xiaoyunday1

                        "Kust sa pärit oled?" if parit == True:
                            pov"Kust sa siis tulnud oled?"
                            xy"Tulin ise Hiinast siia. Hangzhou Shi linnast. See on Shanghaile üpris lähedal, tegelikult."
                            xy"Tahtsin veidi rahulikumalt kirjandust õppida. Siin on seda akadeemilist survet palju vähem."
                            pov"Akadeemilist survet?"
                            show xy neutral at jumper
                            xy"Jah. Tead kuidas enne eksamit on kõigil närv sees, sest nad ei taha läbi kukkuda?"
                            xy"Kujuta ette seda, aga iga päev."
                            pov"See... ei kõla väga lõbusalt jah."
                            xy"Jah."
                            $ parit = False
                            $ xiaoyun += 1
                            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
                            jump xiaoyunday1

                        "Miks sa klubiga liitusid?" if klubi == True:
                            pov"Miks sa selle klubiga üldse liitusid?"
                            xy"Ausalt öeldes tahtsin lihtsalt vaikset kohta, kus lugeda ja õppida."
                            pov"Sellepärast ainult?"
                            xy"Veidi jabur, ma tean, aga vähemalt on aus vastus."
                            pov"Seda küll."
                            show xy neutral with fastdissolve
                            $ klubi = False
                            $ xiaoyun += 1
                            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
                            jump xiaoyunday1
                    xy"See on kõik? Ma küsin siis sinult."
                    "Xiao küsib sinult küsimusi, samal ajal heidab vahepeal pilku õue. "
                    pov"Sulle meeldib õue vaatada?"
                    "Xiao vaatab sinu poole."
                    xy"Ma saan loodusest inspiratsiooni. Need puude lehed on väga ilusad."
                    pov"Seda küll. Kas me saame sinu tunnis kuulda mõnda sinu luuletust?"
                    xy"Vaatame."
                    hide xy neutral with fastdissolve
                    $ xyd1 = False
                    $ menuchoices += 1
                    jump day1

            "Glass" if gld1 == True:
                pov"(Mulle tundub, et Glass pole väga sõnade inimene. Vaatme, mida ma temalt saan.)"
                show gl neutral with fastdissolve
                "Glass istub klassi taga nurgas ja tundub olevat omas maailmas. Sa istud ta kõrvale."
                pov"Tere."
                "Glass vaatab sinu poole"
                gl"Tere."
                pov"..."
                "Paar hetke möödub vaikuses. Sina alustad rääkimist."
                $ hobi = True
                $ parit = True
                $ klubi = True
                label glassday1:
                    menu:
                        "Millega sa tegeled/Mis on sinu hobid?" if hobi == True:
                            pov"Mis sinu hobiks siis on?"
                            gl"Ma mängin klaverit."
                            gl"Vahel kuulan muusikat ka."
                            pov"(Kõrvaklappide järgi arvaks, et rohkem kui ainult vahel.)"
                            $ hobi = False
                            $ glass += 1
                            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
                            jump glassday1

                        "Kust sa pärit oled?" if parit == True:
                            pov"Kust sa siis tulnud oled?"
                            gl"Taist. Vanemad kolisid siia ja võtsid minu ka kaasa."
                            "Rohkem Glass ei selgita."
                            $ parit = False
                            $ glass += 1
                            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
                            jump glassday1

                        "Miks sa klubiga liitusid?" if klubi == True:
                            pov"Miks sa selle klubiga üldse liitusid?"
                            gl"Sa eelmine kord juba kuulsid vist, aga ma otsin sarnaste huvidega inimesi."
                            pov"Siis kui Carina küsis? Jah, ma kuulsin."
                            "Glass ei vasta sulle."
                            $ klubi = False
                            $ glass += 1
                            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
                            jump glassday1
                    "Paar hetke läheb jälle vaikuses mööda."
                    gl"Õigus, ma pean ka küsima."
                    "Glass küsib sinult küsimusi, sa vastad. Pärast seda on kõik jälle vaikne. Sa kuuled kuidas teised üksteisega rääkivad."
                    gl"Hei."
                    "Sa vaatad tema poole. Ta annab sulle enda telefoni ja paneb endale kõvaklapid pähe."
                    gl"Pane mingi laul peale."
                    "Sa paned esimese laulu, mis sul meelde tuleb."
                    gl"Lahe."
                    hide gl neutral with fastdissolve
                    $ gld1 = False
                    $ menuchoices += 1
                    jump day1

label day1end:
    show ca neutral with dissolve
    "Carina seisab uuesti klassi ees."
    ca"Olgu, me vist rohkem täna ei jõua. Aitäh kõigile, et tulite. Kohtume järgmine nädal."
    hide ca neutral with fastdissolve
    "Sa ütled kõigile head aega ja kõnnid koju. Järgmine nädal hakkavad huvide tutvustused."
    pov"See saab lõbus olema."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    $ minigame = 0
    if xyd1 == False:
        menu:
            "Kust Xiao pärit on?"
            "Taist":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli Hiinast!"

            "Hiinast":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"

            "Jaapanist":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli Hiinast!"
    elif ird1 == False:
        menu:
            "Kust Irene pärit on?"
            "Norrast":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli Ameerika Ühendriikidest!"

            "Ameerika Ühendriikidest":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"

            "Prantsusmaalt":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli Ameerika Ühendriikidest!"

    else:
        menu:
            "Mis on Glassi hobiks?"
            "Programmeerimine":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli muusika!"

            "Muusika kuulamine ja koostamine":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"

            "Joonistamine ja kunst":
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli muusika!"

    centered"Mis täna veel juhtus?"
    menu:
        "Kes esimesena oma hobi tutvustab?"
        "Irene":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Carina":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

        "Xiao":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Mis on sinu kohustus hobitunni asemel?"
        "Ei pea midagi tegema":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli teha kokkuvõte klubi tegevustest!"

        "Aidata koristada":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli teha kokkuvõte klubi tegevustest!"

        "Teha kokkuvõte klubi tegevustest":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."
    call screen display_stats

#Kolmas päev
label day3:
    scene bg must
    with fade
    centered"{size=*2}Teisipäev, Irene hobipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg hallway
    with fade
    show xy neutral at midright with fastdissolve
    "Teisipäeval peale tunde lähened sa klubiruumile ja märkad Xiao Yuni ukse taga ootamas."
    "Ta seisab niisama akna ääres ja vaatab oma telefoni."
    pov"Hei. Mis teed?"
    xy"Hei. Irene viskas mind välja. Ütles, et ta tahab ettevalmistusi teha või midagi."
    pov"Õigus jah, täna pidi tema ju rääkima meile."
    #Vastus oleneb mängija varasemast valikust
    if ird1 == False:
        pov"Ta tegeleb programmeerimise ja videomängude tegemisega, onju?"
        pov"Tundub veidi keeruline, ausalt."
        xy"Veidi hirmus jah. Ma ei tea arvutitest suurt midagi."
    else:
        pov"Millega ta üldse tegeleb?"
        xy" Ta teeb videomänge. Programmeerimine ja värki. Tundub jube keeruline."
        pov"Tundub lahe ka."
        xy"Seda küll."

    xy"Igal juhul, Irene teab mida ta teeb. Ma arvan, et see tuleb huvitav tund."
    pov"Nõus."
    "Te jääte mõlemad vait. Xiao vaatab aknast välja. Sina vaatad hoopis koridoris ringi ja märkad Aislingi, kes just trepist üles jõudis."
    show ai happy at midleft with fastdissolve
    ai"Oi, tsau! Kuidas läheb? Mis te nädalavahetusel tegite? Miks te klassi ei lähe?"
    show ai neutral with fastdissolve
    xy"Irene teeb mingeid ettevalmistusi. Me ei tahtnud segada."
    ai"Aaaa, okei. Arusaadav. Kaua te siin oodanud olete?"
    pov"Ainult mõne minuti."
    xy"Umbes kümme."
    ai"Siis ei ole väga kaua. Kas Glass on ka juba kohal? Carina ilmselt on koos Irenega, sest ta on president ja värki."
    xy"Ma ei näinud Glassi, seega ta ilmselt tuleb alles."
    ai"Ahsoo."
    "Te seisate niisama, nüüd kolmekesi, ja vahite ringi. Ei lähe väga kaua, enne kui Glass ka sõnatult kohale jõuab."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    "Ta noogutab teile ja toetab vastu seina."
    ai"Tervist, Glass! Kuidas su nädalavahetus oli?"
    show gl neutral at jumper
    gl"..."
    gl"Tore."
    show ai neutral at jumper
    ai"Tore kuulda!"
    "Aisling ei jõua Glassi kaua küsitleda, sest Irene avab klassiukse ja kutsub teid sisse."
    scene bg clubroom
    with fade
    show ir neutral
    "Kõik istuvad laudade taha. Irene jääb klassi ette, kus projektor näitab tema arvutiekraani tahvlile."
    show ir happy at jumper
    ir"Hästi. Mina siis räägin täna veidi programmeerimisest!"
    ir"Carina hankis meile raamatukogust lauuaarvutid, et te saaksite kõik ka proovida."
    ir" Ma tean, et osad arvavad, et programmeerimine on jube raske ja segadust tekitav. Ja kui niisama koodi vahtida, siis on see tõsi."
    show ir neutral at jumper
    ir"Aga me teeme selle täna veidi lihtsamaks."
    ir"Ma leidsin ühe veebilehe, mis on tehtud programmeerimise õppimiseks. Seega täna me teeme kõik oma väikese mängu!"
    "Irene kirjutab veebilehe aadressi tahvlile. Kõik trükivad selle arvutites sisse."
    "Leht näeb väga lihtne välja. Ekraani vasakus küljes on tühi kast ja paremas on mänguekraan."
    ir"Kood koosneb nii-öelda “klotsidest,” mida saab omavahel kokku panna et erinevaid asju teha. Teil peaks vasakus küljes olema üks väike riba värviliste klotsidega."
    ir"Otsige sealt üles \“kui start\” klots. Peaks olema kollast värvi."
    ir"Kõik, mis sellele tükile järgneb, juhtub peale start nupu vajutamist. Nüüd on meil vaja tegelast ja selle jaoks on vaja spraiti. "
    ir"Te saate kõik otsida mingisuguse pildi oma mängu tegelaseks. Lihtsalt arvestage, et ta oleks piisavalt väike."
#Mängija valikust oleneb dialoog ja mälumängu õige vastus
    menu:
        "Kelle sa enda tegelaseks tahad valida?"

        "Kassi":
            "Sa valid oma tegelaseks hüppava kassi pildi."
            $ tegelane = "kass"
        "Koera":
            "Sa valid oma tegelaseks jooksva koera pildi."
            $ tegelane = "koer"
        "Linnu":
            "Sa valid oma tegelaseks lendava linnu pildi."
            $ tegelane = "lind"

    ir"Ma teen kiire ringi, ja näitan kustkohast te saate tegelase spraidi koodi sisestada. Oodake hetk."
    hide ir neutral with fastdissolve
    "Samal ajal, kui Irene ringi jalutab ja kõigepealt Carina juures peatub, tuleb Aisling sinuga jutustama."
    show ai happy at midleft with fastdissolve
    ai"Millise spraidi sa valisid? Mul on koer. Vaata! Ta näeb välja täpselt, nagu mu vanaisa koer!"
    "Aislingi ekraaanil seisab pisike kuldne retriiver."
    pov"Nunnu."
    if tegelane == "koer":
        pov"Ma valisin ka koera. Aga minu oma on lihtsalt suvaline."
        show ai happy at jumper
        ai"Jess! Ühtekad oleme."
        $ aisling += 1
        $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
    elif tegelane == "kass":
        pov"Mul oli hoopis kass."
        show gl neutral at midright with fastdissolve
        "Glass toetub kõrvallauast sinu poole."
        gl"Nunnu kass. Mul on ka."
        "Glassi ekraanil on näha musta kassi roheliste silmadega."
        $ glass += 1
        $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
        hide gl neutral with fastdissolve
    else:
        pov"Mul oli hoopis lind."
        show xy neutral at midright with fastdissolve
        "Xiao, kes istub sinu ees, toetab küünarnuki su lauale."
        xy"Mul oli ka lind. "
        xy"Kanaarilind, kui täpne olla."
        pov"Väga eredat värvi."
        xy"Nad käivadki nii."
        hide cy neutral with fastdissolve
        $ xiaoyun += 1
        $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
    "Sa pöördud enda arvuti poole tagasi."
    hide ai happy
    show ir neutral at midright
    with fastdissolve
    "Irene jõuab ringiga sinu juurde ja näitab sulle ekraanil õige koha kätte."
    "Tunni lõpuks on kõigil õnnestunud kokku panna lihtne väike mäng, kus tegelane hüppab ekraanil üle takistuste."
    show ir happy at jumper
    ir"Näete! Saitegi kõik hakkama."
    show ir neutral
    show xy happy at midleft
    with fastdissolve
    xy"See ei olnudki nii hirmus, kui ma arvasin."
    hide xy happy
    show gl happy at midleft
    with fastdissolve
    "Glass mõmiseb niisama, kuid ta tundub rahul olevat."
    hide gl happy
    show ca happy at midleft
    with fastdissolve
    ca"See oli tore, Irene! Suur tänu!"
    show ir happy at jumper
    ir"Suur tänu sulle selle võimaluse eest!"
    hide ca happy
    show ir neutral
    with fastdissolve
    ir"Nüüd kui te olete mängu tegemist proovida saanud, kas te tahaks ühte ka mängida?"
    ir"Mul on üks poolik projekt, mis tahaks tagasisidet."
    show ai happy at midleft with fastdissolve
    ai"Muidugi!"
    hide ai happy
    show ca neutral at midleft
    with fastdissolve
    ca"Ikka. Milline mäng see on?"
    ir"Väike 2D RPG."
    pov"RPG?"
    ir"{i}Roleplay game.{/i} Rollimäng. Tegelane on ette antud ja sa mängid temana. Mul on tehtud terve maailm, mida saab avastada, kus võidelda, inimestega rääkida!"
    ir"Või noh. NPC-dega rääkida. Nad on programmeeritud dialoogiga, seega nad kordavad lihtsalt sama asja lõpuks."
    hide ca neutral
    show xy neutral at midleft
    with fastdissolve
    xy"Kõlab täitsa ägedalt. Prooviks hea meelega."
    show ir happy at jumper
    ir"Super!"
    hide xy neutral
    show ir neutral
    with fastdissolve
    "Irene otsib arvutis õiget faili ja paneb mängu käima."
    "Ekraanile ilmub väike haldjalaadne tegelane mõõgaga. Taustal mängib rahulik muusika, mis meenutab sulle metsa vihmasajus."
    ir"Olgu, [player_name], tule proovi sina esimesena. Ma tean, et Aisling tahab ilmselt niisama ringi jalutada ja Carina tahab inimestega rääkida."
    show ai neutral at midleft with fastdissolve
    ai"Kust sa teadsid?"
    ir"Sa rääkisid minuga eile peale tunde, mäletad? Küsisid soovitusi?"
    ai"Ahjaa. See läks mul meelest ära."
    hide ai neutral with fastdissolve
    "Sa klikkad läbi algmenüü ja leiad oma tegelase külas seisvat."
    "Ümbrus on pikslites joonistatud ja üpris detailne."
    "Sa jalutad veidi ringi ja avastad metsatuka. Metsas on väikesed ämblikud, kes sind ründama hakkavad."
    pov"Mis nupuga ma neid tagasi ründan, Irene?"
    ir"Hiireklõpsuga."
    "Sa klõpsad paar korda hiirt, ekraanil olev haldjas vehib oma mõõgaga ja varsti pole ekraanil enam ühtegi ämblikku."
    menu:
        "Mis sa mängust arvad?"

        "Väga detailne ja ilus mäng on.":
            pov"Ümbrus ja spraidid on kõik nii detailsed. Kas sa tegid need ise?"
            ir"Ikka ise, kuidas siis veel. Carina aitas ideedega veidi tegelikult. Aga spraidid tegin ma ise."
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')

        "Täitsa lõbus on.":
            pov"See on täitsa lõbus. Ma võiksingi siia avastama jääda."
            show ca neutral at midleft with fastdissolve
            ca"Ära praegu vist jää, me tahame ka proovida."
            ir"Ma saan teile kõigile valmis mängu saata kui soovite."
            pov"Ikka."
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')
            hide ca neutral with fastdissolve

        "Kui kaua selle tegemine aega võttis?":
            pov" Kui kaua kõige selle tegemine sul aega võttis?"
            show ir sigh with fastdissolve
            ir" Liiga kaua. Sa ei taha teada. Mõnikord läheb mitu tundi, et ühe menüü pikslid täpselt õigesse kohta paika saada."
            show ir neutral
            show gl neutral at midleft
            with fastdissolve
            gl"See kõlab karmilt."
            ir"See ongi veidi, aga lõpptulemus on minu arvates seda väärt."
            hide gl neutral
            show ca happy at midleft
            with fastdissolve
            ca"Nõus! See on äge!"
            hide ca happy with fastdissolve
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')

    pov"Igal juhul muljetavaldav."
    show xy neutral at midleft with fastdissolve
    xy"Nõus."
    hide xy neutral
    show ai happy at midleft
    with fastdissolve
    ai"On jah! Jube lahe! Ma tahan ka nüüd proovida!"
    show ai neutral with fastdissolve
    ir"Tule proovi siis. [player_name], vaheta Aislingiga kohad ära?"
    pov"Ikka."
    "Aisling jooksis mängus ringi ja sai kaks ringi surma, enne kui ta arvuti Carinale üle andis"
    hide ai neutral
    show ca neutral at midleft
    with fastdissolve
    "Carina avastas mängus menüüsid ja tal õnnestus leida koodiviga, mis lubas mängijal läbi seinte joosta. Irene lubas selle ära parandada."
    hide ca neutral
    show gl neutral at midleft
    with fastdissolve
    "Glass jooksis otsekohe võitlusesse ja tal õnnestus leida miniboss, mille ta ka maha murdis. Ise ta ei kommenteerinud, aga tundus, et tal oli lõbus."
    hide gl neutral
    show xy neutral at midleft
    with fastdissolve
    "Xiao Yun vaatas niisama metsas ringi ja leidis tiigi, kus kala püüda. Irene selgitas samal ajal, kuidas erinevate kalade leidmise võimalusi koodis kirjutada."
    hide xy neutral with fastdissolve
    "Lõpus küsib Irene kokkuvõtvat tagasisidet."
    show ir neutral at jumper
    ir"Olgu, saite kõik proovida. Mis te arvasite?"
    #Mitme punktiarvuga valik
    menu:
        "Anna Irenele mängu kohta tagasisidet."

        "Üli vinge.":
            pov"Üli vinge mäng on. On näha, et palju aega ja vaeva on sinna sisse läinud. Suur tänu, et meil seda mängida lasid."
            show ir happy at jumper
            ir"Hea meelega! Tore, et teile meeldis!"
            $ irene += 3
            $ renpy.notify('Teenisid Irenega 3 sõpruspunkti')

        "Raske vigu leida.":
            pov"Jube raske on vigu leida. Hästi tehtud!"
            show ir neutral at jumper
            ir"Suur tänu! Muidugi on vigade leidmine ka hea. See tähendab, et ma saan need ära parandada!"
            $ irene += 2
            $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

        "Näen, kuhu sa sellega sihid.":
            pov"See pole just maailmaklassil mäng, aga ma näen kuhu sa sellega sihid."
            ir"Tänan. Ma olen jah suurtest mängustuudiotest väga kaugel, aga ma üritan õppida ja end parandada!"
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')

    show ca neutral at midleft
    ca"Sa oled aastatega ikka kaugele jõudnud. Ma mäletan, kui sa alles Pythoni õppima hakkasid!"
    show ir neutral at jumper
    ir"Head ajad. Kõik peavad kusagilt ju alustama."
    hide ca neutral
    show gl neutral at midleft
    with fastdissolve
    gl"Võitluse süsteem on hea. Bossi HP on tasakaalus ja rünnakumustrid on mõnusa vahega."
    hide gl neutral
    show ai sigh at midleft
    with fastdissolve
    ai"Ma ei saanud üldse võitlemisest aru, aga see on ilmselt mu enda süü."
    ai"Ma ajasin kogu aeg nuppe sassi."
    show ir neutral at jumper
    ir"Tore teada. Suur tänu tagasiside eest!"
    hide ai sigh
    show xy neutral at midleft
    with fastdissolve
    xy"Mulle meeldis. Kui tahad, siis on rahulik kalapüüdmine ja jalutamine. Ja kui tahad, siis on mängitav eepika. Vinge."
    ir"Suur aitäh teile kõigile. Ma üritan uueks aastaks mängu valmis saada, siis saate ehk uuesti proovida ja kogu mängu läbi mängida."
    hide xy neutral
    show ca happy at midleft
    with fastdissolve
    ca"Hea meelega!"
    hide ir neutral
    show gl neutral at midright
    with fastdissolve
    gl"Ikka."
    hide ca happy
    show ai neutral at midleft
    with fastdissolve
    ai"Kas ma tohin oma õele ka proovida anda? Ma tean, et talle meeldivad sellised keskaegsed mängud ja fantaasialood."
    hide gl neutral
    show ir neutral at midright
    with fastdissolve
    ir"Keelama ma sind ei hakka. Nautigu!"
    show ai happy at jumper
    ai"Suur tänu!"
    "Tundub, et kõik on tunniga rahul ja natuke targemad."
    "Sa otsustad kiiresti grupi heast tujust pildi klõpsata."
    "Saad sellest ja teistest tulevastest piltidest teha fotoalbumi klubi tegevustest."
    hide ai happy with fastdissolve
    "Glass aitab Carinal arvutid tagasi raamatukokku viia."
    "Xiao Yun vabandab end ja jookseb bussi peale."
    "Sina ja Irene kõnnite koos garderoobi ja sätite sammud kodu poole."
    hide ir neutral with dissolve

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada, mis kõik täna juhtus."
    $ minigame = 0
    menu:
        "Kellega su mängusprait sarnane oli?"
        "Aisling":
            if tegelane == "koer":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"
            else:
                $ renpy.notify('Vale vastus')
                if tegelane == "kass":
                    centered"Valesti mäletasid. Õige vastus oli Glass!"
                else:
                    centered"Valesti mäletasid. Õige vastus oli Xiao!"

        "Xiao":
            if tegelane == "lind":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"
            else:
                $ renpy.notify('Vale vastus')
                if tegelane == "koer":
                    centered"Valesti mäletasid. Õige vastus oli Aisling!"
                else:
                    centered"Valesti mäletasid. Õige vastus oli Glass!"

        "Glass":
            if tegelane == "kass":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"
            else:
                $ renpy.notify('Vale vastus')
                if tegelane == "koer":
                    centered"Valesti mäletasid. Õige vastus oli Aisling!"
                else:
                    centered"Valesti mäletasid. Õige vastus oli Xiao!"

    centered"Mis täna veel juhtus?"
    menu:
        "Kes ajab kogu aeg nuppe sassi?"
        "Aisling":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Carina":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

        "Xiao":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Millise koodivea Carina avastas?"
        "Läbi seinte jooksmise":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Topelthüppe":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli läbi seinte jooksmise!"

        "Surematuse":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli läbi seinte jooksmise!"

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas su lle Irene mäng meeldis?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."


    call screen display_stats

#Neljas päev
label day4:
    scene bg must
    with fade
    centered"{size=*2}Reede, Carina hobipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg hallway
    with fade
    "Sa kõnnid pärast tunde klubi klassiruumi poole."
    "Seekord pole kedagi väljas istumas. "
    scene bg clubroom
    with fade
    "Sa astud sisse ja näed, et keegi on toa keskele pannud kõik lauad üheks suureks lauaks, selle ümber mõned toolid klubi liikmetele."
    "Laua peal on igasuguseid värvilisi materjale. Puuvillast ja siidist kangas, mingisugune traat, papp ja paar parukat."
    show ca neutral at midright
    show ai neutral at midleft
    with fastdissolve
    "Carina võtab oma kotist veel kangast välja ja annab selle Aislingile, kes paneb selle lauale teiste juurde."
    "Aisling näeb sind esimesena."
    show ai neutral at jumper
    ai"Hei, [player_name]! Vaata, kui palju asju meil täna vaja läheb! See on kõik nii ilus!"
    "Carina märkab ka nüüd sind. Ta paneb lauale kääre, liimipulki ja teisi asju, mis võivad kasulikud olla."
    ca"Need on mu paremad materjalid. Ma usun, et need on muljetavaldavamad."
    pov"Need näevad välja päris kallid. Kas me peaksime hiljem sulle nende eest maksma?"
    ca"Ei, ei, ei! Muidugi mitte! Mul polnud raske neid saada, kõik on korras."
    hide ai neutral
    show gl neutral at midleft
    with fastdissolve
    gl"Tore, sest ma ei taha teada, kui palju see mu rahakotile haiget teeks."
    show ca neutral at jumper
    "Carina hüppab üllatusest. Aisling vaatab üllatunud sinu taha. Sa keerad ringi ja näed Glassi, kes tuli vaikselt klassi sisse."
    "Glass noogutab oma tervitust ja istub laua taha maha."
    hide gl neutral
    hide ca neutral
    show ir neutral at midright
    show xy neutral at midleft
    with fastdissolve
    "Irene kõnnib sisse, Xiao tema järel. Irene tõstab üles ühe purgi sädelust ja vaatab seda paar hetke."
    ir"Kas kõik asjad peavad niimoodi sädelema?"
    hide xy neutral
    show ai neutral at midleft
    with fastdissolve
    ai" Mulle meeldib! Need näevad välja nagu tähed."
    hide ir neutral
    hide ai neutral
    show ca neutral
    with fastdissolve
    ca"Olgu, nüüd kui kõik on kohal, palun istuge."
    "Sa istud ühe traadijupi ette, Irene sinu paremal, Glass vasakul."
    ca" Nii, enne ma räägin natuke teooriat ja siis ma annan teile ülesande. "
    ca"{i}Cosplay{/i} on, kui seda lihtsalt panna, viis kuidas inimesed saavad ennast väljendada oma lemmikute tegelaste abil. "
    show ca neutral at jumper
    ca"{i}Cosplay{/i} on ka väga üksteisest sõltuv, ühte asja ei saa teha teiseta. See võib ka olla päris keeruline, aga neid osi me ei puuduta täna."
    ca"Näiteks parukate stiilimine võtab palju aega, ning volangide õmblemine on mõnede arust piin."
    ca"Aga mulle need meeldivad. Sellised korduvad tegevused on teraapilised mulle."
    ca"Igatahes, ma olen vist piisavalt palju lobisenud. Nüüd siis see ülesanne. "
    "Carina võtab oma kotist välja ühe nuku ja näitab seda teile."
    show ca neutral at jumper
    ca" Kuna meil pole aega üht tegeliku kostüümi teha, siis me teeme lihtsalt väiksema mahuga selle."
    ca" Ma olen lipikute peale kirjutanud kaks riideeset, mõlemat kaks tükki. Sinu paarilised on need, kellel on sinuga sama ese."
    ca"Ning see riideese on ka see, mille te koos valmistate. Mina olen selles gruppis, kus on üks inimene puudu."
    "Carina võtab õpetaja laualt ühe keraamilise kausi. Ta paneb selle laua keskele."
    menu:
        "Sa vaatad kausi sisse ja võtad välja…"
        "???":
            jump sark
        "???":
            jump seelik
        "???":
            jump sark
        "???":
            jump seelik

label sark:
    "Sa avad lipiku ja näed seal kirjas sõna \“Särk\”."
    $ nukk = "sark"
    show ai neutral at midleft with fastdissolve
    ai"Ma sain seeliku!"
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    xy"Mina ka."
    hide ai neutral
    show ir neutral at midleft
    with fastdissolve
    ir"Mul on kirjas särk."
    pov"Sama siin."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    "Glass lihtsalt noogutab."
    hide gl neutral
    hide ir neutral
    show ca neutral
    with fastdissolve
    ca"Mina siis aitan Aislingi ja Xiaod. Siin on meie juhendid."
    "Carina annab sulle paberi, kuhu on peale kirjutatud sammud, mida tegema peab."
    ca"Kui teil on küsimusi, siis ma hea meelega vastan!"
    hide ca neutral
    show ir neutral at midleft
    show gl neutral at midright
    with fastdissolve
    "Te hakkate tööle. Esimene asi, mida on vaja teha, on kangas valida."
    "Irene võtab kangaste hunnikust ilusa tume punase kanga. Glass valib ühe heledama sinise. "
    gl"Ma arvan, et see oleks parim."
    "Irene vaatab sinist kangast."
    ir"Mulle meeldib minu punane rohkem."
    "Glass heidab pilgu Irene valitud kanga poole ja kergitab kulmu. Glass vaatab sulle otsa."
    gl"Sina vali."
    menu:
        "Mis värvi kangast särgi jaoks kasutada?"
        "Punane":
            pov"Punane läheb rohkemate värvidega kokku. Me ei tea, mis värvi teised enda seeliku teevad ja ma julgen oletada, et nukul on ka erinevad aksessuaarid."
            show ir happy with fastdissolve
            "Irene naeratab võidukalt, Glass noogutab."
            show ir neutral with fastdissolve
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')
        "Sinine":
            pov"Sinine on ilusam sellel nukul. Läheb tema silmadega kokku."
            show gl happy with fastdissolve
            "Glass muigab, Irene kortsutab kulmu."
            ir"Kui sa nii arvad."
            show gl neutral with fastdissolve
            $ glass += 1
            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
        "Midagi muud":
            "Sa vaatad kangaid lähemalt ja tõmbad välja ühe roosaka kanga."
            pov"Tavaliselt on nukkudel sellised riided. Tundub, et on ohutu värv."
            "Glass noogutab."
            ir"Olgu. Miks ka mitte?"

    "Edasi läheb koostöö teil sujuvalt. Te võtate nuku mõõtmeid, mõõtate välja õige pikkusega ja laiusega kanga ning liimite peale mõned väikesed lilled."
    ir" Nii, nüüd peab ainult kokku õmblema mõlemad pooled."
    gl"Väga täpne töö. Ma hea meelega ei teeks seda."
    jump omblemine

label seelik:
    "Sa avad lipiku ja näed seal kirjas sõna \“seelik\”."
    $ nukk = "seelik"
    show ai neutral at midleft with fastdissolve
    ai"Ma sain seeliku!"
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    xy"Mina ka."
    hide ai neutral
    show ir neutral at midleft
    with fastdissolve
    ir"Mul on kirjas särk."
    pov"Ma sain ka seeliku."
    hide ir neutral
    show ai neutral at midleft
    with fastdissolve
    "Sa tõused ja istud Xiao ja Aislingi juurde."
    hide ai neutral
    hide xy neutral
    show ca neutral
    with fastdissolve
    ca"Mina siis aitan Irene'i ja Glassi. Siin on meie juhendid."
    "Carina annab sulle paberi, kuhu on peale kirjutatud sammud, mida tegema peab. "
    ca"Kui teil on küsimusi, siis ma hea meelega vastan!"
    hide ca neutral
    show ai neutral at midleft
    show xy neutral at midright
    with fastdissolve
    "Te hakkate tööle. Esimene asi, mida on vaja teha, on kangas valida."
    "Aisling võtab oma kätte sädeleva hõbeda kanga. Xiao katsub mattmusta kangast."
    ai"Mulle meeldib see. Paistab silma."
    xy"Ma arvan, et tagasihoidlikum on parem."
    ai"[player_name], mida sina arvad?"
    menu:
        "Mis värvi kangast seeliku jaoks kasutada?"
        "Hõbedane":
            pov"Hõbedane on tõesti ilus. Kui see oleks võistlus, siis me kindlasti võidaksime mingi auhinna."
            show ai happy at jumper with fastdissolve
            "Aisling naeratab ja hüppab enda kohal rõõmsalt. Xiao vaatab järgmisi samme."
            show ai neutral with fastdissolve
            $ aisling += 1
            $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
        "Must":
            pov"Must on hea värv. See läheb vist kõigega kokku."
            show xy happy with fastdissolve
            "Xiao noogutab ja tõstab kanga teie poole."
            "Aisling ikkagi naeratab."
            show xy neutral with fastdissolve
            $ xiaoyun += 1
            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
        "Midagi muud":
            "Sa vaatad kangaid lähemalt ja tõmbad välja ühe valge kanga."
            pov"Valge on lihtne ja puhas. Tundub, et on ohutu värv."
            "Aisling noogutab. Xiao kehitab õlgu."

    "Edasi läheb koostöö teil sujuvalt. Te võtate nuku mõõtmeid, mõõtate välja õige pikkusega ja laiusega kanga ning Aisling joonistab peale paar joont, lihtsalt, et lahedam välja näeks."
    xy"Viimane asi on selle kokku õmblemine."
    ai"Mul on päris täpsed käed, aga ma pole midagi sellist teinud, nii et ma ei tea."
    jump omblemine

label omblemine:
    pov"Ma võin seda teha. Ei tundu nii raske."
    "Ah, kui vale see on. Mitu korda lähevad sinu õmblused ebaühtlaseks ja sa pead seda lahti harutama. Pärast 10 minutit seda piina tuleb Carina sinu juurde."
    hide ir neutral
    hide gl neutral
    hide ai neutral
    hide xy neutral
    show ca neutral
    with fastdissolve
    ca"Oota, las ma näitan sulle kuidas seda teha."
    "Carina võtab su käest nõela ja hoiab seda ning kangast sinu ees."
    ca"Näed, sa paned selle niimoodi läbi ja siis niimoodi välja, siis on see tugev."
    menu:
        "Kas sa tead ka teisi õmbluseid?":
            pov"Kas sa tead veel teisi õmbluseid? See tundub päris tülikas."
            ca"Ei ole tegelikult. Erinevaid õmblusi on palju. Ma ei tea selle eestikeelset nime, aga minu lemmik on \“{i}Lazy daisy{i}\” õmblus."
            ca"Nagu nimigi ütleb, see näeb välja nagu väike lill. Väga armas minu meelest."
            pov"On tõesti armas."
            "Carina naeratab."
            $ carina += 3
            $ renpy.notify('Teenisid Carinaga 3 sõpruspunkti')
        "Näita korra veel.":
            pov"Kas sa näitaksid ühe korra veel? Ma tahan seda õigesti teha."
            ca"Jah muidugi. Vaata."
            "Carina demonstreerib õmblust korra veel."
            ca"Said aru?"
            pov"Jah, aitäh."
            ca"Alati valmis aitama."
            $ carina += 2
            $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')
        "Sain aru.":
            pov"Ma vist sain aru. Aitäh."
            ca"Ah, olgu."
            $ carina += 1
            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')

    hide ca neutral

    if nukk == "sark":
        show ir neutral at midleft
        show gl neutral at midright
        with dissolve
        "Sa lõpetad särgi kokku õmblemise ja näitad teistele."
        show ir happy at jumper
        ir"Uuu, see on ilus."
        show gl happy with fastdissolve
        gl"Täiega."
        hide ir happy
        hide gl happy
        show ca neutral
        with fastdissolve
        ca"Teil seal ka valmis?"
        pov"Jah, Carina."
        ca"Tooge siis siia."
        "Te viite oma särgi teise grupi juurde ja Carina pane selle nukule selga. Teine grupp tegi valge tennise seeliku, mis läks teie särgiga ilusti kokku."
        hide ca neutral

    else:
        show ai neutral at midleft
        show xy neutral at midright
        with dissolve
        "Sa lõpetad seeliku kokku õmblemise ja näitad teistele."
        show ai happy at jumper
        ai"Aahhh, see on nii ilus!"
        show xy happy with fastdissolve
        xy"Hästi õmmeldud."
        hide ai happy
        hide xy happy
        show ca neutral
        with fastdissolve
        ca"Teil seal ka valmis?"
        show ai neutral at left with fastdissolve
        ai"Jah, Carina."
        hide ai neutral with fastdissolve
        ca"Tooge siis siia."
        "Te viite oma seeliku teise grupi juurde ja Carina pane selle nukule selga. Teine grupp tegi roosaka särgi, mis läks teie seelikuga ilusti kokku."
        hide ca neutral


    show ai neutral at midleft
    with fastdissolve
    ai"Vaata, kui ilus! Me tegime täitsa head tööd!"
    show ir neutral at midright with fastdissolve
    ir"Kuidagi jah. Päris hästi tehtud."
    "Glass ja Xiao Yun noogutavad."
    hide ai neutral
    hide ir neutral
    show ca neutral
    with fastdissolve
    ca"Ma panen paar viimast asja talle selga ja siis on tehtud."
    "Carina võtab oma kotist välja väikese musta kardigani ja samasugused tennised ning paneb need nukule selga ja jalga."
    show ca happy at jumper
    ca"Ma arvan, et see on üks parimad nuku riietusi, mida olen näinud."
    "Kõik noogutavad talle. Carina vaatab kella."
    show ca neutral with fastdissolve
    ca"Siin me peame kahjuks lõpetama. Aitäh, et seda minuga tegite."
    hide ca neutral
    show ai happy at midleft
    with fastdissolve
    ai"See oli väga lõbus!"
    show xy neutral at midright with fastdissolve
    xy"Aitäh, et jagasid oma huvi."
    hide ai happy
    show ir neutral at midleft
    with fastdissolve
    ir"Ma teadsin, et see tuleb huvitav."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    gl"Mõnus oli."
    pov"Jah, väga tore."
    hide gl neutral
    hide ir neutral
    with fastdissolve
    "Te aitate Carinal oma asjad uuesti ära pakkida ja lahkute koolimajast."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    $ minigame = 0
    menu:
        "Mis värvi oli teise grupi riideese?"
        "Valge":
            if nukk == "sark":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"
            else:
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli roosa!"


        "Sinine":
                $ renpy.notify('Vale vastus')
                if nukk == "seelik":
                    centered"Valesti mäletasid. Õige vastus oli roosa!"
                else:
                    centered"Valesti mäletasid. Õige vastus oli valge!"

        "Roosa":
            if nukk == "seelik":
                $ minigame += 1
                $ renpy.notify('Õige vastus')
                centered"Mäletasid õigesti!"
            else:
                $ renpy.notify('Vale vastus')
                centered"Valesti mäletasid. Õige vastus oli valge!"

    centered"Mis täna veel juhtus?"
    menu:
        "Kes küsis: \"Kas kõik asjad peavad niimoodi sädelema\"?"
        "Irene":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Carina":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

        "Glass":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Irene!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Mis täpselt on Carina hobi?"
        "Õmblemine":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli cosplay!"

        "Nukkude tegemine":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli cosplay!"

        "Cosplay":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas sulle Carina nukk meeldis?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."


    call screen display_stats

#Viies päev
label day5:
    scene bg must
    with fade
    centered"{size=*2}Teisipäev, Aislingi hobipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg hallway
    with fade
    "Koridoris istudes ootad sa lõunavahetunni lõppu."
    "Tavaliselt käiksid sa kiiresti õues jalutamas, aga täna sajab vihma, seega sa otsustasid toas püsida ja nüüd on sul aega üle."
    "Paar klassikaaslast liituvad sinuga pingil. Te olete kõik telefonides."
    "Järsku märkad sa tuttavat nägu sinu poole tormavat."
    show ai neutral with fastdissolve
    ai"[player_name]! Siin sa oled! On sul aega veidi?"
    pov"Ikka on, vahetunni lõpuni on ju veel kümme minutit."
    ai"Super. Mul on veidi abi vaja kastide tõstmisega, saad sa tulla?"
    pov"Muidugi. Sinu järel?"
    "Aisling naeratab ja kõnnib treppide suunas. Sa järgned talle."

    show bg trepid
    with fade
    "Te jõuate lõpuks garderoobi, kus Aisling tõstab maast ühe kingakarbi."
    ai"Need ei ole väga rasked, aga ma ei tahtnud kolm ringi kolmandale korrusele ka joosta."
    pov"Mis siin sees on?"
    "Aisling naeratab salakavalalt."
    show ai happy at jumper
    ai"See on saladus! Peale tunde saad teada. Need on tänaseks klubitunniks."
    pov"Materjalid mingisugused?"
    show ai neutral with fastdissolve
    ai"Midagi sellist, jah."
    "Aisling ulatab sulle ühe karpidest ja ise võtab teise. Kaks kingakarpi jääb veel põrandale."
    pov"Need ei ole väga rasked, jõuaks vist kõik korraga ka ära viia."
    ai"Ma ei julge, tead. Ma pillan raudselt maha."
    pov"Okei siis. Käime kaks ringi."

    show bg hallway
    with fade
    "Aisling ja sina kõnnite kastidega trepist üles ja klubiruumi juurde ning panete kastid ukse taha maha."
    ai"Ma pean võtme ka tooma veel. Ei taha kola keset koridori ka jätta."
    pov"Need karbid võivad jah ette jääda."
    "Te käite ühe ringi veel all garderoobis ja Aisling toob samal ajal kaasa klassi võtme."
    show bg clubroom
    with fade
    "Te panete kastid klassi tagaseina äärde laua peale."
    show ai happy with fastdissolve
    ai"Super! See on kõik, mis mul vaja oli. Suur tänu!"
    pov"Aitan hea meelega. Pole tänu väärt."
    hide ai happy with fastdissolve
    "Te mõlemad naasete oma tundidesse."
    scene bg must
    with fade
    scene bg hallway
    "Peale kooli lõppu naased sa klubiruumi juurde. Uks on juba pärani lahti, kui sa kohale jõuad."
    "Klassi sisse piiludes näed sa Aislingi laudu kokku lükkamas ja asju ettevalmistamas."
    menu:
        "Mine appi":
            scene bg clubroom
            with fade
            show ai neutral with fastdissolve
            "Sa astud uksest sisse ja lehvitad Aislingile."
            "Ta lehvitab energiliselt vastu."
            show ai neutral at jumper
            ai"Hei! Sa võid nüüd tulla vaadata, mis seal kastides oli. Aita mul igale lauale umbes võrdselt värve panna."
            hide ai neutral with fastdissolve
            "Sa astud klassi tagumisse otsa, kingakarpidele lähemale ja tõstad ühe kaant."
            "Kastis on mitu tavalist pruuni savist lillepotti."
            "Selle kõrval on juba lahtine kast värvitopsikutega."
            "Sa võtad kastist mõned topsid kummassegi kätte ja lähed neid laudadele viima."
            "Mõnel laual on juba värve, aga mõned on tühjad."
            "Sa viid tühjadele laudadele mõned kollased, punased ja sinised värvitopsid ning lisad mõnele Aislingi koostatud värviplahvatusele ka valget."
            "Paar minutit möödub mugavas vaikuses."
            $ aisling += 1
            $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')
            "Selleks ajaks, kui te laudade valmis sättimise lõpetasite, olid teised ka juba kohal."

        "Oota ukse juures":
            "Sa otsustad, et ei taha Aislingi segada ja jääd ukse taha ootama."
            "Ei lähe mööda kaua aega, enne kui märkad Glassi sinu poole jalutamas."
            show gl neutral with fastdissolve
            "Ta jääb sinu ees seisma ja võtab kõrvaklapid ära ning topib need kotti."
            pov"Tervist."
            gl"..."
            gl"Tere."
            "Paar hetke möödub suhtelises vaikuses, ainsaks heliks vihmapiiskade maandumine aknale."
            gl"Kas sa sisse ei taha minna? Uks on lahti."
            pov"Aisling tegeles seal millegagi, ma ei tahtnud teda segada."
            "Glass noogutab nõusolevalt."
            show gl neutral at jumper
            gl"Kas sa tead, mis tal tänaseks plaanis on?"
            pov"Pole aimugi. Ma aitasin tal lõuna ajal kaste tassida, aga ma ei tea mis nende sees oli."
            gl"Mis, sa ei küsinudki?"
            pov"Küsisin küll, aga ta ütles, et see on saladus."
            "Sa naeratad Glassi poole. Ta muigab tagasi."
            show gl happy with fastdissolve
            gl"See kõlab jah Aislingi moodi."
            pov"Onju?"
            $ glass += 1
            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
            scene bg clubroom
            with fade
            show gl neutral at midright with fastdissolve
            "Glass pistab nina ukse vahelt sisse."
            gl"Hei, Aisling? On sul abi vaja?"
            show ai neutral at midleft with fastdissolve
            ai"Ega ma ära ütlema ei hakka. Võite potid laudadele valmis panna."
            show gl neutral at jumper
            gl"Potid…?"
            hide ai neutral with fastdissolve
            "Lähete Glassiga koos klassi tahaotsa laua juurde, kuhu sa lõuna ajal karbid asetasid."
            "Glass teeb ühe lahti."
            pov"Ahah, lillepotid. Kas me hakkame lilli istutama?"
            gl"Kas sa näed siin labidaid või mulda?"
            "Glass muigab jälle omaette."
            "Aisling hõikab laudade juurest seletuse."
            show ai happy at midleft
            ai"Me värvime lillepotte!"
            pov"See kõlab täitsa toredalt."
            ai"Onju?"
            show ai neutral with fastdissolve
            "Te aitate Aislingil lauad valmis panna. Selleks ajaks, kui te lõpetanud olete, on teised ka juba kohal."
            hide gl neutral
            with fastdissolve
    show ai happy at midleft
    show ir neutral at midright
    with fastdissolve
    ai"Hästi siis, tere tulemast Aislingi tagasihoidlikusse töökotta!"
    "Aisling plaksutab korra õnnelikult."
    show ai neutral with fastdissolve
    ai"Mõned teist panid ilmselt juba üks ja üks kokku, aga kui mitte siis tänaseks tegevuseks on lillepottide värvimine! Maalimine! Kaunistamine! Misiganes te tahate teha!"
    ai"Laudadel on liimi, sädelust, värve, värvipalette, pintsleid ja veetopse. Võite teha mida iganes! Niisama lõbu pärast! Ja te võite pärast oma lillepoti koju ka võtta!"
    ai"Äge, kas pole?"
    hide ir neutral
    show ca neutral at midright
    with fastdissolve
    ca"Kõlab lõbusalt!"
    hide ca neutral with fastdissolve
    ai"Kui küsimusi on siis küsige, aga muidu ma maalin koos teiega!"
    "Aisling istub ka laua taha maha ning krabab pintsli."
    hide ai neutral with fastdissolve

    menu:
        "Kellega sa istuda tahaks?"
        "Aisling ja Glass":
            "Sa otsustad istuda Aislingi ja Glassiga ühte lauda."
            show ai neutral at midleft
            show gl neutral at midright
            with fastdissolve
            "Glass on juba jõudnud oma potti valgeks värvima hakata."
            "Aisling tõmbab alles esimesi siniseid jooni enda poti küljele."
            "Sa vaatad enda puutumata lillepotti."
            hide ai neutral
            hide gl neutral
            with fastdissolve
            $ istun = "aigl"

        "Irene, Carina ja Xiao Yun":
            "Sa otsustad istuda Irene, Carina ja Xiaoga ühte lauda."
            show ir neutral at midright
            show ca neutral at midleft
            with fastdissolve
            "Carina ja Irene istuvad koos ja jutustavad niisama erinevatest maalimise ideedest."
            hide ir neutral
            hide ca neutral
            show xy neutral
            with fastdissolve
            "Xiao Yun juba maalib. Ta poti ülemine serv on juba heleroheline."
            pov"Mis sa maalid?"
            show xy happy with fastdissolve
            xy"Metsa. Samblavaibaga männimetsa, kui täpne olla."
            "Sa noogutad ja suunad tähelepanu enda lillepoti poole."
            hide xy happy with fastdissolve
            $ istun = "ircaxy"

    menu:
        "Kuidas sa enda potti kaunistada soovid?"
        "Mereteemaline maaling":
            "Otsus tehtud, ulatad sa pintsli sinise värvitopsiku poole."
            "Poti ülemine serv on kiiresti üleni sinine ja sa otsid juba tumedamat tooni, mida merepõhjas kasutada."
            "Toonid paigas, liigud sa edasi liivase merepõhja juurde."
            "Otsustad lisada ka mõned kirjud merekarbid ja paar ujuvat kala."
            "Sa pole kindel mis sorti kalad need täpselt peaks olema, aga need on niisama uimedega kujundid, millel on üksik must täpp silma eest. Kala täpne liik ei olegi vist oluline."
            "Üles äärde lisad sa veel valgega lainelise mustri merevahuks."
            "Oled lõpptulemusega täitsa rahul."
            $ pott = "meri"

        "Niisama ilusad värvid":
            "Otsus tehtud, ulatad sa värvisegamisaluse poole ning otsid sobivaid värve, mida kasutada."
            "Silma jäävad lilla, sinine ja punane. Neist peaks ilusa tooni kokku saama."
            "Sa võtad ka veidi valget, et heledamaid toone segada."
            "Poti ülemise ääre värvid sa siniseks, alumise punaseks."
            "Keskele teed triibu lillaga, siis hakkad sinist ja punast omavahel sobivateks toonideks kokku segama."
            "Läheb jupp aega, enne kui sa sobiva sinise-lilla-vahelise tooni kätte saad ja seda potile kandma hakkad."
            "Protsess kordub ka punase-lilla vahelise tooni jaoks."
            "Siis jääb üle värvid enam-vähem ilusti kokku sulandada, et ei jääks näha otseseid triipe."
            "See on keerulisem, kui see tundub, aga sa saad sellega lõpuks ikkagi hakkama. Peaaegu. Enam-vähem. Piisavalt hästi, et sa kulutatud ajaga rahul oleks."
            $ pott = "värvid"

        "Geomeetrilised mustrid":
            "Otsus tehtud, hakkad sa otsima kõige peenema otsaga pintslit."
            "Seda on täpsete joonte maalimiseks vaja."
            "Värvid poti ülemise poole valgeks, enne kui sinna kujundeid hakkad maalima."
            "Alumise poole katad erinevat värvi kolmurkade, ruutude, pentagonide ja muude kujunditega."
            "Ülemise, valge taustaga poole täidad sa sarnaste hõljuvate kujunditega."
            "Lõpptulemus on veidi segane, aga täitsa kena."
            $ pott = "kujundid"

    if istun == "aigl":
        "Pott valmis, pöördud sa Aislingi poole, kelle pott ka juba värviga üleni kaetud on."
        show ai neutral with fastdissolve
        pov"Kas see sobib?"
        "Aisling vaatab sinu poole."
        ai"Mis sa maalisid?"
        label aislingiarvamus:
        if pott == "meri":
            pov"Merepõhja tegin."
            show ai neutral at jumper
            ai"Ooo! See on täitsa ilus ju. Oled sa varem maalinud niimoodi?"
            pov"Noh, väiksena kunstitunnis ikka, aga hiljuti küll mitte."
            ai"Muljetavaldav! Mulle meeldib! Näe, ma ise tegin taeva. Need on täitsa sarnased niimoodi, käivad kokku omavahel."
            "Aislingi ja sinu lillepotid on mälemad peamiselt sinised valgete ääristega. Sinu oma kaunistavad kalad, tema oma aga linnud."
            pov"On jah. Ühtekad."
            show ai happy with fastdissolve
            "Aisling naeratab."
            $ aisling += 3
            $ renpy.notify('Teenisid Aislingiga 3 sõpruspunkti')
        elif pott == "värvid":
            pov"Panin lihtsalt ilusad värvid kokku. Punasest siniseks, nagu vikerkaare puuduv jupp."
            ai"Vikerkaare puuduv…"
            show ai happy with fastdissolve
            ai"Ahjaa! Vikerkaarel on jah ühes küljes punane ja teises lilla. See on siis see vahepealne jupp mis puudu on, et ta uuesti punaseks läheks!"
            show ai neutral with fastdissolve
            ai"Täitsa kaval. Ma polekski osanud seeda niimodi öelda."
            ai"Mulle meeldib. Näe, ma ise tegin taeva, pilvede ja lindudega. Seega mõnes mõttes käiksid meie potid nagu kokku. Taevas ja vikerkaar."
            pov"Mõnes mõttes jah."
            $ aisling += 2
            $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')
        else:
            pov"Ma tegin geomeetrilised mustrid sellised. Värvilised."
            show ai neutral at jumper
            ai"Miks kõik kolmnurgad sinised on?"
            pov"Sinine on kolmnurga värv. Kollane võib-olla ka. Aga roheline kindlasti mitte."
            ai"Kust sa võtad seda, et kolmnurk ei tohi roheline olla?"
            pov"Ei tea. See lihtsalt tundub vale. Mis sina tegid?"
            show ai neutral at jumper
            ai"Ma joonistasin taeva!"
            ai"Minu ainsad kujundid on pilved ja linnud."
            pov"Minu meelest on see ilus."
            ai"Arvad?"
            pov"Ei, ma tean. See on ilus maaling."
            show ai happy at jumper
            ai"Aitäh!"
            $ aisling += 1
            $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')
        if istun == "ircaxy":
            jump glassiarvamus
        show ai neutral at midleft with dissolve
        ai"Glass, mida sina tegid?"
        show gl neutral at midright with fastdissolve
        "Glass tõstab enda lillepoti veidi kõrgemale, et seda paremini näha oleks."
        "See on üleni kaetud erinevates valge ja halli toonides, nagu tormine pilv."
        gl"See on… Niisama värvitud."
        "Veidral kombel tundub see näiliselt lihtne, samas keeruliselt kokku sulandunud värvidega disain, väga sobiv Glassi jaoks."
        ai"Kuidas sa need värvid nii sujuvalt kokku sulatasid? Isegi mina ei oska nii hästi seda teha."
        gl"Ma lihtsalt segasin sellise vahepealse tooni."
        "Glass näitab pintsliga enda segamisaluse suunas, mis on täidetud erinevate halli toonidega. Mõned on nii sarnased, et su silm ei tee neil isegi vahet."
        pov"Muljetavaldav. Minu oma on selline."
        "Sa tõstad enda poti ka kõrgemale ja keerutad seda veidi ringi. Glass jälgib seda mõtliku pilguga."
        show gl happy with fastdissolve
        gl"Kena."
        "Ta naeratab veidi. Sa naeratad vastu. Aisling naeratab ka. Te olete kõik tööga rahul."
        $ glass += 1
        $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')

    else:
        "Pott valmis, tõstad sa pilgu teiste lauas istujate poole."
        show ca neutral at midleft with fastdissolve
        "Carina pott jääb sulle esimesena silma."
        "See on üleni kirjusid värviplekke täis."
        pov"Carina, mis sa maalisid?"
        show ca neutral at jumper
        "Carina vaatab veidi ehmunult sinu poole."
        ca"Ah? Aa, ma tegin abstrakset kunsti veidi. Tavaliselt ma teen kõike hästi täpselt ja korralikult, seega ma mõtlesin, et täna teeks veidi… Teistmoodi. Tead?"
        "Sa noogutad."
        pov"Tean."
        "Su pilk pöördub Carina kõrval istuvale Irenele."
        show ir neutral at midright with fastdissolve
        pov"Irene, aga sina?"
        "Irene paneb pintsli veetopsi ja keerab enda potti veidi."
        "See on peamiselt ikka veel tavaline savipruun, aga ühest küljest on see täidetud imeilusate keerlevate mustritega."
        ir"Ma proovisin neid pisikesi pintsleid."
        "Ta lehvitab käega oma poti poole."
        show ir neutral at jumper
        ir"Vist isegi tuli välja."
        show ca happy with fastdissolve
        ca"Vist? See on imeline, minu meelest. Ma ei saaks elu sees nii täpselt neid jooni paika."
        hide ir neutral
        show xy neutral at midright
        with fastdissolve
        "Xiao Yun mõmiseb sinu kõrvalt nõusolevalt."
        xy"Täitsa uhke jah. See nõuab ikka kogemust. Või talenti. Oleneb."
        pov"Xiao, milline sinu oma on?"
        "Xiao tõstab enda potti sinu poole. See on kaetud erinevate roheliste toonidega, mis üleval heledamad olid. Maalis oli näha ka mõned puud ja põõsad."
        "Xiao keerab potti veidi ja näitab näpuga ühte täpset kohta. Seal on pruun… midagi. Tundmatu pruun täpp."
        xy"See peaks orav olema. See ei tulnud mul nii hästi välja, kui puud."
        show ca neutral at jumper
        "Sa kuuled kuidas Carina naeruga turtsatab ja seda viisakalt tagasi üritab hoida. Xiao naeratab talle vastu."
        show xy happy with fastdissolve
        xy"Ma tean onju. Täitsa metsa läks."
        pov"(Aaa, metsa läks… Metsa pildiga pott.)"
        "Varsti itsitab kogu teie laud."
        "Carina pöörab tähelepanu sinu poole tagasi."
        hide xy happy
        hide ca neutral
        show ca neutral
        with fastdissolve
        ca"[player_name], mis sina tegid?"

        if pott == "meri":
            pov"Mul on mere pilt, selline."
            hide ca neutral
            show xy neutral
            with fastdissolve
            xy"Mul on metsas orav ja sul on meres kalad. Kena."
            "Xiao noogutab rahulolevalt. Talle vist meeldib su maaling."
            $ xiaoyun += 1
            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')

        elif pott == "värvid":
            pov"Mul on Carinale sarnane värvide segadus veidi. Tegin punasest siniseks ülemineku nii, et keskel on lilla."
            show ca happy at jumper
            ca"Oh, kui tore! Nagu vikerkaar!"
            show ca neutral with fastdissolve
            ca"Või noh, tegelikult ei ole. Värvid on valed. Aga sa saad aru küll, mida ma mõtlesin."
            "Sa noogutad vastuseks."
            pov"Meil on jah täitsa ühte maitset need."
            ca"Tore teada, et ma ainuke pole, kes midagi joonistama ei hakanud."
            $ carina += 1
            $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')

        else:
            pov"Ma tegin sellised geomeetrilised mustrid."
            hide ca neutral
            show ir neutral
            with fastdissolve
            ir"See näeb täitsa äge välja. Mina ei taibanud tausta valgeks värvida, ma oleks ka vist pidanud seda tegema. Minu sinist on pruuni taustal veidi raske näha."
            pov"Pole hullu, ma arvan, et seda on piisavalt näha."
            ir"Tore. Ma muretsesin, et äkki ei ole üldse eemalt näha."
            show ir neutral at midleft
            show xy neutral at midright
            with dissolve
            xy"Kui see tumedam oleks siis võib-olla jah, aga sul on piisavalt ere värv et pruuni taustal on ikkagi näha."
            pov"Igatahes mulle meeldib sinu oma ka, Irene."
            show ir happy with fastdissolve
            "Irene naeratab."
            $ irene += 1
            $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')

    scene bg clubroom
    with dissolve
    "Pärast juppi aega maalimist ja jutustamist hüppab Aisling jalule."
    show ai neutral with fastdissolve
    ai"Nonii, meil hakkab aeg otsa saama, seega hakake otsi kokkupoole tõmbama."
    ai"Me saame potid aknalauale kuivama jätta, homseks peaks need täiesti kuivad olema!"
    show ai happy at jumper
    ai"Suur tänu tulemast ja näeme reedel!"
    hide ai happy with fastdissolve
    "Klassis tekib vestlusmelu."
    if istun == "ircaxy":
        "Samal ajal, kui teised värve kokku hakkavad pakkima, astud sa Aislingi laua poole."
        show ai neutral at midleft
        show gl neutral at midright
        with fastdissolve
        pov"Hei, ma tahtsin sinu ja Glassi potte ka näha."
        show ai neutral at jumper
        ai"Tsau, [player_name]! Ikka jaa, näed, siin on minu oma."
        "Aislingi pott on üleni sinine, kaunistatud pilvede ja lindude piltidega."
        ai"Mis sa maalisid?"
        jump aislingiarvamus
        label glassiarvamus:
        show ai neutral with fastdissolve
        pov"Milline Glassi oma on?"
        "Glass, endiselt oma kohal istumas, tõstab enda lillepoti veidi kõrgemale, et seda paremini näha oleks."
        "See on üleni kaetud erinevates valge ja halli toonides, nagu tormine pilv."
        gl"See on… Niisama värvitud."
        "Veidral kombel tundub see näiliselt lihtne, samas keeruliselt kokku sulandunud värvidega disain, väga sobiv Glassi jaoks."
        pov"Meenutab mulle tormist pilve."
        ai"Nüüd kui sa seda mainid… Meenutab jah. Vot, kui äge, Glass! Meie disainid käiksid nagu kokku!"
        "Sa jätad Aislingi ja Glassi jutustama ning lähed Irenele ja Carinale appi koristama."
    else:
        "Sa aitad Aislingil ja Carinal koristada."
    "Kõik saavad lõpuks oma lillepotid aknalauale kuivama."
    pov"(Tänane on täitsa tore olnud.)"
    "Sa lähed pärast pikka päeva koju."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    $ minigame = 0
    menu:
        "Mitu kingakarpi tõi Aisling kooli?"
        "Kolm":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli neli!"


        "Neli":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Viis":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli neli!"

    centered"Mis täna veel juhtus?"
    menu:
        "Mis värvi oli Glassi lillepott?"
        "Tumesinine":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli hall!"

        "Hall":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Valge mustade laikudega":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli hall!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Kui kaua läheb pottidel aega kuivamiseks?"
        "Homseni":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Reedeni":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli homseni!"
            centered"Lisaks, reede ongi järgmine klubipäev."

        "Järgmise klubipäevani":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli homseni!"
            centered"Lisaks, järgmine klubipäev ongi reede."

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas sulle kõigi potid meeldisid?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."

    call screen display_stats

#Kuues päev
label day6:
    scene bg must
    with fade
    centered"{size=*2}Reede, Xiao Yuni hobipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg clubroom
    with fade
    "Sa istud klubi klassis ja vaatad aknast välja. Terve nädal on pidevalt sadanud."
    show xy neutral with fastdissolve
    "Sa oled üks esimesi, kes täna kohale jõudis. Xiao istub õpetaja laua taga ja kirjutab midagi oma märkmikku. Teised pole veel siin."
    pov"Hei, Xiao?"
    "Xiao ei tõsta oma pead."
    xy"Mm?"
    pov"Mida me täna üldse teeme?"
    xy"Küll sa näed."
    pov"Ah, okei."
    hide xy neutral with fastdissolve
    "Paari minuti pärast ilmuvad Carina, Irene ja Aisling koos. Neil oli mingisugune kontrolltöö ja nad arutavad vastuseid."
    show ir neutral at midleft with fastdissolve
    ir"Ma olen päris kindel, et vastus oli 27."
    show ca sigh at midright with fastdissolve
    ca"Ah, tõesti? Siis läks mul küll see töö metsa. Sain vist 64,7…"
    hide ir neutral
    show ai neutral at midleft
    with fastdissolve
    ai"Kuidas sul nii mööda läks?!"
    show ca sigh at jumper
    ca"Mina ei tea!"
    "Aisling ja Irene naeravad Carina üle, kes istub toolile ja paneb oma pea kätele. Paari hetke pärast hakkab ka Carina naerma."
    show ca neutral with fastdissolve
    ca"Kuidas see võimalik on?"
    hide ca sigh
    hide ai neutral
    with fastdissolve
    show gl neutral at midright with fastdissolve
    "Glass astub sellel hetkel klassi ja heidab sulle küsitleva pilgu. Sa kehitad õlgu."
    show ir neutral at midleft
    hide gl neutral
    with fastdissolve
    "Irene vaatab klassis ringi."
    ir"Kõik on kohal. Nii siis, Xiao. Sinu kord meiega tegeleda."
    show xy neutral at midright with fastdissolve
    xy"Nii on."
    hide ir neutral with fastdissolve
    show xy neutral:
      xalign 0.73
      linear 0.5 xpos 0.5
    "Xiao tõuseb püsti ja istub uuesti maha, seekord laua peale."
    xy"See tuleb lihtne: me hakkame luuletusi kirjutama."
    show ai happy at left with fastdissolve
    ai"Uu, lõbus!"
    "Xiao noogutab."
    hide ai happy with fastdissolve
    xy"Väga palju mul selle kohta öelda ei ole, ma jätan detailid teile. Kui teil on küsimusi, küsige."
    "Xiao võtab laualt mõned paberid."
    xy"Kes tahab paberit?"
    menu:
        "Võta Xiaolt paber":
            "Sina, Carina ja Aisling tõstate käed. Glass ja Irene võtavad välja telefonid. Xiao jagab teile paberi."
            $ xiaoyun += 1
            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')

        "Kirjuta telefoni":
            "Carina ja Aisling tõstavad käe. Glass, Irene ja sina võtate välja telefonid. "

    "Paar hetke on klassis täielik vaikus. Keegi ei tea, mida kirjutada. Õhk on pingeline. Xiao vaatab klassi ja mõtleb."
    xy"Te ei pea selle peale nii pingsalt mõtlema. Luule tuleb välja kõige paremini siis, kui see tuleb sinu südamest. "
    xy"Ükskõik kes võib teha mingi suvalise riimuva luuletuse, aga ainult sina saad oma tunded õigesti kirja panna."
    "Pinge õhus kaob ja inimesed hakkavad paberile kritseldama või telefoni tippima. "
    show xy neutral at midright
    show ca neutral at midleft
    with fastdissolve
    ca"Kas luuletustel peavad pealkirjad ka oleme?"
    xy"Kohustuslik ei ole, kuid ma soovitan jätta selle viimaseks, kui tahad seda panna."
    ca"Olgu, aitäh."
    hide ca neutral
    show ir neutral at midleft
    with fastdissolve
    ir"Kas see peab riimuma? Riimide leidmine on nii tüütu."
    xy"Ei pea. Ma ise kirjutan vabavärsilise luuletuse ehk riimiteta luuletuse."
    ir"Väga tore."
    hide ir neutral
    show ai neutral at midleft
    with fastdissolve
    ai"Riimidest rääkides, mis on hea sõna, mis riimiks sõnaga elegantsus?"
    xy"Hmm, ainsus? Asus? Kahetsus?"
    hide xy neutral
    show ir neutral at midright
    with fastdissolve
    ir"Meelsus? Leidlikus?"
    hide ir neutral
    show ca neutral at midright
    with fastdissolve
    ca"Pesus? Tavalisus?"
    hide ca neutral
    show gl neutral at midright
    with fastdissolve
    gl"Muusikalisus, närvilisus."
    ai"Ah! Närvilisus! See võib töötada."
    gl"Mm."
    hide gl neutral
    hide ai neutral
    with fastdissolve
    "(Tundub, et kõik on välja mõelnud millest nad kirjutavad. Isegi Glass tundub väga keskendunud.)"
    pov"(Mida peaksin mina kirjutama…)"
    menu:
        "Perest":
            pov"(Ma kirjutan perest. Hea lihtne teema, millest on palju rääkida.)"
            $ luule = "pere"
        "Sotsiaalmeediast":
            pov"(Sotsiaalmeedia on väga aktuaalne teema. Sellest on kindlasti midagi tähtsat rääkida.)"
            $ luule = "sotsiaalmeedia"
        "Loodusest":
            pov"(Loodus on üks asjadest, mis on alati olemas olnud. See peaks inspiratsiooni andma.)"
            $ luule = "loodus"
        "Elu raskustest":
            pov"(Iga elu on erinev. Huvitav, kuidas erinevad on kõigi inimeste elud siin klassis?)"
            $ luule = "elu"
        "Harmooniast":
            pov"(Harmoonia on asi, mida paljud proovivad saavutada. Mida mul selle kohta öelda on?)"
            $ luule = "harmoonia"
        "Sõprusest":
            pov"(Sõprus on väga väärtuslik. Mul on hea meel, et olen siin leidnud häid inimesi, kellega suhelda.)"
            $ luule = "soprus"
    "Pärast pooletunnist küsimuste küsimist ja kirjutamist on kõigi luuletused valmis. "
    show xy neutral with fastdissolve
    xy"Kui kõik on valmis siis teeme nii: võtame korraks paaridesse ja siis kes tahab, võib klassi ees kõigile ette lugeda."
    "Irene ja Carina istuvad kohe üksteise kõrvale. Aisling istub Glassi juurde ja hakkab jutustama."
    "Xiao tuleb sinu juurde."
    pov"Tundub, et me oleme koos."
    xy"Mhm. Tahad sina esimesena ette lugeda või mina?"
    pov"Ma lähen esimesena, vähem pinget nii."
    xy"Pinget?"
    pov"Noh, see on nagu sinu asi, eks? Sa kirjutad ka nii palju, et sa oled ilmselt väga hea juba selles."
    show xy happy at jumper
    "Xiao naeratab häbelikult."
    xy"Ah, kui sa nii arvad. Lase aga käia."
    $ xiaoyun += 1
    $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')
    show xy neutral with fastdissolve
    "Sa loed oma luuletuse ette. Xiao kuulab tähelepanelikult, vahepeal noogutades. Kui sa oled lõpetanud, plaksutab Xiao paar korda."
    xy"Täitsa hea. Sul on annet."
    pov"Ah, aitäh. Sinu kord nüüd."
    "Xiao avab oma märkmiku, hingab sügavalt sisse ja alustab. Kui ta on lõpetanud, sa plaksutad."
    menu:
        "Nagu päris etleja":
            pov"See oli imeline! Sa räägid nagu õige etleja!"
            show xy happy at jumper
            "Xiao naeratab suurelt."
            xy"Ma arvan, et sa liialdad."
            $ xiaoyun += 3
            $ renpy.notify('Teenisid Xiaoga 3 sõpruspunkti')
            show xy neutral with fastdissolve

        "Südamest kirjutatud":
            pov"Oli näha kui südamest sa seda kirjutasid. Väga hea."
            show xy happy at jumper
            "Xiao naeratab."
            xy"Aitäh, see tuli tõesti südamest."
            $ xiaoyun += 2
            $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')
            show xy neutral with fastdissolve

        "Parem, kui minu oma":
            pov"Ilus. Palju parem kui minu oma."
            xy"Ei ei, sul on tõesti annet."
            $ xiaoyun += 1
            $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')

    "Sina ja Xiao räägite veel paar minutit oma luuletustest. Kui rohkem midagi öelda ei ole, tõuseb Xiao püsti."
    show xy neutral at jumper
    xy"Olgu, kas kõik on valmis?"
    "Teised klassis olijad noogutavad."
    xy"Sellisel juhul, kes tahab, lava on sinu."
    "Paar hetke ei liigu keegi."
    xy"Olgu, ma siis alustan."
    "Xiao läheb klassi ette ja avab oma märkmiku."


label luuletused:
    play music "emotions go brr.mp3" fadeout 0.7 fadein 0.7 volume 0.5
    xy"Mõtted pole mul kunagi korras,"
    xy"Tunded ka mul haprad."
    xy"Taevatähed mu ainsad sõbrad,"
    xy"Ja leida teisi ma ei suuda."
    xy"Lõbu sinu jaoks on üks asi,"
    xy"Minu jaoks täpne vastand."
    xy"Rahus istuda tahan kodus,"
    xy"Väljas lapsed naeratavad."
    xy"Ära joosta võiks ma"
    xy"Maailma, kus lihtsam olla."
    xy"Kuid minema ei taha hakata."
    xy"Asju maha jätta ei saa."
    xy"Nii jään ma siia istuma"
    xy"Ja mõtlen kuidas seda muuta."


    "Xiao saab aplausi."
    hide xy neutral
    show ca happy at midleft
    show ir happy at midright
    with fastdissolve
    ca"Sa tõesti oskad seda!"
    ir"Sa pead päris palju kirjutama, kui nii lühikese ajaga suudad selle kirjutada."
    show xy happy
    hide ca happy
    hide ir happy
    with fastdissolve
    "Xiao naeratab."
    xy"Luuletused on alati mulle südamelähedased olnud. Ma olen käinud nendega konkurssidel ja mõned korrad võitnud, aga see muutus nii väsitavaks."
    xy"Mul oli tunne, et ma ei suutnud nautida seda, mida armastasin. Tegelikult sellepärast ma siia kooli tulingi, et rahulikult luuletada."
    show xy neutral with fastdissolve
    "Xiao vaatab korraks ringi ja näeb, kuidas kõik teda kuulavad."
    xy"Ah, ma räägin vist liiga palju. Kes järgmine tahab olla?"
    hide xy neutral
    show ai happy
    with fastdissolve
    ai"Mina, mina!"
    "Aisling keksib klassi ette."
    show ai neutral with fastdissolve
    ai"Ma olen päris uhke selle üle. Ahem."

    ai"Elu, värvid ja lilled."
    ai"Inimese silmas olev sära,"
    ai"Tema iseloomu isepära,"
    ai"Metshobuse elegantsus,"
    ai"Opossumi närvilisus."
    ai"Meelespea kaunis taevasinine."
    ai"..."
    ai"Muda mu põlved ära määris,"
    ai"Kõik mu tunded justkui päris,"
    ai"Puude langevad lehed,"
    ai"Maailma ääre lahed."
    ai"Saialille imeline apelsinikollane."
    ai"..."
    ai"Merepõhjas istuvad kivid,"
    ai"Puudes kiikuvad ahvid."
    ai"Taevas lendavad linnud,"
    ai"Probleemid neil laabunud,"
    ai"Pojengi ilus kahvatupunane."
    "Aisling jääb hetkeks vait."

    ai"Aitäh."
    "Kõik plaksutavad valjult."
    show ai neutral:
      xalign 0.5
      linear 0.5 xpos 0.27
    show xy neutral at midright with fastdissolve
    xy"Väga ilus. Kui ma võin küsida, miks selline teema?"
    ai"Ma usun, et loodus ja elu on põhimõtteliselt üks ja sama. Üks ei saa olla ilma teiseta. Ja ma lisasin ka värvid, sest need on mu lemmikud asjad."
    "Xiao mõmiseb vastuseks ja noogutab."
    "Aisling istub uuesti oma endisele kohale."
    hide xy neutral
    hide ai neutral
    show ca neutral
    with fastdissolve
    ca"Ma tahan järgmine olla."
    "Carina seisab klassi ees. Ta sobib juhi positsiooni."

    ca"Rikaste elu."
    ca"Leidlik ja edukas lahendus."
    ca"Raha ja töö põhimõttel."
    ca"Aja ja koha alustel."
    ca"Igapäevane vabadus."
    ca"..."
    ca"Aina kõrgem positsioon."
    ca"Iga vähema punktiga,"
    ca"Iga uue probleemiga,"
    ca"Aina rahulikum kõnetoon."
    ca"..."
    ca"Töö juures on jälle kriis."
    ca"Vali ja pidev kriitika,"
    ca"Kõlab nagu aatomifüüsika."
    ca"Täitsa tavaline eluviis."

    "Jällegi, kõik plaksutavad. Irene vilistab. Carina naeratab."
    show ca happy at jumper
    ca"Aitäh. See teema on väga tähtis mulle, kui keegi kes elab rikkamas peres. Ma tean, et see tundub väga tore, olla rikas, aga igal elul on oma raskused."
    show ca neutral with fastdissolve
    ca"Ausalt öeldes pole ma kunagi oma vanemate tööst aru saanud, aga ma olen lõputult tänulik selle üle, mida nad minu heaoluks teinud on."
    ca"Igatahes, kes järgmine on?"
    "Glass tõstab oma käe ja liigub klassi ette."
    show gl neutral:
        xalign 1.0
        yalign 1.0
        linear 0.5 xpos 0.65
    show ca neutral:
        xalign 0.5
        linear 0.5 xpos -0.3
    gl"..."
    hide ca neutral
    gl"Mida tähtsamaks muutub meedia,"
    gl"Mida kõrgemale  sirguvad inimesed,"
    gl"Seda olulisemaks muutub muusika,"
    gl"Seda suuremaks lähevad kaebused."
    gl"Muusika nagu mere vool"
    gl"Minemas ja tulemas,"
    gl"Siin ja seal, igal pool."
    gl"Uhkeid unistusi ajamas."
    gl"Mitte kunagi samasugune"
    gl"Täielik korralagedus"
    gl"Kuid muusika igavene"
    gl"Ja pühendunud lojaalsus."

    "Kõik plaksutavad."
    pov"(Mu käed hakkavad plaksutamisest valutama.)"
    show gl neutral:
        xalign 0.5
        yalign 1.0
        linear 0.5 xpos 0.73
    show ir neutral at midleft with fastdissolve
    ir"Miks ma pole üllatunud, et sa muusikast räägid. Tõesti tähtis sulle, eks?"
    "Glass noogutab."
    gl" Luuletamisel ja muusikal on palju sarnasusi. Ma võib-olla kasutan seda ühe laulu tekstina."

    hide ir neutral
    show ai happy at midleft
    with fastdissolve
    ai"See oleks üli lahe!"
    hide ai happy
    show ca neutral at midleft
    with fastdissolve
    ca"Kahe hobi kokku panemine, päris hea idee."
    hide gl neutral
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    xy"Irene? [player_name]? Te olete viimased. Kui te ei taha te ei pea seda tegema. "
    show ir neutral at midleft with fastdissolve
    ir"Teeme lihtsalt ära."
    hide xy neutral with fastdissolve
    show ir neutral:
      xalign 0.27
      linear 0.5 xpos 0.5
    "Irene läheb klassi ette."
    show ir neutral at jumper
    ir"Ma pole eriti kirjutaja, aga siin see on."

    ir"Internet."
    ir"Kiire, kuid kaasahaarav"
    ir"Õpetlik, kuid meelelahutuslik"
    ir"Sügavmõtteline, kuid humoorikas."
    ir"..."
    ir"Leia sarnasused inimestega,"
    ir"Kes sinust ei hooli."
    ir"Kes tahavad sinu üle nalja teha,"
    ir"..."
    ir"Käi trendidega kaasas,"
    ir"Jää alati iseendaks,"
    ir"Siis, kui see on kasulik,"
    ir"..."
    ir"Räägi maailmale oma probleemidest,"
    ir"Kui need pole liiga depressiivsed."
    ir"Kui sa valetad iseendale."

label loppeee:
    play music "chill bg.mp3" fadeout 0.7 fadein 0.7
    "Kõik plaksutavad."
    "Jälle."
    pov"(Ai.)"
    ir"Aitäh."
    show ir neutral at midright
    show ca neutral at midleft
    with fastdissolve
    ca"Kas tahaksid meile rääkida, mida mõte selle luuletuse taga on?"
    show ir neutral at jumper
    ir"Noh, põhimõtteliselt lihtsalt sellest, kuidas elu sotsiaalmeedias või internetis on. Millised raskused on ja nii…"
    hide ca neutral
    show xy neutral at midleft
    with fastdissolve
    xy"Kaasahaarav."
    show ai neutral at left with fastdissolve
    ai"[player_name]? Kas sa lähed ka?"
    pov"Miks mitte."
    show gl neutral at right
    show ca neutral
    with fastdissolve
    "Sa seisad klassi ette ja vaatad kõiki."
    "Sa loed oma luuletuse ette. Kõik plaksutavad (Üllatus, üllatus)."
    hide gl neutral
    hide xy neutral
    hide ai neutral
    hide ir neutral
    with fastdissolve
    ca"Huvitav. Miks selline teema?"
    if luule == "pere":
        pov"Pere on päris lai teema, sellest on palju rääkida. Ma arvan ka, et pere on üks kallimaid asju elus."
        show ca happy with fastdissolve
        "Carina naeratab sulle."
        $ carina += 1
        $ renpy.notify('Teenisid Carinaga 1 sõpruspunkti')

    elif luule == "sotsiaalmeedia":
        pov"Sotsiaalmeedia on meie elus väga suureks osaks muutunud. Tundus õige sellest rääkida. "
        show ca happy with fastdissolve
        "Irene vilistab nõusolevalt."
        $ irene += 1
        $ renpy.notify('Teenisid Irenega 1 sõpruspunkti')

    elif luule == "loodus":
        pov"Loodus on väga inspireeriv. Selleta me siin ei oleks."
        hide ca neutral
        show ai happy
        with fastdissolve
        ai"Onju?"
        $ aisling += 1
        $ renpy.notify('Teenisid Aislingiga 1 sõpruspunkti')

    elif luule == "elu":
        pov"Elust on alati hea luuletada. Kõik elud on erinevad ja näitavad ka inimest ise."
        hide ca neutral
        show xy happy
        with fastdissolve
        "Xiao noogutab."
        $ xiaoyun += 1
        $ renpy.notify('Teenisid Xiaoga 1 sõpruspunkti')

    elif luule == "harmoonia":
        pov"Paljud inimesed proovivad oma elus leida teistega harmoonia. Ma tahtsin näha, mida mina suudaks sinna lisada."
        hide ca neutral
        show gl happy
        with fastdissolve
        "Glass naerab vaikselt."
        $ glass += 1
        $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')

    else:
        pov"Ma arven, et te kõik nõustute minuga, kui ütlen, et see klubi on muutunud meid sõpradeks. Ma tahtsin näidata kui palju siin olemine mulle tähendab."
        "Teised noogutavad nõusolekus."

    hide ca happy
    hide gl happy
    hide ai happy
    hide ir happy
    hide xy happy
    with fastdissolve
    "Kõik plaksutavad jälle. Kõigi käed ilmselt valutavad pärast tänast plaksutamisest."
    show xy neutral at midright with fastdissolve
    xy"Olgu. Minu poolt on siis kõik. Aitäh, et tegite seda koos minuga. Näeme järgmine nädal."
    show ai neutral at midleft with fastdissolve
    ai"Oot oot. Enne seda, kes pole veel oma lillepotid teisipäevast võtnud, te saate seda teha nüüd."
    "Sina, Aisling ja Glass võtate oma värvilised potid ja lahkute klassist."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    $ minigame = 0
    menu:
        "Mis sõnaga otsis Aisling riimi?"
        "Kohus":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"elegantsus\"!"

        "Närvilisus":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"elegantsus\"!"

        "Elegantsus":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

    centered"Mis täna veel juhtus?"
    menu:
        "Kes neist kirjutas oma luuletuse paberile?"
        "Irene":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Carina!"

        "Glass":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Carina!"

        "Carina":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Kuidas kirjeldas Glass muusikat oma luuletuses?"
        "Igavene":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Imeilus":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"igavene\"!"

        "Voolav":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"igavene\"!"

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas sulle kõigi luuletused meeldisid?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Pika õhtu lõpuks otsustad sa lõpuks magama minna."

    call screen display_stats

#Seitsmes päev
label day7:
    scene bg must
    with fade
    centered"{size=*2}Teisipäev, Glassi hobipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg sookla
    with fade
    "Lõunasöögi vahetunnis istud sa sööklas üksinda. Igalpool sinu ümber on kuulda teiste inimeste vestlusi, kahvlite kõlisemist taldrikutel ja telefoni mängude helisid."
    "Sa sööd rahulikult oma sööki kuni keegi istub sinu lauda."
    show gl neutral with fastdissolve
    "Sa tõstad oma pea üles ja näed Glassi."
    pov"Tsau?"
    gl"Hei."
    "..."
    pov"(Mis toimub? Glass tavaliselt ei veeda aega teiste inimeste seltsis.)"
    gl"Um. Klubi toimub täna muusika klassis."
    pov"Ah, olgu."
    "Sa eeldad, et Glass lahkub pärast seda, aga ta paar hetke veel ootab."
    gl"..."
    gl"Kas sa saaksid äkki mind enne klassi algust korra aidata?"
    menu:
        "Jah":
            pov"Jah, muidugi."
            $ glass += 1
            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')
            gl"Tore."
            "Glass lahkub kohe, kui on vastuse saanud."
            "Sa naased oma lõuna söömisesse."
            scene bg must
            with fade
            centered"{size=*2}Peale tundide lõppu{/size}"
            scene bg muusika
            with fade
            "Sa lähed pärast tunde otse muusikaklassi."
            "See on üks suuremaid klasse koolis, peamiselt selleks, et tiibklaver ära mahuks."
            show gl neutral with fastdissolve
            "Klaveri taga istub Glass ja toksib suvalisi noote."
            "Ta tõstab pea kui kuuleb ust avamas ja tõuseb püsti."
            gl"Aita mul seda liigutada."
            "Te liigutate klaveri rohkem klassi keskele."
            pov"(Tänu taevale, et sellel on rattad.)"
            gl"Aitäh."
            "Glass istub jälle klaveri taha ja sinu lähed ühe laua taha istuma."
            "Natukese aja pärast jõudsid ka teised kohale."

        "Ei":
            pov"Vabandust, kahjuks ei saa. Mul on üks asi juba plaanitud."
            "Glass noogutab ja lahkub."
            scene bg must
            with fade
            centered"{size=*2}Peale tundide lõppu{/size}"
            scene bg hallway
            with fade
            "Natuke aega pärast tunde asud sa muusikaklassi poole teele."
            show xy neutral at midright
            show ca neutral at midleft
            with fastdissolve
            "Tee peal kohtad sa Xiaod ja Carinat."
            show ca neutral at jumper
            ca"Hei, [player_name]."
            "Sa lehvitad talle viisakalt. Kolmekesi lähete te muusikaklassi. "

            scene bg muusika
            show ir neutral at midleft
            show gl neutral
            show ai neutral at midright
            with fastdissolve
            "Sees näed sa Irenet ja Aislingi, kes aitavad Glassil klaverit liigutada."
            show ir sigh at midleft with fastdissolve
            ir"Miks peab kool kulutama raha selliste asjade peale?"
            ai"Aga sa pead tunnistama, et see on päris lahe."
            "Irene mõmiseb niisama vastuseks."
            show ir neutral at midleft with fastdissolve
            "Kui klaver paigas, tervitavad Irene, Aisling ja Glass ka teid."
            hide ai neutral
    show gl neutral at midright
    with fastdissolve
    "Glass istub klaveri tabureti peale, teised istuvad klassis laudade taha."
    show ir neutral at midleft with fastdissolve
    ir"Nii siis, mis sul meile pakuda on?"
    gl"Noh, põhimõte on lihtne."
    gl"Kuna muusika tähendab igale inimesele midagi teistsugust, siis ma arvasin, et mina mängid mingeid laule ja teie kas kirjutate, joonistate või midagi seoses sellega mida te tunnete."
    hide ir neutral
    show ai happy at midleft
    with fastdissolve
    ai"Uu, lõbus!"
    hide ai happy
    show ca neutral at midleft
    with fastdissolve
    ca"See on huvitav! Teeme ära."
    hide ca neutral with fastdissolve
    "Carina, Aisling ja Irene võtavad välja paberi, Xiao teeb oma telefoni lahti."
    pov"(Ma poleks üllatunud, kui Xiao hakaks lihtsalt luuletusi kirjutama.)"
    pov"(Mida peaksin ma tegema?)"
    menu:
        "Kirjuta":
            "Sa võtad ka oma telefoni välja."
            $ tvv = "telefon"
            pov"(Miks mitte kirjutada?)"
            if xiaoyun > 5:
                "Xiao kaldub oma toolil veidi sinu poole."
                show xy neutral at midleft with fastdissolve
                xy"Kirjutad sina ka luuletust?"
                pov"Ma ei tea veel. Vaatame."
                "Xiao noogutab ja istub jälle otse."
                hide xy neutral with fastdissolve

        "Joonista":
            "Sa võtad oma kotist ühe suvalise vihiku."
            $ tvv = "vihik"
            pov"(Joonistamine on lõbus.)"
            if aisling > 5:
                "Aisling nihkub veidi sinu poole."
                show ai neutral at midleft with fastdissolve
                ai"Mis värvi pliiatsid sul on?"
                pov"Põhilised värvid, tead. Sinine, punane, lilla, roheline, hall..."
                ai"Ega sul roosat laenata ei ole?"
                pov"Siin."
                ai"Aitäh!"
                hide ai neutral with fastdissolve
    show gl neutral at jumper
    "Glass hakkab mängima. Esimene laul on väga aeglane ja kõlab vanalt. "
    pov"(Kui ma peaks arvama, siis see on kas Mozart või Beethoven. Mul pole eriti kõrva selle jaoks.)"
    "Kui laul on lõpule jõudnud vaatab Glass klassi."
    hide gl neutral
    show ca neutral
    with fastdissolve
    "Carina tõuseb püsti ja näitab meile oma kritseldust. See on poolikult värvitud kleit, millel on tumedamad värvid ja mustrid, mida näeksid kanga poes."
    ca"Mu peamine tunne seda kuuldes oli nostalgia. See kleit oli minu vanaema joonistatud aastaid tagasi. Ma aitasin tal selle tegelikult ära õmmelda."
    hide ca neutral
    show ai neutral
    with fastdissolve
    "Järgmisena tõuseb püsti Aisling. Tema paberil on joonistatud õhtune taevas ilusates värvitoonides."
    ai"Ma arvan, et selline muusika oleks väga hea keskendumiseks. Ma tahaks sellisel taustal seda kuulata ja ka maalida midagi."
    hide ai neutral
    show ir neutral
    with fastdissolve
    "Nüüd tõuseb püsti Irene. Tema paberil on näha geomeetrilisi kujundeid ja matemaatika valemeid."
    ir"See muusika tegi mu uniseks, esimene asi mis mul pähe tuli oli sama väsitav matemaatika tund."
    show gl happy at right with fastdissolve
    "Selle peale hakkavad kõik naerma. Isegi Glass irvitab."
    hide gl happy
    hide ca neutral
    hide ir neutral
    show xy neutral
    with fastdissolve
    "Xiao ei tõuse püsti, kuid loeb oma telefonist."
    xy"Hobuste kappamine kruusal,"
    xy"Sigade ruigamine laudas."
    xy"Maakoha kõrvetav päike ja jahe tiik."
    xy"Terve pere kokku tulnud,"
    xy"Nii palju meid, peaaegu et küla."
    show xy neutral at midright
    show ca happy at midleft
    with fastdissolve
    ca"Luuletaja mis luuletaja."
    hide xy neutral
    hide ca happy
    with fastdissolve
    "Sina oled järgmine."

    if tvv == "telefon":
        pov"Ma kirjutasin mõned märksõnad: ajalugu, vanalinn, kunagine, aeg versus mälestused ja tänapäev."
        show ai neutral with fastdissolve
        ai"Neist saaks loo kirjutada."
        pov"Võib-olla kunagi."
        hide ai neutral with fastdissolve
    else:
        "Sa näitad teistele oma paberit."
        pov"See peaks olema vanalinn. Ma mõtlesin sellele, kuidas ma seda laulde kuuldes seal kõnniksin ja aega veedaksin."
        show ca neutral with fastdissolve
        ca"Ah, see kõlab mõnusalt."
        hide ca neutral with fastdissolve
    show gl neutral with fastdissolve
    gl"Olgu, järgmine laul."
    "Teine laul on kiirem, kaasaegsem. Kõlab nagu peaks rohkem instrumente olema."
    hide gl neutral
    show gl neutral at midright
    with fastdissolve
    "Laulu lõpus tõuseb esimesena püsti Aisling. Seekord on tema paberil lagendik üksiku puuga, mille all istub poolikult joonistatud inimene."
    show ai neutral at midleft with fastdissolve
    ai"See laul tuletab mulle meelde suve lõunaid maal. Seda kuidas kunagi oleksin ma võinud tunde õues kiiguta ja olla õnnelik."
    hide gl neutral
    show ca neutral at midright
    with fastdissolve
    ca"Kas sa ei saaks teha seda ka see suvi?"
    show ai happy at jumper
    ai" Saaks! Ja see teeb mind õnnelikuks."
    show ai neutral
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    xy"Mul on midagi sarnast."
    xy"Suvi tulnud, lehed ammu rohelised."
    xy"Talv kaugel mälestuses, lilled juba õitsenud."
    xy"Lapsed õnnelikud, nad mängivad koos."
    xy"Kiikudes ja ronides, aega veedavad kiirelt."
    show ai neutral at jumper
    ai"Mm, ma näen sarnasust."
    hide ai neutral
    hide xy neutral
    show ir neutral at midright
    with fastdissolve
    "Aisling istub ja Irene tõuseb."
    "Tema paberil on palju erivärvilisi joone, mis suvaliselt voolavad üksteise ümber."
    ir"See laul oli väga sujuv, minu arust. Ma ei suutnud emotsioone üksteisest eraldada, nii et panin need kõik kokku."
    hide ir neutral
    hide xy neutral
    show ca neutral
    with fastdissolve
    "Nüüd tõuseb Carina. Ta on joonistanud mütsi, millel on ka palju erinevaid värve."
    ca"Ma nõustun Irene'iga. Ma tundsin erinevates kohtades erinevaid tundeid ja panin kõik siia."
    "Carina istub."
    hide ca neutral with fastdissolve
    if tvv == "telefon":
        pov"Märksõnad, jällegi: otsimine, mets, soojus, koos kuid üksi ja festival."
    else:
        "Sa näitad teistele oma pilti. Sa oled ka joonistanud põllu, kuid sellel pole inimesi. Ainult lilled ja vili."
        pov"Ma mõtlesin ühe põllu peale, millest ma iga päev möödun. Suvel on see alati täis õitsenud ja ilus."
    show ai neutral at midleft with fastdissolve
    ai"Nii palju sarnasusi!"
    show ir neutral at midright with fastdissolve
    ir"Kuid ka päris palju erinevusi."
    hide ir neutral
    show gl neutral at midright
    with fastdissolve
    gl"Muusika võlud. Ma räägin, muusika on võimas. Viimane laul siis? Ma ei tea kauaks see klass meie päralt veel on."
    hide ai neutral with fastdissolve
    "Viimane laul kõlab nagu ühe laulu kaver, aga mulle ei meenu laulu nimi. Laul lõpeb kiiremini kui teised, kuid kõigil on juba tehtud. "
    show ir neutral at midleft with fastdissolve
    "Irene tõuseb. Paberil on näha erinevaid mustreid."
    ir"See laul oli minu jaoks väga korralik, kuid korduv. Vähe erinevusi, kuid ilus."
    hide gl neutral
    show ai neutral at midright
    with fastdissolve
    "Aisling tõuseb. Tema paberil on midagi, mida võib kirjeldada kui segadust. Erinevad kujundid üksteise peal, kõik erinevates värvides ja segamini."
    ai"Kui ma peaksin panema sellele laulule juurde instrumente, siis ma arvan, et lõpuks kõlaks see samamoodi nagu näeb välja see pilt. Mõned laulud ei vaja palju hääli, et olla hea."
    hide ir neutral
    show xy neutral at midleft
    with fastdissolve
    "Siin võtab sõna Xiao."
    xy"Korduv, kuid korratu."
    xy"Plagiaat samas originaal."
    xy"Leidlik, aga juba tehtud."
    xy"Uued hääled nagu müüdid,"
    xy"Võimatu leida."
    show ai  neutral at jumper
    ai"Näed? Xiao saab minust aru."
    hide ai neutral
    show ca neutral at midright
    with fastdissolve
    "Aisling istub, Carina tõuseb."
    "Ta paberile on joonistatud kott, mis oleks päris elus liiga palju maksma läinud. "
    ca"Ausalt öeldes, ma poleks üllatunud kui laulu autoril oleks selline kott. Kõlab nagu selle lauluga oleks läinud palju vaeva ja raha."
    pov"(Minu kord jälle.)"
    if tvv == "telefon":
        pov"Tänapäev, kontserdid, suve festivalid ja peod, puhkus soojal maal."
    else:
        "Sa tõstad üles oma pildi."
        pov" Üks kontsert, kus ma eelmine aasta perega käisin. Tuletas mulle seda meelde."
    hide xy neutral
    show gl neutral at midleft
    with fastdissolve
    gl"Tundub, et selle lauluga olete te enam-vähem ühel arvamusel."
    hide ca neutral
    show ir neutral at midright
    with fastdissolve
    ir"Enam-vähem on õige sõna."
    gl"Mis te arvasite muidu mängimisest?"
    menu:
        "Kontserdi tasemel":
            pov"Ausalt, ma maksaks raha selle kuulamise eest. Tundus täitsa tipptasemel olevat."
            show gl neutral at jumper
            gl"Päriselt?"
            pov"Ma ei ütleks seda, kui ma seda ei mõtleks, Glass."
            show gl happy with fastdissolve
            gl"Aitäh."
            $ glass += 3
            $ renpy.notify('Teenisid Glassiga 3 sõpruspunkti')

        "Palju harjutamist":
            pov"Selle oskuse saavutamiseks pidi ikka väga palju harjutamist minema."
            show gl neutral at jumper
            gl"Ikka. Aastaid."
            pov"Muljetavaldav."
            show gl happy with fastdissolve
            gl"Aitäh."
            $ glass += 2
            $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

        "Kadestan veidi":
            pov"Ausalt, ma veidi kadestan su talenti."
            pov"Tahaks ka niimoodi klaverit mängida."
            show gl neutral with fastdissolve
            gl"See võtab harjutamist."
            pov"Seda küll."
            $ glass += 1
            $ renpy.notify('Teenisid Glassiga 1 sõpruspunkti')


    hide gl neutral
    show ca neutral at midleft
    with fastdissolve
    ca"Igatahes, aitäh Glass selle lõbusa tunni eest. Ma usun, et me kõik oleme sellega väga rahul."
    "Kõik noogutavad. "
    hide ca neutral
    hide ir neutral
    show gl neutral
    with fastdissolve
    gl"Olgu, siis. Me peaks ilmselt nüüd minema."
    "Te panete kõik koos klaveri oma õigesse kohta tagasi ja lahkute koolist."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()

    centered"Pärast seda pikka päeva, oleks mõistlik meelde tuletada mis kõik täna juhtus."
    $ minigame = 0
    menu:
        "Mida meenutas esimene laul Irenele?"
        "Voolavaid jooni":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli matemaatika tundi!"


        "Matemaatika tundi":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Ruute":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli matemaatika tundi!"

    centered"Mis täna veel juhtus?"
    menu:
        "Kelle joonistusele oli Xiao luuletus kolmanda laulu kohta sarnane?"
        "Aislingi":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Sinu":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Aislingi!"

        "Carina":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli Aislingi!"

    centered"Siin on kolmas küsimus!"
    menu:
        "Mida meenutas sulle eelviimane laul?"
        "Mets või põld":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"kontserti\"!"

        "Kontserti":
            $ minigame += 1
            $ renpy.notify('Õige vastus')
            centered"Mäletasid õigesti!"

        "Vanalinna":
            $ renpy.notify('Vale vastus')
            centered"Valesti mäletasid. Õige vastus oli \"kontserti\"!"

    centered"Vinge, saidki kõik vastatud!"
    centered"Noh, vaatame, kas sa mäletasid õigesti."
    centered"{size=*2}Õigesti: [minigame]{/size}"
    if minigame < 3:
        centered"Tundub, et mitte. Kahju, aga homme saad uuesti proovida!"

    else:
        centered"Tundub nii! Palju õnne! Saad kellelegi täna veel helistada."
        menu:
            "Kellele sa helistada tahaksid?"
            "Carina":
                "Sa otsustad helistada Carinale."
                "Telefon heliseb hetke, enne kui ta vastab."
                ca"Halloo, kes on?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas klubiüritus meeldis?"
                "Sa lobised veidi Carinaga."
                $ carina += 2
                $ renpy.notify('Teenisid Carinaga 2 sõpruspunkti')

            "Irene":
                "Sa otsustad helistada Irenele."
                "Telefon heliseb hetke, enne kui ta vastab."
                ir"Kes helistab?"
                pov"[player_name] siin. Tahtsin niisama lobiseda. Kuidas tänane üleüldse läks?"
                "Sa lobised veidi Irenega."
                $ irene += 2
                $ renpy.notify('Teenisid Irenega 2 sõpruspunkti')

            "Xiao":
                "Sa otsustad helistada Xiaole."
                "Telefon heliseb hetke, enne kui ta vastab."
                xy"Nja, halloo?"
                pov"Heihoo. [player_name] siin. Tahtsin niisama lobiseda. Kuidas su päev läks?"
                "Sa lobised veidi Xiaoga."
                $ xiaoyun += 2
                $ renpy.notify('Teenisid Xiaoga 2 sõpruspunkti')

            "Glass":
                "Sa otsustad helistada Glassile."
                "Telefon heliseb jupp aega, enne kui ta vastab."
                "Toru otsas kostab ainult vaikus."
                pov"Halloo? [player_name] siin. Tahtsin rääkida?"
                gl"Millest?"
                pov"Niisama."
                gl"Hm. Ma praegu ei saa väga."
                pov"Olgu peale. Ma siis rohkem ei sega."
                "Enne kui sa toru hargile jõuad panna, kuuled sa Glassi poolt kergendunud ohet."
                $ glass += 2
                $ renpy.notify('Teenisid Glassiga 2 sõpruspunkti')

            "Aisling":
                "Sa otsustad helistada Aislingile."
                "Telefon heliseb hetke, enne kui ta vastab."
                ai"Kesse on?"
                pov"Tsau! [player_name] siin. Tahtsin niisama lobiseda. Kuidas sulle Glassi laulud meeldisid?"
                "Sa lobised Aislingiga jupp aega."
                $ aisling += 2
                $ renpy.notify('Teenisid Aislingiga 2 sõpruspunkti')

    "Enne magama minekut töötad sa veel klubi fotoalbumi kallal."
    "Sa kleebid viimase pildi oma albumisse ja silud selle ilusaks. Lõpuks, pärast albumine tegemise mitmekordset edasilükkamist, on see lõpuks tehtud."
    "Kõik pildid, mida sa oled tegevuste toimumise ajal teinud on kleebitud."
    "Sa kirjutada paar sõna Glassi klaverimängu ja teiste klubiliikmete sõnade või piltide kohta ning paned oma isetehtud albumi kinni."
    pov"Hmm. Midagi on ikka puudu."
    "Sa vaatad albumi heleroosat kaant."
    pov"See vajab mingeid kaunistusi. Kas mul on midagi selleks?"
    "Sa vaatad oma toas ringi, teed lahti erinevaid sahtleid ja karpe, isegi vaatad oma voodi alla, kus võib ükskõik mida olla, aga ei leia midagi."
    pov"Äkki teistel on midagi. Aislingil on kindlalt kleepse või midagi. Viimane tegevus terve grupiga."
    "Järeldusega, et hetkel sa rohkem midagi lisada ei saa, sätid sa magama."

    call screen display_stats

#Kaheksas päev
label day8:
    scene bg must
    with fade
    centered"{size=*2}Reede, viimane klubipäev{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg classroom
    with fade
    "Sa vaatad oma viimases koolitunnid iga paari minuti tagant kella."
    "Päris närve tegitav on näidata teistele inimestele midagi, mida oled ise teinud. Aga samas on elevust tekitav, sest sa oled päris uhke oma albumi üle."
    "See sisaldab väga ilusaid mälestusi sinu uutes sõpradest ja kõigest mida te siiamaani teinud olete."
    "Kell näitab lõpuks täistundi ja õpetaja laseb teid vabaks. Sa pakid oma asjad kokku ja suundud klubi poole."
    scene bg hallway
    with fade
label viimanevoimalus:
    if glass < min(aisling, xiaoyun, carina, irene):
        jump glass_viimane
    elif aisling < min(glass, xiaoyun, carina, irene):
        jump aisling_viimane
    elif xiaoyun < min(aisling, glass, carina, irene):
        jump xiaoyun_viimane
    elif carina < min(aisling, xiaoyun, glass, irene):
        jump carina_viimane
    elif irene < min(aisling, xiaoyun, carina, glass):
        jump irene_viimane
    else:
        jump skipimeviimasevoimaluse

label glass_viimane:
    show gl neutral with dissolve
    "Ühel hetkel kui sa kõnnid ilmub ei kuskilt sinu kõrvale Glass. Sa võpatad korraks, aga taastud kiiresti."
    "Glassil on oma kõrvaklappid peas, nii et teretamise asemel te lihtsalt kõnnite koos klubi poole."
    $ glass += 3
    $ renpy.notify('Teenisid Glassiga 3 sõpruspunkti')
    "Glass annab sulle ühe oma kõrvaklappidest."
    if gld1 == True:
        pov"Kustkohast sa pärit oled, muide? Me ei jüudnud esimesel päeval rääkida."
        gl"Taist."
        "Jalutate kahekesi muusikat kuulates klubiruumini."
        jump skipimeviimasevoimaluse
    else:
        "Jalutate kahekesi muusikat kuulates klubiruumini."
        jump skipimeviimasevoimaluse
label aisling_viimane:
    "Ühel hetkel klubiruumi poole liikudes sa kuuled oma selja tagant häält sind kutsumas."
    show ai neutral with dissolve
    "Sa pöörad ümber ja näed Aislingi."
    "Sa peatud ja lehvitad talle. Ta kõnnib sinu poole ja te jalutate koos klubi suunas."
    show ai neutral at jumper
    ai"Hei! Sinu kord meile midagi näidata, eks?"
    pov"On tõesti. Päris närve tekitav."
    ai"Hmm, jah, nii on vahepeal. Aga usu mind, see on ka väga lõbus. Eriti kui oled uhke oma töö üle!"
    pov"Seda ma õnneks olen. Arvan, et tuli päris hästi välja. Ilmselt pole nii hea, kui seda oleksid sina kui kunstnik teinud, aga see on ikkagi hea."
    $ aisling += 3
    $ renpy.notify('Teenisid Aislingiga 3 sõpruspunkti')
    show ai neutral at jumper
    ai"Eh, mis kunstnik? Ma lihtsalt teen mis mulle meeldib!"
    pov"Ütle mis tahad, aga minu silmis oled ikka kunstnik."
    pov"Ahjaa, muide, ega sul mingit sädelust ega midagi kaasas ei ole? Mõtlesin, et album tahaks veidi särtsu juurde."
    ai"Sädelust kohepraegu ei ole kahjuks kaasas. Aga mul on värvilist teipi?"
    pov"See töötab ka!"
    ai"Super!"
    if aid1 == True:
        pov"Ahjaa, me ei jõidnud esimesel päeval ju rääkida. Kustkohast sa pärit oled?"
        ai"Ahmina? Natuke siit ja sealt, ausalt."
        ai"Hüppame perega peamiselt Portugali ja Iirimaa vahet."
        pov"Tundub äge."
        ai"See on täitsa mõnna."
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse
    else:
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse

label xiaoyun_viimane:
    show xy neutral with dissolve
    "Siis kui sa kõnnid treppidest ülesse, et klassi jõuda, näed sa Xiao Yuni. Ta istub treppide peal ja kirjutab midagi oma märkmikusse."
    pov"Hei, mis kirjutad?"
    "Xiao vaatab üles."
    show xy neutral at jumper
    xy"Ei midagi tähtsat. Sama mida alati."
    pov"Kuid ikkagi super hea?"
    $ xiaoyun += 3
    $ renpy.notify('Teenisid Xiaoga 3 sõpruspunkti')
    xy"Loota võib. Liigume klubi poole?"
    "Ta tõuseb püsti ja te hakkate koos kõndima."
    if xyd1 == True:
        pov"Ahjaa, me ei jõidnud esimesel päeval ju rääkida. Kustkohast sa pärit oled?"
        xy"Hiinast, Hangzhou Shist. Linn Shanghai lähedal, seda sa vist tead."
        pov"Ja, ma tean kus Shanghai on."
        xy"Mhm. Ma tulin Eestisse, sest siin on rahulikum elada. See on nagu pisike küla, kus kedagi ei huvita mdia sa täpselt teed."
        xy"Mulle meeldib see."
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse
    else:
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse

label carina_viimane:
    show ca neutral with dissolve
    "Tee peal näed sa Carinat klassiruumist väljumas. Ta näeb sind ja lehvitab."
    show ca neutral at jumper
    ca"Hei. Kuidas läheb?"
    pov"Hei, hästi. Kuidas sul? Viimane ametlik klubi päev, eks?"
    ca"Ah, jah, on küll. Natuke kurb on, et me kõik koos ei ole iga teisipäev ja reede, aga nagu ma saan aru, et inimestel on asju teha ja ei saa siis tulla."
    pov"Tõsi. Kuid see ei ole nagu me ei näe üksteist enam kunagi. Tuba on meile ikka kasutamiseks, eks?"
    pov"Me saame siis vahepeal lihtsalt üksteisega hängida, veel tuttavamaks saada."
    $ carina += 3
    $ renpy.notify('Teenisid Carinaga 3 sõpruspunkti')
    ca"Õnneks jah. Meie liikmed on kõik nii huvitavad isiksused. Tore oleks nende kohta juurde õppida."
    if irenedialoog1 == 1:
        ca"Esimesel päeval ütlesid sa, et liitusid klubiga loovuse arendamiseks. Kas said ka, mis tahtsid?"
        pov"Muidugi. Õppisin kõigi teiste hobide kohta palju, mõnda võib ise ka proovida."
    elif irenedialoog1 == 2:
        ca"Esimesel päeval ütlesid sa, et meie klubi oli esimene huvitav, mis ette jäi. Kas jöid rahule?"
        pov"Muidugi! Tegevused olid toredad ja inimesed sõbralikud. Ei oleks osanud paremat küsidagi, tegelikult."
    else:
        ca"Algselt sa liitusid ju ainult punktide jaoks. Kas sa lõpuks midagi muud ka said?"
        pov"Kogemusi, ehk. Õppisin palju."
        ca"Tore. See eesmärk oligi."
    if cad1 == True:
        pov"Muide, ma alguses ei jõudnudki sinuga rääkida. Kustkohast sina siis pärit oled?"
        ca"Ah, mina?"
        ca"Norrast, tegelikult."
        pov"Norrast?"
        ca"Jah, koos perega paar aastat tagasi."
        pov"Tore teada. Ja miks sa klubi üldse alustasid?"
        ca"Ma tahtsin oma vanematele näidata, et sarnaste huvidega inimesi on veel. See tuli lõpuks täitsa hästi välja."
        pov"Siis on ju tore."
        ca"Tore jah."
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse

    else:
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse

label irene_viimane:
    show ir neutral with dissolve
    "Teel klubiruumi näed sa Irenet oma klassikaaslastega rääkimas. Ta näeb sind, ütleb teistele midagi ja tuleb sinu kõrvale kõndima."
    show ir neutral at jumper
    ir"Tead, lihtsalt kuna ma oskan hästi programmeerida ei tähenda, et ma pean kõik esitlused ise tegema."
    pov"Ah, grupi esitlus? Jah, need pole peaaegu kunagi toredad."
    show ir sigh with fastdissolve
    ir"Onju! Nagu, okei, kui te ei taha tööd teha, siis öelge õpetajale, et olete laisad ja minge oma eluga edasi."
    pov"Lihtne lahendus. Aga tead, sa saad hakkama nendega. Sa oled piisavalt tark, et mitte lasta neil sinust üle kõndida."
    $ irene += 3
    $ renpy.notify('Teenisid Irenega 3 sõpruspunkti')
    show ir happy with fastdissolve
    ir"Jah, sul on õigus!"
    if ird1 == True:
        pov"Hei kuule, ma ei jõudnudki klubi alguses sinuga väga rääkida. Kustkohast sina pärit oled?"
        show ir neutral with fastdissolve
        ir"Hm, sul on õigus. Ma olen Ameerika Ühendriikidest."
        pov"Päris kaugelt, siis."
        ir"Nujah, üle mere."
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse
    else:
        "Rääkides jalutate kahekesi klubiruumini."
        jump skipimeviimasevoimaluse

label skipimeviimasevoimaluse:
    scene bg clubroom
    with fade
    "Te jõuate koos klassi ja näete teisi juba üksteisega vestlemas."
    "Nad on moodustanud väikse ringi toole, et kõik üksteist näeksid. Sa istud ühe tühja tooli peale ja võtad kotist fotoalbumi."
    pov"Enne kui me alustame, ma ei leidnud enda majast ilusaid kaunistusi kaane jaoks ja arvasin, et võiksime koos seda kaunistada."
    show ca neutral at midleft with fastdissolve
    ca"Nagu viimane tegevus meie kõigiga? "
    show ai happy at midright with fastdissolve
    ai"Jah, jah! Mul on täpselt õiged asjad!"
    hide ca neutral
    show ir neutral at midleft
    with fastdissolve
    ir"Kas paneme kõik midagi sinna?"
    hide ai happy
    show xy neutral at midright
    with fastdissolve
    xy"Siis oleksime kõik esindatud."
    hide ir neutral
    show gl neutral at midleft
    with fastdissolve
    "Glass noogutab."
    hide gl neutral
    hide xy neutral
    with fastdissolve
    "Kõik hakkavad otsima asju, millega albumit kaunistada."
    "Xiao leiab oma pinalist ilusaid värvilisi pastakaid, Glass võlub kuskilt välja noodipaberi ja lisab sellele paar nooti."
    "Carinal on erivärvilisi paelu mingi pärast kaasas."
    "Irene ei leia midagi, aga õnneks on Aislingil kaasas natuke liiga palju kleepse ja värvilist paberit, et Irene võtab käärid ja hakab paberist kujundeid lõikama."
    "Sa asetad albumi laua peale ja te hakkate seda koos ilusaks tegema."
    "Mõne minuti pärast on kõigil oma asjad lisatud. Kaanel on kujutatud kõiki isiksusi, mida selle albumi lehtedel on näha."
    show ai happy at midleft with fastdissolve
    ai"See on nii ilus!"
    show ir neutral at midright with fastdissolve
    ir"Me tegime tõesti head tööd sellega!"
    hide ai happy
    show ca neutral at midleft
    with fastdissolve
    ca"Nüüd saame ka lõpuks näha, mis seal sees on. [player_name], näita meile, mida sa oled teinud."
    "Sa avad albumi esimese lehekülje."
    pov"Esimene hobide tutvustamise päev: Irene programmeerimise {i}crash-course{i}."
    ir"See on alguses, kui ma õpetasin teile kuidas spraite lisada, eks? Ma näen välja nagu õpetaja niimoodi klassi ees."
    ca"Tehniliselt sa olid sellel hetkel õptaja."
    "Irene ja Carina naeratavad üksteisele."
    "Sa keerad lehte."
    "Järgmisel leheküljel on näha kõikide isetehtud tegelaste pilte."
    show ca happy with fastdissolve
    ca"Vaata kui armsad nad kõik koos on!"
    hide ir neutral
    show ai happy at midright
    with fastdissolve
    ai"Glass vaata! See näeb välja nagu meie tegelased mängiksid koos!"
    "Lehekülje nurgas on näha Aislingi retriiverit ja Glassi musta kassi üksteise kõrval liikuvates asendites."
    "Nende kohal on näha ilusat kanaarilindu."
    "Xiao näitab näpuga linnu poole."
    hide ai neutral
    show xy neutral at midright
    with fastdissolve
    xy"See oli minu oma."
    show ca neutral at jumper
    ca"Ilus!"
    "Järgmisel pildil on näha Irenet ja Carinat."
    "Nende taga projektoril on näha Irene tehtud mängu ja seda, kuidas Carina leidis koha, kus mängija sai läbi seina joosta."
    hide xy neutral
    show ir neutral at midright
    ir"Ma olen õnneks selle ära juba parandanud. Ja ka teisi probleeme leidnud. Aga ma olen päris kaugele juba sellega jõudnud."
    ir"Hei, Aisling. Kas sa näitasid oma õele seda juba?"
    hide ca neutral
    show ai neutral at midleft
    with fastdissolve
    ai"Ah, jah. Ta ütles, et talle väga meeldis ja küsis kas saaks olla lõpu mängu esimene proovija."
    ir"See oleks minu au."
    "Sa keerad uuesti lehte."
    pov"Nii, teine päev: Carina miniriiete õmblema õppimine."
    "Esimesel pildil on näha Carinat rääkimas."
    ir"Sa rääkisid nii suure kirega seal ees. Näha oli, et sa armastad seda."
    hide ai neutral
    show ca neutral at midleft
    with fastdissolve
    "Carina punastab."
    ca"See on väga südamelähedane mulle."
    "Järgmistel piltidel on näha särgi tegemise gruppi ja seeliku tegemise gruppi."
    if nukk == "sark":
        hide ca neutral
        show gl neutral at midleft
        with fastdissolve
        ir"Mina, Glass ja [player_name] olime särgi gruppis. Mina ja Glass ei suutnud valida särgi jaoks õiget värvi, nii et küsisime [player_name] arvamust."
        gl"Ta tegi õige valiku lõpuks."
        "Irene noogutab."
    else:
        hide ca neutral
        hide ir neutral
        show ai neutral at midright
        show xy neutral at midleft
        with fastdissolve
        ai"[player_name] pidi valima seeliku värvi, sest mina ja Xiao ei suutnud otsustada."
        xy"Lõpu toode on õnneks ilus."
    "Viimasel pildil on näha nukku, mille riided te kõik koos tegite."
    hide gl neutral
    hide xy neutral
    hide ir neutral
    show ca neutral at midleft
    show ai neutral at midright
    with fastdissolve
    ai"Kas sa oled midagi sellele nukule veel teinud, Carina?"
    ca"Ma paar kombinatsiooni olen välja kavandanud, kuid mul pole aega olnud, et neid kokku õmmelda."
    ai" Kui jõuad, saada meile kindlalt pilte!"
    ca"Muidugi."
    "Sa pöörad albumis lehekülje."
    pov"Kolmas päev: Aislingi töökoda."
    "Esimesel pildil on näha kõiki kõvasti tööd tegemas."
    hide ca neutral
    show ir neutral at midleft
    with fastdissolve
    ir"See tund oli mõnus, peaaegu teraapiline."
    ai"Sellepärast ma selle valisingi. Lihtne kuid mõnus tegevus."
    "Järgmistel piltidel on näha kõikide erinevaid lillepotte."
    hide ir neutral
    show xy neutral at midleft
    with fastdissolve
    xy"Päris ilusad kõik koos niimoodi."
    ai"On tõesti. Kas keegi on juba midagi nendesse juba istutanud?"
    hide ai neutral
    show gl neutral at midright
    with fastdissolve
    "Glass ja Xiao raputavad oma päid."
    hide gl neutral
    hide xy neutral
    show ca neutral at midleft
    show ir neutral at midright
    with fastdissolve
    ca"Mu vanemad ostsid just ühe uue väikese lille. See on natuke aega minu potis, kuni seda liikutama peab."
    ir"Ma panin lillepotti mingid väiksemad vidinad. Juukseklambrid, patsikummid, kirjaklambrid sellised asjad."
    "Kõik itsitavad selle peale."
    hide ca neutral
    show ai neutral at midleft
    with fastdissolve
    ai"Noh, see on ka võimalus!"
    pov"Järgmine: Luuletamine Xiaoga."
    "Esimesel pildil on näha kõiki vaatamas oma telefone või paberit."
    hide ai neutral
    show xy neutral at midleft
    with fastdissolve
    xy"Te olite nii pinges alguses. Ilmselt oleksin pidanud alguses teile ütlema, et see ei ole {i}nii{/i} tähtis kui hästi see välja tuleb."
    ir"Õnneks hakkasime põhimõtteliselt kohe kirjutama pärast sinu inspireerivat kõnet."
    xy"Ma ei usu, et see eriti inspireeriv oli, aga olgu."
    "Teistel pilditel on näha inimesi paarides või klassi ees oma luuletusi lugemas."
    xy"Need tulid teil väga hästi välja. Teie sõnad ütlesid palju rohkem, kui te arvate."
    hide ir neutral
    show gl happy at midright
    with fastdissolve
    "Glass, kes pole täna eriti sõna võtnud, naeratab."
    gl"See oli minu arust kõige teraapilisem tund. Sain ka inspiratsiooni laulude jaoks sellelt."
    show xy happy with fastdissolve
    xy"Xiao naeratab."
    xy"Tore kuulda."
    hide gl happy
    hide xy happy
    with fastdissolve
    "Sa pöörad jälle lehekülge."
    pov"Ja viimane hobipäev: Glassi klaverikontsert."
    "Paar pilti on Glassist klaveri taga istumas. Ülejäänud on sellest kuidas teised mõtlevad, kirjutavad joonistavad või mida iganes nad sellel hetkel tegid."
    show ca neutral at midleft with fastdissolve
    ca"See oli väga huvitav, kuidas me kõik neid laule tõlgendasime. Nii erinevad kuid ka nii sarnased."
    show xy neutral at midright with fastdissolve
    xy"Mulle meeldis kuidas viis, mille kaudu me tõlgendasime seda näitas meie kõigi isiksusi."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    gl"See näitas kui erinevad, aga samas sarnased me kõik oleme."
    "Selle peale noogutavad kõik."
    pov" See on siis kõik. Ma olen jätnud mõned leheküljed tühjaks, kui me peaksime millalgi tahtma veel siia lisada."
    hide gl neutral
    show ai sigh at midright
    with fastdissolve
    ai"Aw, see on kõik? Aga ma ei taha veel minna, meil on nii lõbus!"
    hide gl neutral
    show ca neutral at midleft
    with fastdissolve
    ca"Me ei pea kohe minema. Tegelikult, ma mõtlesin, et võiksime natuke veel lobiseda üksteisega. Ma tõin snäkke."
    hide ai sigh
    show ir happy at midright
    with fastdissolve
    ir"Uuuu, söök!"
    "Te panete üksteise kõrvale paar lauda ja Carina paneb oma snäkid selle peale. Aisling võtab ei-kuskilt välja mõned kommid ja lisab need söögi hulka."
    "Kuigi kool on ammu lõppenud, te kuuekesi vestlete, naerate ja lihtsalt veedate aega kuni üks koristaja ütleb teile, et koju minna."

    scene bg bedroomn
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    with fade
    $ renpy.force_autosave()
    call screen display_stats





#Lõpud
scene bg must
with fade
centered"{size=*2}Laupäev{/size}"
#Punktiarvu võrdlemine, jätkamine kõrgeima punktiarvuga tegelase lõpu suunas
label class_end:
    if glass > max(aisling, xiaoyun, carina, irene):
        jump glass_ending
    elif aisling > max(glass, xiaoyun, carina, irene):
        jump aisling_ending
    elif xiaoyun > max(aisling, glass, carina, irene):
        jump xiaoyun_ending
    elif carina > max(aisling, xiaoyun, glass, irene):
        jump carina_ending
    elif irene > max(aisling, xiaoyun, carina, glass):
        jump irene_ending
    else:
        jump koos_end
#Kui kahel tegelasel juhtub mängu lõpus olema võrdselt punkte, on eraldi kuues lõpp

label aisling_ending:
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on ainult üks asi veel teha: tuletada meelde kõiki häid filme, mida oma elus oled näinud."
    "Õnneks, samal ajal kui sa mõtled selle peale, et kuna me pilgutame, siis me pole kunagi näinud 100 protsenti tervest filmist, kuuled sa oma telefoni heli. Sa võtad vastu."
    pov"Jah?"
    show ai neutral at right with dissolve
    ai"{i}Tsau, [player_name], mina siin!"
    pov"Aisling? Hei, kuidas läheb?"
    ai"{i}Väga hästi, aitäh! Sul?"
    pov"Sama."
    ai"{i}Lahe, igatahes, helistan, sest tahtsin teada kas sul täna aega on?"
    pov"Täna? Jah, mul on päris palju aega."
    ai"{i}Väga tore. Kas sul oleks võimalik tulla minu ja Glassiga lilli istutama?"
    ai"{i}Küsisin ka teistelt, aga neil on tegevusi küllaga."
    pov"Jah, miks ka mitte."
    show ai happy at jumper
    ai"{i}Juhuu! Tead seda parki kooli lähedal? Seal see toimub. Me plaanime igasuguseid taimi tegelikult istutada, aga ma tahtsin lille tiimis olla. Loodan, et see on okei."
    pov"Jah, jah."
    show ai neutral with fastdissolve
    ai"Hästi. Oh, ja veel!"
    "Aisling rääkis sinuga veel pool tundi enne kui sa said hakata ennast valmis panema."
    scene bg tanav
    with fade
    pov"(Imelik on näha kooli nädalavahetusel.)"
    "Sa kõnnid mööda kooli väravatest ja piilud korraks sisse. Kõik on ebatavaliselt vaikne, tavaliselt on siin palju lapsi mängimas."
    scene bg park
    with fade
    "Sa kõnnid edasi kuni jõuad pargini. Sa pole siia palju sattunud, kuna pole olnud põhjust, ja sa oled üllatunud kui palju inimesi on kogunenud."
    "Vähemalt 50 inimest seisavad gruppides nagu nad ootaksid midagi."
    "Sa oletad, et nad on istutamiseks siin ja lähened. Sa proovid leida tuttavaid nägusid, aga ei näe kedagi."
    show gl neutral with fastdissolve
    gl"Hei."
    "Ei kuskilt ilmub sinu ette Glass. Sa ehmud."
    pov"Ah, Glass. Ära ilmu niimoodi välja lihtsalt."
    show gl happy with fastdissolve
    "Glass muigab kergelt."
    pov"Igatahes, kus Aisling on?"
    show gl neutral with fastdissolve
    gl"Ma pole teda veel näinud. Ütles, et saame siin kokku."
    "Seekord ilmub Glassi taha ei kuskilt Aisling."
    show gl neutral at midleft
    show ai neutral at midright
    with fastdissolve
    ai"Hei! Vabandust, et hilinesin! Ma tulin ühelt töökohalt."
    gl"Glass võpatab korraks. Ta vaatab sulle otsa."
    gl"Olgu, ma saan aru mida mõtled."
    "Aisling näib segaduses olemas. Sa kehitad õlgu."
    show ai sigh with fastdissolve
    ai"Ok…"
    show ai neutral with fastdissolve
    ai"Igatahes, lähme võtame meie käepaelad."
    pov"Käepaelad?"
    ai"Et korraldajad teaksid, kes mida teeb."
    "Te lähete ühe laua juurde, kus paar inimest paaniliselt asju otsivad. Üks nendest märkab teid ja annab teile klassikalise klienditeenindaja naeratuse."
    kt"Tere! Kas te tulite siia asju istutama?"
    ai"Täpselt nii! Kas saaks lillede meeskonda minna?"
    "Abiline vaatab mingit paberit."
    kt"Seal on meil ainult kaks kohta järgi. Kas te tahate kindlalt koos olla?"
    "Aisling vaatab teie poole."
    gl"Ma võin midagi muud teha. Sa tahtsid neid lilli kindlalt onju, Aisling?"
    show ai sigh with fastdissolve
    ai"Ah,oled kindel? Ma ei tahaks teid tülitada?"
    show gl happy with fastdissolve
    gl"Nah, ma võin üksinda ka asju teha."
    kt"Ma panen su siis puude istutamisse kirja."
    "Abiline annab sulle ja Aislingile punase käepaela ja Glassile pruuni."
    show ai neutral with fastdissolve
    pov"Näeme siis hiljem?"
    "Glass noogutab ja liigub teise grupiga kaugemale teise pargi otsa."
    hide gl happy with fastdissolve
    "Sina ja Aisling liitute lillede meeskonnaga. Te ei pea õnneks kaugele liikuma, paarkümmend meetrit kohtumiskohast on valmis pandud erinevad lilled ja mõned väiksemad põõsad."
    "Väike peenra ala on juba valmis."
    pov"Äkki võtame need põõsad? Siis saame koos teha."
    hide ai neutral
    show ai happy
    with fastdissolve
    ai"Ooh, see oleks lõbus!"
    "Te tõstate koos paar väikest põõsast väikse peenra otstesse. Sina ja Aisling mõõdate välja kuhu peab põõsad panema, et need näeksid head välja."
    "Te küsite paarilt kaaslaselt arvamusi ja siis võtate labidad ning hakkate kaevama."
    show ai neutral with fastdissolve
    ai"See on ilmselt kõige rohkem trenni, mis ma saan täna."
    pov"Tundub nii, isegi kehalises oleks lihtsam käia."
    ai"Eeh, ärme drastiliseks küll lähe."
    pov"Hm, olgu. Sa ütlesid enne, et tulid kuskilt töölt. Kui ma võin küsida, mis töö see on?"
    ai"Ah, lihtsalt üks assistendi töö. Üks mu sugulastest on laste kunstiterapeut, aitan teda vahepeal, kui vaja."
    pov"Tõesti? Väga sinulik töö minu arust."
    ai"Jah, seda on mulle ennegi öeldud."
    "Te istutate mõlemad põõsad ära ja jääte neid korraks vaatama."
    ai"Nii palju kui ma olen aru saanud on need väga ilusad põõsad kui need on täielikult õitsenud. Me peame mingi hetk tagasi tulema, et neid vaadata."
    pov"Seda küll. Mida me nüüd teeme? Meil aega veel on."
    ai"Hmm…"
    "Aisling vaatab korraks ringi. Kõik kokku tulnud inimesed teevad töökalt oma ülesandeid. Aislingi pilk peatub kauguses oleval elupuude hekil."
    ai"Mulle tundub, et need seal vajavad natuke pügamist."
    "Te lähete koos tagasi kohtumispaika ja võtate sealt käärid. Te lähete elupuude juurde ja hakkate neid tasaseks tegema."
    "Kuna teil on käärid juba käes, te vaatate üle ka roosid. Paari tunni pärast on teil töö tehtud."
    show ai sigh at jumper
    ai" Ma ei mäletagi, millal ma viimati nii palju torgata sain."
    pov"Roosid võivad ilusad olla, aga nad saavad ka väga valusad olla."
    show ai neutral with fastdissolve
    ai"Sellest on kindlalt mingi metafoor. Igatahes, meil siin kõik tehtud. Kas otsime Glassi üles ja hakkame minema?"
    pov"Kui ta just juba pole koju läinud. Mul on tunne, et me oleme ühed viimased, kes siin on."
    "Te lähete kohtumispaika tagasi, et kõik tööriistad tagastada. Te vaatate korraks jälle ringi, kõik teised on vist juba läinud."
    "Aisling vaatab oma telefoni."
    ai" Ah, jep. Glass kirjutas, et pidi ühe sõbraga kokku saama. Tundub, et me oleme tõesti viimased siis."
    pov" Samas, ma pole üllatunud. Lähme siis koju?"
    ai"Lähme."
    "Te mõlemad lehvitate üksteisele nägemiseni ja sätite sammud kodu poole tagasi."
    jump end

label glass_ending:
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on ainukene asi mida teha: meenutada ajaloo tunde, milles sa oleksid pidanud rohkem õpetajat kuulama."
    "Õnneks, enne kui su ajus võtavad üle mõtted Rooma impeeriumist, kuuled sa oma telefoni teate heli. Sa vaatad, kes sulle kirjutanud on."
    show gl neutral at right with dissolve
    gl"{i}hei"
    gl"{i}sul aega on"
    "Kirjutad kiiresti Glassile vastuse."
    pov"{i}On küll."
    gl"{i}lahe"
    gl"{i}viitsid kontserdile täna tulla"
    gl"{i}mul on sõbra lisapilet"
    pov"{i}See sõber sinuga kaasa ei tule?"
    gl"{i}plaani muutus"
    pov"{i}Olgu, võin tulla küll."
    gl"{i}lahe"
    gl"{i}kooli kõrval pargis õhtu poole"
    pov"{i}Olgu, näeme siis!"
    hide gl neutral with dissolve
    scene bg park
    with fade
    "Mõne tunni pärast oled sa teel kooli poole. Sinu ümber on mitu gruppi täis inimesi, kes rõõmsalt räägivad üksteisega."
    "Nii palju kui sa pealt kuulasid (mitte meelega, aga 100\% meelega) lähevad ka nemad sellele kontserdile. "
    "Sa pole täpselt aru saanud milline ansambel esineb, aga nüüd on juba liiga hilja, et koju tagasi minna."
    show gl neutral with fastdissolve
    "Pargi väravatele lähenedes näed sa Glassi nendele nõjatumas."
    show gl happy with fastdissolve
    "Ta tõstab oma pilgu maast üles ja näeb sind. Ta lehvitab."
    pov"Hei. Kontsert pole veel alanud ega? Nii palju inimesi on juba kohal."
    show gl neutral with fastdissolve
    gl"Veel mitte. Bänd pidi päris populaarne olema."
    pov"Mis ansambel see on? Mingi kohalik?"
    gl"Jep. Pole nendest varem kuulnud. Tahtsin vaatama tulla, kas on head."
    pov"Ah, loogiline. Kas lähme sisse?"
    "Glass noogutab ja kõnnib ees lava poole."
    scene bg pink
    with fade
    show gl neutral at midright with fastdissolve
    "Te möödute mitmest söögiputkast täis igasuguseid festivali toite. Te ostate paar pudelit vett ja midagi näksida. Te leiate lavast natuke kaugemal ühe pingi ja istute sinna."
    "Te vaatate rahulikus vaikuses kuidas lavatöötajad panevad viimased detailid paika. Nende seas leiad sa ühe tuttava näo."
    pov"Kas see on Carina? Mida ta siin teeb?"
    show gl neutral at jumper
    gl"Huh, on jah. "
    "Glass tõuseb püsti ja kõnnib lava juurde. Sa kiirustad talle järgi."
    show bg concert
    with fade
    gl"Hei."
    show ca neutral at midleft with fastdissolve
    "Carina pöörab ringi, ta näol on näha üllatust."
    show ca happy at jumper
    ca"Glass? [player_name]?"
    ca"Vabandust, ma ei ootanud, et näen teid siin."
    pov"Me ei ootanud sind ka."
    ca"Ah, ma aitan lava disainiga. Bändi laulja on üks pere sõber ja küsis minult abi."
    gl"Mmm, loogiline."
    pov"Kas sa jääd siia kauaks? "
    show ca neutral with fastdissolve
    ca"Ma ilmselt lähen varsti ära. Mind pole eriti tegelikult vaja. Tahtsin lihtsalt vaadata kuidas nad asjad seavad."
    pov"Noh, kui sa ümber mõtled anna teada. Me oleme ilmselt kuskil läheduses."
    show ca happy at jumper
    ca"Saab tehtud!"
    hide ca happy with fastdissolve
    "Glass ja sa lähete oma pingi juurde tagasi. Iga minutiga tuleb parki üha rohkem inimesi."
    pov"Kas me peaks lavale lähemale minema? Me vist ei näe siin midagi."
    gl"Ma vist jääksin siia, kui sa pahaks ei pane."
    pov"Ei, mulle sobib siin ka. Me oleme siin muusika jaoks, onju?"
    show gl happy with fastdissolve
    "Glass noogutab. Lava tuled korraks kustuvad ja kontsert algab."
    play music "kontsert.mp3" fadeout 1.0 fadein 1.0 volume 0.5
    "Tunni pärast saad sa aru, et Glassil oli õigus. Kui te oleksite püsti seisnud oleksite juba väsinud."
    "Peaaegu terve rahvahulk kas hüppab või tantsib lõbusalt."
    "Ja siis olete sina ja Glass, kes istute kõrvalliinil nagu vanemad, keda sunniti tulema kellegi suvalise lapse sünnipäeva peole."
    "Aga teil on sama lõbus. Te istute oma pingil ja noogutate oma päid."
    "Te mainite väikseid märkuseid, mida kontserdi ajal näete, nagu kuidas süntesaatori mängija paar korda valet nooti mängib ja kuidas mõned laulud on päris tuttavad."
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg pink
    with fade
    show gl neutral with fastdissolve
    "Paar tundi (ja mõned lisapalad) hiljem on kontsert lõppenud ja inimesed sammuvad väljapääsu poole. Te ootate natuke, et enamikud inimesed läheksid ära."
    pov"Tundub, et Carina läks siis koju."
    gl"Tal on palju teha."
    pov"Seda küll. Hakkame nüüd minema?"
    show gl happy with fastdissolve
    "Glass noogutab, tõuseb püsti ja kõnnib minema. Sa järgned talle."
    scene glass bg
    with fade
    show gl neutral with fastdissolve
    "Te jõuate Glassi maja ette. Ta kõnnib ukse juurde ja pöörab ringi."
    show gl happy at jumper
    gl"Aitäh, et kaasa tulid. Mul oli hea päev."
    "Sa noogutad."
    pov"Mul ka."
    "Pärast nimetatud head päeva lähed sa ka ise koju."
    jump end

label carina_ending:

    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on vaid üks asi, mida teha: mõelda asjadele nii, nagu oleksid Vana-Kreeka filosoof."
    "Õnneks, enne kui sa saad Pythagorase teoreemist edasi mõelda, kuuled sa oma telefoni helinat. Sa võtad vastu."
    pov"Jah?"
    show ca neutral at right with dissolve
    ca"{i}Hei, [player_name], kuidas läheb?"
    pov"Hästi, hästi. Sul?"
    ca"{i}Väga hästi, aitäh. Tegelikult, ma tahtsin sulle helistada ühe küsimuse pärast."
    pov"Mis oleks?"
    ca"{i}Kui sa just hõivatud pole, kas sa saaksid minuga rabasse täna tulla?"
    ca"{i}Ma mõtlesin, et võib-olla saan sealt inspiratsiooni, kuid ma vajaksin kellegi abi."
    ca"{i}Küsisin algselt Irenelt, aga ta pidi raamatukokku minema."
    pov"Jah, muidugi võin ma aidata. Mis kell ja kus ma kohal olema peaksin?"
    show ca at jumper
    ca"{i}Väga tore! Kella kahe ajal sobiks mulle kõige paremini."
    ca"{i}Ma saadan sulle varsti juhised. Lihtsam kui see, et ma sulle ise seletan."
    pov"Olgu, näeme siis."
    ca"{i}Head aega!"
    hide ca neutral with dissolve
    "Pärast kõne ära panemist seisad sa hetke ja mõtled, kus sa oma head kummikud eelmine kord panid."

    scene bg must
    with fade
    centered"{size=*2}Paar tundi hiljem, rabas{/size}"
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg mets
    with fade
    "Mõne tunni pärast oled sa metsa serval matkaraja alguses ja ootad Carinat. Minutid mööduvad, sa vaatad pilvist taevast."
    show ca neutral with dissolve
    "Umbes viie minuti pärast näed sa Carinat. Ta lehvitab."
    ca"Hei. Vabandan, et jäin hiljaks."
    pov"Ainult viis minutit. Pole eriti palju."
    ca"Ikkagi, hilinemine on ebaviisakas. Igatahes, kas lähme?"
    "Te hakkate mööda rada kõndima."
    pov"Ma oletan, et otsid uue kollektsiooni jaoks inspiratsiooni?"
    ca"Mingis mõttes. Irene plaanib uut mängu programmeerida ning küsis tegelaste disainiga abi."
    pov"Ah. Kuidas see rabaga seotud on?"
    ca" Niipalju kui ma aru sain, põhinevad mängu tegelased erinevatel bioomidel ning nende disain on ka nende põhjal."
    ca" Ma proovin nii paljudes bioomides ise käia, sest internetist otsides ei pruugi ma saada õiget pilti."
    pov"Hmm, arusaadav."
    pov"Oota. Eestis ei ole kõiki neid ökosüsteeme. Kuidas sa plaanid neid näha?"
    ca"Hmm?"
    show ca happy at jumper
    ca"Ah, ma saan oma vanematelt küsida, et nad mind sinna viiksid."
    pov"(Rikas elu kõlab mõnusalt… Mida Carina oma luuletuses jälle ütles? Igal elul oma raskused?)"

    scene bg soo
    with fade
    show ca neutral with dissolve
    "Te jõuate raba algusesse. Päike on pilvede tagant välja tulnud, selle kiired langevad turbale nagu siid."
    "Carina võtab oma kotist välja ühe tunduvalt kalli kaamera ja hakkab pildistama."
    "Ta teeb seda mitu minutit, otsib õigeid nurki ja valgust, sellised asjad. Ta teeb paar pilti ka sinust."
    ca"See valgus komplimenteerib sind väga hästi."
    pov"Eh, aitäh."
    "Te hakkate raba sisse kõndima. Teid ümbritsevad erinevad põõsad ja puud, enamikud tuhmid pruunid ja rohelised, aga ka vahepeal erinevad punased ja eredamad värvid."
    "Iga kord, kui Carina midagi ilusat näeb, teeb ta sellest kümneid pilte. Ta ka küsib, kas ta võib teha sinust pilte."
    "Te kõnnite umbes tund aega, kuni jõuate linnuvaatlusplatvormini."
    show ca neutral at jumper
    ca"Kas lähme üles?"
    pov"Kui juba rabas oleme."
    "Te ronite platvormi tippu ja vaatate üle raba. Pilved hakkavad vaikselt taanduma ja Päikest on juba näha. "
    "Sina ja Carina seisate paar hetke vaikuses, mõlemad naudite vaadet. Carina võtab oma kaamera ja hakkab jälle pilte tegema."
    "Sa nõjatud reelingule."
    pov"Kas sul on juba mõteid disaini poolest?"
    show ca neutral at jumper
    ca"Midagi on mul alati peas, probleem on nende täide viimisega."
    pov"Hmm. Aga sa saad hakkama. Nii palju kui ma olen su teoseid näinud, on need alati olnud kaunid."
    "Carina naeratab oma kaamera tagant."
    "Te passite veel paar minutit platvormil ja siis hakkate mööda rada edasi kõndima. Teekond möödub umbes samamoodi, Carina teeb vahepeal pilte ja te räägite millest iganes tahate."
    scene bg  mets
    with fade
    show ca neutral at right
    show ca neutral:
        xalign 1.1
        linear 3.0 xpos 0.65
    ca" Noh, tegelikult olen ma Irenet päris kaua teadnud, aga ma pole kunagi nii hästi läbi saanud kellegiga kui temaga, nii et ma usun, et me oleme juba ammu olnud parimad sõbrad."
    pov"Te olete tõesti lähedased, nii palju kui olen tähele pannud."
    show ca neutral at jumper
    ca"Seda võib küll öeld- Ah! Vaata!"
    "Carina osutab käega ühe väikse laigu poole, mis on raja keskel."
    "Lähemalt vaadates on see laik tegelikult väike sisalik, kes on ilmselt hirmust tardunud."
    show ca neutral:
        xalign 0.5
        linear 0.5 xpos 0.2
    "Carina kükitab selle kohale."
    show ca happy with fastdissolve
    ca"Ah, väike loomake. Ma tõstaksin su kuhugi ära, aga ei taha sind eriti puudutada."
    ca"[player_name], kas sa võiksid ta ohutusse kohta panna?"
    "Sa tõstad sisaliku vaikselt ülesse ja paned ta rahulikult raja kõrvale maa peale."
    "Sisalik ootab paar hetke ja siis jookseb minema. Ta kaob põõstaste taha peitu."
    show ca happy at jumper
    ca"Ah, ta oli nii armas. Oleksin temast pilti teinud, aga ta oli nii hirmunud. Võib-olla näeme sarnaseid."
    pov"Me oleme peaaegu raja lõpus. Ma eriti ei usu, et palju rohkem näeme."
    show ca neutral with fastdissolve
    ca"Hmm, kurb. Tundub, et peab kunagi tagasi tulema."
    pov"Miks mitte? Siin on päris mõnus olnud."
    ca"Seda küll. Perega oleks hea puhkus."
    show ca neutral:
        xalign 0.1
        linear 1.0 xpos 0.4
    "Te räägite edasi ja vaikselt jõuate raja lõppu, mis on ka tegelikult raja algus."
    ca"Kas sa tahaksid, et ma viin su koju?"
    pov"Ega ma vastu ei hakka ütlema."
    "Te lähete koos ühe musta auto juurde, mis viib teid koju."
    hide ca neutral with fastdissolve
    scene bg tanav
    with fade
    "Mõnikond minutit hiljem jõuate tagasi linna."
    "Sa astud autost välja. Carina teeb oma akna lahti, et sinuga räägida."
    show ca neutral with fastdissolve
    ca"Aitäh, et tulid minuga täna. Ma ei oleks tahtnud seda üksinda teha."
    pov"Jah, muidugi. Aitäh, et mu koju tõid."
    show ca happy at jumper
    ca"Alati."
    hide ca happy with dissolve
    "Sa lehvitad Carinale kui auto minema sõidab."
    "Kui auto nurga taha kaob, astud sa maja uksest sisse."
    "Täna on olnud tore päev."
    jump end

label irene_ending:
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on vaid üks asi, mida teha: mõelda asjadele nii, nagu oleksid Vana-Kreeka filosoof."
    "Õnneks, enne kui sa saad Pythagorase teoreemist edasi mõelda, kuuled sa oma telefoni helinat. Sa võtad vastu."
    pov"Jah?"
    show ir neutral at right with dissolve
    ir"{i}[player_name], kuidas läheb?"
    pov"Hästi, hästi. Sul?"
    ir"{i}Sama. Kiire küsimus, kas sul aega on?"
    pov"Sõltub, milleks?"
    ir"{i}Noh, põhimõtteliselt, ma programmerin üht mängu onju, mul on põhimõte olemas, aga mul ei tule selle sisu jaoks ühtegi head ideed."
    pov"Mhm. Ja kuidas mina sellesse sobitun?"
    ir"{i}Mu plaan on vaadata, mis mul olemas on ning leida neist rohkem infot. Ma tahaks seda teha, aga mitte üksinda. Siin tuled sina mängu!"
    pov"Olgu, see võib lõbus olla. Kuigi ma arvaksin, et sa küsid enne Carinalt."
    ir"{i}Juba proovisin, ta läheb rabasse."
    ir"{i}Igatahes, saadan sulle kohe ühe aadressi. Proovi tunni pärast kohal olla."
    pov"Juba?"
    "See tundub nagu jube kiiresti, aga kella piiludes tuleb sulle meelde, et sul pole midagi paremat niikuinii teha."
    pov"Olgu peale."
    ir"{i}Juhuu! Näeme siis raamatukogus!"
    scene bg must
    with fade
    centered"{size=*2}Tund hiljem{/size}"
    scene bg tanav
    with fade
    "Tunni pärast kõnnid sa mööda kesklinaa tänavaid ja otsid raamatukogu, millest Irene sulle kirjutas."
    pov"(See oleks lihtsam kui iga teine tee poleks teetööde pärast kinni…)"
    "Samal hetkel kui sa ümber nurga keerad avab sinu nina ees uks. Sa astud üllatunult tagasi."
    show ir happy with fastdissolve
    ir"Seal sa oled!"
    "Irene võtab su käest kinni ja tõmbab su tuppa."
    scene bg library
    with fade
    "Esimese asjana märkad sa raamaturiiuleid."
    "Muidugi, see on ju raamatukogu."
    show ir neutral with fastdissolve
    "Irene tirib sind ühte nurka kus on üksik laud, mille peal on mõned looduse teemalised raamatud."
    ir"Ma paar raamatut olen juba leidnud, aga igaks juhuks võiks mõned veel läbi vaadata. "
    pov"Ma võin otsida neid. Mis teemaks on?"
    ir"Peamiselt erinevad ökosüsteemid või bioomid. Ma hakkan siis lugema."
    pov"Teeme siis nii."
    hide ir neutral with fastdissolve
    "Sa leiad üles looduse osakonna ja hakkad otsima."
    "Sa näed mitmeid kohti, kus on mõned raamatud puudu. Oletavasti on need praegu Irene laual."
    "Sa otsid läbi kõik riiulid, kuni jõuad osakonna lõppu."
    pov"(Ah, siin pole midagi. Äkki on Irene kõik juba ära võtnud?)"
    "Sa vaatad järgmisi riiuleid, aga need on teistsuguse teema peale.  Ühes vahes leiad inimese, kes korrastab riiuleid."
    pov"(Töötaja, ta peaks teadma, kus kõik on.)"
    pov"Vabandust?"
    "Töötaja vaatab sinu poole."
    show xy neutral with fastdissolve
    xy"Tere- [player_name]?"
    pov"Xiao? Mida sina siin teed?"
    xy"Ah, ma töötan siin vahepeal. Kas sa otsid midagi?"
    pov" Ehm, jah. Midagi ökosüsteemide kohta, ma ise ei leidnud midagi rohkemat."
    xy"Olgu, las ma vaatan."
    "Te lähete koos tagasi looduse osakonda. Xiao vaatab paar mintuit ringi, Aga tuleb tühjade kätega tagasi."
    xy"Imelik, see oleks nagu kõik sellised raamatud oleks ära varastatud. Tavaliselt on ned päris mitu."
    pov"Siis on Irene kõik ära võtnud."
    show xy neutral at jumper
    xy"Irene?"
    pov"Jah, ta vajas natuke abi ühe uue mänguga ja siin ma nüüd olen. "
    xy"Hm, ma oleks arvanud, et ta küsib Carinalt."
    pov"Tal oli midagi teha. Igatahes, aitäh, et proovisid mind aidata, ma lähen aitan Irenet edasi."
    "Xiao noogutab sulle ja sa lähed tagasi laua juurde, kus näed Irenet lugemas."
    hide xy neutral
    show ir neutral
    with fastdissolve
    pov"Tundub, et sa oled juba kõik raamatud võtnud."
    ir"Tõesti? Vabandust, et ma su aega raiskasin."
    pov"Ai ole midagi, ma olen siin, et aidata."
    pov"Kas sa teadsid, et Xiao töötab siin?"
    ir"Mida? Tegelikult ma pole üllatunud. See sobib talle."
    ir"Igatahes, me peaksime nüüd uurima hakkama. Võta need."
    "Ta annab sulle mõned raamatud, peamiselt kõrbe teemal."
    "Mõne kaanel on näha liivaluiteid ja kaamleid."
    ir"Põhimõtteliselt, kirjuta üles mõned tähtsamad asjad, mida välja loed. Asjad, mis võiksid kirjeldada ka inimest."
    pov"...Okei?"
    "Irene vaatab sind korraks."
    ir"Hmm, nagu, mägedes elav inimene on alati soojalt riides või vihmametsa inimene armastab eredaid värve ja vihma. Sellised asjad."
    pov"Olgu, vist saan aru. "
    "Sa hakkad lugema ja paned vahepeal midagi oma märkmetesse kirja. Sa näitad neid Irenele ja ta ütleb, et nendega oleks hea tegelase kirjutamist alustada."
    "Irene annab sulle järgmise bioomi ja paneb sinu märkmed omale kuhugi kirja."
    "Te teete seda uuesti ja uuesti paar tundi, kuni te mõlemad olete väsinud."
    ir"Ma arvan, et mul on piisavalt tegelasi, et midagi välja mõelda. Aitäh jälle, et appi tulid."
    pov"Ah, see polnud midagi. Mul polnud paremat teha nii või naa. Miks mitte sõpra aidata."
    ir"Ikkagi, lase mul mingi kohvi või midagi välja teha."
    pov"Sa ei pea, tõesti."
    ir"Aga ma tahan! Selle eest, et pidid vabal päeval tööd tegema. "
    pov"Kui sa nõuad. Kas peaksime Xiao ka kutsuma?"
    show ir happy at jumper
    ir"Kui me ta leiame, miks mitte?"
    show ir neutral with fastdissolve
    "Te vaatate ringi paar minutit, aga ei leia Xiaod kuskilt."
    ir"Ta on ilmselt juba ära läinud. "
    pov"Siis peame kahekesi minema."
    "Te panete raamatud oma kohtadele tagasi ja lahkute kohviku poole."
    scene bg kohvik
    with fade
    "Kohvikusse sisenedes on kohe tunda saiade lõhna."
    show ir happy with fastdissolve
    ir"Mm, siin lõhnab nii hästi!"
    "Sa vaatad seinatahvlit kus on klik erinevad joogid kirjaks ja näed leti taga tuttavat nägu."
    show xy neutral at midright with dissolve
    pov"Hei, kas see pole mitte Xiao?"
    "Irene vaatab ka leti poole. Ta kõnnib selle juurde."
    ir"Tere Xiao. Teine töökoht, ma näen."
    show xy neutral at jumper
    xy"Ah, jah. On tõesti."
    "Sa seisad Irene kõrvale."
    pov"Ei arvanud, et ma sind täna teist korda veel näen."
    xy"Ausalt öeldes, mina ka mitte. Mul on kohe paus, võin teiega natuke lobiseda."
    "Sina ja Irene tellite oma joogid ja istute ühe laua äärde. Xiao toob teie joogid ja ühineb teiega."
    "Te hängite koos kuni Xiao Peab tagasi tööle minema."
    ir"Ma peaks vist koju minema, hilja on juba."
    pov"Jah, ma ilmselt ka lähen."
    "Te astute kohvikust välja, Xiaole lehvitades."
    "Ta lehvitab tagasi."
    scene bg tanav
    with fade
    show ir neutral with dissolve
    ir"Aga aitäh jälle, et mind aitasid."
    pov"Muidugi, alati kui vaja."
    "Te mõlemad sätite sammud koju."
    jump end

label xiaoyun_ending:
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on ainult üks asi veel teha: muretseda, kas sul on midagi poest vaja, mille oled täiesti ära unustanud."
    "Õnneks, enne kui sa saad lähemalt mõelda selle peale, et kui tomat on puuvili, kas siis ketšup on moos, heliseb su telefon. Sa võtad vastu."
    pov"Jah?"
    show xy neutral at right with dissolve
    xy"{i}Hei, [player_name]. Kuidas elu?"
    pov"Praegu päris igav. Pole midagi teha eriti."
    xy"{i}Ah, jah, tean seda tunnet. Kuigi mul on sulle ettepanek."
    pov"Kuulan."
    xy"{i}Ma Aislingilt juba küsisin, aga tal oli kuhugi kiire. Kas tahaksid minuga maalima tulla? Mõtlesin, et proovin ise järele."
    pov"Ikka, mul aega on, nagu sa juba tead."
    xy"{i}Lahe."
    hide xy neutral with fastdissolve
    "Peale kõne sätid sa end valmis Xiaoga kokku saamiseks."
    scene bg tanav
    with fade
    "Mõne tunni pärast seisad sa ühe kunstistuudio ees ja ootad Xiaod."
    "Sa pole kunagi siin linna osas käinud ja vaatad sellepärast ringi. Kõik majad näevad välja vanad, nagu oleksid pärit renessansi ajast."
    "Peale mõne minuti ilmub Xiao välja."
    show xy neutral with fastdissolve
    xy"Hei."
    pov"Tsau. See maja siin, eks?"
    xy"Täpselt nii."
    "Te astute koos sisse."
    scene bg muusika
    with fade
    show xy neutral with fastdissolve
    "Esimesed asjad, mida on toas näha on värvid ja taimed."
    "Igal seinal on näha erinevaid postreid ja kunstiteoseid, nurkades on poolikud skulptuurid, iga kapp ja iga riiul on täis kunstitarbeid ning igal aknalaual on vähemalt paar ilusat taime."
    "Toas on ainult mõned inimesed. Üks vanem naine maalib midagi seinale ja paar algklassi last ning nendest vanem tüdruk, kes neid õpetab ja kes tundub sulle tuttav."
    "Xiao paneb oma kotti ühe laua peale ning läheb ühe kapi juurde, et asju võtta. Sa paned oma asjad sama laua peale ning lähed Xiao kõrvale."
    pov"Mis sul plaan teha?"
    xy"Täpselt ei oska öelda. Ma lihtsalt võtan mõned asjad ja vaatan, mis välja tuleb."
    pov"Ah."
    "Xiao hakkab vaikselt nokitsema ning sina vaatad vaikuses paberit oma ees."
    pov"(Mida küll teha?)"
    hide xy neutral with fastdissolve
    "Sa vaatad korraks õue. Puud vaikselt kõiguvad tuule käes, päike paistab eredalt ja taevas on ainult paar pilve."
    "Sa vaatad tagasi tuppa. Naine on lõpetanud oma seinamaali ja seisab selle ees uhkelt. Lapsed on läinud tema juurde, et selle kohta küsida ja tüdruk, kes nendega kaasas oli vaatab sulle otsa."
    pov"(Ah. Aisling?)"
    "Sa lehvitad talle, ta lehvitab vastu ja kõnnib teie juurde."
    show ai neutral at midleft
    show xy neutral at midright
    with fastdissolve
    ai"[player_name]! Xiao! Mida teie siin teete?"
    xy"Hei, Aisling. Ma küsisin sult eile kas tahad minuga maalida, aga sul oli tegevust, mäletad? [player_name] tuli sinu asemel kaasa."
    pov"Ma ei oodanud, et sa siin oled. Mida sa nende lastega teed?"
    ai"Ah, nemad. Ma olen tegelikult selle naise assistent. Lapsed käivad temaga siin kunsti teraapias ja nad tahtsid, et ma kaasa tuleksin."
    show ai happy with fastdissolve
    ai"Muidugi ütlesin ma jah, sest nagu, kes ei tahaks siin oma aega veeta! See on vist mu lemmik koht terves maailmas."
    pov"Mm, see on lahe. Kas sul on veel palju tööd? Sa võid meiega hängida."
    ai"Ah, ei saa väga. Ma pean parki minema ühe asja jaoks kohe kui siin kõik tehtud. Aga aitäh pakkumast!"
    show ai neutral with fastdissolve
    "Aisling läheb tagasi oma laua juurde ja paneb oma asjad kokku. Ta ütleb naisele ja lastele head aega ja lahkub stuudiost. Xiao lehvitab talle."
    hide ai neutral with fastdissolve
    "Xiao vaatab sinu poole ja näeb, et su paber on täiesti tühi."
    show xy happy with fastdissolve
    xy"Pole inspiratsiooni?"
    pov"Tegelikult, mul tuli just täiuslik idee."
    "Sa hakkad kritseldama, Xiao läheb oma töö juurde tagasi."
    hide xy happy with fastdissolve
    "Mitu minutit läheb mööda, te mõlemad tegeleta vaikuses oma tööga. Naine ja lapsed on ära läinud, nii et te olete kahekesi."
    show xy neutral with fastdissolve
    "Sa näed oma silmanurgast kuidas Xiao võtab välja oma luuletuste märkmiku ja kirjutab midagi sisse."
    pov"Mida sa kirjutad?"
    xy"Lihtsalt üks väike asi, mis mul pähe tuli."
    pov"Kas ma võin küsida mis see on?"
    "Xiao on korraks vait."
    xy"Võib-olla hiljem."
    "Sa noogutad ja te hakkate jälle tööle. Õhtu hakkab lähenema, kui te valmis saate. Xiao näitab sulle oma joonist."
    xy"Ma proovisin mitu asja kokku panna ühte joonisesse, aga ma ei tea kui hästi see välja tuli."
    "Joonis on nii täidetud, et peaaegu pole aru saada, mis selles toimub. Selles on igasuguseid jooni ja kujundeid ning värve rohkem kui ma oleks suutnud ette kujutada."
    pov"See on väga segane. Aga kuidagi ka rahulik. Huvitav."
    xy" Peaks Aislingilt küsima, äkki olen kogemata uue stiili loonud. Näita nüüd enda oma."
    "Sa annad Xiaole enda joonise."
    xy"Hm? Kas see on meie klubi tuba?"
    pov"Nii palju kui ma suutsin seda ette kujutada. Aisling ütles, et see on tema lemmik koht terves maailmas ja ma hakkasin mõtlema, mis oleks minu versioon sellest stuudiost?"
    show xy happy with fastdissolve
    "Xiao naeratab."
    xy"See klass hoiab palju mälestusi."
    "Xiao mõtleb korra ja võtab jälle välja oma märkmiku. Sa proovid piiluda üle ta õla, aga ta paneb selle kiiruga kinni."
    show xy sigh with fastidssolve
    xy"Vabandust, mulle ei meeldi, kui inimesed mu mustandeid vaatavad."
    pov"Ah, vabandust. Ma tahtsin lihtsalt teada, mida sa enne kirjutasid."
    "Xiao tõuseb püsti ja annab sinu joonistuse tagasi."
    show xy neutral at jumper
    xy"Pole midagi. Kas hakkame minema? Peaaegu on õhtu."
    "Sa noogutad ja te panete oma asjad kokku."
    scene bg tanav
    with fade
    "Tagasi kõnd on vaikne. Sa mõtled, kas peaksid äkki jälle vabandama, et Xiao märkmiku vaatasid."
    show xy neutral with fastdissolve
    xy"Tühjus ja vaikus."
    "Sa vaatad segadusega Xiao poole."
    xy"Kaalutlus ja andekus. Kavatsus ja leidlikus. Üksteisest vahel sõltuv. Üksteise peale toetuv."
    xy"Koht, kus ma alati tahan olla? Seal, kus ma näen su hinge hella."
    "Sa plaksutad vaikselt. Xiao vaatab maha."
    xy"See on väga huvitav, kuidas hetked suudavad ennast mõteteks muuta. Sellepärast mulle meeldivadgi luuletused, need ütlevad nii palju rohkem, kui sa alguses arvad."
    "Sa noogutad vaikselt. Te kõnnite edasi mõnusas vaikuses."
    jump end

label koos_end:
    play music "chill bg.mp3" fadeout 1.0 fadein 1.0
    scene bg livin
    with fade
    "Nagu iga nädalavahetus möödub laupäeva hommik aeglaselt."
    "Su vanemad on kodust ära, seega väga palju pole teha."
    "Sa oled kolme tunniga jõudnud ära teha kõik oma kodutööd ning söönud hommikusööki."
    "Nüüd on ainukene asi mida teha: lõõgastuda. Pikk nädal on möödas."
    "Ühel hetkel, kui sa olid just peaaegu magama jäänud, kuuled sa oma telefoni teate helinat."
    "Sa võtad telefoni kätte ja avad gruppi vestluse “Loovuse klubi”."
    show ca neutral at midright with dissolve
    ca"{i}Tere, kõik! Ma tahtsin küsida, kas teil on täna/homme vabat aega? Mõtlesin, et võiksime kokku saada ja midagi teha."
    show ir neutral at midleft with fastdissolve
    ir"{i}Yeah, ma peaks saama"
    hide ir neutral
    show xy neutral at midleft
    with fastdissolve
    xy"{i}ma olen täna vaba küll"
    hide xy neutral
    show ai neutral at midleft
    with fastdissolve
    ai"{i}Mul on üks väike töö asi, aga ma saan varsti ära."
    hide ai neutral
    show gl neutral at midleft
    with fastdissolve
    gl"{i}ma vaba"
    hide gl neutral with fastdissolve
    pov"{i}Mul ka on aega. Mis plaanis on?"
    show ca happy at jumper
    ca"{i}Õues on ilus ilm. Minu pakkumine oleks pikniku teha."
    show ai happy at midleft
    ai"{i}Ooh, äkki lähme randa? Ei tund eriti tuuline!"
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    xy"{i}Äkki paneme mõlemad kokku?"
    hide ai neutral
    show ir neutral at midleft
    with fastdissolve
    ir"{i}Nagu lähme randa pikniku pidama?"
    pov"{i}Kõlab lõbusalt."
    hide ir neutral
    show gl neutral at midright
    with fastdissolve
    gl"{i}näeme seal"

    scene bg rand
    with fade
    play mar "sea go brr.mp3" fadeout 1.0 fadein 1.0
    "Paarikümne minuti pärast jõuad sa kodu lähedal olevasse randa."
    "Ilm on tõesti ilus, päike on väljas, taevas pole peaaegu ühtegi pilve ja tuul on ka nii vaikne, et peaaegu pole tunda."
    "Sa vaatad korraks oma käes olevat kotti, mis on täis erinevaid küpsiseid."
    pov"(Ma loodan, et see on piisavalt.)"
    show ir neutral at midleft
    show ca neutral at midright
    with fastdissolve
    "Mõnesaja meetri kaugusel sa näed üht blondi pead ja üht punast pead. Nad vaatavad sinu poole ja lehvitavad. Sa lehvitad vastu ja kõnnid nende poole."
    pov"Hei! Irene, Carina!"
    show ca happy at jumper
    ca"[player_name]! Kuidas su nädalavahetus on läinud?"
    pov" Täitsa hästi. Tegin hommikul mõned asjad ära, nii et saan rahulikult siin hängida."
    show ca neutral with fastdissolve
    ir"Väga tore! Kas sul on aimu, millal teised jõuavad?"
    pov"Ei, kahjuks mitte-"
    show gl neutral at right with fastdissolve
    "Just sellel hetkel tuleb Glass, vaikne nagu hiir, sinu kõrvale seisma."
    gl"Xiao peaks varsti jõudma ja Aislingil läheb veel aega."
    show ca neutral at jumper
    "Carina võpatab korra, aga taastub kiiresti."
    ca"See on hea. Oh! Glass, sa tõid midagi kaasa? [player_name], sina ka?"
    "Glassil on käes väike kilekott."
    show gl sigh with fastdissolve
    gl"Ehm, jah? Palju aega mul polnud, nii et ainult mõned kommid."
    show gl neutral with fastdissolve
    show ir neutral at jumper
    ir" See on nii armas sinust! Pane need meie asjade hulka. Me ei arvestanud, et te ka poes käite. Vist on natuke palju asju."
    pov"Küll me midagi välja mõtleme."
    "Sina ja Glass panete oma kotid pikniku teki peale, teiste asjade hulka."
    "Carina ja Irene olid päris mitu asja kaasa toonud: pirukaid ja leibu, puu- ja köögiviljad ning erinevaid jooke."
    ir" Hehe, me saame ülejäägid kaasa võtta."
    hide ca neutral
    show xy neutral at midright
    with fastdissolve
    "Sa vaatad tagasi ranna sissekäigu poole ja näed üht tuttavat nägu."
    "Sa lehvitad Xiaole ja teised märkavad ka teda. Xiao kõnnib teie juurde."
    xy"Tsau, kõik."
    gl"Hei."
    ir"Tsau!"
    show ca neutral at left
    with fastdissolve
    ca"Tere! Kuidas läheb?"
    xy"Täitsa hästi. Aisling peaks ka kohe varsti jõudma. Nägin teda ühe stuudio juures, mida tahtsin vaadata ja ta ütles, et oli peaaegu tööga valmis."
    ir"Ah jah. Ta mainis vestluses ka mingit tööd. Huvitav, mida ta küll seal teeb?"
    ca"Ei oska öelda, peame talt küsima."
    pov"Xiao, kas sa ka tõid midagi?"
    show xy neutral at jumper
    xy"Ah, õigus."
    "Xiao näitab termost, mida käes hoidis."
    xy" Mul tekkis korraks koduigatsus ja tegin teed. Mõtlesin, et selle kaasa võtta ja teile maitsmiseks anda."
    show ca happy at jumper
    ca"Ah, nii armas sinust!"
    show ca neutral with fastdissolve
    ir"Olgu, meil on siis ainult Aisling vaja ära oodata, eks?"
    hide xy neutral
    show ai neutral at midright
    with fastdissolve
    ai"Hei!"
    "Irene jõuab vaevu oma lauset lõpetada, kui Aisling ilmub ähkides tema kõrvale nagu oleks ta mitu kilomeetrit jooksnud."
    ai"Heh, vabandust, heh, et hiljaks jäin."
    ca"Pole midagi! Vähemalt tulid kohale."
    ir"Mhm, poleks sama, kui keegi oleks puudu."
    "Xiao ja Glass noogutavad. Aisling naeratab."
    ai"Seda küll. Ma tõin vabanduseks natuke head süüa kaasa."
    hide ai neutral
    show xy happy at midright
    with fastdissolve
    "Irene ja Carina vaatavad üksteist. Xiao itsitab."
    hide ir neutral
    hide ca neutral
    show gl neutral at midleft
    with fastdissolve
    gl"Meil jääb kindlalt asju üle."
    "Mis see ütlus on? Aeg lendab kui sul on lõbus? Mis iganes see ka poleks, nii sa tundsiki ennast."
    hide xy neutral
    hide gl neutral
    with fastdissolve
    "Mitu tundi läks mööda, mis sulle tundus nagu mõnikümmend minutit. Te rääkisite kõigest, mis pähe tuli."
    "Te suutsite ära süüa (peaaegu) kõik, mille olite kaasa toonud ning oli tunda, kuidas Irenel ja Carinal oli niimoodi lihtsam hingata."
    "Sellest päevast jäävad sulle igaveseks mälestused. Mõned paremad kui teised."
    show ca neutral at midright
    show ai neutral at midleft
    with fastdissolve
    ca"Nii et, Aisling. Kas sa võibolla ütleksid meile, mis töö see on, mille pärast sa natuke hiljaks jäid?"
    ai"Kõik vaatavad Aislingi poole, kui ta jutustama hakkab."
    ai"Ah jah, see. Noh tegelikult olen ma ühe kunstiterapeuti assistent. Ainult poole kohaga, muidugi, koolis peab ju ka käima."
    ai" Peamiselt aitan teda, kui ta tegeleb lastega. Ta ütles, et saan nendest ja nende joonistustest paremini aru kui tema, nii et vahel olen seal."
    hide ca neutral
    show ir neutral at midright
    with fastdissolve
    ir"Tõesti? Väga sinulik töö kui ma võin öelda."
    hide ir neutral
    show xy neutral at midright
    with fastdissolve
    xy"Mhm. Huvitav ka, kuidas sina saad aru paremini lastest kui litsentsiga terapeut."
    pov" Ilmselt kuna sa oled vanuse mõistes nendega lähedasem."
    hide xy neutral
    show gl neutral at midright
    with fastdissolve
    gl"Pluss sa oled alati olnud tähelepanelik, nii et sul on lihtne inimesi lugeda."
    show ai happy with fastdissolve
    "Aisling naeratab Glassile ja nüksab tema õlga."
    ai"Teie, muusikud, ja teie sügavad mõtted."
    "Teised itsitavad Aislingi sõnade peale."
    "Te räägite mõnda aega jälle oma eludest."
    hide ai happy
    hide gl neutral
    show xy neutral at midleft
    show ca neutral at midright
    with fastdissolve
    "Xiao mainib kuidas tal on ka päris mitmes kohas poolekohaga töö ning Carina imestab selle peale, kuna ta ei oodanud, et üks inimene suudab nii palju erinevaid asju korraga teha."
    "Xiao ainult kehitab õlgu selle peale."
    hide xy neutral
    hide ca neutral
    show gl neutral
    with fastdissolve
    "Glass räägib kuidas tal on plaan uut muusikat hakkata kuulama ning küsib teistelt soovitusi. Päeva lõpuks on tal uus seitsme tunnine esitusloend, mida ära kuulata."
    hide gl neutral
    show ir neutral at midleft
    show ca neutral at midright
    with fastdissolve
    "Irene ja Carina seletavad lahti uue mängu ja selle disaini, mille plaanivad järgmiseks aastaks valmis saada."
    "Nüüd imestavad kõik selle peale, kuidas Carina saab nii vabalt käia ringi, kus iganes tahab. Carina teeb ettepaneku nad kunagi kaasavõtta, millega kõik ilmselgelt nõus on."
    "Ühel hetkel hakkab vestlus minema natukene teises suunas."
    pov"Mida teil on plaanis tulevikus teha? Ma poleks üllatunud, kui te otsustaksite teha midagi suurt."
    hide ca neutral
    hide ir neural
    with fastdissolve
    "Kõik mõtlevad paar hetke."
    show xy neutral at midleft with fastdissolve
    xy"Noh, kindel ma täpselt pole. Ilmselt midagi luuletustega, üllatus üllatus."
    show gl neutral at midright with fastdissolve
    gl"Ma mõtlen sarnaselt. Midagi muusikaga, kaugemale ma pole veel mõelnud."
    hide xy neutral
    show ir neutral at midleft
    with fastdissolve
    ir" Ma tahaksin reisida. Leida uut inspiratsiooni mängude jaoks."
    hide gl neutral
    show ca neutral at midright
    with fastdissolve
    ca"Sellega saan ma aidata. Ma tahan lihtsalt teha midagi, mis mind huvitab. Võibolla cosplay, võibolla tuleb mulle pähe midagi muu."
    hide ir neutral
    show ai neutral at midleft
    with fastdissolve
    ai"Midagi loovat. Äkki olen ka tulevikus terapeut nagu mu mentor. Kunagi ei tea."
    pov"Seda küll. Tulevik on piiritu ja hirmus."
    scene bg must
    with fade
    pov"Aga mul on sõbrad, kes on alati olemas, kui ma neid vajan."
    stop mar fadeout 1.0
    jump end

#End
label end:
    scene bg must
    with fade
    play music "chill night music.mp3" fadeout 1.0 fadein 1.0
    centered"{size=*2}Mängu lõpp{/size}"
    centered"{size=*2}Täname mängimast!{/size}"
    centered"{size=*2}Dialoog - Lehtmets{/size}"
    centered"{size=*2}Tegelaste spraidid - Õispuu{/size}"
    centered"{size=*2}Programmeerimine - Kupits{/size}"
    return
