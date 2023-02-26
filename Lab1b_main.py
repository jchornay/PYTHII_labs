#Jonathan Chornay
#CMSY 257 Spring 2023 Class
#Professor Charles Edwards
#
#Lab 1 Problem 2

#imports module random
import random

def main():

    #creates list of question objects
    q1 = Question("Which car company makes the Ranger?", "BWM", "Mazda", "Ford", "Mercedes",3)
    q2 = Question("How many lug nuts does a car typically have?", "3", "4 to 6", "10 or more", "Cars do not have lug nuts", 2)
    q3 = Question("What purpose does engine oil serve?", "It fuels the engine", "It lubricates the wheel bearings", "It cools and lubricates the engine", "It cleans the windows", 3)
    q4 = Question("What does 'MPH' stand for?", "Miles per hour", "Minutes per hour", "Maximum piston height", "Miniature pony house", 1)
    q5 = Question("Why are we here, and what is our purpose?", "To learn Java", "To learn CSS", "To watch helplessly while ChatGPT replaces us", "To learn Python while ChatGPT replaces us", 4)
    q6 = Question("Which car company makes the Silverado?", "Chevy", "Fiat", "Tesla", "Honda", 1)
    q7 = Question("Which fluid is most dangerous to run out of while driving?", "Windshield washer fluid", "Blinker fluid", "Coolant", "Power steering fluid", 3)
    q8 = Question("How many reverse lights is a car legally required to have?", "At least 1, but not necessarily 2", "2", "3", "It varies by state", 1)
    q9 = Question("What is one of the most likely suspects behind a squeaking sound when the engine is running and the car isn't moving?", "The brakes","The belts", "The differential", "The radiator", 2)
    q10 = Question("What does 'ABS' stand for?", "All Bearing System", "After Brake Stopping", "A Bored Student", "Antilock Braking System", 4)

    questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

    #initializes player scores
    p1_score = 0
    p2_score = 0

    print(f"-----------------------\nPlayer One's turn!\n-----------------------\n")

    #displays five questions
    for i in range(5):

        print(f"Question {i+1}:")

        #chooses a random index on the list
        current = random.randint(0,len(questions)-1)

        #prints __str__ function of random indexed Question object
        print(questions[current])

        #saves player answer as integer
        player_answer = int(input("Select 1-4: "))

        #compares player answer to correctAns attribute of current Question object
        #if player answer matches correct answer, player gets a point
        if player_answer == questions[current].get_correctAns():
            print("Correct! One point for Player One!")
            p1_score+=1
        else:
            print(f"Sorry, that is not the correct answer. The correct answer is {questions[current].get_correctAns()}.")


        input(f"Press enter to continue...\n")

        #removes current question from the list so same question is never asked twice
        del questions[current]

    print(f"-----------------------\nPlayer Two's turn!\n-----------------------\n")

    #same as above, but for Player Two
    for i in range(5):
        print(f"Question {i + 1}:")

        current = random.randint(0, len(questions) - 1)

        print(questions[current])

        player_answer = int(input("Select 1-4: "))

        if player_answer == questions[current].get_correctAns():
            print("Correct! One point for Player Two!")
            p2_score += 1
        else:
            print(
                f"Sorry, that is not the correct answer. The correct answer is {questions[current].get_correctAns()}.")

        input(f"Press enter to continue...\n")
        del questions[current]

    print(f"-----------------------\nThat's the game! Player One has {p1_score} points, and Player Two has {p2_score} points.")

    #prints appropriate message depending on whether there is a win or a tie
    if p1_score == p2_score:
        print(f"...Wow, a perfect tie!")
    elif p1_score > p2_score:
        print(f"Player One wins!")
    else:
        print(f"Player Two wins!")
    print(f"-----------------------")

class Question:

    #init method
    def __init__(self, question, ans1, ans2, ans3, ans4, correctAns):
        self.__question = question
        self.__ans1 = '1. '+ans1
        self.__ans2 = '2. '+ans2
        self.__ans3 = '3. '+ans3
        self.__ans4 = '4. '+ans4
        self.__correctAns = correctAns

    #getters and setters

    def get_question(self):
        return self.__question
    def set_question(self, question):
        self.__question = question

    def get_ans1(self):
        return self.__ans1
    def set_ans1(self, ans1):
        self.__ans1 = ans1

    def get_ans2(self):
        return self.__ans2
    def set_ans2(self, ans2):
        self.__ans2 = ans2

    def get_ans3(self):
        return self.__ans3
    def set_ans3(self, ans3):
        self.__ans3 = ans3

    def get_ans4(self):
        return self.__ans4
    def set_ans4(self, ans4):
        self.__ans4 = ans4

    def get_correctAns(self):
        return self.__correctAns
    def set_correctAns(self, correctAns):
        self.__correctAns = correctAns

    def __str__(self):
        return f'{self.__question}\n\n' \
               f'{self.__ans1}\n' \
               f'{self.__ans2}\n' \
               f'{self.__ans3}\n' \
               f'{self.__ans4}\n'

if __name__ == '__main__':
    main()