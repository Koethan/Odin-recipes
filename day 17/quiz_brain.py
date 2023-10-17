

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0 #to start in the front of the list 
        self.question_list = question_list
        self.score = 0

    
    def still_has_questions(self):
        """Returns true if we are not at the end of the list and False if there are no more questions"""
        return self.question_number < len(self.question_list)    
    
    def next_question(self):
        """creates the current question and then increases the question number to move to the next question then asks the user for their answer and then uses the check_answer method to check for the current question"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_answer, current_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        """the process of checking if the guess was the right answer and then increases the score, then is prints out the count of current score, then prints a line break"""
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print("Incorrect...")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
    
    
    # def next_question(self):
    #     self.user_guess = input(f"Q{self.question_number + 1}: {self.question_list[self.question_number].text}: (True/False) ").lower()
    #     self.answer = self.question_list[self.question_number].answer.lower()
        
   
    # def still_has_questions(self):
    #     while self.question_number < len(self.question_list)-1:
    #         self.question_number += 1
    #         return True
    #     return False
    
    # def score_tracker(self):
        
    #     if self.user_guess == self.answer:
    #         self.score += 1
    #         print(f"Correct ({self.score}/{self.question_number})")
    #     else:
    #         print(f"Incorrect ({self.score}/{self.question_number})")



    #     # self.correct = 0
    #     # self.question_number += 1
    #     # while self.correct < 3:
    #     #     if self.user_guess == self.answer:
    #     #         self.correct += 1
        #         print(f"Correct ({self.correct}/3)")
        #         self.next_question()
        #     else:

        #         print(f"Incorrect ({self.correct}/3)")
        #         self.next_question()
        # return False
    
    # def answer_checker(self):
    #     if self.answer == self.question_list:
    #         print("Correct")
    #     else:
    #         print("Incorrect")
    #     self.next_question()

# q1 = QuizBrain(question_bank)
# q1.next_question()


