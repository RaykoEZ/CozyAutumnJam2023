# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The game starts here.

label start:
    scene black
    call prologue from _call_prologue
    # These display lines of dialogue.
    call chapter1 from _call_chapter1
    call chapter2 from _call_chapter2
    # This ends the game.
    return
