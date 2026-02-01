# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sobechi", color="005d5b")

define e = Character("Emily", color="000000")

define m = Character("Michelle", color="734f96")

define a = Character("Anna Pretzel", color="3264cb")

define l = Character("Andrew Pretzel", color="0000aa")

define n = Character(None, what_italic=True)

define p = Character("Protagonist", color="000000")

define po = Character("Police Officer", color="0000aa")

default points = 50

default anna = False # if anna likes you 

default michelle = False 

default sobechi = False

default fentanyl_flag = False

default car_flag = False

default gun_flag = False

default murder_method = None # can be: "fent", "car", "gun", None

default murder_stage = 1 # 1 = fent 2 = car 3 = gun

init:
    $ center = Position(xpos=0.5, ypos=0.8)
    $ left = Position(xpos=0.25, ypos=0.8)
    $ right = Position(xpos=0.75, ypos=0.8)

screen source_screen():
    frame:
        align(1.0, 0.0)
        text "Reputation: [points]%"

# The game starts here.

label start:
    show screen source_screen()

    ### INTRODUCTION ### 
    scene hallway 
    with dissolve

    n "You are an assassin who has taken over the body of an alien on this planet. This information will only appear once so remember it well."

    n "Here is information about who you have to be. You are a university student. You are best friends with Sobechi who has a massive crush on Anna Pretzel."

    n "Here is information about the planet. On this planet, the people have very long tongues. As such, people wag their tongues in greeting. They also find it rude when people don't lick their plates clean."

    n "Here is information about the target. Andrew Pretzel is a loan shark who is exploiting your planet with predatory loans. He has a daughter: Anna Pretzel."

    n "Your goal is to get away with murder. In order to do this, you must befriend the people in the universe and blend in with their culture. If you do this, you will gain reputation (in the top right corner)."

    ### ANNA ###
    scene hallway
    with fade

    show sobechi normal at center
    s "Hey, how are you feeling about the first day of classes?"
    show sobechi happy at center
    "Sobechi wags her tongue in greeting."
    p "I'm excited for my first class! It's called Money and Banking, it sounds like it's going to be a lot of fun!"
    s "Wow, look at the time, we should get going to class."

    scene classroom 
    with fade
    show anna happy at center
    a "Hey, I don't think I've seen you around before, nice to meet you!"
    p "Yeah, nice to meet you!"

    menu: 
        "Anna wags her tongue at you."

        "Make a face":
            show anna normal at center
            a "Oh..."
            p "Did I do something wrong?"
            a "No…"
            $ points += 0
            n "Your reputation remains the same."
            jump option1 # Sobechi
            

        "Wag back": 
            p "You're so pretty, we should study together for this class sometime!"
            a "I'd be down. Hey, aren't you friends with Sobechi? Let's all study together."
            p 'Yeah of course! Oh, why’d you choose this class?' 
            show anna normal at center
            a 'Oh my dad is in finance so he wants me to learn about loans. Ugh.'
            p 'Do you not like your dad?'
            a 'Yeah he wants me to take over the family business.'
            p 'Oh wow. That seems stressful.'
            a 'Yeah {b}he’s taking 10 sleeping pills every night{b}.'
            p 'Oh no, is he okay?'
            show anna happy at center
            a 'Yeah-–actually you should meet him! Let’s study together at my house! Bring Sobechi!'
            $ points += 10
            $ anna = True
            n "They seem pleased. Reputation increases by 10%%."
            jump option2 # meet Emily
            

        "Go for a handshake": 
            show anna normal at center
            a "Woah, I don't know you like that."
            p "My bad, it was a reflex--I mean…"
            a "So you shake hands with everyone?"
            p "No, that was a slip of the tongue, I don't do that."
            a "Oh. Well, class is starting, we should probably be quiet."
            p "Okay…"
            $ points -= 10
            $ anna = False
            n "They are displeased. Reputation decreases by 10%%."
            jump option1 # Sobechi

    ### VIA SOBECHI ### 
    label option1: 
        scene hallway
        with fade
        show sobechi happy at center
        s 'Good news! I got a text from Anna and she invited us to study at her house since we share classes together!'
        p 'Oh that’s great!'
        n 'You can take the opportunity to get closer to her father.'
        show sobechi normal at center
        s 'Oh but I’d be careful with her dad-–I heard {b}he takes 10 sleeping pills every night{b} because he’s so stressed.'
        jump option2


    ### EMILY ### 
    label option2: 
        scene football field
        with fade
        "You run into Emily, the local drug dealer, by the football fields."
        show emily at center
        e "Hey, do you want to fly?"
        p "Huh? Fly?"
        e "Yeah, fly. Like an angel."

        # Buying fent
        menu:
            "Yes sure, give me some angel dust.":
                e "Angel dust? That’ll cost a pretty penny."
                p "I’ve got money."
                e "Okay moneybags, here’s your angel dust."
                $ fentanyl_flag = True
                n "You gained fentanyl."
                jump choice2_done
            "Yes, give me fentanyl.":
                e "Fentanyl? I don’t know what you’re talking about."
                p "Like the white stuff? Don’t you have that?"
                e "Now you’re just giving me attitude. I’m only giving you this because you’re a regular."
                $ fentanyl_flag = True
                n "You gained fentanyl."
                jump choice2_done

            "No, I don't want anything.":
                e "Okay. Goodbye."
                $ fentanyl_flag = False
                n "You don't buy anything from the drug dealer."
                jump choice2_done
        

    ### DAY 2 ###
    label choice2_done:
        scene living room
        with fade
        show sobechi normal at left
        "You arrive at the Pretzel house. You knock on the door. It swings open to reveal…"
        show loan at right
        l "Oh. You must be Anna’s acquaintances. She’s been expecting you. Come in."
        hide loan
        show anna happy at right
        a "Thank you guys for coming! Ignore my father, he’s such a grump. Let’s study upstairs in my room!"
        hide anna
        show loan at right
        l "I’ll be going to bed soon. Try not to be loud, I’ll need my rest if I’m going to squeeze every last cent out of those filthy humans at work."
        hide loan
        show anna sad at right
        a "Dad! …I’m sorry about him. Let’s… let’s just go to my room now. *Sigh*"
        p "Could I use the bathroom first?"
        show anna normal at right
        a "Sure, it’s the room at the end of the hallway on the left. It’s right across from my dad’s room."
    if fentanyl_flag == True: 
    # Planting the fent
        menu:
            "The weight of the fentanyl feels heavy in your pocket. What will you do?"

            "Go to the bathroom":
                jump choice3_1

            "Go to the loan shark's room":
                scene room night
                with fade

                "You slip into the loan shark’s room and find a pill bottle resting on a nightstand. You switch out the pills in the bottle for the fentanyl you got from Emily. You slip out of the bedroom before the loan shark can notice you, then join Anna and Sobechi."

                $ murder_method = "fent"

                scene living room
                with fade

                "As you head upstairs, you feel a little pee dribble down your leg and ignore it. Your bladder is screaming, but your worries dissipate when you hear sounds from the loan shark’s bedroom: a yawn and the shake of the pill bottle."
                
                jump choice3_done
    else: 
        jump choice3_1

    label choice3_1: 
        scene bathroom
        with fade

        "You go to the bathroom and relieve yourself. You’re too scared to confront the loan shark, but you leave a present for him in the toilet before joining Anna and Sobechi."

        n "You missed your chance to assassinate the loan shark."

        jump choice3_done
        

    # SLEEPOVER

    label choice3_done: 
        scene room
        with fade

        show anna normal at left
        show sobechi normal at right

        "Empty snack wrappers are scattered everywhere. Anna licks salt from her fingers."
        a "Ugh, I’m still hungry." 
        s "Same. Cafeteria food never fills you up unless you do it right." 

        menu:
            "They both glance at you, waiting."
            "Yeah, you really have to lick the plate clean":
                show sobechi happy at right
                show anna happy at left
                a "Exactly." 
                s "See? They get it." 
                n "They seem pleased. Reputation increases by 10%%."
                $ points += 10
            "Guess you just eat more next time":
                show sobechi normal at right
                show anna normal at left
                a "…That’s not what I meant." 
                n "Reputation remains the same."
                $ points += 0 
            "I don’t really think about it":
                show sobechi sad at right
                show anna sad at left
                n "That answer feels wrong." 
                n "They seem displeased. Reputation decreases by 10%%."
                $ points -= 10

        s "My cousin skipped that once and my aunt almost disowned him." 
        a "That’s basic manners." 

        "Anna sticks her tongue out playfully, wagging it side to side."

        menu: 
            s "Are you going to save your food for later?"
            "Nah, leaving food is rude":
                show sobechi happy at right
                show anna happy at left
                a "You're right."
                s "Glad you said that."
                n "They seem pleased. Reputation increases by 10%%."
                $ points += 10

            "I’ll throw it out":
                show sobechi sad at right
                show anna sad at left
                a "Wow."
                s "That’s… bad."
                n "They seem displeased. Reputation decreases by 10%%."
                $ points -= 10

            "I’ll box it up and forget about it":
                show sobechi normal at right
                show anna normal at left
                s "That still counts as waste."
                n "Reputation remains the same."
                $ points += 0 

        s "Anna’s dad once yelled at a server for not finishing his food." 

        menu:
            a "He hates waste." 
            "Yeah, people like that care more about control than food":
                show sobechi happy at right
                show anna happy at left
                a "…You noticed that too." 
                n "They seem pleased. Reputation increases by 10%%."
                $ points += 10
            "He just sounds strict":
                show sobechi sad at right
                show anna sad at left
                a "You could say that." 
                n "They seem displeased. Reputation decreases by 10%%."
                $ points -= 10
            "I don’t know him":
                show sobechi normal at right
                show anna normal at left
                n "They both look unconvinced." 
                n "Reputation remains the same."
                $ points -= 0

        "The conversation drifts after that."

        if points >= 90:
            n "You feel like you belong here." 
            $ sobechi = True
            $ anna = True
        else:
            n "You feel like you’re still pretending." 

        "You and Sobechi have a great time at Anna’s. You spend the night there before heading to school."

        jump resolve_ending

    
    ### MICHELLE DAY 3 ###
    label option3: 
        scene hallway
        show sobechi happy at left
        if anna: 
            show anna happy at right 
            "When you see Anna the next day at school, she’s unusually happy to see you two."
        else: 
            show anna sad at right 
            "When you see Anna the next day at school, she seems wary of seeing you two."
        p "What's up?"
        a "My dad's making the rounds tonight--{b}he'll be out walking around the neighbourhood all day.{b}"
        a "But I'm excited for the club fair happening today!"
        s "Let’s go!"

        scene classroom
        show sobechi happy at left 
        show michelle normal at right
        s "We’re here! I’ve been meaning to check out the autophile club!"
        menu: 
            m "Hi… I’m Michelle. I’m here with the autophile club. We… like cars…obviously. We 'fix' them too… Would you like to hear more?"
            "Nah...that sounds boring.":
                show michelle sad at right
                m "Oh...okay."
                $ points -= 10
                n "Your reputation decreases by 10%%."
                hide michelle sad
                jump choice4_01
            "I’d love to!":
                show michelle happy at right
                m "*Sigh* Okay… well… right now we mainly help students get into their cars when they accidentally lock themselves out. We’re trying to raise money for a new monkeywrench."
                s "So you guys {b}break into their cars?{b}"
                m "I mean…if they pay us enough…yeah."
                p "Hey, can I get your number then Michelle? Just in case I get locked out of my car."
                m "Yeah of course! Here you go."
                $ points += 10
                n "Your reputation increases by 10%%."
                jump choice4_1

    ### SOBECHI FALLBACK ###
    label choice4_01:
        scene hallway
        show sobechi at center
        s "Hey! I got Michelle's number. She said she can fix people's cars!"
        p "Fix people's cars? What does that mean?"
        s "Oh like she helps people {b} break into people's cars if they get locked out of them {b}"
        n "You can break into a car and steal it to hit the target."
        p "Oh, could I get her number then?"
        s "Here, I'll add it to your phone."
        jump choice4_1

    ### CAR ATTEMPT ###
    label choice4_1: 
        scene parking lot 
        "Now's your chance to steal a car and hit the target."
        menu: 
            "Call Michelle": 
                m "Hi? What's up?"
                p "Hi, I got locked out of my car. I'm in the parking lot right now."
                m "Okay...I'll be right there!"
                show michelle happy at center
                m "So is this your car?"
                p "Yeah."
                "Michelle spends a couple minutes hijacking the car."
                m "Okay it's done! Have a good day!"
                p "You too!"
                jump car_attempt
            "Don't call Michelle": 
                n "You miss your second chance to assassinate the target."
                jump resolve_ending

    label car_attempt: 
        scene road
        "You drive in your stolen car around town, looking for Andrew Pretzel."
        show loan at center
        "You spot him by the side of an empty road."
        l "Huh?"
        menu: 
            "You press the gas pedal.": 
                $ murder_method = "car"
                "You have successfully murdered Andrew Pretzel. You run away and set the car on fire."
                jump resolve_ending
            "You press the brake pedal.": 
                n "You miss your second chance to assassinate the target."
                jump resolve_ending

    label gun_attempt:
        scene college campus
        s "I have a favor to ask of you, but you have to promise not to tell anyone."
        p "I promise I won’t tell a soul, what is it?"
        s "I know that guns aren’t allowed on this campus, but the thing is…*reveals firearm* I think people are getting suspicious and I don’t want it to be in my room in case they do a surprise inspection."
        p "Wow, I was expecting you to ask me to look over your homework or something."
        s "As my best friend, I know I can trust you. Will you hold onto the gun for me?"
        menu: 
            "Of course, I’ll make sure it isn’t found.":
                s "I knew you would have my back."
                p "Always."
                n "Time is ticking and your mission still has not been completed. Drastic measures have to be taken. No more beating around the bush, it's time to go straight to the target."
                n "You arrive at the Pretzel residence."
                scene front door
                show loan
                l "Oh. Are you one of Anna's little friends?"
                menu: 
                    "Shoot him in the face with your newly acquired gun":
                        $ murder_method = "gun"
                        jump resolve_ending
                    "Ask how he's doing and offer him a hug":
                        jump resolve_ending
            "I’m not sure that’s the best idea…":
                s "I guess our friendship isn’t as strong as I thought."
                p "That’s not true."
                s "That’s what it seems like right now."
                n "You lost trust with Sobechi and didn’t take the opportunity to obtain a weapon. Reputation decreases by 10%%."
                n "This was your last opportunity to assassinate the evil loan shark Andrew Pretzel and complete your mission. You have failed."
                jump resolve_ending

    ### SWITCHBOARD ###
    label resolve_ending:

        # Success conditions
        if murder_method and points >= 90:
            jump murder_success

        # Caught
        elif murder_method and points < 90:
            jump police

        # Failed attempt → go to next method
        elif murder_stage == 1:
            $ murder_stage = 2
            jump option3

        elif murder_stage == 2:
            $ murder_stage = 3
            jump gun_attempt

        # All attempts failed
        else:
            jump bad_end
            
    label police: 
        scene hallway
        show anna sad at right
        show sobechi sad at left

        a "Hey guys. Not to bring the mood down… but did you hear the news?"
        p "What news?"
        a "My dad is dead." 
        if murder_method=="fent": 
            a "Apparently the sleeping pills he’s been taking all this time were Fentanyl and yesterday he overestimated his tolerance."
        elif murder_method=="car": 
            a "Apparently he got hit by a car in a hit-and-run."
        elif murder_method=="gun": 
            a "Apparently he committed suicide using his own gun."
        s "Oh my gosh! You must be devastated."
        a "Not really. I’m pretty happy actually."
        "She turns to face you."
        a "It’s just that the police want to take you in for questioning. They’re behind you right now. Sorry. They asked if I had been around anyone odd lately and I had to tell the truth."
        "You feel strong arms grab you. A hard force hits the back of your head. Everything goes black."
        hide sobechi sad
        hide anna sad

        scene black 
        "You wake up in a police station, bound to a chair that’s facing the wall. A gruff voice behind you begins to speak."
        po "We’ve heard that you’ve been acting… strangely. The planet is currently under an advisory watch for humans that may be trying to infiltrate our society and assassinate our citizens."
        
        menu: 
            po "Answer this question for me: if you see a dog, what is the appropriate response?"
            "You pet it.": 
                "You hear a sound of disapproval from the officer."
                po "Oh hell nah fam. You’re definitely a human. Sorry, but we’re locking you up."
                jump bad_end
            "You lick it.":
                po "Oh okay nevermind you’re good. You’re free to go."
                jump good_end


    label murder_success: 
        scene hallway
        show anna happy at right
        show sobechi happy at left
        a "Hey guys! Did you hear the news? My dad is dead!"
        if murder_method=="fent": 
            a "Apparently the sleeping pills he’s been taking all this time were Fentanyl and yesterday he overestimated his tolerance."
        elif murder_method=="car": 
            a "Apparently he got hit by a car in a hit-and-run."
        elif murder_method=="gun": 
            a "Apparently he committed suicide using his own gun."
        s "And you’re happy about this?"
        a "Of course! My Dad was a menace, both to me and to humans. The police came over earlier to investigate, but when I told them how weird he acts they knew it was an accidental death."
        p "Wow. Well, I’m happy for you."
        a "This is all thanks to you!"
        p "IT IS?"
        a "Yeah! If it wasn’t for you encouraging me, I wouldn’t have the bravery to do this."
        jump good_end

    label good_end: 
        scene hallway
        show anna happy at right
        show sobechi happy at left
        n "Anna turns to Sobechi."
        a "Will you marry me now that my homophobic father is out of the way?"
        s "Anna… of course I will!"
        
        scene chapel
        n "Thanks to your efforts, society is free from the exploitative loan shark, and Sobechi and Anna get married. You’re the person of honor at their wedding, and get a promotion at work. Congratulations!"
        "{b} Good Ending. {b}"
        jump credits

    label bad_end: 
        scene black
        n "Unfortunately, you couldn’t accomplish your mission without being discovered. Disturbed by recent strange events, Anna decides she and Sobechi may be better off as friends for now. Sobechi is distraught. You’re fired from your job. Condolences!"
        jump credits

    label credits: 
        "Made with Ren'Py"
        "Made by Emily Lan (Lead Writer, Programmer), Michelle Jiang (Lead Programmer, Writer, Artist), Sobechi Igweatu (Lead Artist, Writer)"
        "Background assets by Uncle Mugen's Free OELVN / Visual Novel Resources"
        "Images by vectorpouch on {a=https://www.freepik.com/free-vector/banquet-hall-ballroom-castle-ready-wedding-ceremony-cartoon-vector-interior-decorated-flower_4015265.htm#fromView=search&page=1&position=3&uuid=081a65da-d025-43e8-a636-3bbbb4d7bd1d&query=Anime+chapel+wedding+setting}Freepik{/a}"
        "Designed by vectorpouch / Freepik"
        "Image by upklyak on {a=https://www.freepik.com/free-vector/empty-dark-urban-backstreet-garbage-containers_34084557.htm#fromView=search&page=1&position=1&uuid=a725eb09-1a5d-48b5-851b-8b259778320e&query=empty+neighbourhood+road+anime+style}Freepik{/a}"
        "ChatGPT was used to debug errors in this game."

    # this ends the game

    return
