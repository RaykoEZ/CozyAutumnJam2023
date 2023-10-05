#set all python init variables here
init python:
    import os
    renpy.music.register_channel("shopDoor", "sfx")
    renpy.music.register_channel("shopBell", "sfx")
    renpy.music.register_channel("siren", "sfx")
    renpy.music.register_channel("wind", "sfx", loop = True)
    renpy.music.register_channel("rain", "sfx", loop = True)

    def PlayBGM(name, isLoop = True, vol = 0.3, fadeIn = 0.5):
        renpy.music.play(filenames = "audio/"+name+".mp3", loop = isLoop, fadein = fadeIn, relative_volume = vol)
    # make 
    def MakeDirectory(dirName):
        path = config.gamedir + "/" + dirName
        if not os.path.exists(path):
            os.mkdir(path)
    # create and write to a file
    def MakeTextFile(filename, text):
        with open(config.gamedir + "/"+ filename, "w") as f:
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
define secret_sayu = "secrets/sayu.txt"
define answer_sayu = "FATTY TUNAS"
define question_sayu = "What is Caesar's favourote food? MHAAF ABUHZ"
# has player solved the sayu puzzle?
default sayuSecretSolved = False              
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
# tales of sacrifice, needed for secret unlock
default talesOfSacrifce = False
# check for secret ending unlock
default secretUnlocked = False
default inquisitorPuzzleSolved = False
#-----------------IT'S A TRAP----------
# TRAP know what to bring/what inquisitor wants - silvergrass
default needSilverGrass = False
# ------------------IT'S A TRAP---------

image kag awkward closeup:
    "images/kaguya/kag awkward.png"
    anchor (540, 1080)
    zoom 2
image kag surprise closeup:
    "images/kaguya/kag surprise.png"
    anchor (540, 1080)
    zoom 2