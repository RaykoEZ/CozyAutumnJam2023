﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
# TODO: Secret ending check
label start:
    # Check for clue 1 to see if we choose to go to shrine
    scene black with dissolve
    call prologue from _call_prologue
    stop music fadeout 1.0
    pause 1.0
    python:
        # find secret file
        inviteCheck = CheckTextInFile("moon/" + inviteFilename, persistent.secretPlayerName)           
        secretCheck = inviteCheck and povName == persistent.secretPlayerName
    if secretCheck:
        pause 1.0
        jump chapter1x
    else:            
        # These display lines of dialogue.
        call chapter1 from _call_chapter1
    stop music fadeout 0.5
    call chapter2 from _call_chapter2
    stop music fadeout 0.5
    pause 1.0
    # check for chapter 2 decision
    if refuseToHelp:
        # Lied to Kaguya, go to bad version of end 1.
        $ affinity -= 1 
        jump end1
    else:
        call chapter3 from _call_chapter3
    stop music fadeout 0.5
    stop rain fadeout 1.0
    pause 1.0
    scene sky night with fade
    # Night begins, need to head to final destination
    "The raining sky clears up."
    "With the sun set, we don't have much time left."
    # panic/worry/frown
    show kag surprise
    pause 1.0
    show monologueFilter
    "Kaguya is getting restless, we need to make a move."
    hide monologueFilter
    $ PlayBGM("bgm_tense", vol = 0.1, fadeIn = 10)
    k "C'mon! Do we know where to find this bugger?"
    jump chooseDestination
    # This ends the game.
    return

menu chooseDestination: 
    p "Where do we go for the night?"
    "Park":
        call confirmDestination from _call_confirmDestination
        if _return:
            jump chapter4_Park        
        else:
            jump chooseDestination 
    "Shrine":
        call confirmDestination from _call_confirmDestination_1
        if _return:
            jump chapter4_Shrine        
        else:
            jump chooseDestination 
    "Store":
        call confirmDestination from _call_confirmDestination_2
        if _return:
            jump chapter4_Store
        else:
            jump chooseDestination 
    "Stay in my room":
        call confirmDestination from _call_confirmDestination_3
        if _return:
            jump chapter4_Room
        else:
            jump chooseDestination 
    "Think about it":
        call thinking from _call_thinking
        jump chooseDestination  

menu confirmDestination:
    "Am I sure about this? We won't have enought time to check other places."
    "Yes":
        return True
    "No":
        return False

# list clues obtained for decision making
label thinking:
    show monologueFilter with fade
    "To sum up what we currently know:"
    
    "We have an idea of the true Identity of the Inquisitor - {color=#fff238}a cunning, shape-shifting black rabbit.{/color}"
    # identity clue check
    if identityKnown:       
        """{color=#fff238}A peculiar elderly man is seen frequenting the shrine at night recently.{/color}
        
        Perhaps he has something important to do at the shrine? What could it be?"""
    else:
        """But {color=#fff238}we don't know the identity of Inquisitor{/color}, but we must be near them right now, though it's only a hunch.
        """
    # location check
    if locationKnown:
        """There is a good chance of {color=#fff238}our target appearing at the shrine again{/color}.
    
        Also, {color=#fff238}people have seen strange shadows lurking near the Park fields at night{/color}. It may be worth a shot to investigate there. 
        """
    # trap check
    if needSilverGrass:
        """
        This year's Moon Festival is likely cancelled due to poor weather, and the sudden devestation of our silver-grass harvest.
        """

    # trap warning
    if needSilverGrass and (talesOfSacrifce):
        """
        However, we lack the full picture of the Inquisitor's intentions, {color=#fff238}we must tread carefully{/color}. 
        """
    hide monologueFilter with fade 
    return

label ThanksForPlaying:
    scene black with dissolve
    $ PlayBGM("main_theme")
    pause 1.0
    """
    Game by: 
    
    {color=#00ff00}raykooooo{/color} (Discord handle):
    General Direction, Environment Art, Game Design, Scripting & Programming, 
    
    {color=#00ff00}rabbleram{/color} (Discord handle):
    Character Design, Character Art, Environment Art, Illustration 
    
    {color=#00ff00}sirlamps{/color} (Discord handle):
    SFX & Music Composer

    Art assets referenced from: Ezekiel Eastbrook, MK online services

    Thanks for Playing!
    """
    stop music fadeout 1.0
    pause 1.0
    return