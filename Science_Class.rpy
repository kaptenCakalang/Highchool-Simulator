define Alvan = Character("Gamma no 1 fan", color="#ffcc00")
transform center_character:
    xalign 0.5  # ✅ Centers horizontally
    yalign 0.5  # ✅ Centers vertically
    zoom 1.2  # ✅ Increase size (adjust as needed)

label science_lab:
    scene bg science_lab  # ✅ Show the Science Lab background

    "You enter the science lab. The smell of chemicals fills the air."

    call screen science_lab_screen  # ✅ Show the interactive screen

    return

screen science_lab_screen():
    modal True  

    # ✅ Clickable NPC (Alvan)
    imagebutton:
        idle "Alvan.jpeg"  # ✅ Use .jpeg if that's the actual format
        hover "Alvan_1.jpeg"
        xpos 400 ypos 300
        action Jump("talk_to_Alvan")

    # ✅ Start Lesson Button
    textbutton "Start Science Lesson" action Jump("science_lesson") xpos 300 ypos 500

    # ✅ Leave Science Lab Button
    textbutton "Leave" action Return() xpos 50 ypos 550

label Science_lesson:
    "You attend a Science lesson. (-10 Energy, -5 Hunger, -5 Thirst)"

    # ✅ Reduce stats
    $ update_stats(energy_change=-10, hunger_change=-5, thirst_change=-5)  
    $ science_lessons += 1  # ✅ Track lessons attended

    # ✅ Unlock exam after 3 lessons
    if Science_lessons == 3:
        $ Science_exam_unlocked = True
        "Science Exam is now available!"


label talk_to_Alvan:
    show Alvan at center

    Alvan "Hello im hungry but im Fasting"

    menu:
        "Give food":
            show Alvan
            Alvan "Dies because of divine judgment."

        "Dont give him food.":
            show Alvan
            Alvan "Dies due to starvation"

    hide Alvan
    return
