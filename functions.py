import random
from hangmanData import words
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

# A password generator app
def py_password_generator ():
    total_characters = int(input("How many characters would you like to have in your password ?"))
    total_symbols = int(input("How many symbols you want to have in your password?"))
    total_numbers = int(input("How many numbers you want to have in your password?"))

    def generate_password (characters, symbols, numbers):
        password_array = []

        def get_random_letter():
            letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
            return letters[random.randrange(0, len(letters))]

        def get_random_symbol():
            symbols = "!@#$%^&*"
            return symbols[random.randrange(0, len(symbols))]

        # store letters
        total_letters = characters - (symbols + numbers)
        for i in range(0,total_letters):
            password_array.append(get_random_letter())
        # store symbols
        for i in range(0,total_symbols):
            password_array.append((get_random_symbol()))
        # store numbers
        for i in range(0,total_numbers):
            password_array.append(str((random.randrange(0,10))))

        random.shuffle(password_array)
        final_password = ''.join(password_array)
        return final_password

    print("Suggested password is " , generate_password(total_characters, total_symbols, total_numbers))

# hangman game
def play_hangman ():

    word_to_be_guessed = words[random.randrange(0,len(words))]
    difficulty_level = {
        'easy': 10,
        'medium': 5,
        'hard': 1
    }
    total_lives = difficulty_level[input("Select difficulty: \n Easy: 10 Lives \n Medium: 5 lives \n Hard: 1 ")]
    word_left_to_be_guessed = ['_'] * len(word_to_be_guessed)

    def show_stats():
        print("Remaining words and guessed successfully", word_left_to_be_guessed)
        print("Lives remaining " + str(total_lives))

    show_stats()
    letters_guessed_successfully = 0
    user_win = False

    while total_lives != 0 and letters_guessed_successfully != len(word_to_be_guessed):
        letter_guessed = input("Guess a letter")
        if letter_guessed not in word_to_be_guessed:
            total_lives = total_lives - 1
            show_stats()
            if total_lives == 0:
                user_win = False

        else:
            for i in range(len(word_to_be_guessed)):
                if word_to_be_guessed[i] == letter_guessed:
                    word_left_to_be_guessed[i] = letter_guessed
                    letters_guessed_successfully += 1

            show_stats()
            if letters_guessed_successfully == len(word_to_be_guessed):
                user_win = True

    if user_win:
        print(f"Congratulations, you won with {total_lives} Lives to Spare")
    else:
        print("Sorry you Lost ")

# Word encode decode app
def caesar_cipher():
    user_message = input("Enter a message you want to encode/decode").lower() #bananaz
    shift_number = int(input("Enter the shift number")) # 3
    letters = 'abcdefghijklmnopqrstuvwxyz'
    user_prompt = input("Do you want to encode or decode the message").lower()
    final_message = ''
    def encode_message(message, shift):
        message_list = list(user_message)
        for i in range(len(message_list)):
            if message_list[i] == ' ':
                message_list[i] = '&'
                continue
            index = letters.find(message_list[i])
            message_list[i] = letters[(index + shift) % 26]

        final_message = ''.join(message_list)
        return final_message

    def decode_message(message, shift):
        message_list = list(user_message)
        for i in range(len(message_list)):
            if message_list[i] == ' ':
                message_list[i] = '&'
                continue
            index = letters.find(message_list[i])
            message_list[i] = letters[(index - shift) % 26]

        final_message = ''.join(message_list)
        return final_message

    if user_prompt == "encode":
        final_message= encode_message(user_message, shift_number)
    elif user_prompt == "decode":
        final_message = decode_message(user_message, shift_number)

    print(f"Your encoded/decoded message is {final_message}")

