init python:
    math_question_bank = [
        {"question": "What is 5 × 4?", "choices": [("20", True), ("25", False), ("15", False)]},
        {"question": "Square root of 81?", "choices": [("9", True), ("8", False), ("7", False)]},
        {"question": "Solve: 2 + 3 × 2", "choices": [("8", True), ("10", False), ("12", False)]},
        {"question": "12 ÷ 3?", "choices": [("4", True), ("3", False), ("6", False)]},
        {"question": "7 + 6?", "choices": [("13", True), ("14", False), ("12", False)]},
    ]

label quiz_math:
    "📘 Math Quiz Time!"
    $ correct = 0
    $ used_questions = renpy.random.sample(math_question_bank, 3)

    python:
        for q in used_questions:
            shuffled = renpy.random.sample(q["choices"], len(q["choices"]))
            formatted = [(text, "correct" if is_correct else "wrong") for text, is_correct in shuffled]
            renpy.call_in_new_context("show_quiz_question", q["question"], formatted)

    if correct == 3:
        "✅ You passed the quiz!"
        $ grade_math = upgrade_grade(grade_math)
    else:
        "❌ You didn't pass this time."

    "Your current Math grade is [grade_math]."
    jump school_hub
