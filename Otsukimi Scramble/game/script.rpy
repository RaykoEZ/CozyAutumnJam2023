# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.
# TODO: Secret ending check
label start:
    stop music
    # Check for clue 1 to see if we choose to go to shrine
    scene black
    call prologue from _call_prologue
    # These display lines of dialogue.
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
    # check for chapter 2 decision
    if refuseToHelp:
        # Lied to Kaguya, go to bad version of end 1.
        $ affinity -= 1 
        jump end1
    else:
        call chapter3
    # Night begins, need to head to final destination
    "The sun has set, we don't have much time left."
    # panic/worry/frown
    show kag surprise
    "Kaguya is getting restless, we need to make a move."
    k "C'mon! Do we know where to find this bugger?"
    jump chooseDestination
    # This ends the game.
    return

menu chooseDestination: 
    p "Where do we go for the night?"
    "Park":
        call confirmDestination
        if _return:
            jump chapter4_Park        
        else:
            jump chooseDestination 
    "Shrine":
        call confirmDestination
        if _return:
            jump chapter4_Shrine        
        else:
            jump chooseDestination 
    "Store":
        call confirmDestination
        if _return:
            jump chapter4_Store
        else:
            jump chooseDestination 
    "Stay in my room":
        call confirmDestination
        if _return:
            jump chapter4_Room
        else:
            jump chooseDestination 
    "Think about it":
        call thinking
        jump chooseDestination  

menu confirmDestination:
    "Am I sure about this? I won't have enought time to check other places."
    "Yes":
        return True
    "No":
        return False

# list clues obtained for decision making
label thinking:
    "To sum up what we currently know:"
    
    """We have an idea of the true Identity of the Inquisitor - a cunning, shape-shifting black rabbit. 

    They must be intimately involved in the recent deacades' of Moon Festivals."""
    # identity clue check
    if identityKnown:       
        """A peculiar elderly man is seen frequenting the shrine on Moon Festival nights.
        
        Perhaps he has something important to do at the shrine? What could it be?"""
    else:
        """But we don't know the identity of Inquisitor, but we must be near them right now, though it's only a hunch.
        """
    # location check
    if locationKnown:
        """Knowing this rabbit is related to the Moon Festival, there is a good chance of our target appearing at the shrine.
    
        Also, people have seen strange shadows lurking near the Park fields at night. It may be worth a shot to investigate there. 
        """
    # key info check
    if talesOfSacrifce:
        """Tales of Sacrifice and Birth - a tale of true virtue. 
        
        Could it be a coincidence that we are also dealing with a Moon Rabbit here?"""
    # trap check
    if needSilverGrass:
        """
        This year's Moon Festival is cancelled due to poor weather, in addition to the sudden devestation of our silver-grass harvest, as witnessedInquisitored by yours truly.    
    
        Luckily, I have some silver-grass as decoration. It might come in handy when we confront this Inquisitor.
        """

    # trap warning
    if needSilverGrass and (talesOfSacrifce):
        """
        However, we lack the full picture of the Inquisitor's intentions, we must treead carefully. 
        """     
    return