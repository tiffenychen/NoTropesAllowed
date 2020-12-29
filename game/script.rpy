# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Eaden = Character("Eaden")
define Kaelin = Character("Kaelin")
define Nhom = Character("Nhom")
define Litt = Character("Litt")
define Jinglu = Character("Jinglu")
define Meraline = Character("Meraline")
define Gladrock = Character("Gladrock")
define MC = Character("Me")
define Gambler = Character("Gambler")
define w = Character("???")

#character transforms
transform sleft:
    yalign 1.0
    xalign .25
transform sright:
    yalign 1.0
    xalign .75
transform hop: #makes character do small jump
    yalign 1.0
    linear .1 yalign .5
    linear .1 yalign 1.0
transform sink: #character sinks down a little
    yalign 1.0
    linear .1 yalign 1.3
transform rise: #character comes back up form a sink
    yalign 1.3
    linear .1 yalign 1.0
transform shake:
        yalign 1.0
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
transform extend_dissolve:
    alpha 0.0
    linear 4.0 alpha 1.0
    on replace:      # when new image appears
        alpha 0.0
        linear 4.0 alpha 1.0
    on replaced:     # when old image disappears
        linear 4.0 alpha 0.0
transform offscreen:
    xalign 1.4

#backgrounds
image bg arena:
    zoom 1.7
    "arena.jpg"
image bg forest:
    zoom .5
    "forest.jpg"
image bg tavern:
    zoom 1.42
    "tavern.jpg"
image bg cave:
    zoom 1.5
    "cave.jpg"
image bg marketplace:
    zoom 2.8
    "marketplace.jpg"
image bg shrubbery:
    zoom 0.8
    "shrubbery.jpg"
image bg dunny_table:
    zoom 2.8
    "thundrone_estate.jpg"

#Eadan images
image Eaden happy:
    zoom .35
    "Eadan_happy.png"
image Eaden sad:
    zoom .35
    "Eadan_sad.png"
image Eaden confused:
    zoom .35
    "Eadan_confused.png"
image Eaden sorry:
    zoom .35
    "Eadan_sorry.png"
image Eaden angry:
    zoom .35
    "Eadan_angry.png"
image Eaden annoyed:
    zoom .35
    "Eadan_annoyed.png"
image Eaden:
    zoom .75
    "Eaden_icon.png"

#Jinglu images
image Jinglu happyh:
    zoom .45
    "Jinglu_happyh.png"
image Jinglu sadh:
    zoom .45
    "Jinglu_sadh.png"
image Jinglu confusedh:
    zoom .45
    "Jinglu_confusedh.png"
image Jinglu cryh:
    zoom .45
    "Jinglu_cryh.png"
image Jinglu angryh:
    zoom .45
    "Jinglu_angryh.png"
image Jinglu annoyedh:
    zoom .45
    "Jinglu_annoyedh.png"
image Jinglu smirkh:
    zoom .45
    "Jinglu_smirkh.png"
image Jinglu worryh:
    zoom .45
    "Jinglu_worryh.png"
image Jinglu blushh:
    zoom .45
    "Jinglu_blushh.png"
image Jinglu happy:
    zoom .25
    "Jinglu_happy.png"
image Jinglu sil:
    zoom .25
    "Jinglu_sil.png"
image Jinglu smirk:
    zoom .25
    "Jinglu_smirk.png"
image Jinglu worry:
    zoom .25
    "Jinglu_worry.png"
image Jinglu:
    zoom .75
    "Jinglu_icon.png"

#Meraline images
image Meraline happy:
    zoom .5
    "Meraline_happy.png"
image Meraline sad:
    zoom .5
    "Meraline_sad.png"
image Meraline angry:
    zoom .5
    "Meraline_angry.png"
image Meraline ehappy:
    zoom .5
    "Meraline_ehappy.png"
image Meraline unsure:
    zoom .5
    "Meraline_unsure.png"
image Meralinei:
    zoom .75
    "Meraline_icon.png"

#Gladrock images
image Gladrock happyh:
    zoom .55
    "Gladrock_happyh.png"
image Gladrock sadh:
    zoom .55
    "Gladrock_sadh.png"
image Gladrock confusedh:
    zoom .55
    "Gladrock_confusedh.png"
image Gladrock angryh:
    zoom .55
    "Gladrock_angryh.png"
image Gladrock worryh:
    zoom .55
    "Gladrock_worryh.png"
image Gladrock happy:
    zoom .4
    "Gladrock_happy.png"
image Gladrock sil:
    zoom .4
    "Gladrock_sil.png"
image Gladrock smirk:
    zoom .4
    "Gladrock_smirk.png"
image Gladrock worry:
    zoom .4
    "Gladrock_worry.png"
image Gladrock:
    zoom .75
    "Gladrock_icon.png"

#Nhom images
image Nhom angry:
    zoom .4
    "Nhom_angry.png"
image Nhom confused:
    zoom .4
    "Nhom_confused.png"
image Nhom happy:
    zoom .4
    "Nhom_happy.png"
image Nhom neutral:
    zoom .4
    "Nhom_neutral.png"
image Nhom sad:
    zoom .4
    "Nhom_sad.png"
image Nhom:
    zoom .75
    "Nhom_icon.png"
#Kaelin images
image Kaelin angry:
    zoom 1.0
    "Kaelin_angry.png"
image Kaelin:
    zoom 1.0
    "Kaelin.png"



#textbutton tr["fr"].music[k] action [mr.Play(music[k]), SelectedIf(renpy.music.get_playing() == music[k])] style "map_label" text_style "map_label_button_text"



# The game starts here.

label start:

    python:
        charProgress = {
            "Eaden": 0,
            "Kaelin": 0,
            "Nhom": 0,
            "Gladrock": 0,
            "Meraline": 0,
            "Jinglu": 0}
        charProblems = {
            "Eaden": False,
            "Kaelin": False,
            "Nhom": False,
            "Gladrock": False,
            "Meraline": False,
            "Jinglu": False}
        storyTag = ["_beg", "_med", "_end"]

    show screen mapicon

    init:
        image black = Solid((0, 0, 0, 255))
        image MediumVioletRed = Solid("#c71585")

    scene black
    "I've been traveling for days and I'm finally here..."
    $ tname = renpy.input("The town of:")
    if tname == "":
        $tname = "Nowheresville"
    MC "The town of %(tname)s awaits me."
    #scene town image with fade
    "Well..it certainly is small. Smaller than I expected, actually. {i}Quite{/i} small."
    show Gladrock happyh at center
    Gladrock "Fare ye well, young traveller!"
    MC "AH! What the?!"
    show Gladrock sadh
    Gladrock "Terribly sorry, fair pilgrim, I did not mean to startle ye. {w}You, that is."
    $ pname = renpy.input("Actually, my name is:")
    MC "Who are you? Why have you accosted me?"
    show Gladrock confusedh at center, hop
    Gladrock "{i}Accosted?{/i}"
    show Gladrock angryh at center, hop
    Gladrock "Why I have never been more offended in all my days, youthful wanderer. I am not here to {i}accost.{/i}"
    show Gladrock happyh at center, hop
    Gladrock "I am here to welcome! I am shocked that you have not heard tell of me, Gladrock the Wise!"
    MC "Oh...my apologies Mr. Gladrock, I have not heard tell. But it is only because I lead the life of a nomad, cursed to wander until I have found my true home...which, I believe, is here!"
    Gladrock "You have come to stay, then?"
    MC "Come to stay? I have come to do more than stay Mr. W. I have come to take charge! To be your leader!"
    show Gladrock confusedh
    Gladrock "Come again?"
    MC "I have come...to run for mayor."
    show Gladrock worryh
    Gladrock "Oh. Well. I see."
    MC "You see, I have walked for many days and many nights to stand before you today. Three, to be exact."
    show Gladrock confusedh
    Gladrock "Three days and nights? So a weekend?"
    MC "I have wandered! And now I have arrived. To my final resting place."
    show Gladrock worryh
    Gladrock "You're not a ghost, are you? Because I'm afraid %(tname)s is not fully equipped to meet the needs of the undead."
    show Gladrock confusedh
    MC "Not dead, oh wise warlock. Very much alive."
    show Gladrock happyh
    Gladrock "I see. So, you are cursed, you say?"
    show Gladrock happyh at sleft, hop
    Gladrock "Point me toward the villain that has hexed you!"
    show Gladrock happyh at sright, hop
    Gladrock "I will make short work of them."
    show Gladrock happyh at center with move
    MC "No, no not that kind of curse. The curse...of ambition! I have long labored under this hex, for it is a formidable curse indeed. I am afraid that I am doomed—no, destined, to assume the office that haunts my dreams!"
    show Gladrock confusedh
    Gladrock "Mayor?"
    MC "Exactly!"
    show Gladrock happyh
    Gladrock "I see. Well, I must offer my congratulations to you. You have reached us just in time for the hour of our mayoral race. Our election be on the very next week."
    MC "It be next week? Oh. I did think I had a bit more time."
    Gladrock "The residents of this great and legendary town will be pleased that someone as illustrious as yourself has come to try their luck in this grand competition: the municipal election! Tell me, what has prepared you to assume this noble office? What life experiences do you bring to our embattled and everlasting town?"
    MC "I bring a lifetime of political expertise! You see, old warlock, I have thrown my name into the proverbial ring, as it were—as in, I have run for mayor—not once, not twice, not thrice, but ten times!"
    show Gladrock worryh at center, sink
    Gladrock "Ten...ten times? Have you ever...won a race?"
    MC "I don't trouble myself with the particulars. I travel, eternally traveling, running in each race that I come across. I have yet to find success. But then I heard that %(tname)s was having a race and I thought, yes, this is the one! The one I have been waiting for! My time has finally come."
    Gladrock "...I see."
    show Gladrock happyh at center, rise
    Gladrock "Well I commend your strength of character. We most definitely need a hero in this town, for %(tname)s has long been threatened by three villains of the most fearsome kind."
    MC "Three villains? A quest, at last! Tell me about these horrors, wise wizard."
    Gladrock "The first is a dragon, a beast whose terrifying reign has gone unchallenged. He has kidnapped a fair maiden from the marketplace and he keeps her locked up in a tower in the forest."
    MC "A fair maiden? Locked in a tower? That's wonderful!"
    show Gladrock confusedh
    "..."
    MC "I mean *cough* that's terrible. I'm so sorry to hear it."
    show Gladrock angryh
    Gladrock "The next villain is a giant, an enormous monster that threatens to destroy our town. His strength is unmatched by anyone, so we have been unable to defeat him."
    show Gladrock worryh
    MC "Sounds terrifying! This is great! Ah—awful. I meant to say awful."
    show Gladrock angryh
    Gladrock "I have saved this villain for last because I sense he will pose the most threat to your plan. Our town is plagued by a demon! And he has decided to make a grab for power...by running for mayor."
    MC "A demon is running for mayor? My sources were correct, this campaign will be a breeze! Point me towards the town's center! I plan to start campaigning right away."
    show Gladrock happyh at center, hop
    Gladrock "Follow me then, oh weary wanderer. The town of %(tname)s welcomes you!"
    hide Gladrock with moveoutright
    #scene marketplace with fade
    MC "Hold on, did that sign say... '%(tname)s: Home of Gladrock the Wet'?"
    show Gladrock angryh with dissolve
    Gladrock "Wise. It was meant to say Wise. Typo."
    MC "How outrageous. Mistakes of that nature won't happen when I'm in charge."
    show Gladrock happyh
    Gladrock "Happy days! In that case may I suggest that changing the sign become a priority for your mayoral administration? You'd have my vote, oh fine, visionary candidate."
    MC "I'll think about it."
    Gladrock "Please do, oh ingenious visitor. Come out to greet me any time you wish to discuss this matter further. In the meantime, this is where I shall leave you. I must stand watch at the entrance to welcome other travelers, such as yourself."
    MC "Do you get visitors often?"
    Gladrock "About once or twice a year. So you see, my job is of utmost importance."
    MC "I do see. Well, farewell Gladrock the Wise. My destiny awaits me!"
    scene black
    call screen map
