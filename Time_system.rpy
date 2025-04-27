label advance_time:
    $ time += 1

    if time >= 23:
        jump end_of_day

    return

label end_of_day:
    "You return home for the night."

    if time < 23:
        "You went to bed on time and feel rested."
        $ energy = min(energy + 50, 100)
    else:
        "You stayed up too late and feel exhausted."
        $ energy = max(energy - 30, 0)

    $ hunger = max(hunger - 10, 0)
    $ thirst = max(thirst - 10, 0)
    $ time = 6
    $ day += 1

    "A new day begins..."

    # ✅ Check if it's the final day
    if day >= 30:
        jump check_ending

    jump home_base
