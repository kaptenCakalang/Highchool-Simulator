init python:
    english_question_bank = [
        {"question": "Synonym of 'Happy'?", "choices": [("Joyful", True), ("Angry", False), ("Tired", False)]},
        {"question": "Correct spelling?", "choices": [("Definitely", True), ("Definately", False), ("Definetly", False)]},
        {"question": "What is a noun?", "choices": [("Person/place/thing", True), ("Action word", False), ("Describing word", False)]},
        {"question": "Correct sentence?", "choices": [("He goes to school every day.", True), ("He go to school.", False), ("He going school.", False)]},
        {"question": "Past tense of 'run'?", "choices": [("Ran", True), ("Runned", False), ("Running", False)]},
    ]

label quiz_english:
    "📝 English Quiz Time!"
    $ correct = 0
    $ used_questions = renpy.random.sample(english_question_bank, 3)

    python:
        for q in used_questions:
            shuffled = renpy.random.sample(q["choices"], len(q["choices"]))
            formatted = [(text, "correct" if is_correct else "wrong") for text, is_correct in shuffled]
            renpy.call_in_new_context("show_quiz_question", q["question"], formatted)

    if correct == 3:
        "✅ You passed the quiz!"
        $ grade_english = upgrade_grade(grade_english)
    else:
        "❌ You didn't pass this time."

    "Your current English grade is [grade_english]."
    jump school_hub
