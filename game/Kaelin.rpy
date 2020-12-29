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
    "She gives you a meaningful look, and you hold your hands up in surrender."
    MC "I'm not here to make trouble."
    w "Hah, here near the arena or here in this town?"
    "Do you really stand out that much?"
    show Kaelin at center, shake 
    "She barks a laugh when she sees your startled face."
    w "You don't look like you're from here at all, if that's what you're gaping at."
    MC "I... Didn't know it was that obvious."
    w "Oh, it's extremely obvious."
    show Kaelin:
        zoom 1.5 
        linear 0.5 xalign 0.9 yalign 1.0  
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
    "You turn around and see Kaelin leering over you."
    MC "Kaelin!"
    "She narrows her eyes."
    Kaelin "How do you know my name?"
    MC "Hahah! Uhh I saw it embroidered on your coat?"
    "She suddenly takes a step back."
    Kaelin "On my coat? You saw my name?"
    MC "Haha, yeah! It looked really fancy."
    Kaelin "Did it?"
    MC "Yeah! Did someone else do that for you?"
    Kaelin "Who? No, I did it myself."
    MC "Really?"
    Kaelin "Yeah, is that so hard to believe?"
    MC "No! I mean, you can be multi-talented, I just didn't expect..."
    Kaelin "What, you didn't expect a tiefling assassin to have a sidehobby in embroidery?"
    MC "That's not what I meant, you can do whatever you want to, I'm not here to judge."
    "She looks at you distrustfully."
    Kaelin "You really think so?"
    MC "Yeah! I mean, you gotta do what makes you happy, right?"
    Kaelin "I gotta do what pays the bills."
    MC "And why can't that be something you're happy with?"
    MC "Are you happy running around doing all of these requests for other people?"
    "She looks at your for some time, weighing your words in her head."
    Kaelin "...No."
    MC "Then there's no reason for you to continue doing it?"
    Kaelin "I mean, the money."
    MC "Yes, but it looks like there are other things that might make you happier. Why did you embroider your cape? With your name no less?"
    Kaelin "I just wanted to, okay? Is there anything wrong with that?"
    MC "No, that's what I'm saying. If you like embroidery and sewing, why not open up a tailor shop or something? People always need new clothes, or mending." 
    "She scoffs."
    Kaelin "I'm not going to mend other people's clothes for a living. That's hardly a job." 
    MC "Well, how is it different from your job now? You take requests from people and fulfill them, it's the same thing." 
    "She narrows her eyes suspiciously."
    Kaelin "Why are you trying to help me anyways?"
    MC "You seemed like you needed it."
    Kaelin "You don't even know me. Stop trying to give me advice."
    "Before you can respond, Kaelin darts off into the crowd and is gone."
    "You look after where she was standing, sigh, and continue to canvass the people around you."
    $ charProgress["Kaelin"] +=1
    jump ending_handler


