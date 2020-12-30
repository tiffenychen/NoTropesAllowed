label Kaelin_handler:
    if charProgress["Kaelin"] == 3:
        "It looks like there's nobody here right now."
        scene black
        call screen map
    else:
        $ renpy.jump("Kaelin" + storyTag[charProgress["Kaelin"]])
label Kaelin_beg:
    "Even from a distance, you can see that the arena is bustling and full of life."
    "People are streaming in and out, and there are many vendors, both licensed and unlicensed advertising their wares."
    "Suddenly there's a loud sigh from the arena, mixed with a few cheers, then more boos. You think you can vaguely hear the clinking of swords."
    show Kaelin with moveinbottom 
    "You notice a figure in the shadows, looking very much like she doesn't want to be seen."
    show Kaelin:
        linear 1.0 xalign 0.3
    "She sneaks up on a much stouter figure and appear to stick something into their back, paralyzing them."
    "No one takes much notice, but you follow her and see her slip a sack around the body."
    "A few other items are rustling around inside as well, and when she lifts it onto their back, the stout figure is impossible to discern from the sack."
    show Kaelin at center, sink 
    "She looks around and sees you looking at her. She eyes you suspiciously."
    w "Who are you?"
    MC "Oh, I'm no one."
    show Kaelin at center, rise
    "She shifts the sack higher onto her shoulder."
    w "Whatever you saw here, you didn't."
    show Kaelin angry
    "She gives you a meaningful look, and you hold your hands up in surrender."
    MC "I'm not here to make trouble."
    show Kaelin
    w "Hah, here near the arena or here in this town?"
    "Do you really stand out that much?"
    show Kaelin at center, shake 
    "She barks a laugh when she sees your startled face."
    w "You don't look like you're from here at all, if that's what you're gaping at."
    MC "I... Didn't know it was that obvious."
    w "Oh, it's extremely obvious."
    show Kaelin angryh
    "She moves extremely quickly and gets right up in your face, blocking your path to safety."
    w "And because of that, I don't trust you."
    w "You're going to tell me who you are, and what you're doing here."
    MC "I'm... Not from here. I've been travelling from some time now, so I'm not really from anywhere."
    MC "I've come here to try and run for mayor."
    w "Mayor... You? You don't even live here."
    "You shrug."
    MC "I just thought I might give it a try. I'm just talking to everyone I see."
    w "Anyways, I'll give you a hint, mayor. Don't stick your nose where it doesn't belong."
    "She turns her back on you, and starts walking away."
    hide Kaelin with moveoutleft 
    "As she does, you can't help but notice a small embroidered name on the base of her cape that reads Kaelin."
    "The name is familiar... You remember reading a poster with an advertisement of the services of a Kaelin, offering any desired services for a fee."
    "You suppose that what you just witnessed was such a service, and shudder a little at the thought." 
    $ charProgress["Kaelin"] +=1
    jump ending_handler
label Kaelin_med:
    "You wander around the arena again, hoping to spot the shadowy Kaelin that you encountered last time."
    MC "Vote for %(pname)s! Vote for %(pname)s in the upcoming election!"
    Kaelin "You're really running for mayor, aren't you?"
    "Your heart leaps a little in shock."
    show Kaelin angryh:
        xalign 0.5
        zoom 1.3
    "You turn around and see Kaelin leering over you."
    MC "Kaelin!"
    "She narrows her eyes."
    Kaelin "How do you know my name?"
    MC "Hahah! Uhh I saw it embroidered on your coat?"
    show Kaelin angry:
        xalign 0.5
        yalign 0.65
    "She suddenly takes a step back."
    Kaelin "On my coat? You saw my name?"
    MC "Haha, yeah! It looked really fancy."
    show Kaelin
    Kaelin "Did it?"
    MC "Yeah! Did someone else do that for you?"
    Kaelin "Who? No, I did it myself."
    MC "Really?"
    Kaelin "Yeah, is that so hard to believe?"
    MC "No! I mean, you can be multi-talented, I just didn't expect..."
    Kaelin "What, you didn't expect a tiefling assassin to have a sidehobby in embroidery?"
    MC "That's not what I meant, you can do whatever you want to, I'm not here to judge."
    show Kaelin angry:
        linear 1.0 yalign 0.3
    "She looks at you distrustfully."
    Kaelin "You really think so?"
    MC "Yeah! I mean, you gotta do what makes you happy, right?"
    Kaelin "I gotta do what pays the bills."
    MC "And why can't that be something you're happy with?"
    MC "Are you happy running around doing all of these requests for other people?"
    "She looks at your for some time, weighing your words in her head."
    show Kaelin
    Kaelin "...No."
    MC "Then there's no reason for you to continue doing it?"
    Kaelin "I mean, the money."
    MC "Yes, but it looks like there are other things that might make you happier. Why did you embroider your cape? With your name no less?"
    Kaelin "I just wanted to, okay? Is there anything wrong with that?"
    MC "No, that's what I'm saying. If you like embroidery and sewing, why not open up a tailor shop or something? People always need new clothes, or mending." 
    "She scoffs."
    Kaelin "I'm not going to mend other people's clothes for a living. That's hardly a job." 
    MC "Well, how is it different from your job now? You take requests from people and fulfill them, it's the same thing." 
    show Kaelin angry 
    "She narrows her eyes suspiciously."
    Kaelin "Why are you trying to help me anyways?"
    MC "You seemed like you needed it."
    Kaelin "You don't even know me. Stop trying to give me advice."
    hide Kaelin with moveoutright
    "Before you can respond, Kaelin darts off into the crowd and is gone."
    "You look after where she was standing, sigh, and continue to canvass the people around you."
    $ charProgress["Kaelin"] +=1
    jump ending_handler
label Kaelin_end:
    "As you near the arena, you notice that there are noticeably fewer people milling around than usual."
    "There are, however, raucous cheers coming from the arena. Suddenly, a pair of doors swing open and a battered Kaelin is thrown out of them."
    show Kaelin:
        linear 0.5 yalign 0.3
    "She looks bruised up, with a faint dark patch blooming across her chest."
    "Another roar comes from the arena as you approach her. She doesn't seem to notice you."
    MC "Are you okay? What's going on in there?"
    Kaelin "Oh, it's you again."
    show Kaelin at left, shake 
    "She brushes herself off, trying to look nonchalant, but she winces a little." 
    MC "Yeah, are you okay? Are you hurt?"
    Kaelin "I'm fine, just tried to earn some money for rent tomorrow with a few jousts in the rink. Turns out, it's a lot harder to fight when your opponent knows you're coming." 
    MC "That tends to make things harder."
    "She groans."
    Kaelin "Ugh, I was only able to survive for two rounds, those people who bet on me must be so pissed..." 
    MC "People bet on you?"
    Kaelin "Yeah, it's a whole sport to them. Meanwhile I'm out there fighting, and they promised me money for each round I survived, but fat chance I'm getting anything now."
    show Kaelin h:
        linear 1.0 xalign 0.5 yalign 0
    "She coughs, and when she moves her arm away, there's blood on her elbow."
    MC "Geez, your clothes are all bloody."
    show Kaelin h at center, rise
    Kaelin "Really??" 
    "She looks incredibly alarmed." 
    Kaelin "No, no, no, I just fixed these up last night, I'm going to have to resew these, this blood is never going to wash out..." 
    "She starts to strip her clothes, revealing a whole cluster of wounds around her chest."
    MC "Whoa, whoa! Here, you can take my coat." 
    "She looks at you, an eyebrow raised."
    Kaelin "Seriously? That won't fit at all."
    MC "Fine, maybe there are some bandages in my pockets, hold on... Yes!"
    "You fish out a few bandages and she takes it quickly, and begins to warm up her wounds."
    show Kaelin
    "Suddenly, there's a shout from behind Kaelin, and a few people come into view, backs hunched, eyes blazing."
    "Kaelin's eyes widen."
    Kaelin "Those are the people that gambled on me! No, no, no, I gotta get out of here..."
    "It's too late. They spot her, and begin to stomp over."
    Gambler "Hey, Kaelin! You didn't survive as long as you said you would."
    show Kaelin at center, shake
    Kaelin "No, I- I'm sorry, I'll do better tomorrow, I promise!"
    Gambler "Now I lost a solid 30 silver pieces betting on you, so I'm not thinking about tomorrow right now. I'm thinking about today, and how you cost me those 30 silver pieces, and how you're gonna pay..."
    MC "Hey, it's not her fault that you bet that much money on her. Leave her alone."
    Gambler "You stay out of this."
    menu: 
        "Offer to pay the 30 silver pieces they lost": 
            $ charProblems["Kaelin"] = True
            MC "Hey, listen."
            "You pull 30 silver pieces out of your money sack and jingle it in your hand."
            MC "I have 30 silver pieces here to give you back what you lost, but in return, you're going to have to leave Kaelin alone."
            "The gamblers contemplate, then one of them takes the pieces from your hand. He turns to look at Kaelin menacingly."
            Gambler "Fine, you're safe this time. But if I ever lose money on you again, I'll make sure you regret it." 
            "They walk away, and Kaelin turns to you."
            show Kaelin h at center 
            Kaelin "I... Thank you, %(pname)s."
            "She falls silent, and you smile encouragingly."
            MC "No problem. Doesn't seem all that great when there are people coming after you all the time."
            Kaelin "No, it isn't."
            show Kaelin h at center, sink
            "She sighs deeply."
            Kaelin "I think.... I think I'm going to try to do something else."
            Kaelin "I can't keep doing this, running around beating people up and getting beaten up. Maybe I should try something new."
            MC "You already seem to have skills in tailoring, so why not start with that?"
            Kaelin "Yeah..."
            show Kaelin at center, hop
            "She looks wistful, but then remembers something and jumps."
            Kaelin "But what about tomorrow's rent? I can't push it back more, I'll get kicked out if I don't pay it this month..."
            MC "How much is it?"
            Kaelin "It's 50 silver pieces, and I don't even have 10."
            MC "Here."
            "You toss your money bag over to her."
            Kaelin "What... Really?"
            "She opens it up and smiles with glee."
            Kaelin "This is more than enough! Wow, there are even some gold pieces in here! Maybe I can even buy a shop with this money..."
            MC "Wait, no, I didn't realize there was that much in there, just take what you need..."
            "You realize you probably should have checked to make sure the sack didn't contain all your life savings, but Kaelin is now smiling broadly."
            Kaelin "I'll go pay up right now, and then I'll go get some more sewing supplies..."
            hide Kaelin with moveoutright 
            "She starts walking off, surprisingly quickly for being injured, and you try and follow her, but once she gets to the populated areas of town, you lose her in the crowd."
            "Oh well. You probably have some emergency money saved in your tavern room..."
        "Try to reason further with the betters":
            MC "She's obviously vulnerable, why are trying to take advantage of her?"
            Gambler "Hey, %(pname)s is it? I've seen your face around town. If you know what's good for you, get out of here. This ain't your business, unless you want to get a beating too."
            "You gulp, look at Kaelin, and hold your hands up. Your mayoral campaign is on the line here, these people look like they're angry enough to take anyone down if they wanted."
            MC "Sorry, I'll take my leave."
            hide Kaelin with dissolve 
            "You make eye contact with Kaelin one more time before you go, and she gives you a look of resignation."
            "You barely know each other, you reason. She seems to understand."
            "There's nothing you can do."
    $ charProgress["Kaelin"] +=1
    jump ending_handler


