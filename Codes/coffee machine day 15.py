import coffee_data

menu=coffee_data.MENU
resources=coffee_data.resources

def check_resources(item,resources):
  if item["ingredients"]["water"] > resources["water"]:
    return False
  elif item["ingredients"]["milk"] > resources["milk"]:
    return False
  elif item["ingredients"]["coffee"] > resources["coffee"]:
    return False
  else:
    return True

def ask_formoney():
  money=int(input("Enter your money"))
  return money
def deduct_resource(item,resource):
  global resources
  resources["milk"]-=item["ingredients"]["milk"]
  resources["water"] -= item["ingredients"]["water"]
  resources["coffee"] -= item["ingredients"]["coffee"]

def make_espresso(item,resources):
  if check_resources(item,resources):
    deduct_resource(item, resources)
    money=ask_formoney()
    if money > item["cost"]:
      change=money-item["cost"]
      print(f"Here is your money {change}")
      print(f"remaining resouces{resources}")
      startcoffee()
    else:
      print("Insufficient amount")

  else:
    print("insufficient resources")
    startcoffee()

def make_latte(item,resources):
  if check_resources(item, resources):
    deduct_resource(item, resources)
    money=ask_formoney()
    if money > item["cost"]:
      change=money-item["cost"]
      print(f"Here is your money {change}")
      print(f"remaining resouces{resources}")
      startcoffee()
    else:
      print("Insufficient amount")

  else:
    print("insufficient resources")
    startcoffee()

def make_cappuccino(item,resources):
  if check_resources(item,resources):
    deduct_resource(item, resources)
    money=ask_formoney()
    if money > item["cost"]:
      change=money-item["cost"]
      print(f"Here is your money {change}")
      print(f"remaining resouces{resources}")
      startcoffee()
    else:
      print("Insufficient amount")

  else:
    print("insufficient resources")
    startcoffee()


def startcoffee():
  flavour=input("What would you like to drink (espresso/latte/cappuccino")
  if flavour=="espresso":
    make_espresso(menu["espresso"], resources)
  elif flavour=="latte":
    make_latte(menu["latte"],resources)
  elif flavour=="cappuccino":
    make_cappuccino(menu["cappuccino"],resources)
  elif flavour=="report":
    print(resources)
    startcoffee()

startcoffee()