#set all python init variables here
init python:
    def MakeTextFile(filename, text):
        with open(config.gamedir + "/" + filename, "w") as f:
            f.write(text)
            f.close()
        return
    
    def CheckTextInFile(filename, checkContent):
        if renpy.exists(filename):
            with open(config.gamedir + "/" + filename, "r") as f:
                return checkContent in f.read()
        else:
            return False
                
# set all persistent variables here
default persistent.bond = False
# set variables for game state

# Kaguya's affinity level, a key to unlock secret ending 
default affinity = 0
default clue0 = False
default clue1 = False
default clue2 = False
default clue3 = False
default clue4 = False
default keyCheck = False