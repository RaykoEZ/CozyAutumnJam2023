label end3:
    "Ever since the day Kaguya returned, my daily life has never been more...spontaneous."
    # secret ending
    $ PlayBGM("main_theme")
    scene clear sky
    with fade
    "She frequently drops by, dragging me on her travels."
    "Though unwilling at first, I eventually succumb to her enthusiasm."
    "From monuments to nature, we journey across the country, forging unforgettable memories."  
    scene end3 with fade
    pause 0.5
    "Ending Ex - My Treasure"
    call ThanksForPlaying from _call_ThanksForPlaying_3
    return