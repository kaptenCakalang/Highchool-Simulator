label english_class:
    scene bg english_classroom
    call screen english_class_screen
    return

screen english_class_screen():
    tag menu
    add "bg english_classroom"
    use player_hud
    imagebutton:
        idle "images/desk_idle.png"
        hover "images/desk_hover.png"
        xpos 400
        ypos 300
        action [Hide("english_class_screen"), Jump("start_english_lesson")]

    textbutton "⬅ Back to Hallway":
        xpos 20
        ypos 20
        action [Hide("english_class_screen"), Jump("school_hub")]

label start_english_lesson:
    "You read some literature and join the class discussion."
    $ charisma += 1
    $ energy = max(energy - 10, 0)
    $ hunger = max(hunger - 5, 0)
    $ thirst = max(thirst - 5, 0)
    $ lessons_english += 1


    if lessons_english % 3 == 0:
        "You've completed 3 English lessons. Quiz time!"
        jump quiz_english
    else:
        "Your vocabulary feels sharper."

        call advance_time from _call_advance_time
        call random_school_event from _call_random_school_event

        jump school_hub

