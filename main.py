# simple calculator

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("Please, enter your choice :")
print("1 - add")
print("2 - substract")
print("3 - multiply")
print("4 - division")

while True:
    choice = input("Please, enter your choice (1 / 2 / 3 / 4) :")
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter your FIRST number : "))
        num2 = float(input("Enter your SECOND number : "))
        if choice == '1':
            print(f"{num1} + {num2} =", add(num1, num2))
        elif choice == '2':
            print(f"{num1} - {num2} = ", substract(num1, num2))
        elif choice == '3':
            print(f"{num1} * {num2} =", multiply(num1, num2))
        elif choice == '4':
            print(f"{num1} / {num2} =", divide(num1, num2))
    else:
        print("Your choice is not valid :(")