# TODO: Flesh out dialogue in chapter 1
label chapter1:
    scene field evening with dissolve
    "Cultivating silver-grass"
    scene clear sky with dissolve
    p "finish for today"
    scene festival with dissolve
    "thinking about moon festival"
    scene clear sky with dissolve
    p "there is a glint in the sky"
    scene clear sky:
        zoom 3.0
    with dissolve
    "Squint eyes, getting closer"
    scene clear sky:
        zoom 6.0
    with dissolve
    with vpunch
    "AH!!"
    scene black
    "boom"
    show kag shadow
    p "Hmm...what is this"
    p "A... girl?"
    # awkward
    show kag awkward
    k "Haha, sorry"
    "She approaches"
    "Silence"
    p "Sorry nope"
    # scream
    # struggle
    show kag surprise
    k "Hey please wait"
    p "Nope"
    # scream
    show kag sad
    k "please, i'll be in trouble"
    p "i'll be in bigger trouble"
    p "I don't even know you"
    k "not too late to make friends"
    p "nah, I'm out"
    k "please wait"
    "Both tired"
    p "Just let go and we get out of here first"
    # surprise
    show kag surprise
    # happy
    show kag happy
    k "Yes let's"
    return

#TODO:secret ending route
label chapter1x:
    return