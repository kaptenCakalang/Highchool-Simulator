label job_minigame:
    scene bg store
    "You're working at the convenience store."

    # ✅ Reset customer count and start first customer
    $ customers_remaining = 5  
    $ new_customer()

    # ✅ Show mini-game screen
    show screen cashier_minigame_screen
    $ renpy.pause()  # ✅ Allows interaction until manually finished
    hide screen cashier_minigame_screen

    "You finish your shift and leave."

    # ✅ Ensure the mini-game properly ends
    $ end_cashier()  

    return
init python:
    def end_cashier():
        global customers_remaining
        customers_remaining = 5  # ✅ Reset for next session

        renpy.hide_screen("cashier_minigame_screen")  # ✅ Ensure UI is hidden
        renpy.jump("show_day_message")  # ✅ Move to next event
