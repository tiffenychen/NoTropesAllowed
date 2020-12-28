label ending_handler:
    if sum(charProgress.values()) == 15:
        jump end_sequence
    else:
        scene black
        call screen map

label end_sequence:
    "Generic ending stuff"
    if charProblems['Jinglu'] == True:
        "To your surprise, Jinglu took your joke to heart and took running for mayor seriously."
        "And when he went around explaining himself to everyone, they really did begin to understand."
        "Some even already had their suspicions something was up with him that they didn't truly understand."
        "With the townspeople quickly growing comfortable with this demon they've known for ages, your canvassing up until now seems to evaporate in an instant."
        "So you:"
        menu:
            "Canvas harder!!":
                "Which does not work."
                "Sure, you might have provided sound advice here and there, but you literally arrived less than a week ago. Who really knows you?"
            "Gracefully step down":
                "You don't really need this position."
                "Plus, how sad would it be to lose a popularity contest to the candidate who 'terrorized' everyone not but a couple days ago?"
    elif charProblems['Jinglu'] == False and charProblems['Kaelin'] == True:
        "Kaelin looks great in her new tailor shop"
        "You proudly watch as she tidies up all the extra cloth and thread with more care for her work than ever before."
        "Then when all the bits and pieces are gathered up she begins to move it all to the backroom."
        "You almost begin to walk away, but stop when she quickly returns and pulls something out from an obscured corner of the room."
        "It's a very fancy, many layered outfit."
        "And it crosses your mind that it looks kind of like something Jinglu would wear?"
        "But you don't dwell on that. You're sure he'll find new acquintances wherever he went."
        "Kaelin's facing away so you can't read her expression, but you swear her shoulders slump a little as she pulls the outfit off the mannequin."
        "When she goes into the backroom this time, she doesn't come out for a good while."
        "You leave to see what the rest of the village is up to."
