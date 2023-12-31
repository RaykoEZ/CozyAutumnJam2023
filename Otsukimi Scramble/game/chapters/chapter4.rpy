define inquisitor = Character("The Inquisitor", what_color="#ff8d8d")
define oldMan = Character("Old Man?", what_color="#e4e4e4")

label chapter4_Shrine:  
    scene shrine night
    with fade
    play wind "audio/wind.mp3" fadein 2 fadeout 3
    "We arrive at the shrine."
    stop wind fadeout 3.0
    "With the festival cancelled, no one can be seen at the shrine."
    "We hunker down near the shrine gates."
    pk "..."
    "Hours later."
    play sound "audio/walk.mp3" fadein 1.0
    "An elderly man approaches the temple."
    play music "audio/bgm_tense_buildup.mp3" fadein 5 volume 0.1
    queue music "audio/bgm_tense.mp3" loop volume 0.3
    k "It's him! It has to be!"
    "Kaguya's eyes widen as she tries to step out of the bush."
    jump inquisitorEncounter

label chapter4_Park:
    scene field night
    play music "audio/bgm_tense_buildup.mp3" fadein 5 volume 0.1
    queue music "audio/bgm_tense.mp3" loop volume 0.3 
    play sound "<from 0 to 3.0>audio/run.mp3" fadeout 1.0
    "We quickly run to A. Park"
    play sound "<from 1.0 to 4.0>audio/run.mp3" fadein 3.0 fadeout 2.0
    "As we arrive at the site, the police tapes surround the perimeter."
    play wind "audio/wind.mp3" fadein 2 fadeout 3
    p "You see anything?"
    k "No...not here."
    play sound "audio/confuse.mp3"
    "Suddenly, a strange waddling sound."
    p "Was that you?"
    k "No."
    "We scan around the field with our lights"
    show inky norm with moveinleft
    pk "!?"
    play sound "audio/swipe.mp3"
    hide inky with moveoutleft
    "A shadow swiftly runs through us."
    p "It's making its way out of the fields!"
    play sound "<from 0 to 3.0>audio/run.mp3" fadeout 1.0
    "As the pursuit intensifies in the streets, we are lead to the santuary of T. Shrine."
    $ identityKnown = True
    play sound "audio/leap.mp3"
    "What lies ahead - {color=#fff238}an old man{/color}, silently watching the Moon."
    jump inquisitorEncounter

label inquisitorEncounter:
    scene shrine night
    with vpunch
    k "Hold it boss!"
    k "You're coming with me! We need you back!"
    oldMan "Boss?"
    k "Enough bluffing boss!"
    oldMan "..."
    show monologueFilter
    "The is not going anywhere, I need to think of something."
    hide monologueFilter
    $ renpy.force_autosave(True, True)
    call questioning1 from _call_questioning1
    show inky norm with fade
    pk "!?"
    "The old man morphs into a dark blob with two pointy ears, resembling a black rabbit."
    stop music fadeout 1.0
    scene black with fade
    # good end
    jump end2


menu questioning1:
    "{color=#fff238}I need to say something before the conversation goes south.{/color}"
    "Let Kaguya handle it.":
        k "Say something boss!"
        k "You need to come with me or our people are going to die!"
        jump inquisitorReject       

    "An old man like you wouldn't come here at midnight.":
        p "An old man like you wouldn't come here at midnight."
        p "I may not know what you are after bu-"
        show inky angry with vpunch
        play sound "audio/outburst.mp3" fadein 1.0
        inquisitor "None of your business! I go where I want!"
        show inky angry with vpunch
        play sound "audio/outburst.mp3" fadein 1.0
        jump inquisitorReject 
    "Bluff my way through this":
        p "Hold it Kaguya."
        k "?"
        "I cut the two off of their argument and step forward."
        p "Sorry about this, my friend is in a hurry."
        oldMan "?"
        p "We are here to witness the Full Moon, it's a shame the festival is cancelled."
        p "May you be on the same boat?"
        "The old man gradually calms down."
        "He laughs."
        scene shrine night
        with vpunch
        oldMan """Ahaha! It's okay, young one.
        
        I like your style! The idiot girl next to you would help to learn your manners."""
        p "?"
        oldMan "We can stop playing dumb now."
        return
    "Does {color=#ff5938}\"[sacrificeClueText]\"{/color} come to mind?" if talesOfSacrifce:
        pause 0.5
        oldMan "..."
        oldMan "Where did you hear that from?"
        p "What is this about? What do you want from all this?"
        return

# When you fail the questioning
label inquisitorReject:
    scene shrine night with fade
    oldMan "...Sorry"
    show inky norm with fade
    inquisitor "I've heard enough, I'm not going with you tonight, Kaguya."
    k "Wh-?"
    k "Why boss?"
    jump inquisitorFail
# Trigger Trap Bad Ending
label inquisitorFail:
    scene shrine night:
        zoom 1.5 
    with vpunch
    show kag surprise
    "With a blink of an eye-"
    p "What!?"
    "A tremendous force knocks me off balance."
    show kag shadow with fade
    play sound "audio/lightPillar.mp3" volume 1.5
    "Following by a pillar of blinding light at the temple, I hit the stone tiles in astonishment."
    scene black with fade
    k "[povName]!"
    hide kag with fade
    pause 1.0
    "When I regain my footing as the light dissapates,"
    "Kaguya and the Inquisitor are nowhere to be seen."
    p "Kaguya?"
    scene shrine night
    with dissolve
    "I search around the shrine for any traces of them."
    "Nothing."
    jump end1
# Head to Lost
label chapter4_Store:
    scene shop night with dissolve
    show kag awkward
    "We arrive at the convenience store."
    k "I don't see anyone of interest here."
    p "Let's not be too impatient."
    "I enter the store, Kaguya stays outside to look out for anything suspicious."
    show monologueFilter
    "Come to think of it, I'm getting a bit peckish, I hope they haven't thrown away the sandwiches yet."
    scene sky night with dissolve
    "Hours go by, no one of interest."
    "Worst of all, it begins to rain."
    pause 0.5
    #rain sfx
    clerk "You two still here?"
    "The store clerk came out the back door, probably coming off his shift."
    clerk "Ah it's raining. You're welcome to wait inside."
    p "Thanks for the offer, we'll go in a minute."
    scene black with dissolve
    "In the end, no one, except a few night owls, came into the store."
    jump chapter4_Lost
# Head to Lost
label chapter4_Room:
    scene room rain with dissolve
    play rain "audio/rain.ogg" volume 2
    show monologueFilter
    """It's nice to take a break from the ordeals awaiting us.
    
    My eyelids feel heavy as I dive into bed.
    
    Everything about today was exhausting.

    School assignments, work, a crash-landed alien girl...
    
    dragging me into her mess... 
    
    I need a break from this..."""
    hide monologueFilter
    show kag surprise
    p "zzz..."
    #zoom in
    show kag awkward
    k "Hey, can we save bed time for a bit later? We have a boss to catch!"
    #zoom in more
    "I didn't take long to fall asleep, despite the incessant shaking from an agitated girl."
    #zoom in more
    p "zzz..."
    stop rain fadeout 1.0
    jump chapter4_Lost
# Got to ending 1
label chapter4_Lost:
    scene black with dissolve
    show kag shadow
    show monologueFilter
    """As night is approaching its end, Kaguya leaves on her own, desperately searching for any traces of the Moon Rabbit.
    
    Afterall, she stands to lose everything if she fails this.

    It's too late, we don't have time to check every place in town.
    
    In the end, we failed to find the Inquisitor."""
    hide monologueFilter
    jump end1


