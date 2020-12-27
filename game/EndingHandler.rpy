label ending_handler:
    if sum(charProgress.values()) = 15:
        jump end_sequence
    else:
        scene black
        call screen map

label end_sequence:
    "Placeholder"
