label chapter2:
    scene black with dissolve
    play siren "audio/siren.mp3" volume 0.05
    "We ran as fast as we could before the echoes of sirens closed in on the scene."
    stop siren fadeout 1.0
    play sound "<from 1 to 4>audio/run.mp3"
    "{color=#fff238}T. Shrine{/color}"    
    scene shrine hill evening
    with dissolve
    show monologueFilter
    "Once we safely reached the foot of the stairs leading to the shrine, I breath a sign of relief."  
    play wind "audio/wind.mp3" fadein 2 fadeout 3
    "The soft rustling of fallen leaves and swaying branches bring me with a familiar feeling of tranquility."
    hide monologueFilter
    p "We should be safe around here."
    $ PlayBGM("bgm_calm")
    "The Moon Festival takes place here tonight, so we should be able to blend in with the preparation staff."
    show kag norm   
    k "Say, I still don't know your name."
    show monologueFilter
    """She's surprisingly strong for her petite figure.
    
    This is not good, the commotion at the field would have attracted the police by now.
    
    I would be in deep trouble if I were to associate with the {color=#fff238}perpetrator{/color} of that massive hole in the ground.
    """
    hide monologueFilter
    stop music fadeout 0.3
    stop wind fadeout 0.3
    p "Now if you'll excuse me, I need to go."
    show kag surprise:
        zoom 0.75
    with vpunch
    k "Hey!"
    # surprise
    show kag angry:
        zoom 1.1
    with hpunch
    play sound "<from 0 to 2.5>audio/grip.mp3" fadein 1 fadeout 1
    p "Aargh!"
    "My neck jerks back as she grips onto the back of my shirt collar and pulls me back."
    call decideToHelp from _call_decideToHelp
    # return to main
    return

label decideToHelp:
    menu: 
        "Looks like I won't be getting away easily."
        "Fine.":
            call chapter2_1 from _call_chapter2_1
        # refuse to help
        "No, this is too much for me.":           
            # sad/frown
            show kag sad
            menu:
                "..."
                "Fine I'll help":
                    call chapter2_1 from _call_chapter2_1_1
                "No":
                    call chapter2_2 from _call_chapter2_2           
    return

label chapter2_1:
    $ PlayBGM("bgm_calm")
    p "Fine, I'll help, but don't do anything reckless, the police are probably on edge after what you did."
    p "My name is {color=#fff238}[povName]{/color}."
    # atl animation for excitement
    show kag shake:
        zoom 1.0
    with vpunch
    k "Yes Mr. [povName]! Thank you!"
    "Kaguya rigorously shakes my hands in excitement."
    p "[povName] is fine, now stop tearing my limbs apart!"
    show kag happy
    k "Ah Sorry about that~"
    "She sticks her tongue out mischievously."
    p "Hmph, so, what help do you need?"
    scene black with fade
    show kag norm
    pause 1.5
    k "I am trying to {color=#fff238}find someone{/color},"
    k "He's the {color=#fff238}Boss of the Moon{/color}! We call him the {color=#fff238}Inquisitor{/color}!"
    k "Why he left was a mystery to us-"
    k "but Boss had a huge tantrum and left us for the Earth."
    k "It's been about a year without the Boss, and our base is in disarray!"
    k "Most of us don't know how to manage our supplies!"
    k "Many of our brethren are on the {color=#ffb338}verge of malnutrition{/color}."
    k "I followed Boss' tracks and landed here." 
    show kag awkward
    k "The trip drains my energy reserves to maintain a connection between the worlds."
    k "{color=#ffb338}And I might not have enough power to travel back if we don't find Boss before dawn.{/color}"
    scene shrine hill evening
    with dissolve
    pause 1.5
    show kag awkward
    k "This might be a lot to take in, but please! Many lives are on the line!"
    p "..."
    "As much as I want this to be a dream, my hand still hurts from her vice grip."
    "I already agreed to help her, guess there's no harm going along with her story for a little while longer."
    p "Sure, Any ideas of what this person might look like?"
    show kag surprise
    pause 0.5
    show kag norm
    k "He's a forceful-yet-charming boss, a strong Moon Rabbit." 
    show kag happy
    k "Maybe one of the {b}muscular highschoolers with mysterious superpowers{/b}!"
    p "Uh-I'm afraid I've no clue where to start."
    show monologueFilter
    "This guy can even be on the other end of the world for all I know."
    "Not to mention the time constraint."
    "I'm already starting to consider the futility of her ordeal."
    hide monologueFilter
    # Option on what to do next
    show kag awkward with hpunch
    "Silence ensues as Kaguya leans against the railings by the stone steps, deep in thought."
    k "Hmm..."
    show kag angry
    k "..."
    show monologueFilter
    """Regardless, {color=#fff238}I still need to report our silver-grass situation to the organizers at the shrine{/color} anyway.

    There mght be some clues to the identity of this {color=#fff238}Inquisitor{/color}."""
    hide monologueFilter
    p "We can ask the shrine workers. It's better than standing around here."
    show kag norm
    "She snaps out of her frustration and nods eagerly."
    k "Let's! You lead the way!"
    hide kag with fade
    call chapter2_shrine from _call_chapter2_shrine        
    "As we head down the shrine path, many questions float in my mind."
    scene shrine hill evening
    with dissolve
    play sound "<from 0 to 3>audio/walk.mp3"
    p "Hey Kaguya."
    show kag surprise
    k "What is it?"
    menu:
        "What do I ask her?"
        "Ask Kaguya about the Inquisitor":
            show kag norm
            p "Hey, about the Inquisitor, what was he like?"
            k "Hmm, he's our bossman, with a big attitude~"
            k "But he does have a soft side {color=#fff238}if you know what buttons to push{/color}~"
            p "Any clues on what those \"buttons\" might be?"
            show kag awkward
            k "Well, he does not like brutes, you might want to be a good boy in front of him."
            p "I'll take that in mind if we meet him."
        "Ask more about Kaguya":
            show kag norm
            p "Hey Kaguya, how did you come to Earth?"
            k "Well, I was sent here with our special technology."
            p "And your the technology also blows things up?"
            k "No..."
            k "That was an accident."
            k "{color=#fff238}Inky{/color} made it so I'm not great at piloting it."
            p "{color=#fff238}Inky{/color}? Is that what you call your boss?"
            show kag happy
            k "Sure is~ It's a popular nickname, everyone loves it."
            "*sigh* Now I have an idea why the guy left you people."
            # increase affinity
            $ affinity += 1  
    play sound "<from 2 to 5>audio/wind.mp3" fadein 1.0 fadeout 1.0
    scene black with fade
    return

define sayu = Character("Sayu")
define elder = Character("Elderly Voice")
# go to shrine to ask for info
label chapter2_shrine:
    scene shrine hill evening with fade
    show monologueFilter
    """
    Lucky for her, I'm an acquaintance of the workers in this shrine and a regular at the shrine. 
    
    A few of them should be staying at the dwelling behind of the sanctuary.
    """
    "As we arrive at the entrance of the shrine, we are greeted by {color=#fff238}Sayu{/color}, a shrine maiden." 
    hide monologueFilter
    sayu "[povName]? Hey [povName]!"
    scene shrine evening
    with fade
    show monologueFilter
    """Sayu is the granddaughter of the shrine master. 
    
    She helps out with daily tasks at the shrine on weekends.
    """
    sayu "Good to see you here, how's everything on your side?"
    """ We are very acquainted with one another from my frequent visits to the shrine.

    Though an ordinary schoolgirl on the outside, she can be quite the trickster.

    On one of my later visits, I laid witness to her smuggling dinner to share with some of the kittens near the shrine.
    """
    hide monologueFilter
    p "As for the silver-grass - not so hot, I'm afraid. There was a fire at the fields just now."
    sayu "Ah, that's too ba-"
    scene shrine evening
    with vpunch
    play sound "audio/outburst.mp3" volume 0.5
    sayu "{b}Wait what!?{/b} So that's what the loud noise was earlier?"
    p "I saw something landed there, next thing I knew - smoke and fire."
    p "It ruined our supplies for the festival."
    k "Ahaha..."
    "I can hear Kaguya's awkward whimper behind my back, her eyes darting across the trees and bushes."
    sayu "Hm? [povName], who might this person be?"
    p "She's...my classmate! We're, looking for her friend, he got lost."
    k "Yes, have you seen anyone wandering around suspiciously?"
    stop music
    $ renpy.force_autosave(True, True)
    sayu "{color=#fff238}Suspiciously{/color}?"
    # autosave here
    # Check if we have any clue files triggered
    $ sayuSecretSolved = CheckTextInFile(secret_sayu, answer_sayu)
    if sayuSecretSolved == True:
        call sayuSecret from _call_sayuSecret
    # Make clue file and directory 
    else:
        $ MakeDirectory("secrets")
        $ MakeTextFile(secret_sayu, question_sayu) 
        sayu "...No, sorry." 
        $ PlayBGM("bgm_calm")
        elder "Sayu! Time to finish up and eat!"
        "A raspy voice calls for Sayu from the back of the shrine."
        sayu "Coming!"
        sayu "Dinner's almost ready, wanna join?"
        p "Thanks for the offer, but we're in a hurry. Say hi for me."
        "Sayu nods politely and bids us farewell."       
        show kag norm with fade
        k "Hmm..."
        p "Alright, let's go ask elsewhere."
        k "Do you think {color=#fff238}the girl might be hiding something{/color}?"
        pause 1.0
        p "?"
        p "What makes you think that?"
        k "A hunch."
        show kag awkward
        p "An alien's intuition? Do you have any special powers to back it up?"
        "I wouldn't be surprise Sayu's hiding something, but it's probably nothing important in this case."
        show kag angry
        p "That was a joke."
        scene black with fade
        show kag norm
        k "But I'd prefer you {color=#fff238}think of something outside the box{/color}," 
        pause 1.5
        k "{color=#fff238}there might be ways to tease out some hidden information from a person{/color}."
        pause 2.0
        p "Hmm...sorry to disappoint, but I'm no mind reader."
        "There is no way for {color=#ff5938}me{/color} to pry Sayu for her secret." 
        "We all have our own little secrets to hide after all."
    return
define pk = Character("Kaguya & I")

label sayuSecret:
    show kag surprise
    sayu "{color=#ff5938}Sacrifice{/color}..."
    $ PlayBGM("bgm_tense", fadeIn = 10.0, vol = 0.1)
    p "Sayu?"
    elder "Sayu! Time to finish up and eat!"
    sayu "Oh! Coming!"
    "She quickly turns to Kaguya and I with a somewhat serious expression."
    sayu "Promise me you won't tell Dad, okay? Pinky swear!"
    "What's this about? What can she be hiding?"
    p "Pinky swear it is."
    k "Sure, I'm in, pinky swear!"
    scene black with fade
    sayu "Last night, I was trying to find Caesar near the shrine, he hadn't come to eat dinner."
    menu:
        "You are so brave!":
            sayu "Hehe~"
        "That was very reckless of you!":
            p "Promise me you don't do this again," 
            p "it's dangerous to go out alone this late!"
            sayu "Okay, I'll call big bro [povName] next time then!"
            p "Jeez, who did you learn this from?"
    sayu "Anyway, I searched all over the trees and bushes for him, and there was nothing, but..."
    sayu "...when I was walking back, I saw {color=#fff238}a weird old guy walking up to the shrine{/color}."
    sayu "I was hiding behind trees, and I remember hearing him mumbling something about a {color=#fff238}\"Rite\"{/color}... and {color=#fff238}\"Sacrifice\"{/color}."
    scene black with vpunch
    play sound "audio/shocked.mp3"
    pk "!!!"
    show kag surprise
    k "Do you remember his face?"
    sayu "No, I could only see a shadowy figure."
    "Disappointed, Kaguya lowers her voice."
    k "Oh, okay."
    hide kag with fade
    sayu "Sorry."
    p "It's fine, thanks to your story, we might have a lead now!"
    scene shrine evening with vpunch
    stop music
    play sound "audio/outburst.mp3" volume 0.2
    elder "{b}Sayu! Dinner's ready!{/b}"
    pause 0.5
    sayu "{b}Coming!{/b}"
    $ PlayBGM("bgm_calm")
    "Sayu bows swiftly and runs off to her parents."
    scene black with dissolve
    # clue triggers
    $ witnessedInquisitor = True
    $ talesOfSacrifce = True
    $ sacrificeClueText = "Sacrifice"
    return
#refuse to help kaguya
label chapter2_2:
    p "I am sorry but I cannot help you any further."
    show kag surprise
    k "..."
    p "The shrine workers can help you more than I can."
    show kag norm
    k "Okay, I understand."
    show kag awkward
    k "I'm sorry we have to meet in such a way."    
    $ refuseToHelp = True
    hide kag with fade
    scene clear sky with dissolve
    play sound "<from 1 to 4>audio/walk.mp3"
    "Kaguya and I parted ways."
    return