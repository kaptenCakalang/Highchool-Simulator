label school_hub:
    call screen school_hallway
    return


screen school_hallway():
    tag menu

    add "bg school_hallway"
    use player_hud
    # 🛡️ KICK OUT if school closed
    if time >= 17:
        timer 0.1 action Jump("school_kickout")

    # 🚪 Math door
    imagebutton:
        idle "images/door_math.png"
        at pop_hover
        xpos 100
        ypos 300
        action [Hide("school_hallway"), Jump("math_class")]

    # 🧪 Science door
    imagebutton:
        idle "images/door_science.png"
        at pop_hover
        xpos 250
        ypos 300
        action [Hide("school_hallway"), Jump("science_class")]

    # 📚 English door
    imagebutton:
        idle "images/door_english.png"
        at pop_hover
        xpos 400
        ypos 300
        action [Hide("school_hallway"), Jump("english_class")]

    # 🏛️ History door
    imagebutton:
        idle "images/door_history.png"
        at pop_hover
        xpos 550
        ypos 300
        action [Hide("school_hallway"), Jump("history_class")]

    # ⬅️ Back button
    textbutton "⬅️ Back to City":
        xpos 10
        ypos 10
        action [Hide("school_hallway"), Jump("city_hub")]


label school_locked:
    "The school gates are locked. Come back tomorrow."
    jump city_hub

label school_kickout:
    "The school gates have closed. You have to leave."
    jump city_hub
