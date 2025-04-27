label history_class:
    scene bg history_classroom
    call screen history_class_screen
    return

screen history_class_screen():
    tag menu
    add "bg history_classroom"
    use player_hud 
    imagebutton:
        idle "images/desk_idle.png"
        hover "images/desk_hover.png"
        xpos 400
        ypos 300
        action [Hide("history_class_screen"), Jump("start_history_lesson")]

    textbutton "⬅ Back to Hallway":
        xpos 20
        ypos 20
        action [Hide("history_class_screen"), Jump("school_hub")]

label start_history_lesson:
    "You study ancient civilizations and take notes."
    $ intelligence += 1
    $ energy = max(energy - 10, 0)
    $ hunger = max(hunger - 5, 0)
    $ thirst = max(thirst - 5, 0)
    $ lessons_history += 1



    if lessons_history % 3 == 0:
        "You've completed 3 History lessons. Quiz incoming!"
        jump quiz_history
    else:
        "You gained more historical knowledge."

        call advance_time from _call_advance_time_1
        call random_school_event from _call_random_school_event_1

        jump school_hub

