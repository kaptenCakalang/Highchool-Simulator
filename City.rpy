label city_hub:
    call screen city_map_screen
    return

screen city_map_screen():
    tag menu

    add "bg city_map"
    use player_hud
    # 🏫 School button
    imagebutton:
        idle "images/school_icon.png"
        at pop_hover
        xpos 200
        ypos 300
        action If(time >= 17, Jump("school_locked"), [Hide("city_map_screen"), Jump("school_hub")])

    # 🏋️ Gym button
    imagebutton:
        idle "images/gym_icon.png"
        at pop_hover
        xpos 400
        ypos 350
        action [Hide("city_map_screen"), Jump("gym_hub")]

    # 🛒 Shop button
    imagebutton:
        idle "images/shop_icon.png"
        at pop_hover
        xpos 600
        ypos 320
        action [Hide("city_map_screen"), Jump("shop_hub")]

    # 🏠 Home button
    textbutton "🏠 Home":
        xpos 10
        ypos 10
        action [Hide("city_map_screen"), Jump("home_base")]


