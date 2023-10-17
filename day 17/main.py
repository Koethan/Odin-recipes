from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []


## to make change the information from a list of dictionaries we loop throught the list and for each dictionary
#we take the text key and the answer key and put them in their own variables. We then create a variable here 
#called entry to create a question object passing the text and the question and the answer as the answer for the 
#Question class! We then append our question_bank list with all of the objects we just created.
for i in question_data:
     question_text = i["question"]
     question_answer = i["correct_answer"]
     entry = Question(question_text, question_answer)
     question_bank.append(entry)

# print(question_bank)
# print(question_bank[1].text)
# print(question_bank[1].answer)
#condition = True
quiz = QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(f"Thanks for playing TRIVIA you have a final score of {quiz.score} correct out of {len(quiz.question_list)}!")

# while condition:
#     #quiz = QuizBrain(question_bank)
#     quiz.next_question()
#     condition = quiz.still_has_questions()
#     quiz.score_tracker()
#     print("\n")
#     if condition == False:
#         break
 #print(f"Thanks for playing TRIVIA you have a final score of {quiz.score} correct out of {len(quiz.question_list)}!")
#     #quiz.next_question()
    
