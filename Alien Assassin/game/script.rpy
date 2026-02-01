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

default points = 50

default anna = False # if anna likes you 

default michelle = False 

default sobechi = False

screen source_screen():
    frame:
        align(1.0, 0.0)
        text "Reputation: [points]%"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    show screen source_screen()

    scene school corridor morning

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show sobechi happy

    # These display lines of dialogue.

    n "You are an assassin who has taken over the body of an alien on this planet. This information will only appear once so remember it well."

    n "Here is information about who you have to be. You are a university student. You are best friends with Sobechi who has a massive crush on Anna Pretzel."

    n "Here is information about the planet. On this planet, the people have very long tongues. As such, people wag their tongues in greeting. They also find it rude when people don't lick their plates clean."

    n "Here is information about the target. Andrew Pretzel is a loan shark who is exploiting your planet with predatory loans. He has a daughter: Anna Pretzel."

    n "Your goal is to get away with murder. In order to do this, you must befriend the people in the universe and help them obtain their goals. If you do this, you will gain reputation (in the top right corner)."

    # DAY 1
    scene school corridor morning
    show sobechi normal
    s "Hey, how are you feeling about the first day of classes?"
    show sobechi happy
    "Sobechi wags her tongue in greeting."
    p "I'm excited for my first class! It's called Money and Banking, it sounds like it's going to be a lot of fun!"
    s "Wow, look at the time, we should get going to class."

    scene classroom
    show anna happy
    a "Hey, I don't think I've seen you around before, nice to meet you!"
    p "Yeah, nice to meet you!"


    # Anna reputation
    menu: 
        "Anna wags her tongue at you."

        "Make a face":
            show anna normal
            a "Oh..."
            p "Did I do something wrong?"
            a "No…"
            jump choice1_0 # the number of points gained
            

        "Wag back": 
            p "You're so pretty, we should study together for this class sometime!"
            a "I'd be down. Hey, aren't you friends with Sobechi? Let's all study together."
            p 'Yeah of course! Oh, why’d you choose this class?' 
            show anna normal
            a 'Oh my dad is in finance so he wants me to learn about loans. Ugh.'
            p 'Do you not like your dad?'
            a 'Yeah he wants me to take over the family business.'
            p 'Oh wow. That seems stressful.'
            a 'Yeah {b}he’s taking 10 sleeping pills every night{b}.'
            p 'Oh no, is he okay?'
            show anna happy
            a 'Yeah-–actually you should meet him! Let’s study together at my house! Bring Sobechi!'

            jump choice1_1
            

        "Go for a handshake": 
            show anna normal
            a "Woah, I don't know you like that."
            p "My bad, it was a reflex--I mean…"
            a "So you shake hands with everyone?"
            p "No, that was a slip of the tongue, I don't do that."
            a "Oh. Well, class is starting, we should probably be quiet."
            p "Okay…"
            jump choice1_01 # 01 meaning -1

    label choice1_0: 
        $ points += 0
        n "Your points remain the same."
        jump option1 # Sobechi
    
    label choice1_1: 
        $ points += 10
        $ anna = True
        n "They seem pleased. Points increase by 10%%."
        jump option2 # meet Emily

    label choice1_01: 
        $ points -= 10
        $ anna = False
        n "They are displeased. Points decrease by 10%%."
        jump option1 # Sobechi

    label option1: 
        scene school corridor morning
        show sobechi happy
        s 'Good news! I got a text from Anna and she invited us to study at her house since we share classes together!'
        p 'Oh that’s great!'
        n 'You can take the opportunity to get closer to her father.'
        show sobechi normal
        s 'Oh but I’d be careful with her dad-–I heard {b}he takes 10 sleeping pills every night{b} because he’s so stressed.'
        jump option2


    label option2: 
        scene football field
        "You run into Emily, the local drug dealer, by the football fields."
        show emily
        e "Hey, do you want to fly?"
        p "Huh? Fly?"
        e "Yeah, fly. Like an angel."

        # Buying fent
        menu:
            "Yes sure, give me some angel dust.":
                e "Angel dust? That’ll cost a pretty penny."
                p "I’ve got money."
                e "Okay moneybags, here’s your angel dust."

                jump choice2_1

            "Yes, give me fentanyl.":
                e "Fentanyl? I don’t know what you’re talking about."
                p "Like the white stuff? Don’t you have that?"
                e "Now you’re just giving me attitude. I’m only giving you this because you’re a regular."

                jump choice2_2

            "No, I don't want anything.":
                e "Okay. Goodbye."
                jump choice2_3

    label choice2_1:
        $ fentanyl_flag = True
        n "You gained fentanyl."
        jump choice2_done
    
    label choice2_2:
        $ fentanyl_flag = True
        n "You gained fentanyl."
        jump choice2_done
    
    label choice2_3:
        $ fentanyl_flag = False
        n "You don't buy anything from the drug dealer."
        jump choice2_done

    #DAY 2
    label choice2_done:
        scene living room
        "You arrive at the Pretzel house. You knock on the door. It swings open to reveal…"
        show loan
        l "Oh. You must be Anna’s acquaintances. She’s been expecting you. Come in."
        hide loan
        show anna happy
        a "Thank you guys for coming! Ignore my father, he’s such a grump. Let’s study upstairs in my room!"
        hide anna
        show loan
        l "I’ll be going to bed soon. Try not to be loud, I’ll need my rest if I’m going to squeeze every last cent out of those filthy humans at work."
        hide loan
        show anna sad
        a "Dad! …I’m sorry about him. Let’s… let’s just go to my room now. *Sigh*"
        p "Could I use the bathroom first?"
        show anna normal
        a "Sure, it’s the room at the end of the hallway on the left. It’s right across from my dad’s room."

    # Planting the fent
    menu:
        "The weight of the fentanyl feels heavy in your pocket. What will you do?"

        "Go to the bathroom":
            jump choice3_1

        "Go to the loan shark's room":
            jump choice3_2

    label choice3_1: 
        scene bathroom

        "You go to the bathroom and relieve yourself. You’re too scared to confront the loan shark, but you leave a present for him in the toilet before joining Anna and Sobechi."

        n "You missed your chance to assassinate the loan shark."

        jump choice3_done

    label choice3_2: 
        scene room night

        "You slip into the loan shark’s room and find a pill bottle resting on a nightstand. You switch out the pills in the bottle for the fentanyl you got from Emily. You slip out of the bedroom before the loan shark can notice you, then join Anna and Sobechi."

        scene living room

        "As you head upstairs, you feel a little pee dribble down your leg and ignore it. Your bladder is screaming, but your worries dissipate when you hear sounds from the loan shark’s bedroom: a yawn and the shake of the pill bottle."
        
        jump choice3_done

    # SLEEPOVER

    label choice3_done: 
        scene room
        


    label end: 
        scene football field

        e "field"

        scene room

        a "room"

        # This ends the game.
 

    return
