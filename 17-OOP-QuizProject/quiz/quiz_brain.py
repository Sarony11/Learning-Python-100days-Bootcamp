class QuizBrain:
    def __init__(self,q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0
    
    def next_question(self):
        actual_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number} - {actual_question.text} - (True/False): ")
        return answer
    
    def still_has_questions(self):
        return self.question_number+1 < len(self.question_list)
    
    def check_answer(self,answer):
        if answer == self.question_list[self.question_number].answer:
            self.score += 1
            print("You got this one! You are right!")
        else:
            print("Sorry but it is not what you think! You are wrong")
        print(f"The correct answer was: {self.question_list[self.question_number].answer}")
        print(f"You current score is: {self.score}/{self.question_number}")

    def end_quiz(self):
        print("----------------------------------------------------------")
        print("You have completed the Quiz")
        print(f"Your final score was: {self.score}/{self.question_number}")