from playsound import playsound
import random
import operator
import winsound
winsound.PlaySound('Alarm.wav', winsound.SND_ASYNC | winsound.SND_ALIAS )

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }
    num_1 = random.randint(1,10)
    num_2 = random.randint(1,10)
    operation = random.choice (list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print (f'What is {num_1} {operation} {num_2}?')
    return answer
def ask_question():
    answer = random_problem()
    UserInput = float (input())
    return UserInput == answer



def game():
    print("Answer at least 4 questions right to stop the timer!")
    score = 0
    for i in range (7):
        if ask_question() == True:
            score += 1
            print ("Correct!")
        else:
            print("Incorrect!")

    print(f'Your score is {score}')
game()
