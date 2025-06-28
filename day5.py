# Smart Calculator with History

def calculator(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        if b != 0:
            return a/b
        else:
            return "ZerodivideError"
    elif op == "%":
        if b != 0:
            return a % b
        else:
            return "ZerodivideError"
    else:
        print("Invalin choice, Choose operator this only(+, -, *, /, %)")


def save_to_history(a, b, op, result):
    with open("History.txt", "w") as f:
        f.write(f"{a} {op} {b} = {result}\n")


def show_history():
    try:
        with open("History.txt", "r") as t:
            print("\n--- Calculation History ---")
            data = t.read()
            print(data)
    except FileNotFoundError:
        print("No history found.")


while True:
    print("choose your choice according to task")
    print("1 = Calaculator\n2 = Calaculator History\n3 = exit")
    choice = input("enter your choice: ")

    if choice == "1":
        a = float(input("Enter first number: "))
        b = float(input("Enter Second number: "))
        op = input("Enter the operator to perform: ")
        result = calculator(a, b, op)
        print("Result:", result)

        save_to_history(a, b, op, result)

    elif choice == "2":
        show_history()

    elif choice == "3":
        break

    else:
        print("invalid choice")
