import random
# character placements and thread tracking

# List of locations a character is allowed to show up in
# - an empty list means the character won't show up
# - places can be appended or removed as flags are hit

# Location encoding:
# 1 = Tailor's shop
# 2 = Bakery
# 3 = Castle
# 4 = Guardpost
# 5 = Port
# 6 = Tavern
# 7 = Marketplace
# 8 = Arena
# 9 = Mountain cave
# 10 = Forest
# 11 = Mystic's

# Example character situation:
loc_exp = []
flag = false

# This would be located where the flag actually happens preferably:
if flag:
    loc_exp.append(1)

# Available characters:
unlockedchars = [a, b, c, d]

# Function run at the start of each map section to place characters
def pick_chars():
    renpy.random.shuffle(unlockedchars)
    chosen = unlockedchars[0:2]
    for x in unlockedchars[3:]:
        appear = renpy.random.random()
        if appear > .5:
            chosen.append(x)
    place_chars(chosen)

def place_chars(chosen):
    return
