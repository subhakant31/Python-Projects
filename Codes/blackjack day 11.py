import random
check = input("Do you want to play a game of BlackJack ?")
def add(cards):
  sum = 0
  for i in cards:
    sum += i
  return sum
if check == "yes":
  def rungame():
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    user_card = [random.choice(cards), random.choice(cards)]
    pc_card = [random.choice(cards), random.choice(cards)]
    print(f"Your cards are {user_card[0]},{user_card[1]}")
    print(f"Computer's first card is {pc_card[0]}")
    print(f"sum of cards is {add(user_card)}")
    draw_check = input("Do you want to draw another card ?")
    sum=0
    while draw_check!="no":
      new_card=random.randint(1,10)
      new_cardpc = random.randint(1, 10)
      user_card.append(new_card)
      pc_card.append(new_cardpc)
      sum_user=add(user_card)
      sum_pc=add(pc_card)
      print(sum_user)
      draw_check2=input("Do you want to draw another card ?")
      if draw_check2=="no":
        draw_check="no"
    sum_user=add(user_card)
    sum_pc=add(pc_card)
    if sum_user<sum_pc and (sum_user>21 and sum_pc<21):
      print("You lose")
    else:
      print("You win")
    print(f"Sum of user is{sum_user}")
    print(f"Sum of pc is {sum_pc}")

  rungame()
else:
  print("Thank you for playing")
