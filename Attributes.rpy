init python:
    import random

default money = 100  # ✅ Now Ren'Py recognizes `money` as a global variable

# 📅 Game Stats
default day = 1
default time_of_day = "morning"
default energy = 100
default hunger = 100
default thirst = 100
default reputation = 0

# Class Attendance Tracking
default math_lessons = 0
default science_lessons = 0
default social_lessons = 0
default english_lessons = 0

# Exam Unlock Flags
default math_exam_unlocked = False
default science_exam_unlocked = False
default social_exam_unlocked = False
default english_exam_unlocked = False

# ✅ Function to update player stats and check for game over conditions
init python:
    def update_stats(energy_change=0, hunger_change=0, thirst_change=0, reputation_change=0, money_change=0):
        global energy, hunger, thirst, reputation, money

        energy += energy_change
        hunger += hunger_change
        thirst += thirst_change
        reputation += reputation_change
        money += money_change  

        # Keep stats within limits
        energy = max(0, min(100, energy))
        hunger = max(0, min(100, hunger))
        thirst = max(0, min(100, thirst))
        money = max(0, money)

        # Check for game over conditions
        if reputation <= -100:
            renpy.jump("game_over_bullying")
        if energy == 0 or hunger == 0 or thirst == 0:
            renpy.jump("game_over_exhaustion")

default day_message = ""  # ✅ Store the message to show later

init python:
    def force_day_end():
        global time_of_day, day, energy, hunger, thirst, day_message

        time_of_day = "night"
        day_message = "The day is over. You go to sleep..."
        day += 1
        time_of_day = "morning"

        energy = min(100, energy + 50)

        # ✅ Only reduce hunger if it hasn't been reduced recently
        if hunger > 50:  
            hunger = max(0, hunger - 20)  
        if thirst > 50:
            thirst = max(0, thirst - 20)


