init python:
    history_question_bank = [
        {"question": "1st U.S. President?", "choices": [("George Washington", True), ("Lincoln", False), ("Adams", False)]},
        {"question": "Great Wall is in?", "choices": [("China", True), ("Japan", False), ("India", False)]},
        {"question": "WW2 ended in?", "choices": [("1945", True), ("1939", False), ("1950", False)]},
        {"question": "Pyramids built by?", "choices": [("Egyptians", True), ("Romans", False), ("Greeks", False)]},
        {"question": "Discovered America?", "choices": [("Columbus", True), ("Napoleon", False), ("Caesar", False)]},
    ]

label quiz_history:
    "🏺 History Quiz Time!"
    $ correct = 0
    $ used_questions = renpy.random.sample(history_question_bank, 3)

    python:
        for q in used_questions:
            shuffled = renpy.random.sample(q["choices"], len(q["choices"]))
            formatted = [(text, "correct" if is_correct else "wrong") for text, is_correct in shuffled]
            renpy.call_in_new_context("show_quiz_question", q["question"], formatted)

    if correct == 3:
        "✅ You passed the quiz!"
        $ grade_history = upgrade_grade(grade_history)
    else:
        "❌ You didn't pass this time."

    "Your current History grade is [grade_history]."
    jump school_hub
