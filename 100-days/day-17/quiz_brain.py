class QuizBrain:
    def __init__(self, ls):
        self.question_number = 0
        self.question_list = ls
        self.score = 0

    def next_question(self):
        for idx, question in enumerate(self.question_list):
            print(f"Q.{idx + 1} {question.text}")
            answer = input("True or False? ").strip()
            if answer == question.answer:
                print("Correct!")
                self.score += 1
            else:
                print("You failed")
        print("you've completed the quiz")
        print(f"you've scored: {self.score}")