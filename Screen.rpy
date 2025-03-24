# ✅ Initialize global variables
init:
    default exam_feedback = ""  # Stores feedback for correct/wrong answers
    default answer_selected = False  # ✅ Prevents selecting multiple answers

# 📊 Display Player Stats in Top-Left Corner
screen stats_hud():
    frame:
        align (0.02, 0.02)  # Position at the top-left
        background "#0008"  # Semi-transparent black background
        padding (10, 10)

        vbox:
            text "Day: [day]" color "#fff" size 20
            text "Time: [time_of_day]" color "#fff" size 18
            text "Energy: [energy]" color "#0f0" size 18
            text "Hunger: [hunger]" color "#ff0" size 18
            text "Thirst: [thirst]" color "#00f" size 18
            text "Reputation: [reputation]" color "#f00" size 18
            text "Money: $[money]" color "#0ff" size 18

# ✅ Always display the stats HUD
init:
    $ config.overlay_screens.append("stats_hud")

# 📝 Exam Question Screen (Now Locks Answer Choices After Selection)
screen exam_screen(question, options, correct_answer):
    frame:
        align (0.5, 0.5)  # Center of the screen
        background "#2228"
        padding (20, 20)

        vbox:
            text "[question]" color "#fff" size 22

            # ✅ Show all answer options (Shuffled)
            for option in options:
                textbutton option:
                    action Function(check_answer, option, correct_answer)
                    sensitive not answer_selected  # ✅ Disables buttons after selecting

            # ✅ Show feedback (Correct/Wrong) after an answer is selected
            if exam_feedback:
                text "[exam_feedback]" color "#ff0" size 18
                textbutton "Next Question" action [SetVariable("exam_feedback", ""), SetVariable("answer_selected", False), Return()]
                
# ✅ Function to Check Exam Answers (Locks Choices)
init python:
    def check_answer(selected, correct):
        global exam_feedback, answer_selected  # ✅ Track if an answer was chosen
        if not answer_selected:  # ✅ Prevent multiple selections
            if selected == correct:
                exam_feedback = "Correct!"
            else:
                exam_feedback = "Wrong!"
            answer_selected = True  # ✅ Lock answer selection

        renpy.restart_interaction()  # ✅ Refresh screen to update UI

init python:
    import renpy.store as store
    import random

    # ✅ Cashier mini-game variables
    customer_total = 0
    customer_paid = 0
    correct_change = 0
    selected_change = 0
    cashier_feedback = ""
    customers_remaining = 5  # ✅ 5 customers per session
    money = 100  # Example starting money

    def new_customer():
        """ Generates a new transaction. """
        global customer_total, customer_paid, correct_change, selected_change, cashier_feedback, customers_remaining

        if customers_remaining > 0:
            customer_total = random.randint(5, 20)  # ✅ Random price
            customer_paid = customer_total + random.choice([5, 10, 15, 20])  # ✅ Paid amount
            correct_change = customer_paid - customer_total  # ✅ Correct change
            selected_change = 0  # ✅ Reset selected change
            cashier_feedback = "Click the correct amount of change!"

            renpy.restart_interaction()  # ✅ Refresh UI
        else:
            end_cashier()  # ✅ Ends mini-game

    def check_cashier():
        """ Checks if the player selected the correct change. """
        global cashier_feedback, money, customers_remaining, selected_change

        if selected_change == correct_change:
            earnings = random.randint(10, 25)  # ✅ Random pay bonus
            cashier_feedback = f"Correct! You earned ${earnings}."
            money += earnings
        else:
            cashier_feedback = f"Wrong! You lost ${correct_change}."
            money -= correct_change  # ❌ Lose money for mistakes

        customers_remaining -= 1  # ✅ Reduce number of customers left
        renpy.restart_interaction()  # ✅ Refresh UI

        # ✅ Move to next customer or end mini-game
        if customers_remaining > 0:
            new_customer()  
        else:
            renpy.hide_screen("cashier_minigame_screen")  # ✅ Close screen before ending
            renpy.jump("show_day_message")  # ✅ Move to next day



screen cashier_minigame_screen():
    modal True  

    frame:
        align (0.5, 0.5)
        padding (20, 20)
        background "#2228"

        vbox:
            text "Customers Remaining: [customers_remaining]" color "#fff" size 22  
            text "Total Price: $[customer_total]" color "#fff" size 20  
            text "Customer Paid: $[customer_paid]" color "#fff" size 20  
            text "Select the correct change: $[selected_change]" color "#ff0" size 20  

            # ✅ Buttons for selecting change amount
            hbox:
                spacing 10
                textbutton "$5" action SetVariable("selected_change", 5)
                textbutton "$10" action SetVariable("selected_change", 10)
                textbutton "$15" action SetVariable("selected_change", 15)
                textbutton "$20" action SetVariable("selected_change", 20)


            # ✅ Confirm Button (Must be clicked to proceed)
            textbutton "Give Change" action Function(check_cashier) text_size 20  

            # ✅ Show feedback
            if cashier_feedback:
                text "[cashier_feedback]" color "#ff0" size 18  

