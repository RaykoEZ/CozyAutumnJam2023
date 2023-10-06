define p = Character("[povName]",who_color = "#abe2ff", what_color="#c4eaff")
define k = Character("Kaguya",who_color = "#ffb1a3" ,what_color="#ffdfd9")
# TODO: Flesh out dialogue in prologue
label playerName:
    python:
        povName = renpy.input("What is your {color=#fff238}name{/color}?", length=16)
        povName = povName.strip()
        if not povName:
            povName = "Name"
        playerName = povName    
    return

label prologue:
    call playerName from _call_playerName
    return