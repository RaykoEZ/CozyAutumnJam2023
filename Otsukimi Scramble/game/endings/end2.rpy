label end2:
    inquisitor "..."
    $ PlayBGM("main_theme")
    "The Moon Rabbit whispers in my ear."
    pause 0.5
    p "What are you saying?"
    inquisitor "Keep this a secret, will you?"
    pause 1.0
    menu:
        "Okay?":
            inquisitor "Then it's settled, make sure you do not break our promise."
        "Yes":
            inquisitor "Then it's settled, make sure you do not break our promise."
    $ MakeDirectory("secrets")
    $ MakeTextFile("secrets/promise.txt", promise)
    $ persistent.promise = True
    scene shrine night: 
        zoom 3.0 
    with fade
    inquisitor "Let's go Kaguya."
    show kag surprise
    k "?"
    show kag norm
    k "Y-Yessir!"
    "Kaguya turns to me, waving her hands."
    k "Thank you for your help!"
    "A great pillar of light emanates from behind her, soaring towards the moon."
    # do ending stuff here
    scene end2 with fade
    pause 1.0
    # normal end 2 farewell
    "End 2 - Lost and Found"
    call ThanksForPlaying from _call_ThanksForPlaying_1
    pause 0.5
    if affinity > 0:
        call end2x from _call_end2x
    return

# secret route unlock scene
label end2x:
    stop music fadeout 1.0
    scene shrine night:
        zoom 3.0
    with fade
    pause 1.0
    p "So this is goodbye."
    play sound "audio/confuse.mp3"
    "Huh?"
    ufo "Testing, testing, can you hear me?"
    "A familiar voice echoes in my head."
    p "Kaguya?"
    ufo "It seems we still have many things to experience." 
    ufo "I leave the preparations to you." 
    ufo "We will meet again [povName]!"
    scene black with fade
    # create moon and invite
    python:
        MakeDirectory("moon")
        content = inviteContent + "\n" + "Regards" + "\n" + "________"
        MakeTextFile(inviteFilename, content)
        persistent.secretPlayerName = povName
    return