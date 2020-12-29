define Janet = Character("Janet")

label Gladrock_handler:
    if charProgress["Gladrock"] == 2 and charProgress["Eadan"] == 1:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Gladrock" + storyTag[charProgress["Gladrock"]])

label Eaden_handler:
    if ((charProgress["Gladrock"] == 1 or charProgress["Gladrock"] == 2) and charProgress["Gladrock"] == 0):
        jump Gladrock_end
    else:
        "Nobody seems to be here right now."

label Gladrock_beg:
    #scene __ with flash
    MC "The time has come, the clock has struck, the hour is upon me. It is time: to fight the dragon."
    show Gladrock happy
    Gladrock "Hello, oh weary wanderer. You called, and I came."
    MC "I didn't call."
    show Gladrock happyh
    Gladrock "Well, you were about to call."
    MC "No, I wasn't."
    show Gladrock angryh
    Gladrock "I just assumed, oh wise mayoral candidate, that you would not presume to attempt a quest of this magnitude with out the counsel of your very own powerful warlock."
    MC "You assumed incorrectly. I am perfectly capable—nay, I am destined—to fight this dragon on my own."
    show Gladrock angryh at center, hop
    Gladrock "Nonsense. I won't allow it. You can't have a quest without a warlock any more than you can have a city without a mayor, or a birthday without cake."
    "You sigh. Looks as though you have no choice. Oh well, maybe he will come in useful."
    show Gladrock happyh at center, hop
    Gladrock "AHA! I have found a talisman that will help us on our journey."
    MC "Pretty sure that's just an ordinary rock."
    show Gladrock confusedh
    Gladrock "You think so? But it shines like the sun. How many rocks have you seen that look thusly?"
    MC "Lots. It's lying on the road where wagons drive. I think it's just been eroded."
    show Gladrock angryh at center, hop
    Gladrock "Drat it all! We shall have to remain on the look out."
    show Gladrock happyh
    "You take it back. Actually, pretty sure the mermaid would've been more useful than this guy."
    hide Gladrock with moveoutright
    scene bg forest with fade
    "You walk together through the forest, shivering as the trees block out the sun. The woods get darker as you continue on, fighting your way through the thorns and bracken on the forest floor."
    "The large stone tower emerges out of the darkness as you walk. The forest is so dark, and the ground so overgrown at the foot of the tower, that it looks as though it had grown there naturally among the trees."
    show Gladrock worryh at center with moveinright
    MC "Ok. Now we have to approach with caution. Careful as you walk to ensure that your footsteps are quiet—"
    show Gladrock angryh at center, hop
    Gladrock "FAIR DAMSEL! FAIR DAMSEL WE HAVE COME HERE TO SAVE YOU. HAVE NO FEAR, YOUR RESCUERS ARE HERE!"
    MC "Are you kidding me?"
    show Gladrock angryh at center, hop
    Gladrock "DAMSEL, SEND US A SIGN IF YOU CAN HEAR US! DROP A RED FLAG OUT YOUR WINDOW IF YOU ARE AWARE OF OUR PRESENCE!"
    MC "{i}What are you talking about???{/i} Why would she have a red flag? How would that help us?"
    show Gladrock angryh at center, hop
    Gladrock "DAMSEL—"
    MC "SHUT UP! Can you just shut up for a second?!"
    show Gladrock angryh at center, hop
    Gladrock "{i}Shut up?{/i} How dare you! I am Gladrock the Witty of  %(tname)s!"
    MC "The Witty? I thought you said—"
    show Gladrock worryh at left with move
    show Eaden angry:
        xalign 2.0
        yalign 1.4
        linear .3 xalign 1.5
        ease .06 xoffset 8
        ease .06 xoffset -8
        ease .05 xoffset 2
        ease .05 xoffset -2
        ease .04 xoffset 4
        ease .04 xoffset -4
        ease .03 xoffset 6
        ease .03 xoffset -6
        ease .02 xoffset 4
        ease .02 xoffset -4
        ease .01 xoffset 2
        ease .01 xoffset -2
        ease .01 xoffset 0
    Eaden "WHO DARES DISTURB MY SLUMBER?"
    "Well. This is not going according to plan."
    show Eaden annoyed
    Eaden "Well, well, well, well, well."
    ".{w}.{w}."
    "Huh. I really thought something more was coming there."
    show Eaden happy
    Eaden "Well, well. If it isn't Gladrock the Wet. And a friend."
    MC "The Wet? Like the sign outside town?"
    show Gladrock angryh
    Gladrock "Gods above, must you Eaden? I have an image to maintain."
    show Eaden confused
    Eaden "Why be ashamed? You solved our bottomless waterfall problem all by yourself. Be proud!"
    show Gladrock angryh at left, hop
    Gladrock "It's hardly my fault that warlocks are named for their first great deed. If I'd known I might have reconsidered."
    MC "You two know each other??"
    show Gladrock happyh
    Gladrock "Long, long ago, when we each attended %(tname)s Primary School. But that was before Eaden stole away the fair damsel—"
    show Eaden happy
    Eaden "Janet."
    show Gladrock angryh
    Gladrock "Yes, Janet, the fair damsel as I said—that was before Eaden stole her away from our peaceful town and terrorized any hero who tried to save her."
    show Eaden annoyed
    Eaden "I mean, how much of a hero could they be if they couldn't get past a dragon? That's like, hero 101."
    MC "All right, can both of you be quiet? I am here to slay you, fearsome beast! Prepare to be slaughtered!"
    show Eaden confused
    Eaden "Slaughtered? That sounds awfully violent. Who are you again?"
    MC "I am your worst nightmare. I am the terror that stalks you in the night. I am... %(tname)s's candidate for mayor."
    Eaden "Hold up, you're a politician? I'm confused."
    show Eaden annoyed
    MC "You should be! Prepare to die!"
    "You raise your sword in the air."
    show Gladrock happyh
    Gladrock "Yes, and I am here to complete the job, for this noble hero knew they would not succeed without my help. Prepare yourself, for this spell will strengthen the blade so that a single blow will snuff out your evil life. *Ferrum radicum suam*!"
    "The blade of your sword crumples up like a paper bag. It folds in on itself as it crinkles, until you're left with the sword's hilt attached to what looks like aluminum foil."
    MC "What the—? Gladrock??"
    show Gladrock confusedh
    Gladrock "Er. Right. Oops. It wasn't supposed to do that."
    show Eaden annoyed
    MC "I should hope not! Undo it! The dragon will attack any minute now!"
    show Gladrock angryh
    Gladrock "Don't pressure me! It's hard to think of spells at the last minute!"
    MC "If you hadn't done *any* spell we wouldn't be in this situation! I don't care about the strengthening spell, just get my sword back."
    show Gladrock sadh
    Gladrock "Well—well the thing is, I don't actually know how to undo it right at this moment. If you'd just give me a half hour I'll nip back to town, get a spell book—I left it in the washing room, serves me right for reading in the bath—"
    MC "WE DON'T HAVE A HALF HOUR! The dragon is going to kill us now!"
    show Eaden angry:
        linear .2 zoom 1.2
        linear .2 zoom 1.0
    "As you talk, Eaden has ripped the aluminum-foil-sword from the hilt with his teeth and is chewing it thoughtfully."
    show Eaden confused
    MC "GLADROCK! The dragon is eating my sword!"
    show Eaden sorry
    Eaden "I wish you wouldn't talk about me in the third person. Really makes me feel like a third wheel if I'm being honest."
    show Gladrock confusedh
    Gladrock "Er, yes, I see, he is doing that. Right then, now what do we—"
    MC "Do a spell! This is your moment, Gladrock! If you know *any* useful spells it's now or never!"
    show Eaden confused
    show Gladrock happyh at left, hop
    Gladrock "Right, um—{i}flos florum!{/i}"
    "Flowers spring up all around the base of the tower."
    MC "Please, please tell me the flowers are at least poisonous."
    show Gladrock happyh at left, hop
    show Eaden annoyed
    Gladrock "Well, no. But they are delightful. Perhaps it will distract the dragon."
    MC "{i}The dragon is currently looking right at us, Gladrock!{/i} I don't think he's distracted."
    show Gladrock angryh
    Gladrock "Will you stop being so negative? I'm doing my best here!"
    show Eaden happy
    Eaden "You know what I suggest? Why don't you both come in for a spot of tea? I'd just put the kettle on anyway. Janet might even feel up to joining us."
    show Gladrock confusedh
    "You give Gladrock a suspicious look. Gladrock looks back at you with a befuddled expression on his face. He's no help. But how can you pass up a chance to venture into the heart of the dragon's lair and see the fair damsel herself?"
    MC "All right. We'll come in."
    show Gladrock happyh at left, hop
    Gladrock "Now that you mention it, I am feeling slightly parched. Probably all that walking we did to get here."
    hide Eaden
    hide Gladrock
    with moveoutright
    "You shoot a glare at Gladrock but he doesn't see as he's too busy following Eaden inside"
    "The inside of the tower is dark, darker than you were expecting. The only light comes from the top of a staircase that winds down towards the bottom of the tower."
    show Gladrock happyh at left with moveinleft
    show Eaden happy:
        xalign 2.0
        yalign 1.4
    Eaden "Sorry about the light. I can see in the dark anyway and Janet doesn't mind it, so we've been putting off getting some new light fixtures in after the last ones blew out."
    "You hear the sound of footsteps and within moments, a young woman is coming down the staircase. In the darkness, only her silhouette is visible. She walks briskly towards a cupboard on the wall and starts handing out mugs."
    show Gladrock happyh at left, hop
    Gladrock "Janet? Fair damsel? Why, we thought we may never lay eyes on you again! Do our senses deceive us?"
    Janet "Nope. Not deceived. It's me."
    show Gladrock angryh
    MC "Damsel, have no fear! I am here to slay the dragon and free you from your wretched prison. If only the wizard had not crumpled my sword the beast would already be slain."
    Janet "Another knight come to rescue me? How original. Am I literally the only damsel in a tower guarded by a dragon in a fifty mile radius? That seems unlikely."
    show Gladrock happyh
    Gladrock "Well, not a *fifty* mile radius. But you're certainly the most convenient, oh noble princess."
    Janet "Princess? I'm not the princess of anything. I'm a baker's daughter from  %(tname)s."
    show Gladrock worryh
    Gladrock "Er, yes, well. Figure of speech."
    Eaden "How do you take your tea?"
    show Gladrock happyh at left, hop
    Gladrock "Milk and sugar, please."
    show Eaden annoyed
    MC "I won't accept any beverage that comes from the lair of a dragon."
    Eaden "Suit yourself."
    show Eaden happy
    Janet "Look, Eaden, I've been thinking and I think I've come to some decisions about my future here."
    show Gladrock happyh at left, hop
    Gladrock "Speak, princess! Your noble voice rings as true as the mountains in summer."
    Janet "What?"
    MC "It's not important. Go on."
    Janet "Anyway, I've been thinking and I think it's time. For me to leave, I mean. I've been preparing long enough. I'm as ready as I'll ever be."
    show Eaden sorry
    Eaden "I suppose so. If that's what you want. I had hoped you might reconsider."
    MC "Huh?"
    Gladrock "Princess—"
    show Gladrock confusedh
    Janet "Stop. Start over."
    Gladrock "Oh Janet, please cure us of our ignorance. Has this dragon not been keeping you here?"
    show Gladrock happyh
    Janet "Nope. I just wanted some time to plan for my future as an explorer and have some space to myself. I was feeling suffocated at home—working in the bakery is an exhausting job. Then I had this idea—faked my own kidnapping and everything. Pretty good, right?"
    MC "Your father's heart was broken by your kidnapping! How could you tell a lie like this?"
    Janet "Have you met him? Because if you had, I think you'd be reassured. I mean, he's great and everything but a little spacey. Pretty sure he still thinks I went off to college in Lispor like I originally told him."
    show Eaden annoyed
    MC "So...we came here...for nothing? What am I going to tell people? I promised to slay the dragon!"
    Janet "Well, I've been thinking it's about time for me to come clean anyway. Deceiving the whole town was fun for a while and all, but it's getting old to have knights showing up all the time banging down the door. Even if you all are the most ineffectual knights I've ever seen."
    MC "We're not knights! Gladrock is a warlock and I—I am the candidate for mayor of this great township!"
    Janet "{i}Mayor?{/i} We have one of those?"
    Gladrock "It's been introduced in the last few years, damsel. We finally hit the sixty person threshold while you were in the tower."
    Janet "Wow. Guess things really have changed."
    show Gladrock sadh
    show Eaden sorry
    "Gladrock looks dejected. Eaden looks thoughtful. You wonder if it would be rude to ask the dragon to carry you to %(tname)s on his back."
    Eaden "If it is your time to go, oh damsel, then it is my time as well. I have spent many years in this tower enjoying the solitude. But now I think I am ready to do something more with my life—something that has meaning in the world."
    "You groan. Looks like Eaden isn't coming back with you after all."
    show Eaden happy
    Eaden "Where to first, Janet? I will take you there and then figure out my own fate."
    hide Eaden with moveoutright
    show Gladrock sadh at center with move
    "As Janet and Eaden talk, you turn to Gladrock."
    MC "Guess it's time for us to head back to town? Gotta admit, that was anticlimactic."
    "The two of you walk back through the forest. The light is coming back now and it is overwhelming to your eyes, which have gotten used to darkness."
    Gladrock "You know, that was the most alive I've felt in a while."
    show Gladrock happyh
    Gladrock"Hiking through the woods, participating in the action—it's not something you do much as a warlock. People expect you to spend all your time studying or casting spells. There's not room for much else in my life."
    MC "Maybe you should consider a career change."
    Gladrock "Maybe. Maybe someday."
    $ charProgress["Gladrock"] +=1
    jump ending_handler

label Gladrock_med:
    show Gladrock sad at center
    "Gladrock is standing in the town center, looking lost. You approach him."
    hide Gladrock with dissolve
    show Gladrock happyh with dissolve
    Gladrock "Hail thee, mayoral candidate of our great and noble province. How goes it with you?"
    MC "It goes, warlock. I have been on many adventures here. How goes it with you? Last time I saw you, we were fighting the dragon."
    show Gladrock sadh
    Gladrock "Yes, yes. Well, I'll admit, I have been doing some soul searching. And crystal ball gazing but all that turned up was a weather forecast."
    MC "Soul searching about what?"
    show Gladrock sadh at sink
    Gladrock "I'm having a difficult time focusing on my work. All I want to do these days is get out there again and do something physical, but I'm stuck here instead poring over books."
    menu:
        "Just keep up what you're doing, I'm sure your passion for your work will come back eventually.":
            show Gladrock happyh at rise
            Gladrock "You're right. I suppose I'll just keep on doing what I've been doing."
            MC "Good on you, Gladrock!"
            show Gladrock happyh at center, hop
            Gladrock "I suppose this sense of perennial dissatisfaction and existential dread wears off eventually."
        "Maybe it's time for you to change things up. I saw a poster for a triathlon in the square. Do you have any interest in doing that?":
            show Gladrock happyh at rise
            Gladrock "Now that you mention it, I saw that myself! Maybe that would be something I could do. Do you really think I could do it?"
            MC "Sure you can! I've seen you not even break a sweat on that hike through the woods we did. With the right training I think you'd be a real competitor. Not to mention the fact that there's probably only two other competitors in this whole town."
            show Gladrock happyh at center, hop
            Gladrock "Thanks. It means a lot to hear you say that."
    $ charProgress["Gladrock"] +=1
    jump ending_handler

label Gladrock_end:
    show Eaden sad at center
    "Eaden is back in town, perched on the road looking aimless. You go up to him."
    MC "Hi, Eaden. I wasn't expecting to see you again."
    Eaden "Yeah, I've been feeling pretty restless. Thought coming back here would give me some perspective."
    show Eaden sorry
    Eaden "Now that Janet's gone I just feel this gap in my life, like there's some meaning that's been taken away. I want to do something meaningful again, but I don't know what to do."
    menu:
        "You know, knighthood is always an option for restless people who want to make a difference.":
            "It's not all rescuing princesses, you know. There's real change that can be made if you do it right."
            show Eaden confused
            Eaden "Knighthood? But, I'm a dragon."
            MC "And? There's a first for everything. I personally think you'd make a great knight. I believe in you."
            show Eaden sorry
            Eaden "Wow, I'd never even thought that could be an option."
            show Eaden happy
            Eaden "Maybe it's worth looking into. Thanks for your advice."
        "Have you thought about working in a bakery? I bet Janet's dad would appreciate an assistant with real life fiery breath, huh?":
            show Eaden confused
            Eaden "Um, no. How would that be making a difference?"
            MC "It'd make a difference for this town's supply of scones! I mean five per day, come on! I have to be there when it opens to even hope to get one."
            show Eaden sad
            Eaden "Right, well. Not something I really considered before."
            show Eaden happy
            Eaden "But...uh, thanks for your thoughts."
            MC "No problem, Eaden! Solving people's problems is just what I do."
    $ charProgress["Eadan"] +=1
    jump ending_handler
