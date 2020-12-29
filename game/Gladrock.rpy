define Janet = Character("Janet")

label Gladrock_handler:
    if charProgress["Gladrock"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Gladrock" + storyTag[charProgress["Gladrock"]])



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
    #UNFINISHED
    $ charProgress["Gladrock"] +=1
    jump ending_handler

label Gladrock_med:
    "You decide to go by the port again with a suit you plan on wearing for a rally later to check in with Gladrock."
    show Gladrock happy:
        zoom .75
        yalign 1.0
        xalign 2.0
        linear .5 xalign 1.3
    "You find her in the same spot as before, except that she's no longer shouting her services. Instead, she's sitting, quietly sewing."
    show Gladrock happy:
        linear .5 xalign .5
        linear .3 zoom 1.0
    "As you approach, she acknowledges your presence from her deep concentration with a simple nod."
    MC "Hi Gladrock, how are you doing?"
    show Gladrock ehappy
    Gladrock "I'm doing great! Business is picking up, people seem to be stopping by a lot more. I'm actually working on someone's custom order right now, so you'll have to wait a minute."
    show Gladrock happy
    MC "I have time to spare."
    "You do, in fact, have time to spare, even though you have no one else working on your mayoral campaign. Sad."
    "You stand around on the port for a few minutes. You notice she's sewing two pieces of brightly colored pieces of fabric together."
    MC "What are you working on?"
    show Gladrock ehappy
    Gladrock "Oh, this? It's a costume for a boxer. He wants me to make a cape and some shorts for a rebrand of his image."
    "The clothes shimmers in yellow and purple. It looks garish, but the stitchwork is immaculate."
    show Gladrock happy
    MC "Which boxer? I follow boxing occasionally."
    Gladrock "It's Roxolometer. Do you know him?"
    MC "Yes! Isn't he a gnome? I love watching his fights when I can."
    show Gladrock unsure
    "This seems to bum her out."
    show Gladrock sad
    Gladrock "I wish I could see one, they look so exciting..."
    MC "You should! They're so exciting, and the energy of the crowd..."
    show Gladrock happy
    Gladrock "Did you know that he started boxing when he was 400 years old?"
    MC "I didn't, that's pretty old!"
    show Gladrock ehappy
    Gladrock "Yeah, and now he's one of the best."
    show Gladrock happy
    Gladrock "You know, before boxing, Roxolometer was really, really good at farming, something about being the bringer of good crops. You know, it's a gnome thing."
    show Gladrock unsure
    "You nod, and she sighs deeply."
    Gladrock "So he had this giant farm with all of his children working on it with him and they were raking in money, you know?"
    Gladrock "I think he was selling some kind of magical mushroom, and it was super expensive, but then, all of a sudden, he decides to go into boxing."
    show Gladrock happy
    Gladrock "Joins a professional league right away, even though he had absolutely no experience."
    Gladrock "Obviously, he had a rough time starting off, but then he got good."
    show Gladrock ehappy
    Gladrock "He got really good."
    show Gladrock unsure
    "She looks at you, hands limply holding the fabric now."
    show Gladrock sad
    Gladrock "Talking with him made me really think about what I do for a living."
    Gladrock "You know, being a tailor is not fun, especially as a mermaid."
    show Gladrock angry
    Gladrock "We don't like changing clothes! I do because it's part of my job, but most people just wear some shells or whatever for life."
    Gladrock "Which, you know, is a long time."
    Gladrock "So I have to deal with other races all the time and you all don't understand what it's like for beings that need to be in water all the time."
    Gladrock "If I'm not at least partially submerged at any time, I will shrivel up and die in a few minutes."
    show Gladrock angry at shake
    Gladrock "But you stupid humans cannot understand that, so you build all your towns close enough to water to talk to us, but we can't actually engage in any meaningful conversation or exchange unless you have a lot of money like those folks."
    "She points at some merpeople in tanks, clearly envious. then she sighs."
    show Gladrock sad
    Gladrock "Sorry for ranting about this all to you, very clearly one of the stupid humans I mentioned, I didn't mean to call you stupid."
    show Gladrock unsure
    Gladrock "My business is looking up, but I..."
    "She trails off wistfully, then looks back at the pieces of clothing in front of her."
    show Gladrock sad
    Gladrock "I wonder if there's something out there more suited for me."
    MC "Maybe you should try something else out? There are plenty of other professions out there."
    MC "You could take a break from tailoring for a while to go and try things out."
    Gladrock "Are you kidding? With the amount of business I'm finally getting?"
    Gladrock "If I take a few more orders I can even buy one of those fancy tanks, and then business will really start taking off."
    show Gladrock unsure
    "You nod, looking around."
    show Gladrock sad
    MC "Hey, it seems like you're busy with Roxolometer's order, so I'll come back another day."
    "She nods glumly as you wave goodbye."
    Gladrock "See you around."
    show Gladrock unsure
    "She slowly waves back, then continues to sew the fabric together."
    hide Gladrock with dissolve
    $ charProgress["Gladrock"] +=1
    jump ending_handler

label Gladrock_end:
    "You finally get some time again to go down to the port and find Gladrock to mend your suit, quietly willing her to be in a better mood than she was when you last saw her."
    show Gladrock happy:
        zoom .75
        yalign 2.0
        xalign .5
        linear .4 yalign 1.0
    "You approach her stand by the port, and see that she's only started laying out her supplies."
    show Gladrock ehappy:
        linear .5 zoom 1.0
    Gladrock "Oh hi! Nice to see you again."
    show Gladrock happy
    MC "Yeah, I didn't get to ask you to mend something last time. Can you fix up this suit of mine? There are a lot of moth holes."
    Gladrock "Of course! Let me just finish up what I'm working on."
    "She seems to be making some sort of sack, large enough to fit several objects into."
    MC "So, how are you doing?"
    show Gladrock sad
    "She heaves a deep sigh."
    "You brace yourself for more woes."
    show Gladrock happy
    Gladrock "You know, I can't complain. Business is doing great, and Roxolometer loved his costume and even asked me to come see a match!"
    show Gladrock ehappy
    Gladrock "The energy and the excitement, and the noise!"
    "She smiles with the memory."
    show Gladrock happy
    Gladrock "I loved it. I was buzzed from that match for days afterwards, I couldn't stop talking to everyone about it."
    MC "They're so exciting!!! You finally got to go!"
    show Gladrock sad
    "She smiles, but her excitement dims, and she goes back to stitching a hole in the bag."
    Gladrock "But I can't go watch boxing matches all the time. I have a job, and I need to make money."
    show Gladrock unsure
    Gladrock "I really wish I could, but..."
    show Gladrock sad
    "She sews silently for some time, and finishes making the bag. She puts it down and looks up at you."
    menu:
        "Encourage her to pursue boxing":
            MC "Gladrock, I'm sure you have more options than you think you do."
            MC "What about training for boxing or something when you have the time?"
            show Gladrock sad
            Gladrock "I guess I could..."
            MC "It doesn't hurt to try!"
            show Gladrock unsure
            Gladrock "I don't know..."
            MC "Hey listen,{w}it might be scary, but you seriously seem quite unhappy at your current job. Why not try something new?"
            show Gladrock sad
            Gladrock "Hey, you're right. I really am unhappy now."
            "She puts the sewing down, and looks at her hands."
            Gladrock "Everything I've been doing now, all of the work I've done, it's all been for other people, not for me."
            Gladrock "Why am I still stitching and mending clothes for other people? I should be chasing my own dreams."
            show Gladrock happy
            MC "Yeah! You should go and find what makes you happy."
            MC "What's the point of life if you aren't trying to strive towards happiness?"
            show Gladrock ehappy
            Gladrock "You're right!"
            show Gladrock happy
            "There are sparks in her eyes now, and she looks determined to change."
            Gladrock "Thanks so much! You've been such a great help."
            show Gladrock ehappy
            Gladrock "And now I'm going to go figure out what to do with my life! Probably boxing!"
            show Gladrock ehappy:
                linear .2 yalign 10.0
            "She dives into the ocean, leaving all of her supplies behind."
            hide Gladrock
            MC "Wait, could you maybe fix my-?"
            "Your sentence stops short when you realize that she is too far to hear you. You sigh and leave the port."
            "Despite not getting your suit mended, you feel like you did something good today."
            $ charProblems["Gladrock"] = True
        "Ask her to mend your suit":
            MC "Would you mind mending my suit? I need it for a rally I'm doing soon, and it's not looking great."
            show Gladrock happy
            Gladrock "Sure, no problem!"
            "She takes the suit from you and starts to mend it. She very quickly patches the holes and hands it back to you."
            show Gladrock ehappy
            Gladrock "There! It's done."
            show Gladrock happy
            MC "Thanks so much, this is great."
            Gladrock "No worries."
            MC "How much do I owe you?"
            show Gladrock ehappy
            Gladrock "Oh, this one is free, for the generous amount you gave me the first time."
            MC "Really? Thanks!"
            show Gladrock happy
            "As you start walking away, another person approaches Gladrock with something to mend. She takes it and starts at her work again."
            hide Gladrock with moveoutleft
    $ charProgress["Gladrock"] +=1
    jump ending_handler
