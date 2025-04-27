label math_class:
    scene bg math_classroom
    call screen math_class_screen
    return

screen math_class_screen():
    tag menu
    add "bg math_classroom"
    use player_hud
    imagebutton:
        idle "images/desk_idle.png"
        hover "images/desk_idle.png"
        xpos 400
        ypos 300
        action [Hide("math_class_screen"), Jump("start_math_lesson")]

    textbutton "⬅ Back to Hallway":
        xpos 20
        ypos 20
        action [Hide("math_class_screen"), Jump("school_hub")]

label start_math_lesson:
    "You attend Math class and work on problems."
    $ intelligence += 1
    $ energy = max(energy - 10, 0)
    $ hunger = max(hunger - 5, 0)
    $ thirst = max(thirst - 5, 0)
    $ lessons_math += 1

    if lessons_math % 3 == 0:
        "You've reached 3 lessons in Math. It's time for a quiz!"
        jump quiz_math
    else:
        "You feel smarter after the lesson."

    call random_school_event from _call_random_school_event_2
    call advance_time from _call_advance_time_2

    jump school_hub


