# Shop.rpy — All shop features (buy, job, talk)

# OPTIONAL: define the shopkeeper character
define s = Character("Shopkeeper", color="#EBA937")

label shop_hub:
    call advance_time from _call_advance_time_6
    call screen shop_screen
    return


label shopkeeper_menu:
    menu:
        "Talk to the shopkeeper":
            jump shop_talk

        "Work part-time (Needs 2 Charisma)":
            if charisma >= 2:
                jump shop_job
            else:
                s "Hmm... you don’t seem confident enough to handle customers."
                jump shop_hub

        "Back":
            jump shop_hub

# 🧑 Shopkeeper Dialog
label shop_talk:
    s "It's good to see a polite student like you."
    $ charisma += 1
    $ energy = max(energy - 5, 0)
    jump shop_hub

label shop_job:
    s "Alright, let's see how you handle the register today."

    $ energy = max(energy - 15, 0)
    $ charisma += 1

    jump job_minigame


# 🛒 Buy Menu
label shop_buy_menu:
    menu:
        "Buy Snack (-$2, +5 Hunger)":
            if money >= 2:
                $ money -= 2
                $ hunger = min(hunger + 5, 100)
                "You eat a quick snack."
            else:
                "You don’t have enough money."
            call advance_time from _call_advance_time_7
            jump shop_buy_menu

        "Buy Water Bottle (-$1, +5 Thirst)":
            if money >= 1:
                $ money -= 1
                $ thirst = min(thirst + 5, 100)
                "You drink some water."
            else:
                "You don’t have enough money."
            call advance_time from _call_advance_time_8
            jump shop_buy_menu

        "Buy Energy Drink (-$4, +10 Energy, +5 Thirst)":
            if money >= 4:
                $ money -= 4
                $ energy = min(energy + 10, 100)
                $ thirst = min(thirst + 5, 100)
                "You feel recharged!"
            else:
                "You don’t have enough money."
            call advance_time from _call_advance_time_9
            jump shop_buy_menu

        "Buy Instant Meal (-$6, +15 Hunger, +5 Energy)":
            if money >= 6:
                $ money -= 6
                $ hunger = min(hunger + 15, 100)
                $ energy = min(energy + 5, 100)
                "You eat a hot packaged meal."
            else:
                "You don’t have enough money."
            call advance_time from _call_advance_time_10
            jump shop_buy_menu

        "Buy Chips (-$3, +10 Hunger, -2 Thirst)":
            if money >= 3:
                $ money -= 3
                $ hunger = min(hunger + 10, 100)
                $ thirst = max(thirst - 2, 0)
                "Crunchy and salty!"
            else:
                "You don’t have enough money."
            call advance_time from _call_advance_time_11
            jump shop_buy_menu

        "Back to shop":
            jump shop_hub

            label job_minigame:
    scene bg shop
    "You're working at the convenience store."

    $ customers_remaining = 5
    $ job_earnings = 0
    $ new_customer()

    show screen cashier_minigame_screen
    $ renpy.pause(hard=True)
    hide screen cashier_minigame_screen

    "You finish your shift and leave."
    "You earned $[job_earnings] today."

    $ money += job_earnings
    $ job_earnings = 0

    if time >= 23:
        jump end_of_day

    jump shop_hub


init python:
    import random

    customer_total = 0
    customer_paid = 0
    correct_change = 0
    selected_change = 0
    cashier_feedback = ""
    customers_remaining = 5
    job_earnings = 0

    def new_customer():
        global customer_total, customer_paid, correct_change, selected_change, cashier_feedback
        if customers_remaining > 0:
            customer_total = random.randint(5, 20)
            customer_paid = customer_total + random.choice([5, 10, 15, 20])
            correct_change = customer_paid - customer_total
            selected_change = 0
            cashier_feedback = "Click the correct amount of change!"
            renpy.restart_interaction()
        else:
            renpy.hide_screen("cashier_minigame_screen")
            renpy.jump("job_minigame_result")

    def check_cashier():
        global cashier_feedback, money, customers_remaining, selected_change, job_earnings

        if selected_change == correct_change:
            earned = random.randint(5, 8)
            cashier_feedback = f"✅ Correct! You earned ${earned}."
            job_earnings += earned
        else:
            penalty = correct_change
            cashier_feedback = f"❌ Wrong! You lost ${penalty}."
            job_earnings = max(job_earnings - penalty, 0)

        customers_remaining -= 1
        renpy.restart_interaction()

        if customers_remaining > 0:
            new_customer()
        else:
            renpy.hide_screen("cashier_minigame_screen")
            renpy.jump("job_minigame_result")

label job_minigame_result:
    "You finish your shift and leave the store."
    "You earned $[job_earnings] today."

    $ money += job_earnings
    $ job_earnings = 0

    jump shop_hub
