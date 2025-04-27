# home.rpy

label home_base:
    call screen home_screen
    return


screen home_screen():
    

    add "bg home"
    use player_hud
    # 🚪 Door (pops on hover)
    imagebutton:
        idle "images/door_idle.png"
        hover "images/door_idle.png"
        xpos 60
        ypos 250
        at pop_hover
        action [Hide("home_screen"), Jump("city_hub")]

    # 🛏 Bed (pops on hover)
    imagebutton:
        idle "images/bed_idle.png"
        hover "images/bed_idle.png"
        xpos 380
        ypos 360
        at pop_hover
        action [Hide("home_screen"), Jump("use_bed")]

    # 🖥 PC (pops on hover)
    imagebutton:
        idle "images/pc_idle.png"
        hover "images/pc_idle.png"
        xpos 700
        ypos 360
        at pop_hover
        action [Hide("home_screen"), Jump("use_pc")]





label use_bed:
    if time < 20:
        "You're not tired yet. It's too early to sleep."
        call screen home_screen
    else:
        "You rest and prepare for tomorrow."
        jump end_of_day

label use_pc:
    "You boot up your PC and check what's happening."

    menu:
        "Check Calendar":
            "Nothing interesting planned today."
            jump start
        "Browse Social Media":
            "You scroll through classmates’ posts. Some gossip gets your attention."
            $ charisma += 1
            jump start
        "Shut Down PC":
            jump start
