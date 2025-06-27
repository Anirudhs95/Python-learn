# list and dictionary

fruits = ["apple", "banana", "mango"]
print("First fruit:", fruits[0])
fruits.append("orange")
print("All fruits:", fruits)

person = {"Name": "Ajay", "Age": 23, "Country": "America"}
print(person)
print(person["Name"])
person["Age"] += 1
print("Updated age:", person["Age"])
print(person.keys)
print(person.values)
for key, values in person.items():
    print(key, ":", values)

# file handling

with open("sample.txt", "w") as file:
    file.write("Welcome to the new file.\n")

with open("sample.txt", "r") as file:
    content = file.read()
    print("File content:", content)

# Expence tracker


def add_expenses(name, cost):
    with open("Expenses.txt", "w") as f:
        f.write(f"{name} = {cost}$")


def show_expenses():
    print("-----All Expenses-----")
    with open("Expenses.txt", "r") as f:
        data = f.read()
        print(data)


print("\n1. adding expenses.\n2. showing expenses.")
choice = int(input("Enter your choice: "))

if choice == 1:
    obj = input("Enter the expenditure name: ")
    ammount = float(input("Enter the price of expenditure: "))
    add_expenses(obj, ammount)
elif choice == 2:
    show_expenses()
else:
    print("invalid choice")
