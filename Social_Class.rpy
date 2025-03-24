label social_class:
    "You attended a Social Studies class. (-10 Energy, -5 Hunger, -5 Thirst)"
    $ update_stats(energy_change=-10, hunger_change=-5, thirst_change=-5)  
    $ social_lessons += 1
    if social_lessons == 3:
        $ social_exam_unlocked = True
        "Social Studies Exam is now available!"
    return
