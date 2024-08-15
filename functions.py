import random
from stonePaperScissorsSigns import stone,paper,scissor, stone_paper_scissor_data


# Each person bill calculator
def bill_calculator_app () :
    total_bill = float(input("What was the total bill ?"))
    tip_given = float(input("How much tip you want to give in percentage ?"))
    total_people = int(input("How many people to split the bill ?"))
    def calculateAmountForEachPerson(bill, tip, people):
        return (bill + ((tip / 100) * bill)) / people
    print("$ " + str(round(calculateAmountForEachPerson(total_bill, tip_given, total_people), 2)))


# A stone paper scissor app
def stone_paper_scissor_app ():
    user_input = int(input("Press 0 for stone, 1 for paper, 2 for scissor"))
    computer_input = random.randint(0, 2)

    def find_winner(user, computer):
        print("Your Choice is \n" + stone_paper_scissor_data[user])
        print("Computer's choice is \n" + stone_paper_scissor_data[computer])
        if user_input == computer_input:
            print("It is a draw")
        elif user_input == 0 and computer_input == 1 or user_input == 1 and computer_input == 2 or user_input == 2 and computer_input == 0:
            print("You lose")
        else:
            print("you win")

    find_winner(user_input, computer_input)






