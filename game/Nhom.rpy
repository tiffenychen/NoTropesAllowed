label Nhom_handler:
    if charProgress["Nhom"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Nhom" + storyTag[charProgress["Nhom"]])

$ end_nhom = "u"

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
    Litt "Boss!! You taught us to uphold honor and justice. This … this scrub! Cretin! Besmirched your good name. I couldn’t allow that"
    "You nervously eye Nhom, trying to gauge if now is the time to finally flee the scene. His whole demeanor unreadable now. Wow, those are some sharp looking weapons holstered to Nhom’s side"
    show Nhom angry:
        zoom 1.3
        xalign .5
        yalign 2.0
        linear .5 yalign 1.0
    "Suddenly, he’s right in front of you and his hand is wrapped around the back of your neck"
    MC "AHHHHHHHHH"
    with vpunch 
    "As he …strikes? No wait…pats? Your neck" 
    show Nhom happy:
        zoom 1.0 
        xalign .7
        yalign 1.0 
    Nhom "Well Litt that just means they haven’t been enlightened in hearing about the Tales of Nhom. Well we can change that with the recounts of"
    Litt "The Awe-Inspiring Nhom %(tname)s "
    Nhom "Would you like to hear about the Fight Against Crastination de Pro, Demise of da Finelles,"
    "Wait. Wait. Stop. I can feel a long monologue coming"
    MC "Actually, I'd love to hear more about your own background. I'm  your mayoral elect hopeful. Let me know what I can do to secure your vote!"
    Nhom "Aye! Will do. I can solve my own problems though!"
    Litt "Adversity quakes at the sight of big Nhom"
    #try to make this section rhyme or epic-ify 
    show Nhom happy:
        linear .5 xalign .75 yalign 1.0 
    Nhom "Escaping my burdensome fate of inheriting the tavern of %(tname)s "
    Litt "The only one to escape the fate since the town’s founding, the envy of his sisters and brothers"
    show Nhom happy:
        linear .5 xalign .25 yalign 1.0
    Nhom "The first dwarven adventurer to go down in legends"
    Litt "Slowly, saving me and my brethren, us wanderers given at last a greater mission of freedom and reckless adventures"
    show Nhom neutral at center, hop
    Nhom "Oi! Sticky fellows I couldn’t shake off but my comrades in arms" 
    Litt "Not against Thundrome! Your ol’ foe of many moons"
    Nhom "Certainly against Prat!"
    Litt "{size=+10} Nhom the Magnificent {/size}.{size=+1} Magnificent {/size} {size=-20} ficent {/size}" 
    show Nhom neutral at center, shake 
    Nhom "For I shall bring more glory to %(tname)s "
    hide Nhom with moveoutleft
    "You nod politely before excusing yourself for the night.  Nhom and invisible Litt joyfully bursting out in song, with more invisible voices (most likely of the brethren Litt mentioned?) joining in."
    "That was certainly enough socialization and schmoozing with the townspeople for the night"
    "Walking out the door, you wonder did Nhom mention fighting against that Thundrome that Terrifying Giant? Perhaps, Nhom would take upon himself another heroic adventurous task."
    $ charProgress["Nhom"] +=1
    jump ending_handler
label Nhom_med:
    "You head to the tavern yet again to both unwind for the day and hopefully hear some useful information from the looser lipped drunks that could help with your candidacy"
    "What is needed to run a successful mayoral campaign anyways? That Gladrock fellow described this town’s desperate need for a hero to rid this town of three villainous troublemakers."
    "You muse as you try to flag down a drink from the nowhere to be found bartender" 
    "Does being a conqueror of villains even equate to being qualified as a mayor anyways? You guess so, who are you to say what being a mayor is in %(tname)s? This may finally be the one to cinch the win. Else…what do they say about lucky number 11?"
    "You get interrupted from your musings by the shouts from the back"
    w "NHOM one of your brats emptied out half of our mead"
    show Nhom neutral:
        xalign .8
        yalign 0
        linear .5 yalign 1.0
    "Suddenly, one of the floor boards shift and out pops Nhom"
    show Nhom confused at center, shake
    Nhom "HEY! You don’t know if it was {i}just{/i} one of them, it could have been multiple. My bet’s on Harris though, he’s so obsessed with flamethrowers recently. Oh no. MILLY GO CHECK ON HARRIS"
    w "Aye, boss! Will do"
    show Nhom happy:
        linear 1.0 xalign .75 yalign 1.0
    Nhom "Aye! Make sure to take the fireproof gear before heading out"
    w "NHOM we barely acquiesced to you straying from the noble tavern owner path to nonsense adventuring. But now here you are an Orphan Collector from your travels that wreak havoc back home"
    MC "Pardon, ‘Orphan Collector’?"
    "The mystery voice continued the berating, either failing to hear me or ignoring me completely"
    w "Hurry back and stick around as the tavern owner of %(tname)s"
    #Nhom gives a conspiratorial wink
    Nhom "Poppycock! Folks can only dream of stopping Nhom the Mighty, the great foe of Thundrome the Giant himself"
    "The mystery voice quiets though you hear faint mumbled curses of Nhom"
    show Nhom happy at center, hop 
    Nhom "I didn’t see you there! How are things going?"
    "Everything is fine. I’m ready to be your qualified leader mode on"
    MC "Fabulously! I’ve got fully fleshed out plans to handle those villains you’ve got hanging around town. The better question is what can I do for you?"
    Nhom "Can’t complain! As you heard before, my family’s itching to get me to stick around for good. While my menaces are itching to get back on the road even though we just got back in town"
    "Suddenly, a new voice chimes in"
    w "{size=-2}Boss! You said that we could get going after you defeat Thundrone once and for all. It’s practically been a month now. We’ve even had to enroll in icky school with scrubs and chumps{/size}"
    Nhom "Boz don’t hang from the ceiling or call your classmates scrubs and chumps. Also shoo shoo you’ve got some homework to finish up. The Mighty Nhom will personally evaluate your evasion tactics later"
    "{size=-2} YES! {/size} You look around wildly in hopes of spotting the owner of said voice. These are surely some high grade evasion abilities already"
    Nhom "Well there you have it! I do have some unfinished business with Thundrone"
    MC "Who exactly is Thundrone? Your foe you said?"
    Nhom "My! He’s probably one of the villains you have a plan about! The monstrous giant that garnishes his meals with children’s flesh. We’ve got into many a scuffle"
    MC "That’s horrible! Let me know how I can help you take down the dastardly fellow"
    Nhom "Aye! Thundrone and I plan on butting heads soon. I shall give you an update when the Mighty Hero, Nhom, is finished with the deed."
    hide Nhom with moveoutbottom
    "A sudden woosh is felt and Nhom is gone"
    "Well, now there’s certainly one plan in Operation Tenth Mayoral Success finalized. Maybe now I can finally get that drink"#cool acronym here instead of Operation Tenth Mayoral Success)
    $ charProgress["Nhom"] +=1
    jump ending_handler

label Nhom_end:
    "You hear rumors about the upcoming clash between the returning adventurer Nhom and the infamous Thundrone the Giant." 
    "You make sure to tell the crowd that you sent Nhom off on this quest which gets you approving nods and even cheers. (Though the validity is slightly questionable)"
    "You head over to the tavern to check in with Nhom and see if there was any way you could help him" 
    show Nhom happy:
        xalign 0.9 yalign 2
    "Coming into the tavern, you hear joyous squeals as you spot Nhom tussling with a rag tag group of kids" 
    w "BOSS BOSS, please show some mercy"  
    Nhom "Brat, you need to stop using the skills I taught you to pick fights in school" 
    MC "If it isn’t our hero Nhom!! How are you feeling, ready to permanently rid %(tname)s of Thundrone?" 
    show Nhom neutral at center
    Nhom "Hey! Aye feeling great, my rascals cause me more trouble than Thundrone ever could" 
    MC "Anything I can help you with? What’s stopping you from running him out of town?"
    show Nhom neutral at right,sright 
    "Nhom’s eyes dart to the commotion among the kids before looking at you appraisingly" 
    Nhom "I’ve been rather busy with helping out here at the tavern since I’m back and juggling the kids into some sense of normalcy. You haven’t heard the town’s chatter? Training for the battle is underway too" 
    Nhom "The Noble Nhom has everything under control!" 
    MC "Of course! I’m sure. I just want to know if there’s anything that I can do to speed the process along?"
    MC "With the electio- ah *cough* With how long the giant’s been terrorizing the people, it’s about time somebody did something about him, right?" 
    show Nhom confused at right, shake 
    "Nhom looks lost in thought, nodding his head in agreement" 
    Nhom "Alright! There is something you can help me with to prepare for the battle"
    "Yes! This will make for great PR"
    Nhom "Here’s a list of items I need to craft a weapon powerful enough to take Thundrone down once and for all" 
    MC "Thank you for the honor, Nhom Sir! I am now the one {size=+10}  anointed with the shopping list of the HERO NHOM himself {/size} ." 
    MC "{size=+20} Wow, I’d be perfect to anoint as something else? I dunno let's say mayor? {/size}" 
    "I do a quick sweep of the eyes to see if anyone is on the receiving end of my subliminal messaging for my campaign" 
    Nhom "Err- alright! No need to shout mate. Though, give me a holler when you’re back with the goodies"
    "You nod eagerly before skirting out of the cavern" 
    "First things first, let’s check the marketplace to see if any of these items are for sale" 
    scene bg marketplace with fade
    "You scramble around the shops with your handy weapons crafting list in hand"
    "Exchanging five bronze coins for a Gnotrs steel blade and other weapony- items at the Blacksmith feels exciting, like you’re the one about to embark on an epic journey" 
    "You start to question your purchases as the bulk of your items are slowly sourced from the grocer stalls. But you reason that you’re a dash salty as the purchases start to do some serious damage to your wallet"
    "You smile charmingly at the elf who hands you your requested assortment of flowers" 
    "Hmm these must be used to make some deadly poisons" 
    scene bg tavern with fade 
    show Nhom neutral at right  
    MC "I’ve got the goodies!" 
    Nhom "Aye! Thanks mate! With this, I’m all set to go"   
    "You nod excitedly as he takes the items and then sets off"
    MC "Wait, that’s it? Don’t you need to assemble your weapon and poisons"
    Nhom "Don’t worry about it! The great adventurer here has everything under control. I’ve got to get going. You’ll here about the victory soon!"
    hide Nhom with moveoutright 
    w "Boss is finally going to the cave to defeat Thundrone once and for all"
    "Man I want to see things go down, see if the hype is all worth it " 
    scene bg cave with fade 
    "Treading around the cave, you don't see anything so you decide to check the permiter" 
    scene bg shrubbery with fade
    "You’re surprised how scenic the site is. And more importantly, how quiet the surroundings are. Wow, Nhom must be good if he’s settled everything already." 
    "You skulk around the shrubs to minimize chances of wandering into the epic fight" 
    scene bg dunny_table with fade 
    show Nhom happy at right 
    "You peak your head up to see Nhom wrestling- no Nhom setting up culinary ware on a table?"
    show Nhom angry 
    Nhom "{size=+10} Who’s there?{/size}"
    with hpunch 
    "You internally (and maybe probably externally) scream as another pointy object (on closer inspection it looks like a fork?) embeds itself too close to your face yet again" 
    MC "It’s just me! What exactly is going on here?"
    show Nhom confused 
    "Nhom starts to say something about poisoning Thundrone’s food supply using his epic skills before he’s silenced by your look"
    Nhom "Well…. It’s kind of a long story" 
    MC "…" 
    Nhom " So Dunny and I actually go way back, like when were wee kiddies at the academy back" 
    MC "Who in the world is Dunny?" 
    Nhom "Oh right! More commonly known as Thundrone" 
    show Nhom happy at center, hop
    "You give him an incredulous look to which he gives a hearty laugh" 
    Nhom "Dunny isn’t even in town right now. He’s out at the Bake Off in the next town over" 
    MC "Thundrone, the Ginormous Giant? Infamous for his evildoings in town? Your foe" 
    Nhom "HmM, Dunny is for sure a giant… I think that’s it in terms of correct aspects in that statement. And I guess you could say foe?" 
    Nhom "Dunny and I are good mates. We crafted a scheme when I was still having arguments with my family about my dreams in becoming an adventurer. Dunny came up with the idea to use him as a cover so I as my \"great foe\" to prove my battle skills"
    MC "But what about the rumors in town?"
    Nhom "Well, every great ‘fight’ that we have, rather than righting we usually get together chat about the kids over some tea and pastries. Today, I’m just getting some me time from the tavern, townspeople, and kids"   
    MC "I don’t get why you went to this extent. Does this mean your adventuring feats are all lies? Why did you ask me to buy you weapons then?" 
    show Nhom neutral at left, sleft 
    "Nhom doesn’t respond and his eyes are trained behind me as if searching for something"   
    Nhom "Guys, you’re going to have to do better if you think you can eavesdrop on your old boss now."
    "It seems like Nhom may just be deranged for dragon puffs" 
    with vpunch 
    "You startle when a new yet familiar voice chimes in out of nowhere. Placing it to Litt, or another orphan of Nhom’s" 
    show Nhom angry at center, shake 
    Nhom "You LOT! I told you to stay away from this zone during my battle"
    Litt  "PSSH what battle??" 
    Litt "Boss, how could you? You go on and on about staying honest whenever any of us swindle someone as a prank? But then you do this?" 
    show Nhom sad 
    "Well, they say those that can’t do, teach{p=.3}.{p=.1}.{p=.2}. even in a telling falsehoods context you suppose"
    Litt "Why are we still in town if your great foe is already defeated? Do you enjoy being nagged at about taking up the noble act of tavern keeping? "
    "Nhom is silent through this all as Litt keeps ranting angrily" 
    Litt "-pastries! You don’t just source sweets from training unless you’ve crafted some big lies" 
    Litt "Since you’ve always been done here, let’s hurry up and get to our next adventure already" 
    "You use your great skills to assess Litt: evasion tactics, weapons arsenal and all. Come to realization about who the weapons will actually be for" 
    show Nhom happy at center, hop  
    "Nhom lets out an awkward chuckle"
    Nhom "Well my kiddos, you must be learning from the nagging masters back at the tavern. I’m sorry for keeping this under wraps from you guys for so long. My supposed battles with Dunny were from many years back that it was hard to take back once I was back in town"  
    Nhom "…And I’ve been thinking a lot about the big thing I want to do next. I just keep going and going, I’ve been having some great reflection tea times with my mate Dunny" 
    Nhom "Well  I can use some of your mayoral candidate wisdom, what do you think I should do next?"  
    menu:
        "Settle Down as Tavern Owner":
            $ end_nhom = "t"
            MC "It’s obvious! You realized from your quests that you’re not suited to being an adventurer after all"
            Litt "No! Don’t listen to this scrub, they don’t know what they’re talking about"
            show Nhom neutral 
            "Nhom doesn’t say anything immediately before beginning to nod"
            Nhom "You may be right, I was so set on defying this predestined fate of %(tname)sers, but everyone’s been right all along"
            MC "Tavern keeping beats out adventuring any day!"
            Nhom "Sorry, my kiddos. You’re free to keep on adventuring but know that there’s always a place for you at Tavern a la Nhom"
            "Suddenly a chorus of voices chimed in refusals and other hushed tones"
            Litt "Boss! We wouldn’t just leave you like that. We’ll stick around and figure out next journey steps here. We’ll always come back"
            show Nhom happy at right, sright 
            "Nhom rushed over to grab Litt in a bear hug, resulting in some laughing shrieks" 
            "You smile at the sight" 
        "Get Ready for Next Adventure":
            $ end_nhom = "a"
            MC "You’re meant to be Nhom the Noble! Adventuring is what you’re meant to do"
            Litt "That’s right boss!" 
            show Nhom neutral 
            "Nhom doesn’t say anything immediately before beginning to nod"
            Nhom "You must be right. I’ve just swept in the slow going ways of life back in town and the tavern. Adventuring must be what I like the most. It’s what I’ve always dreamed of doing"
            MC "Don’t settle for the nagging! Follow your childhood aspirations: adventure galore!"
            Nhom "Let’s move out kiddos!! I even got some lovely new supplies from our sponsor over here to go out on our next big quest" 
            "Suddenly a chorus of cheers cried out"
            Litt "Aye Boss! Let’s get ready to go, maybe we can get to Thundrone, no Dunny’s pastries when we head to next town"
            show Nhom happy at right, sright 
            "Nhom gets jumped on by his group of kids resulting in some laughing shrieks" 
            "You smile at the sight" 
        "Something Else":
            $ charProblems["Nhom"] = True
            MC "You keep thinking in absolutes. You’re not restricted to the extremes of either succumbing to ‘family destiny’ or fulfilling your childhood dreams of adventuring to be fulfilled"
            MC "I think you could start up an academy for adventurers for your kiddos or an orphanage or something else entirely!"
            Litt "Hmm, that’s an interesting idea boss!" 
            show Nhom neutral at center, shake  
            "Nhom smiles and nods his head immediately"
            Nhom "Exactly! That’s how I’ve been feeling all this time. I know I don’t like taking care of the tavern but I’m not sure if adventuring is for me anymore. I love being with my kiddos the most. Maybe I’ll set up an orphanage or adventurer’s guild or just a School of Adventurers"
            MC "Wacky as it may sound, Nhom the Orphan Collector is truly the best title for you"
            Nhom "Kiddos! I know it’s different from what you joined me for initially but I’d love for you guys to join me on this new adventure" 
            "Suddenly a chorus of cheers cried out"
            Litt "Aye Boss! We’ll keep training under you, get that sense of normalcy you keep droning on about. We’ll head out on quests before coming back home to you!"
            show Nhom happy at center, hop 
            "Nhom and his group of kids cheer and dance in some coordinate movement resulting in some laughing shrieks" 
            "You smile at the sight" 
    MC "Well, things turned out much differently from what I expected. But there’s one less dastardly villain (who turned out to be not so dastardly) to deal with after all!"
    Nhom "AYE! Let’s go back to the tavern and celebrate, drinks on me!" 
    "One step closer to winning this election!" 
    $ charProgress["Nhom"] +=1
    jump ending_handler

