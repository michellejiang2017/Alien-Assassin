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

    show sobechi happy: 
        zoom 0.75

    # These display lines of dialogue.

    n "You are an assassin who has taken over the body of an alien on this planet. This information will only appear once so remember it well."

    n "Here is information about who you have to be. You are a university student. You are best friends with Sobechi who has a massive crush on Anna Pretzel."

    n "Here is information about the planet. On this planet, the people have very long tongues. As such, people wag their tongues in greeting. They also lick everything."

    n "Here is information about the target. Andrew Pretzel is a loan shark who is exploiting your planet with predatory loans. He has a daughter: Anna Pretzel."

    n "Your goal is to get away with murder. In order to do this, you must befriend the people in the universe and help them obtain their goals. If you do this, you will gain reputation (in the top right corner)."

    s "Hey, how are you feeling about the first day of classes?"

    "Sobechi wags her tongue in greeting."

    p "I'm excited for my first class! It's called Money and Banking, it sounds like it's going to be a lot of fun!"

    s "Wow, look at the time, we should get going to class."

    scene classroom

    a "Hey, I don't think I've seen you around before, nice to meet you!"

    p "Yeah, nice to meet you!"

    menu: 
        "Anna wags her tongue at you."

        "Make a face":
            a "Oh..."
            "Anna looks at you weirdly."
            jump choice1_0 # the number of points gained
            

        "Wag back": 
            p "You're so pretty, we should study together for this class sometime!"
            a "I'd be down."
            "You have a great conversation where Anna tells you her dad takes 10 sleeping pills every night and she invites you and your friend Sobechi to a sleepover."
            jump choice1_1
            

        "Go for a handshake": 
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
        n "They seem pleased. Points increase by 10%."
        jump option2 # meet Emily

    label choice1_01: 
        $ points -= 10
        n "They are displeased. Points decrease by 10%."
        jump option1 # Sobechi

    label option1: 
        "You're in the hallway and you talk to Sobechi where Sobechi tells you she heard from the rumour mill that Anna's dad takes sleeping pills. You encourage Sobechi to ask Anna to hang out because you know she likes her."
        
        scene dorm
        "You receive a text from Sobechi saying that Anna invited you both to her house for a sleepover!"
        jump end


    label option2: 
        scene football field
        "You have an idea: you can swap the sleeping pills and poison her dad. You run into Emily, the local drug dealer on campus. She asks in code words if you want anything."
        jump end
        

    label end: 
        scene football field

        e "field"

        scene room

        a "room"

        # This ends the game.
 

    return
