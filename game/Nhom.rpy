label Nhom_handler:
    if charProgress["Nhom"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Nhom" + storyTag[charProgress["Nhom"]])



label Nhom_beg:
    "You wander into the local tavern in search of a buzz after the long day of meeting the town’s people so you’ve made the executive decision to unwind by {p=1} {i}drinking{/i} with the town’s people… The grind never really stops"
    "Walking into the tavern, you’re mildly surprised about the misleading exterior which leads into a cozy welcoming bar with a few townspeople milling about"
    "A dagger suddenly whizzes past, narrowly missing your ear. You gawk at the embedded dagger on the darts board"
    w "My bad, dude! Didn't expect you to suddenly appear"
    "You look around wildly, spotting no one that looks like they could have plausibly endangered your life"  
    MC "...Hello is someone there? You didn't think I would enter through the door?"
    w "Pssh of course you can’t see me. You don’t take down super villains by allowing some randos to see you all willy nilly.The big boss has taught us much better than whoever your sad disappointed teacher is" 
    w "Also, as a matter of fact my brethren and I verified there are at least 31 better ways to escape this hovel before we got stopped by the big boss"
    MC "Sorry, who's this 'Big Boss' you speak of? I don't think I've met them yet"
    w "Man, not only are you a rando but you’re also a scrub that doesn’t know the big boss? Sir %(tname)s the Great, the Magnificent."
    w "The All Powerful"
    w "Adventurer of our Century"
    w "Defender of those within a 10.2 meters squared radius"
    w "132 times (and counting) Challenger of the Giant Thundrone himself"
    w "{size=+10}Nhom the dwarf{/size}"
    MC "…. Dwarf?" 
    "You stifle your internal cackles. Must channel professional, charismatic vibes. A dwarf they say? Ha!"
    "You feel the woosh of yet another dagger. This time actually embedding your sleeve into the nearby wall."
    "Apparently not stifled well enough. Before you make the decision to attack the invisible voice or escape the death tavern"
    show Nhom angry with moveinright
    w "LITT NÉE LE. What did I say about throwing sharp objects indoors and using when we're in %(tname)s ?! Also this is the 10th time today that I told you not to use Eestanc to prey on the defenseless" 
    "Oh my goodness. Is that Nhom? Is this really the supposed dwarf??? You can’t help staring at this larger than life entity that’s at least a head taller than you" 
    w "Boss!! You taught us to uphold honor and justice. This … this scrub! Cretin! Besmirched your good name. I couldn’t allow that"
    "You nervously eye Nhom, trying to gauge if now is the time to finally flee the scene. His whole demeanor unreadable now. Wow, those are some sharp looking weapons holstered to Nhom’s side"
    "Suddenly, he’s right in front of you and his hand is wrapped around the back of your neck"
    MC "AHHHHHHHHH"
    "As he …strikes? No wait…pats? Your neck" 
    Nhom "Well Litt that just means they haven’t been enlightened in hearing about the Tales of Nhom. Well we can change that with the recounts of"
    Litt "The Awe-Inspiring Nhom %(tname)s "
    Nhom "Would you like to hear about the Fight Against Crastination de Pro, Demise of da Finelles,"
    "Wait. Wait. Stop. I can feel a long monologue coming"
    MC "Actually, I'd love to hear more about your own background. I'm [name], your mayoral elect hopeful. Let me know what I can do to secure your vote!"
    Nhom "Aye! Will do. I can solve my own problems though!"
    Litt "Adversity quakes at the sight of big Nhom"
    #try to make this section rhyme or epic-ify 
    Nhom "Escaping my burdensome fate of inheriting the tavern of %(tname)s "
    Litt "The only one to escape the fate since the town’s founding, the envy of his sisters and brothers"
    Nhom "The first dwarven adventurer to go down in legends"
    Litt "Slowly, saving me and my brethren, us wanderers given at last a greater mission of freedom and reckless adventures"
    Nhom "Oi! Sticky fellows I couldn’t shake off but my comrades in arms" 
    Litt "Not against Thundrome! Your ol’ foe of many moons"
    Nhom "Certainly against Prat!"
    Litt "{size=+10} Nhom the Magnificent {/size}.{size=+1} Magnificent {/size} {size=-20} ficent {/size}" 
    Nhom "For I shall bring more glory to %(tname)s "
    "You nod politely before excusing yourself for the night.  Nhom and invisible Litt joyfully bursting out in song, with more invisible voices (most likely of the brethren Litt mentioned?) joining in."
    "That was certainly enough socialization and schmoozing with the townspeople for the night"
    "Walking out the door, you wonder did Nhom mention fighting against that Thundrome that Terrifying Giant? Perhaps, Nhom would take upon himself another heroic adventurous task."
    $ charProgress["Nhom"] +=1
    jump ending_handler


    
    
