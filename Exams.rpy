init python:
    def shuffle_exam_questions(questions):
        random.shuffle(questions)
        for q in questions:
            random.shuffle(q["options"])
        return questions

    exam_questions = {
        "math": [
            {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
            {"question": "Solve: 5 x 3", "options": ["15", "20", "25"], "answer": "15"},
            # (Add 8 more)
        ],
        "science": [
            {"question": "What is H2O?", "options": ["Oxygen", "Water", "Hydrogen"], "answer": "Water"},
            {"question": "What planet is known as the Red Planet?", "options": ["Earth", "Mars", "Venus"], "answer": "Mars"},
            # (Add 8 more)
        ],
        "social": [
            {"question": "Who was the first President of the USA?", "options": ["Lincoln", "Washington", "Jefferson"], "answer": "Washington"},
            {"question": "What is the capital of France?", "options": ["Berlin", "Madrid", "Paris"], "answer": "Paris"},
            # (Add 8 more)
        ],
        "english": [
            {"question": "What is the plural of 'mouse'?", "options": ["Mouses", "Mice", "Mousen"], "answer": "Mice"},
            {"question": "Which word is a synonym for 'happy'?", "options": ["Sad", "Angry", "Joyful"], "answer": "Joyful"},
            # (Add 8 more)
        ]
    }

label take_exam:
    python:
        current_exam = shuffle_exam_questions(exam_questions[exam_subject])
        question_index = 0

    while question_index < len(current_exam):
        $ q = current_exam[question_index]
        call screen exam_screen(q["question"], q["options"], q["answer"]) with dissolve
        $ question_index += 1

    "Exam completed!"
    $ force_day_end()  # ✅ Use `force_day_end()` instead
    return
