#set all python init variables here
init python:
    import os
    # make 
    def MakeDirectory(dirName):
        path = "[config.gamedir]/[dirName]"
        if not os.path.exists(path):
            os.mkdir(path)

    # create and write to a file
    def MakeTextFile(filename, text):
        with open("[config.gamedir]/[filename]", "w") as f:
            f.write(text)
            f.close()
        return
    #check id file exists & its content
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
default refuseToHelp = False

# identity of the treasure - inquisitor
# details of the inquisitor life on earth
default identityKnown = False
# witnessedInquisitor the inquisitor at the park
default witnessedInquisitor = False
# where to go after chapter 3
default locationKnown = False
# red herring - history of immortality
default immortality = False
# tales of sacrifice, needed for secret unlock
default talesOfSacrifce = False
# score for the inquisitor decision at chapter 4
default inquisitorScore = 0
# check for secret ending unlock
default secretUnlocked = False

#-----------------IT'S A TRAP----------
# TRAP know what to bring/what inquisitor wants - silvergrass
default needSilverGrass = False
# brought grass to the shrine on the showdown 
default hasGrass = False
# gave grass to the inquisitor
default giveGrass = False
# ------------------IT'S A TRAP---------

