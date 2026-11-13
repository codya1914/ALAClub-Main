
# Online Connections - Visual Novel

# Characters
define mc = Character("[player_name]")
define friend = Character("[friend_name]")
define narrator = Character(None)

# Player information
default player_name = "Player"
default friend_name = "Mike"

# Backgrounds
image bg bedroom = Solid("#303b55")
image bg computer = Solid("#202b3d")
image bg outside = Solid("#697c91")

# Start of the game
label start:

    scene bg bedroom

    play music "12 PM.mp3" fadein 2.0

    narrator "..."

    narrator "The sound of an alarm slowly pulls you out of sleep."

    narrator "Another morning. Another day."

    $ player_name = renpy.input(
        "What is your name?",
        default="Player",
        length=20
    ).strip()

    if player_name == "":
        $ player_name = "Player"

    mc "Well, time to get up."

    narrator "You reach for your phone and check your notifications."

    scene bg computer

    narrator "After getting ready, you sit down at your computer."

    narrator "A message notification appears."

    $ friend_name = renpy.input(
        "What is your freinds name?",
        default="Mike",
        length=20
    ).strip()

    if friend_name == "":
        $ friend_name = "Mike"

    friend "Hey! Are you there?"

    mc "Yeah, what's up?"

    friend "I found something I think you'd like."

    mc "What is it?"

    friend "It's this new online friendship platform."
    
    friend "You can meet people, talk, and make new friends."

    mc "You know I don't usually do stuff like that."

    friend "Come on! Just give it a try."

    mc "..."

    stop music fadeout 2.0
    
    menu:
        "Download the platform":
            mc "Fine. I'll give it a shot."
            jump download_platform

        "Tell Alex you're not interested":
            mc "I don't really think it's for me."
            friend "That's fair. Just thought I'd ask."
            jump stay_offline


label download_platform:

    narrator "You open the website and begin downloading the application."

    narrator "A registration screen appears."

    mc "Well... here goes nothing."

    narrator "You have officially joined the platform."

    narrator "Little do you know, this decision will change your life."

    jump game_continues


label stay_offline:

    narrator "You close the conversation and return to what you were doing."

    narrator "Maybe another day."

    return


label game_continues:

    narrator "Your story is just beginning."

    return