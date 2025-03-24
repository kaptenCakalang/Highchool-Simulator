label start:
    scene bg room
    "You wake up. It's morning."

    menu:
        "Eat breakfast (+10 Hunger, +5 Thirst)":
            $ update_stats(hunger_change=10, thirst_change=5)

        "Skip breakfast (No change)":
            pass

    menu:
        "Go to class":
            call class_selection from _call_class_selection

        "Take an Exam":
            call exam_selection from _call_exam_selection

        "Go to the store":
            call store_menu from _call_store_menu

        "Work Part-Time":
            call job_selection from _call_job_selection  # ✅ Calls new job selection menu

        "End the day":
            $ force_day_end()  # ✅ Ends the day properly
            jump start

# ✅ CLASS SELECTION MENU
label class_selection:
    menu:
        "Math Class":
            call math_classroom from _call_math_classroom  # ✅ Now it matches the actual label name
        "Science Class":
            call science_lab from _call_science_lab
        "Social Studies Class":
            call social_class from _call_social_class
        "English Class":
            call english_class from _call_english_class
        "Back":
            jump start  # ✅ Prevents resetting time
    
    $ force_day_end()  # ✅ Day only ends AFTER attending a class
    jump start

# ✅ EXAM SELECTION MENU
label exam_selection:
    menu:
        "Math Exam" if math_exam_unlocked:
            $ exam_subject = "math"
            call take_exam from _call_take_exam
        "Science Exam" if science_exam_unlocked:
            $ exam_subject = "science"
            call take_exam from _call_take_exam_1
        "Social Studies Exam" if social_exam_unlocked:
            $ exam_subject = "social"
            call take_exam from _call_take_exam_2
        "English Exam" if english_exam_unlocked:
            $ exam_subject = "english"
            call take_exam from _call_take_exam_3
        "Back":
            jump start  

    $ force_day_end()  # ✅ Ends the day ONLY if an exam was taken
    jump start

# ✅ STORE MENU (Now includes Part-Time Job option)
label store_menu:
    menu:
        "Buy Supplies":
            "The store is not implemented yet."
            jump store_menu  # ✅ Allows player to return instead of resetting

        "Work Part-Time":
            call job_selection from _call_job_selection_1  # ✅ Goes to the job selection screen

        "Back":
            jump start  # ✅ Prevents resetting time

# ✅ JOB SELECTION MENU
label job_selection:
    menu:
        "Cashier Job":
            call job_minigame from _call_job_minigame  # ✅ Calls cashier mini-game

        "Back":
            jump store_menu  # ✅ Goes back to store, doesn't reset time

    $ force_day_end()  # ✅ Ends the day ONLY if a job was done
    jump start


label show_day_message:
    "The day is over. You go to sleep..."
    return
