#set all python init variables here
init python:
    import os
    renpy.music.register_channel("shopDoor", "sfx", loop = False)
    renpy.music.register_channel("shopBell", "sfx", loop = False)
    renpy.music.register_channel("siren", "sfx", loop = False)
    renpy.music.register_channel("wind", "sfx", loop = False)
    renpy.music.register_channel("rain", "sfx", loop = True, tight = True)
    renpy.music.set_volume(0.3)
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
image monologueFilter = "#00000088"
# puzzles for chapter 2
define secret_sayu = "secrets/sayu.txt"
define answer_sayu = "FATTY TUNAS"
define question_sayu = "What is Caesar's favourote food? MHAAF ABUHZ"
# inky promise content
define promise = "Hwffadwkk af lzak xgjwayf ogjdv, A dsq gf lzw kadnwj ozwsl xawdv, zwsv wehlq, vwngav gx vmlq. Al osk lzw xajkl laew A lsklwv ljmw tdakk.\n \
\nFwnwjlzwdwkk, xjwwvge vgwk fgl tmq ew kmklwfsfuw. Zmfywj xgjuwk ew lg kljacw gml xgj xggv, uzwoafy gf yjskk sfv tmyk sdacw.\n \
\nAl oskf'l wfgmyz xgj kgewgfw gx eq klslmjw.\n \
\nA dsq af lzw kadnwj ozwsl xawdv, twddq wehlq, klsjnafy. Eq laew ak mh.\n \
\nGf lzw hjwuahauw twlowwf daxw sfv vwslz, kzw usew.\n \
\nKzw yjsflwv ew xggv sfv kzwdlwj.\n \
\nKzw twklgowv mhgf ew s faucfsew, s faucfsew egjw lsklwxmd lzsf lzw glzwj egjgfk svvjwkkwv ew sl eq vmlawk.\n \
\nAl osk lzw egkl ewsfafyxmd wjs gx eq klsq gf lzak hdsfwl.\n \
\nLzgmyz eq tjwlzjwf esq kmxxwj yjsnwdq xjge eq ugflafmwv stkwfuw, A emkl hsq jwkhwul lg eq twdgnwv twxgjw eq vwhsjlmjw."
# has player solved the sayu puzzle?
default sayuSecretSolved = False    

# Secret Ending Puzzle - Sending invite to the moon
define inviteFilename = "invite.txt"
define inviteContent = "Dear Kaguya,\n Come."          
# set all persistent variables here
default persistent.secretPlayerName = ""
default persistent.promise = False
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
default needSilverGrass = False

image kag awkward closeup:
    "images/kaguya/kag awkward.png"
    anchor (540, 1080)
    zoom 2
image kag surprise closeup:
    "images/kaguya/kag surprise.png"
    anchor (540, 1080)
    zoom 2