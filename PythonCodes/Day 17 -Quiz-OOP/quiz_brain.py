class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            #print("YES")
            return True
        else:
            print("You have completed the quiz")
            print(f"Your final score was {self.score}/{self.question_number}")
            return False
        

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True / False: )")
        self.check_answer(user_answer, current_question.answer)
       

    def check_answer(self, user_answer, current_question):
        if user_answer.lower() == current_question.lower():
            print("Correct answer")
            self.score +=1
            print(f"courrect score: {self.score}/{self.question_number}")
        else:
            print("Wrong answer")
        print("\n")
    
    def test():
        print("Hi there")

 