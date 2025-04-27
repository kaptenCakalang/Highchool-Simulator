init python:
    science_question_bank = [
        {"question": "Red Planet?", "choices": [("Mars", True), ("Jupiter", False), ("Saturn", False)]},
        {"question": "Boiling point of water?", "choices": [("100°C", True), ("90°C", False), ("110°C", False)]},
        {"question": "Part that makes food?", "choices": [("Leaves", True), ("Roots", False), ("Stem", False)]},
        {"question": "We breathe in?", "choices": [("Oxygen", True), ("CO2", False), ("Hydrogen", False)]},
        {"question": "Center of an atom?", "choices": [("Nucleus", True), ("Proton", False), ("Electron", False)]},
    ]

label quiz_science:
    "🔬 Science Quiz Time!"
    $ correct = 0
    $ used_questions = renpy.random.sample(science_question_bank, 3)

    python:
        for q in used_questions:
            shuffled = renpy.random.sample(q["choices"], len(q["choices"]))
            formatted = [(text, "correct" if is_correct else "wrong") for text, is_correct in shuffled]
            renpy.call_in_new_context("show_quiz_question", q["question"], formatted)

    if correct == 3:
        "✅ You passed the quiz!"
        $ grade_science = upgrade_grade(grade_science)
    else:
        "❌ You didn't pass this time."

    "Your current Science grade is [grade_science]."
    jump school_hub
