label ending_handler:
    if sum(charProgress.values()) == 15:
        jump end_sequence
    else:
        scene black
        call screen map

label end_sequence:
    scene black
    "The week went by in a flash, but you find that with the size of the town you already know basically everyone's name."
    "You're sure you have this election in the bag."
    if charProblems['Jinglu'] == True:
        show Jinglu happyh with dissolve
        "However, to your surprise, Jinglu took your joke to heart and took running for mayor seriously."
        "And when he went around explaining himself to everyone, they really did begin to understand."
        "Some already had their suspicions something was up with him that they didn't truly understand."
        "With the townspeople quickly growing comfortable with this demon they've known for ages, your canvassing up until now seems to evaporate in an instant."
        "So you:"
        menu:
            "Canvas harder!!":
                "Which does not work."
                "Sure, you might have provided sound advice here and there, but you literally arrived less than a week ago. Who really knows you?"
            "Gracefully step down":
                "You don't really need this position."
                "Plus, how sad would it be to lose a popularity contest to the candidate who 'terrorized' everyone not but a couple days ago?"
        "Not being mayor stung, but not nearly as much as you thought it would."
        "You think maybe you should see how everyone is doing at the start of this new era of leadership."
        hide Jinglu with dissolve
    elif charProblems['Jinglu'] == False:
        "This became especially true when your only opponent quietly left in the middle of the night."
        "He left a small note saying good luck and to watch over Kaelin for him."
        "So knowing that, the first thing you do as mayor is go to check on her."
        if charProblems['Kaelin'] == True:
            show Kaelin with dissolve
            "Kaelin looks great in her new tailor shop"
            "You proudly watch as she tidies up all the extra cloth and thread with more care for her work than ever before."
            "Then when all the bits and pieces are gathered up she begins to move it all to the backroom."
            "You almost begin to walk away, but stop when she quickly returns and pulls something out from an obscured corner of the room."
            "It's a very fancy, many layered outfit."
            "And it crosses your mind that it looks kind of like something Jinglu would wear?"
            "But you don't dwell on that. You're sure he'll find new acquintances wherever he went."
            show Kaelin at sink
            "Kaelin's facing away so you can't read her expression, but you swear her shoulders slump a little as she pulls the outfit off the mannequin."
            hide Kaelin with moveoutleft
            "When she goes into the backroom this time, she doesn't come out for a good while."
            "You leave to see what the rest of the village is up to."

    if charProblems['Jinglu'] == True and charProblems['Kaelin'] == True:
        show Kaelin with dissolve
        "You notice a new tailor shop opening right by the entrance of town, and you are delighted to see Kaelin there, sweeping up loose threads."
        "She brightens when she sees you, and shows you all of the threads and fabrics she has in stock, and sends you away with a nice new shirt."
        "The store is bustling and in time, has to expand next door."
        "You're so proud at all the work she's done, and go to see what the rest of the village is up to."
        hide Kaelin with moveoutright
    elif charProblems['Kaelin'] == False:
        "You don't find Kaelin, but all of her posters offering her services are still up."
        "You still hear of a well-dressed tiefling offering to do anything for a price, but no one seems to take the offer seriously."
        "Soon, you realize, all of her posters are gone, covered up or ripped away."
        "When you ask a barkeep, you hear that she's left town."
        "When you press the barkeep further, he snorts in derision."
        "No one seems to care, and soon, you don't either."
        "You go instead to see what the rest of the town is up to."

    if charProblems['Meraline'] == True:
        show Meraline ehappy with dissolve
        "Following your encouragement, Meraline pursues a career in underwater boxing."
        "It's tough work, but her flashy costumes make her stand out, and she ends up winning the championship in five years. She goes by 'Sharpgill' in the rink."
        hide Meraline with dissolve
    elif charProblems['Meraline'] == False:
        show Meraline happy with dissolve
        "Meraline continues to repair clothes for passersby at the port."
        show Meraline sad
        "She gets a few more big name clients, but business soon starts to slow down. She wasn't ever able to purchase a fancy tank."
        hide Meraline with moveoutright

    if charProblems['Nhom'] == True:
        show Nhom happy with dissolve
        "Nhom happily uses the funds that he's accrued from his family's legacy of tavern owners and dips into his quests' rewards to purchase a large home in a nice crook of the forest."
        "Nhom doesn't end up defining what exactly this new building is, but at its core: it's a home."
        "Nhom's collection of orphans are frequently seen running amok in town or coming back with new stories about the quests they've been on. You see Nhom at the tavern on Fridays laughing away with Dunny the Giant about what the kids are up to these days"
        hide Nhom happy with moveoutright
    elif charProblems['Nhom'] == False:
        show Nhom neutral with dissolve
        if end_nhom == "t":
            "Nhom takes up the pedestal of being tavern owner of %(tname)s to the surprised delight of his entire family."
            "Nhom's orphans gradually all leave %(tname)s as they feel like they're a burden on their old boss' funds."
            "You see him frequently telling travelers of the great exploits he used to get up to and his crew of orphans that would accompany him."
            "Nhom's often found lost in thought if he isn't taking care of tavernly responsibilities"
        elif end_nhom == "a":
            "Nhom leaves %(tname)s with his crew of orphans and sets out for his next big quest over and over again."
            "He feels content getting up to mischief with his found family but makes sure to check in with his family back home every so often."
            "He worries his hair gray, nagging at his kids to be careful of their safety. The mischief starts taking a toll on his bones but he keeps going to serve as the heroic boss to his kiddos."
            "He feels his heart break every time they get injured and wonders if this is the best of parenting conditions for them"
        hide Nhom with dissolve

    if charProblems['Eaden'] == True:
        show Eaden happy with dissolve
        "People were skeptical about Eaden's desire to be a knight, but with you vouching for him, they let him try."
        "And it works gloriously."
        "Who doesn't love being defended by a giant dragon?"
        "After getting the position, he promises to visit you regularly and bring tea when he comes."
        hide Eaden with dissolve
    elif charProblems['Eaden'] == False:
        show Eaden happy with dissolve
        "Eaden does end up talking to Janet's father about working at the bakery, but they agreed it wasn't a fit."
        show Eaden sad
        "The town just feels too small and empty to him after Janet left."
        hide Eaden with dissolve
        "So Eaden eventually takes off, too. You only realize when you saw the shadow of a dragon pass one last time over the town before swooping into the mountains."
        "He never even said goodbye."

    if charProblems['Gladrock'] == True:
        show Gladrock happy with dissolve
        "Gladrock's always seemed exceedingly high energy, but after you recommend the triathalon he just became a force of nature."
        "And not of only the watery kind."
        "He waves at you as he runs past the finish line before anybody else."
        hide Gladrock happy with dissolve
    elif charProblems['Gladrock'] == False:
        "Gladrock's door is locked when you go to see what he's up to."
        "There's just a do not disturb sign up."
        "You guess he's trying really hard to get back into his studies."

    $ success = sum(charProblems.values())

    if success >= 3:
        if charProblems['Jinglu'] == True:
            "As you finish checking up, you find you've actually grown pretty attached to all the townsfolks."
            "And when you begin to pack up your wagon once more, you find you can't bear to leave {w}even if you're not mayor."
            "Without really thinking about it too hard, you wander over to a cottage you remembered had a vacancy a couple days ago..."
        else:
            "The town already adores you because you've helped so many of them."
            "You have a good feeling that this is going to be meaningful and long lasting position."
        "And you think thank goodness that whole campaign business is over because no matter what this..."
        scene black
        with Pause(1)
        show text "{size=50}This is home{/size}"
        with Pause(2)
        hide text
    else:
        if charProblems['Jinglu'] == False:
            "You're happy to have won, but the townsfolk don't all seem as excited."
            "In fact, it doesn't take very long for them to decide that perhaps they still aren't ready for a mayor."
            "And with them hovering at the cusp of having a large enough population for one..."
            "They simply remove the office the second someone else moves out."
        else:
            "You did end up sticking around a while to see if Jinglu slips up and leaves you an opening..."
            "But he doesn't. He's pretty good at his job and you hate to admit it."
            "Oh well."
        "You suppose it's time to get back on the road."
        "The town was sure full of some interesting characters."
        "Too many of which seem unhappy with what they're doing."
        "So it's off to greener pastures! The next town will be better. You're sure of it."
