define p = Character("[povName]", what_color="#c4eaff")
define k = Character("Kaguya", what_color="#ffdfd9")
# TODO: Flesh out dialogue in prologue
label playerName:
    python:
        povName = renpy.input("What is your name?", length=16)
        povName = povName.strip()
        if not povName:
            povName = "Name"
    return

label prologue:
    call playerName from _call_playerName
    return
