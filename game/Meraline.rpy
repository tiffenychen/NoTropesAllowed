label Meraline_handler:
    if charProgress["Meraline"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Meraline" + storyTag[charProgress["Meraline"]])



label Meraline_beg:
    "You near the port, and find a lively settlement of merpeople and other fantasy folk trading, chatting, doing business. One voice rises above the rest in its sweetness."
    Meraline "Ahoy! Travellers! I see the holes in your trousers, the rips in your shirts. Bring them to me, Meraline, and I shall fix them as you watch!"
    show Meraline happy:
        zoom .75
        xalign .5
        yalign 2.0
        linear .5 yalign 1.0
    "A bystander parts in front of you, and you see the face of Meraline resting on the planks of the port."
    show Meraline ehappy:
        linear .1 yalign .7
        linear .1 yalign 1.0
    "As you make eye contact with her, her eyes brighten and she beckons you over. You go over reluctantly."
    "As you approach, you see that it is a mermaid, half-submerged in water, and stretched to reach the dock with her arms."
    "She has an assortment of needles and thread and pushpins around her."
    show Meraline happy:
        zoom .75
        linear .4 zoom 1.0
    Meraline "Traveller! You look well-worn, and your clothes most definitely need mending! Here, let me take them and patch those gaping holes, you will feel much better after my handiwork is done."
    show Meraline happy:
        zoom 1.0
        linear .2 zoom 1.2
        linear .2 zoom 1.0
    "She proceeds to grab at your clothes."
    MC "Hey! My clothes are fine, what are you doing?"
    "You try and protest, but her grip is strong. You relinquish a scarf that really does have lots of holes and rips."
    Meraline "What is your name, traveller?"
    show Meraline ehappy
    "You tell her your name and she nods appreciatively."
    show Meraline happy
    Meraline "Hm, that isn't a common name around these parts. You aren't from here are you? I've never seen you before and I can't say I recognize you ."
    MC "No, I'm not. I've travelled around, don't know if I can say I'm from anywhere anymore."
    "She nods again."
    show Meraline happy at center, hop
    Meraline "See, I have a sense for these things. And your scarf is done!"
    show Meraline ehappy
    "You look down and notice that your scarf is, in fact, completely mended. It looks slightly wet, but as she hands it to you, the fabric is soft to the touch and feels like new."
    show Meraline happy
    MC "Wow, this is remarkable. Why aren't more people here to ask for your services?"
    show Meraline sad
    Meraline "It's only because I'm down here and I don't have the money to afford one of those elevated tankards, I can't advertise as well."
    show Meraline happy
    Meraline "All I have is my voice and my skills, which I think you'll agree are pretty good, no?"
    MC "I completely agree. My scarf feels completely mended."
    "You rewind the scarf around your neck."
    MC "Hey, how much do you want for that? I hope this is enough."
    "You hand her three bronze coins, and she gapes at them."
    show Meraline ehappy at center, hop
    Meraline "Th-thank you!"
    MC "Don't mention it. Three bronze coins really isn't that much..."
    show Meraline happy
    Meraline "No one has ever paid me that much before. I'm really grateful, thank you so much!"
    MC "With skills as quick and high-quality as yours, why not?"
    Meraline "Oh, I usually charge only one bronze piece."
    show Meraline sad
    Meraline "Honestly, I'm lucky to get any business at all. There are so many tailors and seamstresses around, and the port is an odd place to go to get your clothes mended..."
    show Meraline happy
    "You nod in agreement, thinking it a pity. For good measure, you toss another bronze coin at her, and walk away."
    hide Meraline with moveoutleft
    $ charProgress["Meraline"] +=1
    jump ending_handler

label Meraline_med:
    "You decide to go by the port again with a suit you plan on wearing for a rally later to check in with Meraline."
    show Meraline happy:
        zoom .75
        yalign 1.0
        xalign 2.0
        linear .5 xalign 1.3
    "You find her in the same spot as before, except that she's no longer shouting her services. Instead, she's sitting, quietly sewing."
    show Meraline happy:
        linear .5 xalign .5
        linear .3 zoom 1.0
    "As you approach, she acknowledges your presence from her deep concentration with a simple nod."
    MC "Hi Meraline, how are you doing?"
    show Meraline ehappy
    Meraline "I'm doing great! Business is picking up, people seem to be stopping by a lot more. I'm actually working on someone's custom order right now, so you'll have to wait a minute."
    show Meraline happy
    MC "I have time to spare."
    "You do, in fact, have time to spare, even though you have no one else working on your mayoral campaign. Sad."
    "You stand around on the port for a few minutes. You notice she's sewing two pieces of brightly colored pieces of fabric together."
    MC "What are you working on?"
    show Meraline ehappy
    Meraline "Oh, this? It's a costume for a boxer. He wants me to make a cape and some shorts for a rebrand of his image."
    "The clothes shimmers in yellow and purple. It looks garish, but the stitchwork is immaculate."
    show Meraline happy
    MC "Which boxer? I follow boxing occasionally."
    Meraline "It's Roxolometer. Do you know him?"
    MC "Yes! Isn't he a gnome? I love watching his fights when I can."
    show Meraline unsure
    "This seems to bum her out."
    show Meraline sad
    Meraline "I wish I could see one, they look so exciting..."
    MC "You should! They're so exciting, and the energy of the crowd..."
    show Meraline happy
    Meraline "Did you know that he started boxing when he was 400 years old?"
    MC "I didn't, that's pretty old!"
    show Meraline ehappy
    Meraline "Yeah, and now he's one of the best."
    show Meraline happy
    Meraline "You know, before boxing, Roxolometer was really, really good at farming, something about being the bringer of good crops. You know, it's a gnome thing."
    show Meraline unsure
    "You nod, and she sighs deeply."
    Meraline "So he had this giant farm with all of his children working on it with him and they were raking in money, you know?"
    Meraline "I think he was selling some kind of magical mushroom, and it was super expensive, but then, all of a sudden, he decides to go into boxing."
    show Meraline happy
    Meraline "Joins a professional league right away, even though he had absolutely no experience."
    Meraline "Obviously, he had a rough time starting off, but then he got good."
    show Meraline ehappy
    Meraline "He got really good."
    show Meraline unsure
    "She looks at you, hands limply holding the fabric now."
    show Meraline sad
    Meraline "Talking with him made me really think about what I do for a living."
    Meraline "You know, being a tailor is not fun, especially as a mermaid."
    show Meraline angry
    Meraline "We don't like changing clothes! I do because it's part of my job, but most people just wear some shells or whatever for life."
    Meraline "Which, you know, is a long time."
    Meraline "So I have to deal with other races all the time and you all don't understand what it's like for beings that need to be in water all the time."
    Meraline "If I'm not at least partially submerged at any time, I will shrivel up and die in a few minutes."
    show Meraline angry at shake
    Meraline "But you stupid humans cannot understand that, so you build all your towns close enough to water to talk to us, but we can't actually engage in any meaningful conversation or exchange unless you have a lot of money like those folks."
    "She points at some merpeople in tanks, clearly envious. then she sighs."
    show Meraline sad
    Meraline "Sorry for ranting about this all to you, very clearly one of the stupid humans I mentioned, I didn't mean to call you stupid."
    show Meraline unsure
    Meraline "My business is looking up, but I..."
    "She trails off wistfully, then looks back at the pieces of clothing in front of her."
    show Meraline sad
    Meraline "I wonder if there's something out there more suited for me."
    MC "Maybe you should try something else out? There are plenty of other professions out there."
    MC "You could take a break from tailoring for a while to go and try things out."
    Meraline "Are you kidding? With the amount of business I'm finally getting?"
    Meraline "If I take a few more orders I can even buy one of those fancy tanks, and then business will really start taking off."
    show Meraline unsure
    "You nod, looking around."
    show Meraline sad
    MC "Hey, it seems like you're busy with Roxolometer's order, so I'll come back another day."
    "She nods glumly as you wave goodbye."
    Meraline "See you around."
    show Meraline unsure
    "She slowly waves back, then continues to sew the fabric together."
    hide Meraline with dissolve
    $ charProgress["Meraline"] +=1
    jump ending_handler

label Meraline_end:
    "You finally get some time again to go down to the port and find Meraline to mend your suit, quietly willing her to be in a better mood than she was when you last saw her."
    show Meraline happy:
        zoom .75
        yalign 2.0
        xalign .5
        linear .4 yalign 1.0
    "You approach her stand by the port, and see that she's only started laying out her supplies."
    show Meraline ehappy:
        linear .5 zoom 1.0
    Meraline "Oh hi! Nice to see you again."
    show Meraline happy
    MC "Yeah, I didn't get to ask you to mend something last time. Can you fix up this suit of mine? There are a lot of moth holes."
    Meraline "Of course! Let me just finish up what I'm working on."
    "She seems to be making some sort of sack, large enough to fit several objects into."
    MC "So, how are you doing?"
    show Meraline sad
    "She heaves a deep sigh."
    "You brace yourself for more woes."
    show Meraline happy
    Meraline "You know, I can't complain. Business is doing great, and Roxolometer loved his costume and even asked me to come see a match!"
    show Meraline ehappy
    Meraline "The energy and the excitement, and the noise!"
    "She smiles with the memory."
    show Meraline happy
    Meraline "I loved it. I was buzzed from that match for days afterwards, I couldn't stop talking to everyone about it."
    MC "They're so exciting!!! You finally got to go!"
    show Meraline sad
    "She smiles, but her excitement dims, and she goes back to stitching a hole in the bag."
    Meraline "But I can't go watch boxing matches all the time. I have a job, and I need to make money."
    show Meraline unsure
    Meraline "I really wish I could, but..."
    show Meraline sad
    "She sews silently for some time, and finishes making the bag. She puts it down and looks up at you."
    menu:
        "Encourage her to pursue boxing":
            MC "Meraline, I'm sure you have more options than you think you do."
            MC "What about training for boxing or something when you have the time?"
            show Meraline sad
            Meraline "I guess I could..."
            MC "It doesn't hurt to try!"
            show Meraline unsure
            Meraline "I don't know..."
            MC "Hey listen,{w}it might be scary, but you seriously seem quite unhappy at your current job. Why not try something new?"
            show Meraline sad
            Meraline "Hey, you're right. I really am unhappy now."
            "She puts the sewing down, and looks at her hands."
            Meraline "Everything I've been doing now, all of the work I've done, it's all been for other people, not for me."
            Meraline "Why am I still stitching and mending clothes for other people? I should be chasing my own dreams."
            show Meraline happy
            MC "Yeah! You should go and find what makes you happy."
            MC "What's the point of life if you aren't trying to strive towards happiness?"
            show Meraline ehappy
            Meraline "You're right!"
            show Meraline happy
            "There are sparks in her eyes now, and she looks determined to change."
            Meraline "Thanks so much! You've been such a great help."
            show Meraline ehappy
            Meraline "And now I'm going to go figure out what to do with my life! Probably boxing!"
            show Meraline ehappy:
                linear .2 yalign 10.0
            "She dives into the ocean, leaving all of her supplies behind."
            hide Meraline
            MC "Wait, could you maybe fix my-?"
            "Your sentence stops short when you realize that she is too far to hear you. You sigh and leave the port."
            "Despite not getting your suit mended, you feel like you did something good today."
            $ charProblems["Meraline"] = True
        "Ask her to mend your suit":
            MC "Would you mind mending my suit? I need it for a rally I'm doing soon, and it's not looking great."
            show Meraline happy
            Meraline "Sure, no problem!"
            "She takes the suit from you and starts to mend it. She very quickly patches the holes and hands it back to you."
            show Meraline ehappy
            Meraline "There! It's done."
            show Meraline happy
            MC "Thanks so much, this is great."
            Meraline "No worries."
            MC "How much do I owe you?"
            show Meraline ehappy
            Meraline "Oh, this one is free, for the generous amount you gave me the first time."
            MC "Really? Thanks!"
            show Meraline happy
            "As you start walking away, another person approaches Meraline with something to mend. She takes it and starts at her work again."
            hide Meraline with moveoutleft
    $ charProgress["Meraline"] +=1
    jump ending_handler
