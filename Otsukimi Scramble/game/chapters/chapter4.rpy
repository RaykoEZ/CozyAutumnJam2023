define inquisitor = Character("The Inquisitor")

label chapter4_Shrine:  
    scene shrine night  
    "We arrive at the shrine and wait"
    "Encount here"
    jump inquisitorEncounter

label chapter4_Park:
    scene field night
    "We reach the park"
    "Sees a figure near the crater" 
    $ identityKnown = True
    jump inquisitorEncounter

label inquisitorEncounter:
    scene shrine night
    #TODO: Flesh out decisions on encounter with Inquisitor
    call questioning1
    inquisitor "You better know what you are talking about. I don't take kindly to slanders."
    call questioning2
    # if player presents silvergrass to the inquisitor (trap), trigger a sacrifice route
    if giveGrass:
        jump inquisitorSacrifice
    # good end
    if inquisitorScore > 1:
        jump end2
    else:
        jump inquisitorReject

menu questioning1:
    "What brings you two here?"
    "To meet you, Mister Inquisitor.": 
        $ inquisitorScore += 1
        return
    "We heard about a suspicious individual...":
        $ inquisitorScore -= 1
        return 
    "Just Sightseeing.":
        return
# if you give grass, inquisitor will scarifice himself

menu questioning2:
    "What should I do next?"
    "Let Kaguya handle this": 
        return
    "Reveal the Inquisitor's motives":
        return 
    # activate trap if player brought grass to the showdown
    "Present the silvergrass" if hasGrass:
        $ giveGrass = True
        return

# When you fail the questioning
label inquisitorReject:
    jump end1
# Trigger Trap Bad Ending
label inquisitorSacrifice:
    jump end1

# Lost, head to End 1
label chapter4_Store:

    jump chapter4_Lost

label chapter4_Room:

    jump chapter4_Lost

label chapter4_Lost:
    

    jump end1


