image bg black = "#000000"
image bg castle:
    zoom 0.8
    "castle.jpg"


screen map():
    add "Map.jpg" xzoom 0.7 yzoom 0.4 #zoom 0.45
    fixed:
        textbutton "CloseMap" xalign 0.5 yalign 0.3 action Hide("map") style "map_label" text_style "map_label_button_text"
    #imagebutton idle "castle.png" xpos  50 ypos 200 action Jump('castle').
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  900 ypos 200 focus_mask True action [Hide('map'),Jump('arena')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  900 ypos 350 focus_mask True action [Hide('map'),Jump('bakery')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  150 ypos 30 focus_mask True action [Hide('map'),Jump('cave')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  280 ypos 350 focus_mask True action [Hide('map'),Jump('castle')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  130 ypos 150 focus_mask True action [Hide('map'),Jump('cottage')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  980 ypos 0 focus_mask True action [Hide('map'),Jump('forest')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  550 ypos 400 focus_mask True action [Hide('map'),Jump('guardpost')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  750 ypos 300 focus_mask True action [Hide('map'),Jump('marketplace')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  1100 ypos 490 focus_mask True action [Hide('map'),Jump('port')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  840 ypos 400 focus_mask True action [Hide('map'),Jump('tailors')]
    imagebutton idle "cottage.png" hover "cottage.png"  xpos  500 ypos 330 focus_mask True action [Hide('map'),Jump('tavern')]

    showif charProgress['Jinglu'] == 0 and sum(charProgress.values()) > 2:
        image "Jinglu_icon.png" xpos 750 ypos 300
    elif charProgress['Jinglu'] == 1:
        image "Jinglu_icon.png" xpos 750 ypos 300
    elif charProgress['Jinglu'] == 2:
        image "Jinglu_icon.png" xpos 980 ypos 0

    image "Eadan_icon.png" xpos 550 ypos 400
    #$ place_chars()
    #imagebutton auto "buttons/exit%s.png" xpos  415 ypos 550 focus_mask True action Jump('castle'), Hide("Anotherscreen") hovered Show("Anotherscreen") unhovered Hide("Anotherscreen")
    #vbox xalign 1.0 yalign 1.0:
     #    imagebutton auto "castle%s.png"
label arena:
    scene bg castle
    MC "We've arrived at the arena"
    return
label bakery:
    scene bg castle
    MC "We've arrived at the bakery"
    return
label cave:
    scene bg castle
    MC "We've arrived at the cave"
    return
label castle:
    scene bg castle
    MC "We've arrived at the castle"
    return
label cottage:
    scene bg castle
    MC "We've arrived at the cottage"
    return
label forest:
    scene bg forest
    jump Jinglu_handler
    return
label guardpost:
    scene bg castle
    jump Gladrock_handler
    return
label marketplace:
    scene bg castle
    jump Jinglu_handler
    return
label port:
    scene bg castle
    jump Meraline_handler
    return
label tailors:
    scene bg castle
    MC "We've arrived at the tailor's"
    return
label tavern:
    scene bg tavern
    jump Nhom_handler
    return

screen mapicon:
  textbutton "Map" action Show("map")
