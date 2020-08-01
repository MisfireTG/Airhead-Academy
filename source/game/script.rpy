# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character
'''
Player values
'''
define name = ""
define charm = 0
define intel = 0
define guts = 0
define fitness = 0
'''
NPC values
'''
define h = Character("Howard")
define twi = Character("Twilight")
define chee = Character("Ms. Cheerilee")
define player = Character("name", dynamic=True)
define twi_prog = 0
define chee_prog = 0

'''
In Game Time
'''
default weekday = 0
default dayPhase = 0
default dayCounter = 1
default days = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
default phases = ["Early Morning", "Morning", "Lunch", "After Noon", "Evening"]
'''
Image Definitions

Mainly needed for backgrounds to fix scaling issues
'''
define my_bedroom = im.Scale("bg myBedroom.png", 1280, 720)
define classroom = im.Scale("bg classroom.png", 1280, 720)
define library = im.Scale("bg library.png", 1280, 720)
define sugarcube = im.Scale("bg sugarCube.png", 1280, 720)
'''
Helper Functions
'''
init python:
    def advance_day(move = 1):
        '''
        Advances the in game time to the next morning
        To be called with every transistion to a morning scene
        '''
        global weekday
        global dayPhase
        global dayCounter
        weekday = (weekday + move) % 7
        dayPhase = 0
        dayCounter += 1
        return

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    show screen calendar()
    show expression my_bedroom


    # These display lines of dialogue.

    "Welcome to Airhead Academy - now ported to Renpy!"
    "It's your first day of class at blah blah whatever off you go."

    show expression classroom

    "Everyone's already in their seats ..."
    "You see an empty one by the window and start getting yourself comfortable"
    "After a few moments of your new classmates talking amongst themselves, the teacch stands up to start the class."
    "???" "Good morning class."
    "A few tired greeting come from your classmates, but most just quietly stare at the teacher."
    "???" "Well it is the start of the school year ... I guess that can be expected."
    chee "My name's Ms. Cheerilee,"
    chee "and although most of you have already been attending Chanterlot High for a few years, there's one student who transferred to this school."
    chee "Could he come up to the front and introduce himself to the class, please?"
    "You look around to see everyone's looking at you already. You go up to the front of the class."
    chee "Let's start by telling everyone your name."
    python:
        name = renpy.input("Your name is ...")
        name = name.strip() or "Annon"

    chee "Glad to meet you, [player]!"
    chee "How about you tell everyone in the class a little bit about yourself?"
    menu:
        "I'm looking forward to getting to know my classmates better":
            # +5 cheeri
            $ charm += 1
            "Most of the students seem apathetic, with a few giving a comforting smile."
            chee "How nice! Though, that wasn't really anything about yourself ..."

        "I've always tested really well":
            # +5 cheeri
            $ intel += 1
            "A few students try to restrain a chuckle, with one coughing 'nerd' into their fist."
            chee "Well ... I'm happy to have such a diligent student."

        "I was expelled from my old school for getting into fights":
            $ guts += 1
            "The room goes into a dead silence, your serious demeanor creating a tense atomsphere."
            chee "Ah, well ... erm, your honesty is quite refreshing, I suppose."

        "I was on the football team at my old school":
            $ fitness += 1
            "The tough guys nod, and the hot chicks smile ... just like at your old school."
            chee "How wonderful! I'm looking forward to seeing you humiliate your old friends in the future."

    chee "Thank you [player], you can sit back down now."
    # scene fade and break
    "Canterlot High is a busy place, especially at lunch time."
    "Everyone has their social circles, and it can be a little overwhelming for a newcomer."
    "So today, you decide to take a break from the lunchroom and find somewhere quieter - the Library"
    # scene fade and break to Library
    show expression library
    "It really is silent, so much so you flinch as the door loudly clicks behind you."
    "An exasperated sigh comes from the checkout desk."
    "???" "Do you mind? Some people are trying to study here."
    "The girl behind the counter gives you a withering glare."
    "You look around and see no one else in sight."
    menu:
        "You mean me?":
            "???" "Who else would I be talking to?"
            "You grin sheepishly, while the girl continues to give you an icy stare until she loses interest in your presence."

        "where is everyone?":
            # +2 twi
            "???" "At lunch - why do you think I'm here in the first place?"
            "The girl stares at you for a moment longer before turning back to the book in front of her."

        "Sorry, I wanted to go somewhere quiet.":
            # +3 twi
            "???" "Oh, I understand that. You're in the right spot; it's just you and me right now."
            "The girl's expression softens into a small smile before she turns back to her book."

    "After a few awkward seconds, you move closer to the table."
    "The girl sighs as you approach, place her finger inside her book and letting the cover close."
    "???" "This is a library. You know, a place to study?"
    "???" "Although, I haven't seen you around before, are you new?"
    "There's a certain curious sparkle in the girl's eyes as she asks about you."
    menu:
        "Have her guess":
            "???" "How would you expect someone you've never met to know something like that?"
            "The girl seems a little put-off by your joke, so you tell her anyway."
            "You also learn her name: Twilight Sparkle."
            "After finishing your introductions, Twilight gives you a smile."
        "Introduce yourself":
            # +2 twi
            "???" "Oh, so you're [player]! I've heard a little about you from my friends."
            twi "My name is Twilight Sparkle."
            "[twi] appreciates your forthrightness. She offers you a soft smile."
            "After finishing your introductions, [twi] gives you a smile."

        "Make a games of it":
            # +3 twi
            "???" "So you'll give me clues and I guess, huh? Hmm, alright, but you should know I'm the queen of solving mysteries!"
            "She figures out your name after three clues. It takes you a dozen to find out hers: Twilight Sparkle."
            "After finishing your introductions, [twi] gives you a smile."

    twi "Well, it was nice to meet you [player], but the bell should be ringing soon."
    twi "I really want to get through this next chapter, too."
    "Tapping her book on the counter, [twi] gives you an expectant look."
    "You don't need to be told twice and give her a friendly wave."
    "[twi] does the same, but immediately goes back to her book as you walk towards the door."
    # scene fade to classroom + teacher
    show expression classroom
    "The rest of the day is pretty uneventful ..."
    hide expression library
    jump my_bedroom_interactive
    #jump morning_cycle


label morning_cycle:
    '''
    Start of a new day
    All event triggers for the morning phase of the day should go here
    '''
    python:
        advance_day()
        day = days[weekday]
        p = phases[dayPhase]
    player "It is [day] [p], day [dayCounter]"
    if dayCounter < 5:
        jump in_class_event
    else:
        jump my_bedroom_interactive

label before_class:
    '''
    Player first enters the classroom for the day
    '''
    "You enter the classroom just in time for the lesson to start"

label weekend_early:

    #   Handle choosing an event for early morning

    # if no event then go to my bedroom
    show expression my_bedroom
    "You wake up early [day[dayCounter]] morning"
    jump my_bedroom_interactive

label in_class_event:

    #   Handle choosing an in-class event


    #hard coded events
    if dayCounter == 4:
        "Its Friday"
    # random events
    else:
        "Nothing happens in class"
        #nothing yet
    jump after_class_interactive
label after_class_interactive:
    # Player enters classroom
    call screen after_class

label after_class_cheeri:
    if chee_prog == 0:
        jump chee_1

    "You see [chee] at her desk, working on papers"
    "It would be best if you did not disturb her right now"
    jump after_class_interactive

label my_computer:
    #hide expression classroom
    #scene expression my_bedroom
    "This is your computer."
    "On the screen is the front page of 4Chan."
    "You dont bother to close the page. Its not like your parents will be poking around."
    jump my_bedroom_interactive

label my_bedroom_interactive:
     # Player interactive bedroom
     call screen bedroom_bed
     return

'''
Character Bonding Scenes
'''

label chee_1:
    "Everyone else is leaving . . . but your teacher looks stressed out."
    "stay and talk to her?"
    menu:
        "Spend time with Cheerilee":
            "You linger around after everyone hurries out of class"
            "Miss Cheerilee wears a professional demeanor up until the last student leaves the room. You watch her shoulders sag."
            "She plants her face on her desk and releases a long suffering sigh."
            "During class she was friendly, but strict. You notice she always seemed a bit tense."
            menu:
                "Ask her if shes okay":
                    #+3
                    "She flinches and looks up, surprised to see you're still in class."
                    chee "Oh! I didn't see you there, and yes, I'm fine, thank you for asking."
                    "She gives you a warm smile."
                    chee "I'm glad you're still here, I was planning to have a talk with you soon anyway."
                    "She gestures for you to grab a chair. You oblige and sit down across from her desk."
                    chee "How are you adjusting to your new school? Are there any subjects giving you trouble? Have you made any new friends yet?"
                    menu:
                        "I'm having trouble catching up to the rest of the class":
                            #+2
                            chee "I was worried that might be the case. I have some free times, how about we go over whats troubling you together?"
                            "Cheerilee is patient, and makes sure to quiz you after going over the material."
                            "She congratulates you when you get a question right, and tries to find the best way for you to learn the current material."
                            "You feel like you've gained a better understanding of your current schoolwork."
                            chee "Great job [player]! Keep this up and you'll catch up in no time."
                            chee "If you have any problems, come see me after class, alright?"
                            "She pulls out a stack of papers and gets ready to grade them."
                            chee "I expect to see you bright and early tomorrow."
                            "You thank her for her time, and head out of the classroom."
                            jump my_bedroom_interactive
                        "I haven't really made new friends yet":
                            "bbb"
                        "Of course not, everyone loves me":
                            "ccc"
                "Gently tap her shoulder":
                    "bbb"
                "Stay quiet":
                    "ccc"

            jump my_bedroom_interactive
        "Nevermind":
            jump after_class_interactive
