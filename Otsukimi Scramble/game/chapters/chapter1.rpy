# TODO: Flesh out dialogue in chapter 1
define ufo = Character("???")
label chapter1: 
    "Flower beds at A. Park."
    $ PlayBGM("bgm_calm")
    scene field evening with fade  
    p "There, all done, this should be the last silver-grass bush for today."
    """I stand up, arms stretched out, letting the refreshing breeze flow through my clothes.
    
    The humid summer air has long since dissipated.
    
    Today is a perfect time to be out in the fields"""
    p "We should have enough for tonight~"
    "Helping the silver-grass harvest for this year's Harvest Moon Festival has been a drag, to say the least."
    "We had a rough season for these little guys this year. I was worried we won't fill our baskets"
    play wind "audio/wind.mp3" fadein 2 fadeout 2
    scene clear sky with fade
    "I take a long stretch and lay down on the grass, staring blankly into the evening sky."
    p "There's nothing to worry about after all."

    "Dozing off from cloud watching, a sudden twinkle in the sky catches my attention."
    p "Hm? A plane?"
    "But it seems too small for a plane, and it's too early to see any stars."
    scene clear sky:
        zoom 1.2
    "The twinkling flying object continus to flash in the sky."
    "I squint my eyes as I try to figure out what this is."
    p "\"It's probably an UFO, then.\" I muttered to myself jokingly."
    "Of course, it was sarcasm. I never believe in delusional ramblings from random people on the web."    
    scene clear sky:
        zoom 1.5

    p "Wait a second, it's getting bigger."
    stop wind fadeout 0.3
    stop music fadeout 0.3
    with Pause(5)
    play music "audio/bgm_tense_buildup.mp3" fadein 5 volume 0.08
    queue music "audio/bgm_tense.mp3" loop volume 0.1
    ufo "...a-"

    "I can hear a quiet buzzing at first, but I soon realized it's someone screaming."
    play sound "audio/shocked.mp3"
    ufo "AHH!!!"
    scene clear sky:
        zoom 2
    with vpunch
    ufo "AAHHHHHHHHH!!!"
    p "!?"
    play sound "audio/explosion0.mp3" volume 0.5
    scene clear sky:
        zoom 2
    with hpunch
    "I was too late to react as a beam of light landed several metres behind me."
    scene black with fade
    # audio explosion
    "The shockwave from the explosion sends me flying towards the shrubs."
    "I struggle to my feet, still in shock, marvelling at the enormous crater before me."
    show kag shadow
    "From the thick smoke and ashes, a human silhouette slowly emerges."
    scene field evening       
    with vpunch
    with dissolve
    play sound "<from 0 to 3>audio/walk.mp3" volume 0.5
    show kag norm
    "It was... a girl?"
    ufo "*Cough* *cough*"
    show kag surprise
    "Shoot! She notices me!"
    show kag surprise closeup
    "And she's approaching me!"
    ufo "Sorry about the mess, I'll help clean it up later but-"
    """Is she an alien? A genetically modified super-soldier? Am I dreaming?

    Standing here, 
    
    I turned around instinctively, 
    
    soon realizing the utter chaos around me as I tried to avert my gaze away from this strange girl."""
    ufo "Hey~ Are you listening?"
    p "Aargh-"
    "My legs refused to work properly as I tried to flee from the scene."
    # struggle
    scene field evening
    show kag surprise
    ufo "Hey wait!"
    "I need to get away from that girl!" 
    "Everything about her sends shivers down my spine!"
    show kag surprise closeup
    with hpunch
    "The girl grips on my shirt and pulls me back."
    # scream
    show kag awkward:
    with vpunch 
    p "Let. Me. Go!"
    ufo "Calm down, I mean no harm!"
    stop music fadeout 0.3
    scene black with fade
    "Already tired from a day's work, I eventually gave up on escaping."
    scene field evening
    with fade
    show kag norm
    ufo "Finally calmed down?"
    ufo "My name's Kaguya, I am a resident of the Moon!" 
    ufo "Details later, let's get out of here before anyone comes."
    k "Please show me the way!"
    p "...sure"
    "Still nervous, I make my way out of the fields with the girl."
    play sound "<from 0 to 2>audio/run.mp3"
    return

label chapter1x:
    "T. Shrine"
    scene clear sky 
    with fade
    $ PlayBGM("bgm_clam")
    play wind "audio/wind.mp3" fadein 0.5 volume 0.3
    p "*Yawn*"
    scene shrine hill evening
    with fade
    "It has been a few weeks since my short time with the people of the Moon, I continued my daily routines."
    "The shrine needs extra hands today, I'm helping with their shopping."
    scene field evening
    with fade
    pause 0.5
    "After a day's work, I stroll through A. Park's flower fields."
    "The massive crater became a niche tourist destination, with many cult following online."
    "The late autumn breeze sends a slight shiver down my body as I lean by the park railings."
    scene black with fade
    p "I wonder what they are doing on the Moon."
    show kag shadow with fade    
    "Images of my experiences with her leak into my consciousness."
    p "...Enough of this, gotta grab some dinner."
    stop music fadeout 1.0
    ufo "May I join you for dinner?"
    p "?"
    show kag norm
    k "Hi."
    pause 1.0
    "Kaguya!?"
    show kag shake
    k "What are we eating today?"
    "I stand there in disbelief for a good second."
    p "Hold on a second!"
    play sound "audio/outburst.mp3" volume 0.3
    p "Why are you here?"
    show kag awkward
    k "I guess you can call it... a vacation."
    p "Huh?"
    k "Well, that is, as soon as I clean up the mess I made, ahaha~"
    "She scratches her head with a weak chuckle."
    show kag happy
    k "Before that...let's go get some food!" 
    k "Can I pay with moon rocks?"
    p "No."
    show kag surprise
    k "But boss said you guys love rocks from the Moon!"
    p "...*sign* I'll pay, just don't go overboard alright?"
    show kag happy with hpunch
    k "[povName]'s the best!"
    stop wind fadeout 1.0
    scene black with fade
    jump end3