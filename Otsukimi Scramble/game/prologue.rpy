define p = Character("[povName]")
define k = Character("Kaguya")

label playerName:
    python:
        povName = renpy.input("What is your name?", length=16)
        povName = povName.strip()
        if not povName:
            povName = "Name"
    return

label prologue:
    call playerName
    "[povName], it is time to begin your story."
    return
