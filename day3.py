# Functions
"""
def greet(name):
    print(f"Welc0me {name}")


def greater(a, b):
    if a > b:
        print(f"{a} is greater")
    else:
        print(f"{b} is greater")


name = input("enter your name: ")
greet(name)
print("Enter number to check greater number")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))

greater(num1, num2)
"""

# Mini Calculator


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    if b >= 1:
        print(f"Divide {a} by {b} is {a/b}")
    else:
        print("Error : ZeroDivideError")


def mod(a, b):
    if b >= 1:
        print(f"dividing {a} by {b} and remainder is {a % b}")
    else:
        print("Error : ZeroDivideError")


print("Select sign:\n+ = Addition\n- = Subtraction\n* = multiplication\n/ = divide\n% = remainder")
choice = input("Enter the sign: ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == '+':
    addition = add(a, b)
    print(f"Sum of {a} and {b} is {addition}")
elif choice == '-':
    subtraction = sub(a, b)
    print(f"Subtraction of {a} and {b} is {subtraction}")
elif choice == '*':
    multiple = mul(a, b)
    print(f"Multiplication of {a} and {b} is {multiple}")
elif choice == '/':
    divide = div(a, b)
elif choice == '%':
    module = mod(a, b)
else:
    print("Invalid sign, please enter sign in ( +, - , * , / , %)")
