label science_class:
    scene bg science_classroom
    call screen science_class_screen
    return

screen science_class_screen():
    tag menu
    add "bg science_classroom"
    use player_hud
    imagebutton:
        idle "images/desk_idle.png"
        hover "images/desk_hover.png"
        xpos 400
        ypos 300
        action [Hide("science_class_screen"), Jump("start_science_lesson")]

    textbutton "⬅ Back to Hallway":
        xpos 20
        ypos 20
        action [Hide("science_class_screen"), Jump("school_hub")]

label start_science_lesson:
    "You attend Science class and run some experiments."
    $ intelligence += 1
    $ energy = max(energy - 10, 0)
    $ hunger = max(hunger - 5, 0)
    $ thirst = max(thirst - 5, 0)
    $ lessons_science += 1



    if lessons_science % 3 == 0:
        "You've reached 3 lessons in Science. Quiz time!"
        jump quiz_science
    else:
        "That was a productive science session."
        
        call advance_time from _call_advance_time_3
        call random_school_event from _call_random_school_event_3

        jump school_hub

