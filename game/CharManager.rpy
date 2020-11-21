python:
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
    availableLocs = []
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
        availableLocs.append(1) #this would be the place we want to add

    # Available characters and their time availabilities:
    unlockedChars = {"a": {1, 2, 3}, "b": {5, 7}, "c": {4}, "d": {6}}

    #time period would be an incrementing variable
    #global period = 0

    #grabs the characters meant to be displayed on this day of the week
    def guarenteed_chars():
        dayofweek = period % 0

        for character in unlockedChars:
            if dayofweek in unlockedChars[character]:
                chosen.append(character)
                #remove location from list of locations a character can spawn
                #maintain a list of available chars
                pass

        availableChars = [unlockedChars.key() not in chosen]
        pick_chars(availableChars)


    # Function run at the start of each map section to pick bonus characters
    def pick_chars(availableChars):
        #renpy.random.shuffle(unlockedchars)
        #chosen = unlockedchars[0:2]
        locs = len(availableLocs)

        if period < 10: #placeholder day 10.
            aRate = .5 #probability a character will appear who isn't meant to
        elif period > 10 and period < 20:
            aRate = .75
        else:
            aRate = .9

        for x in availableChars[3:]:
            if locs <= 0: #we only want to pick as many characters as we have unlocked places
                break

            appear = renpy.random.random()
            if appear > aRate:
                chosen.append(x)
                locs = locs - 1
        place_chars(chosen)

    def place_chars(chosen):
        pass
