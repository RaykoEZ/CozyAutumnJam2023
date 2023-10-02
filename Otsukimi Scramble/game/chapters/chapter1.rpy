# TODO: Flesh out dialogue in chapter 1
define ufo = Character("???")
label chapter1: 
    scene field evening:
        zoom 3.0
    with fade  
    p "There, all done, this should be the last silver-grass bush for today."
    """I stand up, arms stretched out, letting the refreshing breeze flow through my clothes.
    
    The humid summer air has long since dissipated.
    
    Today is a perfect time to be out in the fields"""
    p "We should have enough for tonight~"
    "Helping the silver-grass harvest for this year's Harvest Moon Festival has been a drag, to say the least."
    "We had a rough season for these little guys this year. I was worried we won't fill our baskets"
    scene clear sky:
        zoom 3.0
    "I take a long stretch and lay down on the grass, staring blankly into the evening sky."
    p "There's nothing to worry about after all."

    "Dozing off from cloud watching, a sudden twinkle in the sky catches my attention."
    p "Hm? A plane?"
    "But it seems too small for a plane, and it's too early to see any stars."
    scene clear sky:
        zoom 6.0
    "The twinkling flying object continus to flash in the sky."
    "I squint my eyes as I try to figure out what this is."
    p "\"It's probably an UFO, then.\" I muttered to myself jokingly."
    "Of course, it was sarcasm. I never believe in delusional ramblings from random people on the web."    
    scene clear sky:
        zoom 12.0
    p "Wait a second, it's getting bigger."
    ufo "...a-"
    "I can hear a quiet buzzing at first, but I soon realized it's someone screaming."
    ufo "AHH!!!"
    ufo "AAHHHHHHHHH!!!"
    p "!?"
    scene clear sky:
        zoom 12.0
    with hpunch
    "I was too late to react as a beam of light landed several metres behind me."
    scene field evening:
        zoom 3.0
    with vpunch
    with dissolve
    # audio explosion
    "The shockwave from the explosion sends me flying towards the shrubs."
    "I struggle to my feet, still in shock, marvelling at the enormous crater before me."
    show kag shadow
    "From the thick smoke and ashes, a human silhouette slowly emerges."
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
    scene field evening:
        zoom 3.0
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
    scene black with fade
    "Already tired from a day's work, I eventually gave up on escaping."
    scene field evening:
        zoom 3.0
    with fade
    show kag norm
    ufo "Finally calmed down?"
    ufo "My name's Kaguya, I am a resident of the Moon!" 
    ufo "Details later, let's get out of here before anyone comes."
    k "Please show me the way!"
    p "...sure"
    "Still nervous, I make my way out of the fields with the girl."
    return

#TODO:secret ending route
label chapter1x:
    return