# This script handles the final ending based on performance and stats

# ✅ Grade scoring function
init python:
    def grade_to_score(grade):
        if grade == "A":
            return 4
        elif grade == "B":
            return 3
        elif grade == "C":
            return 2
        elif grade == "D":
            return 1
        else:
            return 0


# ✅ Final check before triggering endings
label check_ending:

    scene black
    with fade
    "Your high school journey is coming to an end..."
    pause 1.0

    "Let's see how you did."

    $ total = (
        grade_to_score(grade_math) +
        grade_to_score(grade_english) +
        grade_to_score(grade_science) +
        grade_to_score(grade_history)
    )

    if total <= 5:
        jump bad_ending

    elif total >= 10 and energy >= 50 and charisma >= 5 and intelligence >= 5:
        jump secret_ending

    else:
        jump good_ending


# ❌ Bad Ending
label bad_ending:
    scene black
    with fade
    pause 1.0
    centered "Ending: Dropout"

    "Despite your efforts..."
    "You failed to meet the school’s graduation requirements."

    "Whether it was poor grades, lack of energy, or just bad luck — it wasn’t enough."

    "You leave school behind with heavy thoughts about what could've been."
    return


# ✅ Good Ending
label good_ending:
    scene black
    with fade
    pause 1.0
    centered "Ending: Graduation Achieved"

    "You didn't ace every subject, but you gave it your best."

    "You kept your health in check and managed to pass your classes."

    "You’ve officially graduated — and the future is yours to shape."
    return


# ⭐ Secret Ending
label secret_ending:
    scene black
    with fade
    pause 1.0
    centered "Ending: Top Student Legend"

    "Not only did you graduate..."
    "You excelled beyond expectations!"

    "Your outstanding grades, balanced life, and charm earned you a prestigious scholarship."

    "You're the pride of the school — and everyone knows your name."
    return


