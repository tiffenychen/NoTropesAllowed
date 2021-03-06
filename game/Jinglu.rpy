image bg wall:
    zoom 1.2
    "wall.jpg"
image bg nightmarket:
    zoom 1.2
    "nightmarket.png"
image table = "table.png"

label Jinglu_handler:
    if charProgress["Jinglu"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Jinglu" + storyTag[charProgress["Jinglu"]])

label Jinglu_beg:
    scene bg marketplace
    "It's really about time you stop by the marketplace to get some groceries for yourself. And right now, your road travel rations are starting to dwindle and you figure a quick break for some shopping won't hurt."
    "You scan the limited stall options, trying to figure out where to start your new stockpile, and land on fresh veggies first—you've had to eat a disturbing amount of jerky and hardtack while on the road, so you need the change."
    show Nhom neutral at center with moveinleft
    "Unfortunately, a dwarf makes it to the stall slightly before you and you're forced to wait behind him."
    w "Didn't you just restock yesterday, Nhom?"
    show Nhom angry
    Nhom "Aye. A certain demon put a dent in that though."
    w "Oh, haha, which of the kids was it this time?"
    show Nhom confused
    Nhom "No, I mean Jinglu."
    show Nhom angry
    Nhom "It's a real shame no one's had the guts to deal with him yet."
    w "Aren't you an adventurer...?"
    show Nhom neutral
    Nhom "Yes, well... You know how it is."
    w "I'm not sure I do?"
    show Nhom sad
    "You decide to valiantly step in as Nhom flounders a little for a response."
    show Nhom neutral
    MC "Excuse me, but I couldn't help overhearing that there's an issue with a demon?"
    show Nhom angry
    "Nhom turns to you and huffs, clearly annoyed just thinking about the situation."
    Nhom "Aye, that would be correct. He took down my house and most of the stuff inside it last night. It was lucky no one else was home or they surely would have been crushed in the debris."
    "You try to put on a very sympathetic look instead of a horrified one."
    show Nhom neutral
    MC "That's terrible! Can I come help you fix things up?"
    "Nhom waves his hand dismissively"
    Nhom "Oh, don't worry about it. I already had a fair few helpers fix up most of it. The structural damage wasn't as bad as I had expected with the amount of house that was spread out everywhere, so I suppose it could be worse."
    Nhom "We did everything back up real quick and that's why I'm out shopping now."
    MC "Oh, can you at least tell me what he looks like, so I know for the future?"
    show Nhom angry at left with move
    show Jinglu angryh:
        xalign .75
        alpha 0.0
        linear 4.0 alpha 1.0
        on replace:      # when new image appears
            alpha 0.0
            linear 4.0 alpha 1.0
        on replaced:     # when old image disappears
            linear 4.0 alpha 0.0
    Nhom "You can't miss him. {w} Shady looking fellow {w}with some twiggy horns and hooves. {w}He's always wearing a lot of fancy clothes. {w}I'm surprised he doesn't get all tangled up in when he runs off after his misdeeds."
    hide Jinglu
    show Nhom angry at center with move
    MC "He ran off?"
    show Nhom neutral
    Nhom "Always does, probably knows he can't handle a real confrontation."
    MC "I see. Well, thanks so much for sharing! I'll keep my eyes peeled and see if I can't do anything about him!"
    show Nhom neutral at center, hop
    Nhom "You do that. I'll see you around."
    "Nhom picks up the bags of items the shopkeeper was filling while you two talked. It's a lot and you're surprised the shopkeeper knew what Nhom would want. Perks of living in a small village you suppose."
    hide Nhom with moveoutleft
    "You then realize you didn't think about what vegetables you would want the entire time you were waiting your turn."
    MC "Uh.... Could I get-"
    $ charProgress["Jinglu"] +=1
    jump ending_handler

label Jinglu_med:
    scene bg nightmarket
    "The marketplace seems oddly empty right now. You understand this is a small village, but even so you expect at least a shopkeep or two to be closing up their stalls right now."
    "Not very long after that thought, voices drift over from the other end of the marketplace and for some reason"
    scene bg wall with Fade(.25, 0, .75, color="#000")
    "You automatically hide behind the nearest empty stall."
    "You realize after hiding that it's super weird to do this, but also the voices are closer now and if you make yourself known that will be even weirder."
    "You decide to hold tight."
    w "I told you no one would be here today. It's fine."
    scene bg nightmarket
    show Kaelin at sright
    show Jinglu sil at sleft
    show table:
        zoom 1.2
        yalign 1.0
    with dissolve
    "That's suspicious. You decide to peek out and see who else in this town is being suspicious aside from you."
    "Is that... The person on the poster? Kaelin was it? And..."
    show Jinglu worry at sleft with dissolve
    "You look over toward the second person"
    scene bg wall with Fade(.25, 0, .75, color="#000")
    "and quickly duck back, heart pounding when you realize who the pair might be."
    "That second person perfectly matches the description of Jinglu that Nhom gave you."
    "And if he's meeting the person who advertises any service for a price..."
    "You thank your lucky stars you hid."
    Jinglu "I suppose you usually are. Perhaps I do worry too much."
    Kaelin "I don't understand why you don't stand up for yourself more. Or let me do it."
    Jinglu "You really don't need to worry about me. I've handled myself this long."
    "A heavy silence descends over the pair and you hear your own blood rushing in your ears."
    "Eventually, Jinglu speaks."
    Jinglu "I have the raw silk you wanted."
    Kaelin "At least you know how to hold up your end of the bargain."
    "You think you hear suppressed laughter tinting Kaelin's words. It makes you wonder what her end of the bargain is."
    Jinglu "Of course, I wouldn't dream of crossing you."
    "The sound of cloth against cloth rustling and a playful shove hits your ears. Then the footsteps start moving away. It doesn't sound like they'll be addressing what Kaelin is going to do in exchange for the raw silk."
    "You wait another beat or two after the footsteps disappear before you come out from behind the stall."
    "You look toward the direction they left in and wonder how well the two actually know each other and what their plan is, but—deciding you don't want to be caught if they come back—you beat a quick retreat from the scene."
    $ charProgress["Jinglu"] +=1
    jump ending_handler

label Jinglu_end:
    "You trudge into the forest with determination as you decide it's time to finally confront this Jinglu character about everything he's been doing to the village."
    "Everything like the... house you presumed he destroyed because he was around when it happened? Actually, you weren't even around for that and it didn't sound so bad if Nhom got it fixed up that same day. Jinglu didn't even stick around to gloat like a proper villain."
    "But there was that time he was with Kaelin!"
    "They were walking around all shady like and... talking. Actually, Kaelin seemed pretty happy after that encounter and you can't recall anything particularly bad happening right after."
    "Honestly, that doesn't sound so bad either."
    "You're starting to feel like maybe you don't have anything to confront Jinglu with, but to heck with it! You're already too far into the forest to turn back."
    "Speaking of, this forest really is starting to feel spooky. Was it this chilly when you started your hike? Is Jinglu really in this forest? Are you still headed the right way?"
    "Maybe you should have brought reinforcements, but no one seemed particularly keen to come with this time."
    "No matter! You're perfectly capable of dealing with this yourself! It will be perfect proof what a good mayor you will be if you can solve these issues on your own!"
    "A branch cracks under your foot and you startle. To your right, you hear what sounds like the smack of hard hooves against soft grass followed by some shushing sounds."
    show Jinglu sil at offscreen with moveinright
    "You pull back the branches between you and the sounds and spot the man himself standing over a deer menacingly-"
    show Jinglu sil at center with move
    "...."
    show Jinglu happy at center with dissolve
    "Running his fingers over the deer's scalp?"
    Jinglu "You can come out if you want."
    MC "Ye, of course! For sure."
    show Jinglu smirk
    "You awkwardly pull yourself through the branches into the small clearing, letting the branches rake over your skin and dislodging more of the brush in the process. The deer eyes you warily throughout the process."
    hide Jinglu
    show Jinglu worry at center, hop
    "Jinglu gasps."
    Jinglu "Oh no! How bad is it?"
    hide Jinglu with dissolve
    MC "What?"
    show Jinglu worryh with dissolve
    "He rushes over and turns your arm around in his hand to reveal a gash."
    Jinglu "Not too bad... Just give me a second."
    "You stare, dumbfounded, as a couple shadowy creatures present what looks like a roll of bandages and some herbs to Jinglu. Then the man proceeds to treat your wound while he talks through your silence."
    show Jinglu happyh
    Jinglu "I wasn't expecting you to actually come out here you know. People always say they're going to 'come visit,' but no one wants to make the trek."
    "Jinglu laughs, but it doesn't sound right. You continue to stare at him and he stops what he's doing."
    show Jinglu blushh at center, hop
    Jinglu "Oh, sorry, I didn't even ask if I could-"
    MC "No, go on."
    show Jinglu sadh
    "Jinglu starts wrapping the bandage on."
    Jinglu "Sometimes I think maybe I should find somewhere else to stay. The people here simply don't seem comfortable around me."
    menu:
        "A fresh start could be good":
            MC "I still don't know you very well, but you're right. They all seem to assume the worst of you and I don't think you deserve it."
            MC "I think you need a new start."
            "You think this must be the best choice for both him and you. You've 'dealt with' the demon living nearby and he gets to find people who will treat him right."
        "They just need to understand you better":
            MC "No."
            show Jinglu worryh
            "Jinglu looks up at you, surprised."
            MC "I just met you and I can already tell you're a good person... or demon or whatever."
            MC "I'm not sure what was happening with the destroyed houses and stuff."
            show Jinglu blushh
            "Jinglu blushes."
            Jinglu "Oh, if this is about Nhom's house, I was actually trying to help put the place back together. A freak storm had blown through the forest and when I followed it to make sure things were okay, I found Nhom's house at the end."
            Jinglu "Unfortunately, he came back before I finished fixing everything and I had to leave; I didn't think he would want to see me."
            show Jinglu happyh
            MC "I think you just need to talk to everyone and let them know the real you."
            MC "Actually it sounds like you help people behind the scenes a lot. Maybe they'll actually vote you into office instead of me."
            "Jinglu laughs with you at your joke."
            Jinglu "Oh, I didn't realize I was in the running. Kaelin must have been serious about entering my name."
            $ charProblems["Jinglu"] = True
    show Jinglu happyh
    "Jinglu finishes tying up the bandage and hums. The sound is pleasant like he's finally made up his mind about something."
    Jinglu "Thank you for saying that. I think I know what I need to do."
    show Jinglu worryh
    Jinglu "I have some preparation to do though. You should probably go so you can take care of that arm."
    show Jinglu happyh
    MC "Okay, sure. Thanks, and good luck."
    hide Jinglu happyh with dissolve
    $ charProgress["Jinglu"] +=1
    jump ending_handler
