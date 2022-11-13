endloop=False

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
result=0
first=int(input("Enter the first number"))
while not endloop:

    print("+ - * /")
    operation=input("Enter an operation")
    second=int(input("Enter second number"))

    if operation=="+":
        result=add(first, second)
    elif operation=="-":
        result=substract(first, second)
    elif operation=="*":
        result=multiply(first, second)
    elif operation=="/":
        result=divide(first, second)

    print(result)
    check=input("Do you have any other numbers ?")
    if check!="yes":
        endloop=True

    else:
        first=result











