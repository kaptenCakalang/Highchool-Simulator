label english_class:
    "You attended an English class. (-10 Energy, -5 Hunger, -5 Thirst)"

    # ✅ Only call this ONCE
    $ update_stats(energy_change=-10, hunger_change=-5, thirst_change=-5)  

    # ✅ Track class attendance
    $ english_lessons += 1

    # ✅ Unlock exam after 3 lessons
    if english_lessons == 3:
        $ english_exam_unlocked = True
        "English Exam is now available!"

    return
