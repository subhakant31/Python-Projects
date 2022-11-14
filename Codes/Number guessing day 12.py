import random
def easy(number):
  life=10
  while life!=0:
    guess = int(input("Guess the number"))
    if guess==number:
      print("You win")
      check=input("Do you want to play again?")
      if check=="Yes":
        startgame()
      else:
        exit()
    elif guess< number:
      print("Too low")
      life-=1
      print(f"life remaining{life}")
    elif guess> number:
      print("Too high")
      life-=1
      print(f"life remaining{life}")
  print("You are noob")

def medium(number):
  life = 5
  while life != 0:
    guess = int(input("Guess the number"))
    if guess == number:
      print("You win")
      check = input("Do you want to play again?")
      if check == "Yes":
        startgame()
      else:
        exit()
    elif guess < number:
      print("Too low")
      life -= 1
      print(f"life remaining{life}")
    elif guess > number:
      print("Too high")
      life -= 1
      print(f"life remaining{life}")
  print("You are noob")

def hard(number):
  life = 3
  while life != 0:
    guess = int(input("Guess the number"))
    if guess == number:
      print("You win")
      check = input("Do you want to play again?")
      if check == "Yes":
        startgame()
      else:
        exit()
    elif guess < number:
      print("Too low")
      life -= 1
      print(f"life remaining{life}")
    elif guess > number:
      print("Too high")
      life -= 1
      print(f"life remaining{life}")
  print("You are noob")

def startgame():
  print("Welcome to the number guessing game")
  print("I'm thinking of  number between 1 and 100")
  level=input("choose a difficulty easy medium or hard")
  number=random.randint(1,100)
  if level=="easy":
    easy(number)
    play_again=input("Do you want to play again ?")
    if play_again=="yes":
      startgame()
    else:
      print("Thank you for playing")
      exit()
  elif level=="medium":
    medium(number)
    play_again = input("Do you want to play again ?")
    if play_again == "yes":
      startgame()
    else:
      print("Thank you for playing")
      exit()
  elif level=="hard":
    hard(number)
    play_again = input("Do you want to play again ?")
    if play_again == "yes":
      startgame()
    else:
      print("Thank you for playing")
      exit()

startgame()