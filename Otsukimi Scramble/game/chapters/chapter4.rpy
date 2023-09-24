define inquisitor = Character("The Inquisitor")

label chapter4_Shrine:    
    "We arrive at the shrine and wait"
    "Encount here"
    call inquisitorEncounter
    if inquisitorScore > 1:
        jump end2
    else:
        jump inquisitorReject

label chapter4_Park:
    

    return

label inquisitorEncounter:

    menu:
        "What brings you two here?"
        "Option":
            return
        "Option":
            return
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

# secret route unlock
label chapter4x:
    

    return
