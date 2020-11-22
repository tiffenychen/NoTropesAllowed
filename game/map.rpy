image bg black = "#000000"
image bg castle:
    zoom 0.8
    "castle.jpg"
image bg tavern:
    zoom 1.2
    "tavern.jpg"

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
    #imagebutton auto "buttons/exit%s.png" xpos  415 ypos 550 focus_mask True action Jump('castle'), Hide("Anotherscreen") hovered Show("Anotherscreen") unhovered Hide("Anotherscreen")
    #vbox xalign 1.0 yalign 1.0:
     #    imagebutton auto "castle%s.png"
label arena:
    scene bg castle
    e "We've arrived at the arena"
    return
label bakery:
    scene bg castle
    e "We've arrived at the bakery"
    return
label cave:
    scene bg castle
    e "We've arrived at the cave"
    return
label castle:
    scene bg castle
    e "We've arrived at the castle"
    return
label cottage:
    scene bg castle
    e "We've arrived at the cottage"
    return
label forest:
    scene bg castle
    e "We've arrived at the forest"
    return
label guardpost:
    scene bg castle
    e "We've arrived at the guard post"
    return
label marketplace:
    scene bg castle
    e "We've arrived at the market place"
    return
label port:
    scene bg castle
    e "We've arrived at the port"
    return
label tailors:
    scene bg castle
    e "We've arrived at the tailor's"
    return
label tavern:
    scene bg tavern
    e "We've arrived at the tavern"
    return

screen mapicon:
  textbutton "Map" action Show("map")
