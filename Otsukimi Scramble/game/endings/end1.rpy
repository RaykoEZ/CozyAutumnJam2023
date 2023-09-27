label end1:
    scene black with dissolve
    "A year passes since my brief time with Kaguya."
    show kag shadow
    "I haven't seen the girl after the night we'd gone our separate ways..."
    hide kag with dissolve
    "after failing to find her treasure in time."
    scene field evening with dissolve
    "Kaguya and I had left footprints as we exited the park, causing police investigators to contact me for questioning."
    "Fortunately, I was soon released as the police failed to find my \"accomplice\", and lacked evidence to keep me locked up."
    scene clear sky with dissolve
    """I returned to my daily life of school assignments and working on odd jobs.
    
    Day by day
    
    Week by week
    """
    scene black with dissolve
    show kag shadow
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

    "It has nothing to do with me."

    "She's just a stranger..."

    "...we had only met once."
    scene black with dissolve
    "I shake off the thoughts and rush past the girl."
    #show ending text
    "Ending 1 - Rejection"
    return

label end1_better:
    scene end1
    k "?"
    scene end1 better with fade
    k "[povName]?"
    P "Kaguya!? Where have you been?"
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