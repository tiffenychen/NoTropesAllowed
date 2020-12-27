# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define Eadan = Character("Eadan")
define Kaelin = Character("Kaelin")
define Nhom = Character("Nhom")
define Jinglu = Character("Jinglu")
define Meraline = Character("Meraline")
define Gladrock = Character("Gladrock")
define MC = Character("Me")
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
transform shake:
        yalign 1.0
        xalign .75
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

#Eadan images
image Eadan happy:
    zoom .35
    "Eadan_happy.png"
image Eadan sad:
    zoom .35
    "Eadan_sad.png"
image Eadan confused:
    zoom .35
    "Eadan_confused.png"
image Eadan sorry:
    zoom .35
    "Eadan_sorry.png"
image Eadan angry:
    zoom .35
    "Eadan_angry.png"
image Eadan annoyed:
    zoom .35
    "Eadan_annoyed.png"
image Eadan = "Eadan_icon.png"

#Jinglu images
image Jinglu happy:
    zoom .45
    "Jinglu_happyh.png"
image Jinglu sad:
    zoom .45
    "Jinglu_sadh.png"
image Jinglu confused:
    zoom .45
    "Jinglu_confusedh.png"
image Jinglu cry:
    zoom .45
    "Jinglu_cryh.png"
image Jinglu angry:
    zoom .45
    "Jinglu_angryh.png"
image Jinglu annoyed:
    zoom .45
    "Jinglu_annoyedh.png"
image Jinglu smirk:
    zoom .45
    "Jinglu_smirkh.png"
image Jinglu worry:
    zoom .45
    "Jinglu_worryh.png"
image Jinglu = "Jinglu_icon.png"

#textbutton tr["fr"].music[k] action [mr.Play(music[k]), SelectedIf(renpy.music.get_playing() == music[k])] style "map_label" text_style "map_label_button_text"



# The game starts here.

label start:

    python:
        charProgress = {
            "Eadan": 0,
            "Kaelin": 0,
            "Nhom": 0,
            "Gladrock": 0,
            "Meraline": 0,
            "Jinglu": 0}
        charProblems = {
            "Eadan": False,
            "Kaelin": False,
            "Nhom": False,
            "Gladrock": False,
            "Meraline": False,
            "Jinglu": False}
        storyTag = ["_beg", "_med", "_end"]

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen mapicon
    #show screen map

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show Jinglu happy

    init:
        image black = Solid((0, 0, 0, 255))
        image MediumVioletRed = Solid("#c71585")


    # These display lines of dialogue.

    #e "Once you add a story, pictures, and music, you can release it to the world!"
    w "Test"

    # This ends the game.

    return
