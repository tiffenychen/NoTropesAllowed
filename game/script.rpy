# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define e = Character("Eileen")


#textbutton tr["fr"].music[k] action [mr.Play(music[k]), SelectedIf(renpy.music.get_playing() == music[k])] style "map_label" text_style "map_label_button_text"

screen map():
    add "Map.jpg" xzoom 0.7 yzoom 0.4 #zoom 0.45
    fixed:
        textbutton "CloseMap" xalign 0.5 yalign 0.3 action Hide("map") style "map_label" text_style "map_label_button_text"
    #imagebutton idle "castle.png" xpos  50 ypos 200 action Jump('castle').
    imagebutton idle "castle.png" hover "castle2.png"  xpos  50 ypos 200 focus_mask True action Jump('castle') #, Hide("mg") hovered [Show("mg", my_picture="map gui/mg_door.png", mg_xpos=0, mg_ypos=505, transition=dissolve)] unhovered [Hide("mg")]

    #imagebutton auto "buttons/exit%s.png" xpos  415 ypos 550 focus_mask True action Jump('castle'), Hide("Anotherscreen") hovered Show("Anotherscreen") unhovered Hide("Anotherscreen")
    #vbox xalign 1.0 yalign 1.0:
     #    imagebutton auto "castle%s.png"

label castle:
      e "We've arrived at Mars "
      return
screen mapicon:
  textbutton "Map" action Show("map")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    show screen mapicon
    #show screen map

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    init:
        image black = Solid((0, 0, 0, 255))
        image MediumVioletRed = Solid("#c71585")
        python:
            style.map_label_button_text.color = "#FF0000"
            style.map_label_button_text.hover_color = "#0000FF"
            style.map_label_button_text.selected_color = "#00FF00"

    # These display lines of dialogue.

    e "You've created a Renpy game! "

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
