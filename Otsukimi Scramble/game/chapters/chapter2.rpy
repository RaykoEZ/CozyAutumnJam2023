label chapter2:
    scene black with dissolve
    "We ran as fast as we could before the echoes of sirens closed in on the scene."
    play siren "audio/siren.mp3" volume 0.1
    play sound "<from 1 to 4>audio/run.mp3"
    scene shrine hill evening:
        zoom 3.0
    with dissolve
    "Once we safely reached the foot of the stairs leading to T. Shrine, I breath a sign of relief."
    play wind "audio/wind.mp3" fadein 2 fadeout 2
    "The soft rustling of fallen leaves and swaying branches bring me with a familiar feeling of serenity."
    
    p "We should be safe around here."
    $ PlayBGM("bgm_calm")
    "The Moon Festival takes place here tonight, so we should be able to blend in with the preparation staff."
    show kag norm   
    k "Say, I still don't know your name."
    """She's still trying to drag me into her mess, this cannot be good.
    
    The commotion at the field would have attracted the police by now.
    
    I would be in deep trouble if I were to associate with the perpetrator of that massive hole in the ground.
    """
    stop music fadeout 0.3
    stop wind fadeout 0.3
    p "Now if you'll excuse me, I need to go."
    show kag surprise:
        zoom 0.75
    with vpunch
    k "Hey!"
    # surprise
    show kag angry with hpunch
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
    p "My name is [povName]."
    # atl animation for excitement
    show kag shake with vpunch
    k "Yes Mr. [povName]! Thank you!"
    "Kaguya rigorously shakes my hands in excitement."
    p "[povName] is fine, now stop tearing my limbs apart!"
    show kag happy
    k "Ah Sorry about that~"
    "She sticks her tongue out mischievously."
    p "Hmph, so, what help do you need?"
    show kag norm
    k "I am trying to find someone, and I need to find him by dawn."
    show kag awkward
    p "Any ideas of what this person might look like?"
    show kag norm
    k """He's a forceful-yet-charming boss man. We used to call him the Inquisitor!

    He might look like one of those muscular high schoolers with mysterious superpowers! 
    """
    p "Uh-I'm afraid I've no clue where to start."
    "This guy can even be on the other end of the world for all I know."
    "Not to mention the time constraint."
    "I'm already starting to consider the futility of her ordeal."
    # Option on what to do next
    show kag awkward with hpunch
    "Silence ensues as Kaguya leans against the railings by the stone steps, deep in thought."
    k "Hmm..."
    show kag angry
    k "..."
    """Regardless, I still need to report our silver-grass situation to the organizers at the shrine anyway.

    There mght be some clues to the identity of this Inquisitor."""
    p "We can ask the shrine workers. It's better than standing around here."
    show kag norm
    "She snaps out of her frustration and nods eagerly."
    k "Let's! You lead the way!"
    hide kag with fade
    scene black with fade
    call chapter2_shrine from _call_chapter2_shrine        
    "As we head down the shrine path, many questions float in my mind."
    scene shrine hill evening:
        zoom 3.0
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
            k "But he does have a soft side if you know what buttons to push~"
            p "Any clues on what those \"buttons\" might be?"
            show kag surprise
            k "Well, he does not like liars, or anyone who can't keep up with his questions."
            p "I'll take that in mind if we meet him."
            k "When! Not \"if\", I'm not going to fail, so don't jinx it for me!"
        "Ask more about Kaguya":
            show kag norm
            p "Hey Kaguya, how did you come to Earth?"
            k "Well, I was sent here with our special technology."
            p "And your the technology also blows things up?"
            k "No..."
            k "That was an accident."
            k "Inky made it so I'm not great at piloting it."
            p "Inky? Is that the Inquisitor?"
            show kag happy
            k "Sure is~"
            # increase affinity
            $ affinity += 1  
    play sound "<from 2 to 5>audio/wind.mp3" fadein 1.0 fadeout 1.0
    scene black with fade
    return

define sayu = Character("Sayu")
define elder = Character("Elderly Voice")
# go to shrine to ask for info
label chapter2_shrine:
    scene shrine hill evening:
        zoom 3.0
    with fade
    """
    Lucky for her, I'm an acquaintance of the workers in this shrine and a regular at the shrine. 
    
    A few of them should be staying at the dwelling behind of the sanctuary.
    """
    scene black with fade
    "As we arrive at the entrance of the shrine, we are greeted by Sayu, a shrine maiden." 
    sayu "[povName]? Hey [povName]!"
    scene shrine evening:
        zoom 3.0
    with fade
    """Sayu is the granddaughter of the shrine master. 
    
    She helps out with daily tasks at the shrine on weekends.
    """
    sayu "Good to see you here, how's everything on your side?"
    """ We are very acquainted with one another from my frequent visits to the shrine.

    Though an ordinary schoolgirl on the outside, she can be quite the trickster.

    On one of my later visits, I laid witness to her smuggling dinner to share with some of the kittens near the shrine.
    """
    p "As for the silver-grass - not so hot, I'm afraid. There was a fire at the fields just now."
    sayu "Ah, that's too ba-"
    scene shrine evening:
        zoom 3.0
    with vpunch
    play sound "audio/outburst.mp3" volume 0.5
    sayu "Wait what!? What happen?"
    p "I'm in the same camp with you. I saw something landed there, next thing I know, there was a fire."
    scene shrine evening:
        zoom 3.0
    with vpunch
    p "This ruins our supplies for the festival!"
    k "Ahaha..."
    "I can hear Kaguya's awkward whimper behind my back, her eyes darting across the trees and bushes."
    sayu "Hm? [povName], who might this person be?"
    p "She's...my classmate! We're, looking for her friend, he got lost."
    k "Yes, have you seen anyone wandering around suspiciously?"
    stop music
    $ renpy.force_autosave(True, True)
    sayu "Suspiciously?"
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
        k "Do you think the girl might be hiding something?"
        p "?"
        p "What makes you think that?"
        k "A hunch."
        show kag awkward
        p "An alien's intuition? Do you have any special powers to back it up?"
        "I wouldn't be surprise Sayu's hiding something, but it's probably nothing important in this case."
        show kag angry
        p "That was a joke."
        show kag norm
        k "I'd prefer you think of something outside the box," 
        k "there might be ways to tease out some hidden information from a person."
        p "Hmm, what do you mean by that?"
    return
define pk = Character("Kaguya & I")
label sayuSecret:
    show kag surprise
    sayu "Sacrifice..."
    $ PlayBGM("bgm_tense")
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
    sayu "Anyway, I searched all over the trees and bushes, and didn't find Caesar, but..."
    sayu "...when I was walking back, I saw a weird old man walking up to the shrine."
    sayu "I was hiding behind trees, and heard him mumbling something about a \"Rite\" and \"Sacrifice\"."
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
    elder "Sayu! Dinner's ready!"
    sayu "Coming!"
    $ PlayBGM("bgm_calm")
    "Sayu bows swiftly and runs off to her parents."
    scene black with dissolve
    # clue triggers
    $ witnessedInquisitor = True
    $ talesOfSacrifce = True
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
    "Kagari and I parted ways."
    return