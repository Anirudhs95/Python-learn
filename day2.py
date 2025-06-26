# if, elif, else statements
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("name:", name)
print("age:", age)

if age <= 18:
    print(name, "is a minor.")
elif age <= 60:
    print(name, "is an adult.")
else:
    print(name, "is a senior citizen.")

# Nested if statements
if age < 18:
    if age < 13:
        print(name, "is a child.")
    else:
        print(name, "is a teenager.")

# Finding the number
num1 = int(input("Enter first number: "))

print("Number:", num1)

if num1 < 0:
    print(num1, "is a negative number.")
elif num1 > 0:
    if num1 <= 10:
        print("number is a positive number and less than or equal to 10.")
    elif num1 > 10:
        print("number is a positive number and greater than 10.")
else:
    print("number is zero.")

# for loop

for i in range(2, 20, 2):
    print(i)

colors = ["red", "green", "blue", "yellow"]
for col in colors:
    print(col)
    for i in col:
        print(i)

# Tables
numb = int(input("Enter a number: "))
for i in range(1, 11):
    result = numb*i
    print(f"{numb} x {i} = {result}")
