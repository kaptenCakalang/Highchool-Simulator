define Stelle = Character("Stelle", color="#66ccff")  # Alex speaks in blue
transform center_character:
    xalign 0.5  # ✅ Centers horizontally
    yalign 0.5  # ✅ Centers vertically
    zoom 1.2  # ✅ Increase size (adjust as needed)

label math_classroom:
    scene bg math_class  # ✅ This should match the image definition!

    "You enter the math classroom."

    call screen math_classroom_screen
    return


screen math_classroom_screen():
    modal True  

    # Clickable NPC (Alex)
    imagebutton:
        idle "Stelle.jpg"
        hover "Stelle.jpg"
        xpos 400 ypos 300
        action Jump("talk_to_Stelle")

    # Start Lesson Button
    textbutton "Start Math Lesson" action Jump("math_lesson") xpos 300 ypos 500

    # Leave Classroom Button
    textbutton "Leave" action Return() xpos 50 ypos 500

label math_lesson:
    "You attend a math lesson. (-10 Energy, -5 Hunger, -5 Thirst)"

    # ✅ Reduce stats
    $ update_stats(energy_change=-10, hunger_change=-5, thirst_change=-5)  
    $ math_lessons += 1  # ✅ Track lessons attended

    # ✅ Unlock exam after 3 lessons
    if math_lessons == 3:
        $ math_exam_unlocked = True
        "Math Exam is now available!"

    return

label talk_to_Stelle:
    show Stelle at center_character

    Stelle "Hi bae you want some melon *nom nom*"

    menu:
        "yes sure why not?":
            show Stelle
            Stelle "cmere and eat it with me"

        "Kiss her":
            show Stelle
            Stelle "BAE place pls"

    return
