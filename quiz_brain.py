class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"{self.question_number} question is {current_question.text}")


    def has_questions_left(self):
        return self.question_number < len(question_list)

    def check_answer(self, user_answer ):
