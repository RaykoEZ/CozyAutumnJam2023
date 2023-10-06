define clerk = Character("Store Clerk")
label chapter3:
    scene sky evening
    with fade
    k "Well, what's our next move?"
    p "We don't have much daytime left, searching around town blindly isn't going to work."
    call chapter3_ChooseLocation from _call_chapter3_ChooseLocation
    # go to shrine dwelling
    return

menu chapter3_ChooseLocation:
    "Where shall we go?"
    "Go to the convenient store":
        p "Let's get some quick grub before anything, I need some time to recharge."
        k "Yes...Oh! I haven't eaten anything since I left home!"
        scene black with fade
        call chapter3_shop from _call_chapter3_shop
        return
    "Search for clues on the internet":
        p """Let's go to my place, 
        
        there should be records on the internet if your friend entered the Earth in a similar manner.
        """
        show kag surprise
        k "Inta-net?"
        "Ignoring her questioning gaze, I gesture her to follow my lead."
        "A break from being outside all day, the timing cannot be better!"
        p "Let's go back to my place, we have little time to waste!"
        k "O-okay!"
        scene black with fade
        call chapter3_room from _call_chapter3_room
        return
# We eat some food, talk to clerk, get out, get rained on, snooze under shelter
label chapter3_shop:
    scene shop with fade
    $ PlayBGM("bgm_calm", vol = 0.1)
    "We arrived at the convenience store."
    play shopDoor "audio/store open.mp3"
    play shopBell "audio/store bell.mp3"
    "Unsurprisingly, the place isn't busy in the evenings."
    p "This your first time in here?"
    "I asked Kaguya."
    k "Wow! So this is what a store looks like!"
    k "Sorry, didn't know what I would expected, we don't have stores at our place."
    p "So, what food can you eat?"
    k "Send me your best chief~ I'll need to save some for souvenirs"
    "Leaving Kaguya at the entrance, I scan around the food section."
    p "Ooh yes, they still have some meal deal leftover, lucky~"
    "Then I turn around, looking for anything interesting to buy for Kaguya."
    p "And for Kaguya..."  
    menu:
        "What food do I get for Kaguya?"
        "Limited Edition Moon Fest Dango":
            show kag surprise with easeinleft
            k "...?"
            "Unaware of the dangers, she puts several dangos into her mouth."
            p "Wait-"
            show kag angry with hpunch
            k "Not bad-"
            k "!!! This issh... sho chewy!"
        "Experimental Veggie Salad":
            "Salad? Sounds nice and refreshing, that'll do."
            show kag surprise with easeinleft
            k "..."
            show kag awkward
            "She takes a long sighs."
            k "Um, do you think I'm a rabbit?"
            k "I'm not a fan of this to be honest, it lacks flavour."
            show kag sad
            k "This is so bland I'm gonna cry..."
            p "Sheesh..."
            $ affinity -= 1
        "Fried Chicken":
            """I shall introduce her to the world of {color=#ff7a38}{b}Convenience Store Hot Foods{/b}{/color}!

            This place has one of the best convenience store fried chickens in town! 

            There is no way she can resist this {color=#ff7a38}crispy, juicy, spicy package of umami{/color}!"""
            scene shop with vpunch
            "{b}She will bow down and submit to the power and the culinary arts of this planet{/b}!"
            show kag surprise with easeinleft
            k "..."
            k "!!!"
            show kag shake with hpunch
            k "{b}Woah!{/b} This is the second best thing I've ever eaten in my life!"
            show kag happy
            k "I'm impressed! You do know what your stuff!"
            k "I'll save a few of these, they'll love this!"
            $ affinity += 1
        
    hide kag with fade
    "After finishing our meals, I come to the counter to get some snacks I picked up for later."
    clerk "Thanks, here are your changes."
    p "Cool thanks, say, how's your shift today? Anyone interesting coming in yet?"
    # suggestion
    if sayuSecretSolved :
        pause 0.5
        p "{color=#fff238}Maybe anyone asking for anything weird{/color}?"
    "It's worth a try to ask anyone about the Inquisitor."
    clerk "?"
    clerk "Oh hehe~ You'd be surprised what I've seen."
    stop music fadeout 2
    clerk "...Apart from you guys..."
    if sayuSecretSolved:
        clerk "Before I was onshift, {color=#fff238}an unreasonable man{/color} was pestering my buddy, had to jump in and calm them down."
        p "What was he talking about? What does he look like? We're trying to find someone."
        clerk "Well, he was asking for fresh flowers? I think it was {color=#fff238}silver-grass{/color}?" 
        clerk "We don't sell any here and the local florist is closed for the day."
        clerk "He looks a bit older than my Dad maybe, has a pretty scary face too."
        clerk "That's pretty much it, hope this helps."
        p "Thank you, this is an important clue!"
        "I bowed towards the clerk and hastily exit the store to inform Kaguya about the situation."
        $ needSilverGrass = True
        $ identityKnown = True
    else:
        clerk "I don't think there's anything out of the ordinary today."
        p "I see, thanks."
    play shopDoor "audio/store close.mp3"
    play shopBell "audio/store bell.mp3"
    pause 1.0
    scene black with fade
    call chapter3_rain from _call_chapter3_rain
    return


label chapter3_rain:
    "After a few exchanges of encouragement, we continue our search."
    "And suddenly..."
    scene rain sky with dissolve
    play rain "audio/rain1.mp3" fadein 2.0
    p "Shoot! I didn't bring my umbrella."
    k "Quick! Lat's stop by the roof there!"
    scene black with fade
    "As we wait for the rain to subside, exhaustion overtakes my mind."
    scene rain sky with dissolve
    p "*Yawn*~"
    "The gentle autumn drizzle woos my mind as I close my eyes to relax as much as I am able."
    "Soon enough, I fell asleep."
    p "zzz"
    k "You'll catch a cold if you sleep here."
    k "Hello?"
    play sound "audio/phone ring.mp3" volume 0.7
    k "Ah!?"
    scene rain sky with hpunch
    k "What the heck is this thing?"
    scene black with dissolve
    pause 1.0
    stop sound
    scene rain sky with dissolve
    "Hey..."
    p "zzz"
    scene rain sky with hpunch
    "Wake up!"
    p "..."
    scene rain sky with vpunch
    play sound "audio/outburst.mp3" volume 0.3
    "Hey! [povName]! Get up!"
    p "...Huh?"
    "Barely awake after Kaguya's rigorous shaking, I stare blankly at the phone in her hand."
    k "A voice just came out of this thing!"
    p "Hold on a sec! Gimme my phone back!"
    "I check my call record and breath a sign of relief - it was Sayu."
    p "Why did she call me? Did she say something to you?"
    k "Yes, in fact, she remembered an {color=#fff238}urban legend{/color} from her classmates."
    k "What's important is - people saw {color=#fff238}weird shadows lurking in the flower fields at night{/color}."
    p "The field you destroyed?"
    "Deep in thought, she ignores my snarky remark."
    k "Maybe it's a clue to where boss lives?"
    p "Hmm...Can't be sure yet, but it's better than nothing."
    "In that case, we should check that place out soon, it's almost nighttime."
    # phone rings, new tip
    $ locationKnown = True   
    return
# We snooze on bed, kaguya annoys us, do some research on PC
label chapter3_room:
    scene room with fade
    play shopDoor "audio/store open.mp3"
    play rain "audio/rain1.mp3" fadein 2.0
    $ PlayBGM("bgm_calm", vol = 0.2)
    
    "Just as we arrived at the dorm, it started to rain."
    p "Woo, just in time~"
    "I reach for the fridge and grab some snacks and drinks."
    scene black with fade
    play sound "audio/typing slow.mp3" fadein 1.0
    """Our investigation brgins with online occult boards, 
    
    though most of the articles are unrelated..."""
    stop music fadeout 1.0
    p "{color=#ff7a38}\"Mysterious Shadows at A. Park\"{/color}? Hmm."
    $ PlayBGM("bgm_tense", fadeIn = 1.0)
    "The post describes a mysterious man wandering around A. Park's field."
    p "Interesting, this is where we were this evening."
    "The accompanied photos are too blurry to confirm his appearances."
    p "Hmm..."
    "Hours go by, we cannot find more solid clues about the Inquisitor."
    # clue triggers
    $ locationKnown = True
    return