label end1:
    scene black with dissolve
    "I was met with the police on the next day."
    scene field evening with dissolve
    "Kaguya and I had left footprints at our first meeting; it was no surprise they would ask questions."
    "Fortunately, I was soon released as the police failed to find my \"accomplice\"."
    scene clear sky with dissolve
    "I haven't seen Kaguya after the night we'd gone our separate ways."
    """
    Day by day,
    
    Week by week.
    """
    scene black with dissolve
    show kag shadow with dissolve
    "The memories of that day fades away."
    hide kag with dissolve
    scene end1 with dissolve
    p "!"
    "That hood!"
    "Could it be her?!"
    scene end1: 
        zoom 1.5
    with dissolve
    "As I close my distance between the girl, whose gaze fixed towards the autumn evening sky,"  

    p "Kaguya."

    # bad end, depend on affinity, slightly different sequence
    if affinity > 0:
        call end1_better
    else:
        call end1_bad
    return

label end1_bad:
    scene end1
    "I muttered to myself, without drawing the girl's attention."   

    "Why is she here?"

    "What has she been doing since then?"

    "But,"
    scene black with dissolve
    "I shake off the thoughts and rush past the girl."
    "I have no business with her anymore."
    #show ending text
    "Ending 1 - Rejection"
    return

label end1_better:
    scene end1
    k "?"
    scene end1 better with fade
    k "[povName]?"
    P "Kaguya!?" 
    p "Where have you been? What happened that night?"
    "As I speak, fear and guilt freeze my conciousness."
    k "It's a pretty long story~"
    k "Wanna chat over some tea and snacks? I found a nice place~"
    p "..."
    k "Oh don't worry, I'll pay for my food!"
    # grey overlay for monologue
    """There were too many questions I wish to ask her.
    
    Yet here she is, in front of me.

    And I cannot look her in the eye."""
    #show ending text
    scene black with dissolve
    "Ending 1 - Rejection & Acceptance"
    return