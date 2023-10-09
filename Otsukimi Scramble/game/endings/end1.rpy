label end1:
    scene black with dissolve
    play rain "audio/rain.ogg" volume 1.5
    if refuseToHelp:
        scene room rain with dissolve
        show monologueFilter
        """An uneventful night goes by.
        
        Focusing on the gentle pattering of the rain, 
        
        worn out by the events I encountered today, 
        
        I soon drift off into sleep."""
    scene field evening with fade
    stop rain fadeout 1.0
    with dissolve
    $ PlayBGM("bgm_calm", vol = 0.1, fadeIn = 10)
    show monologueFilter
    "A few days later, the police was at my doors."
    "Kaguya and I had left footprints at our first meeting; it was no surprise they would ask questions."
    "Fortunately, I was soon released as the police failed to find my \"accomplice\"."
    scene clear sky
    with dissolve
    show monologueFilter
    "I haven't seen Kaguya after the night we'd gone our separate ways."
    """
    Day by day,
    
    Week by week.
    """
    scene black with dissolve
    show kag shadow with dissolve
    "The memories of that day fades away."
    hide kag
    pause 3
    stop music
    scene end1
    p "Huh?"
    show monologueFilter
    "That hood!"
    "Could it be her?!"
    scene end1: 
        zoom 1.5
    with dissolve
    "As I close my distance between the girl, whose gaze fixed towards the autumn evening sky,"  

    p "{color=#fff238}Kaguya.{/color}"

    # bad end, depend on affinity, slightly different sequence
    if affinity > 0:
        call end1_better from _call_end1_better
    else:
        call end1_bad from _call_end1_bad
    return

label end1_bad:
    scene end1
    show monologueFilter
    "I muttered to myself, without drawing the girl's attention."   

    "Why is she here?"

    "What has she been doing since then?"

    "But,"
    hide monologueFilter
    scene black with dissolve
    "I shake off the thoughts and rush past the girl."
    "I have no business with her anymore."
    #show ending text
    "Ending 1 - Rejection"
    return

label end1_better:
    scene end1 base with fade
    $ PlayBGM("main_theme")
    k "?"
    scene end1 surprise with fade
    p "Kaguya!?"
    k "[povName]?"
    scene end1 wave with fade
    k "Long time no see~"
    k "Wanna chat over some tea and snacks? I found a nice place~"
    k "And...I'll pay for the food this time~"
    p "..."
    # grey overlay for monologue
    show monologueFilter
    "There were too many questions I wish to ask her."
    #show ending text
    scene black with dissolve
    "Ending 1.1 - Acceptance"
    call ThanksForPlaying from _call_ThanksForPlaying
    return