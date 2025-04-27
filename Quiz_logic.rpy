# quiz_logic.rpy

# Grade upgrader function
init python:
    def upgrade_grade(current_grade):
        grade_order = ["E", "D", "C", "B", "A"]
        if current_grade in grade_order and current_grade != "A":
            return grade_order[grade_order.index(current_grade) + 1]
        return current_grade

label show_quiz_question(question_text, choices):
    $ _return = None
    call screen quiz_question(question_text, choices)
    $ result = _return

    if result == "correct":
        $ correct += 1

    return


