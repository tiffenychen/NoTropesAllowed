image bg black = "#000000"
image bg castle:
    zoom 0.8
    "castle.jpg"
image bg tower:
    zoom 1.2
    "tower.jpg"
image bg port:
    zoom 1.2
    "port.jpg"

screen map():
    add "Map.jpg" xzoom 0.7 yzoom 0.4 #zoom 0.45
    fixed:
        textbutton "CloseMap" xalign 0.0 yalign 0.0 action Hide("map") style "map_label" text_style "map_label_button_text"
    #imagebutton idle "castle.png" xpos  50 ypos 200 action Jump('castle').
    imagebutton idle "m_arena.png" hover "mh_arena.png"  xpos  900 ypos 220 focus_mask True action [Hide('map'),Jump('arena')]
    imagebutton idle "m_cottage.png" hover "mh_cottage.png"  xpos  95 ypos 150 focus_mask True action [Hide('map'),Jump('cottage')]
    imagebutton idle "m_forest.png" hover "mh_forest.png"  xpos  1000 ypos -20 focus_mask True action [Hide('map'),Jump('forest')]
    imagebutton idle "m_guardpost.png" hover "mh_guardpost.png"  xpos  220 ypos 410 focus_mask True action [Hide('map'),Jump('guardpost')]
    imagebutton idle "m_marketplace.png" hover "mh_marketplace.png"  xpos  680 ypos 310 focus_mask True action [Hide('map'),Jump('marketplace')]
    imagebutton idle "m_port.png" hover "mh_port.png"  xpos  1130 ypos 600 focus_mask True action [Hide('map'),Jump('port')]
    #imagebutton idle "cottage.png" hover "cottage.png"  xpos  840 ypos 400 focus_mask True action [Hide('map'),Jump('tailors')]
    imagebutton idle "m_tavern.png" hover "mh_tavern.png"  xpos  500 ypos 300 focus_mask True action [Hide('map'),Jump('tavern')]
    imagebutton idle "filler2.png" hover "filler2.png"  xpos  800 ypos 350 focus_mask True action [Hide('map'),Jump('bakery')]
    #imagebutton idle "cottage.png" hover "cottage.png"  xpos  150 ypos 30 focus_mask True action [Hide('map'),Jump('cave')]
    imagebutton idle "filler1.png" hover "filler1.png"  xpos  330 ypos 365 focus_mask True action [Hide('map'),Jump('castle')]

    showif charProgress['Jinglu'] == 0 and sum(charProgress.values()) > 2:
        image "Nhom_icon.png" xpos 750 ypos 300
    elif charProgress['Jinglu'] == 1:
        image "Jinglu_icon.png" xpos 750 ypos 300
    elif charProgress['Jinglu'] == 2:
        image "Jinglu_icon.png"  xpos  1000 ypos 10

    showif charProgress['Nhom'] != 3:
        image "Nhom_icon.png"  xpos  500 ypos 300

    showif ((charProgress["Gladrock"] == 1 or charProgress["Gladrock"] == 2) and charProgress["Eaden"] == 0):
        image "Eadan_icon.png" xpos 220 ypos 410

    showif charProgress["Gladrock"] != 2:
        image "Gladrock_icon.png" xpos  95 ypos 150

    showif charProgress["Kaelin"] != 3:
        image "Kaelin_icon.png" xpos 900 ypos 220

    showif charProgress['Meraline'] != 3:
        image "Meraline_icon.png"  xpos  1130 ypos 600
    #$ place_chars()
    #imagebutton auto "buttons/exit%s.png" xpos  415 ypos 550 focus_mask True action Jump('castle'), Hide("Anotherscreen") hovered Show("Anotherscreen") unhovered Hide("Anotherscreen")
    #vbox xalign 1.0 yalign 1.0:
     #    imagebutton auto "castle%s.png"
label arena:
    scene bg arena
    jump Kaelin_handler
    return
label bakery:
    "You wander around town for a bit, but nothing of interest happens. Maybe try somewhere else?"
    call screen map
    return
#label cave:
    #scene bg castle
    #MC "We've arrived at the cave"
    #return
label castle:
    "You wander around town for a bit, but nothing of interest happens. Maybe try somewhere else?"
    call screen map
    return
label cottage:
    jump Gladrock_handler
    return
label forest:
    scene bg forest
    jump Jinglu_handler
    return
label guardpost:
    scene bg tower
    jump Eaden_handler
    return
label marketplace:
    jump Jinglu_handler
    return
label port:
    scene bg port
    jump Meraline_handler
    return
#label tailors:
    #scene bg castle
    #MC "We've arrived at the tailor's"
    #return
label tavern:
    scene bg tavern
    jump Nhom_handler
    return

screen mapicon:
  textbutton "Map" action Show("map")
