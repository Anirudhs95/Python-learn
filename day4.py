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

def add_expense(name, amount):
    with open("Expenses.txt", "a") as file:
        file.write(f"{name} = {amount} Rupees\n")

def show_expenses():
    print("\n--- All Expenses ---")
    with open("Expenses.txt", "r") as file:
        print(file.read())

while True:
    print("\n1. Add Expense\n2. Show Expenses\n3. Exit")
    choice = input("Choose option: ")

    if choice == "1":
        item = input("Enter expense item: ")
        cost = input("Enter amount: ")
        add_expense(item, cost)
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        break
    else:
        print("Invalid option. Try again.")
