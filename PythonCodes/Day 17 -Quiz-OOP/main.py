from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


#print(question_data)


### question bank create

question_bank = []

for data in question_data:
    #print(data)
    question_text = data["text"]
    question_answer = data["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#print(question_bank[1].text)
#print(question_bank[1].answer)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()



