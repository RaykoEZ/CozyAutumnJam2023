﻿define p = Character("[povName]")
define k = Character("Kaguya")
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
