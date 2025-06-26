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