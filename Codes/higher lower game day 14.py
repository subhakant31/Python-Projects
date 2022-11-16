import random
import gamedata
def compare(data1,data2):
  for item in gamedata.data:
    if gamedata.data[item]["follower_count"]==data1:
      user1=gamedata.data[item]
  for item in gamedata.data:
    if gamedata.data[item]["follower_count"]==data2:
      user2 = gamedata.data[item]

  # print(f"which is higher? {data1} or {data2}")

  answer=input(f"is {user2} lower or higher than {user1}")
  if answer=="high" and data2>data1:
    return True
  elif answer=="low" and data2<data1:
    return True
  elif answer=="high" and data2<data1:
    return False
  elif answer=="low" and data2>data1:
    return False
def startgame(first_data):
  ctr=0

  lost=False
  while not lost:
    second = random.choice(gamedata.data)
    second_data=second["follower_count"]
    if compare(first_data, second_data):
      ctr+=1
      first_data=second_data
    else:
      print(f"Your total score is {ctr}")
      exit()
first=random.choice(gamedata.data)
first_data=first["follower_count"]

startgame(first_data)