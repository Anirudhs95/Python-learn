# Day 2 - If/Else
marks = int(input("Enter your marks: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C or below")

# Day 2 - Loops

# For loop example
for i in range(1, 6):
    print("Step", i)

# While loop example
count = 0
while count < 3:
    print("Repeating:", count)
    count += 1

# Write a program to find the sum of numbers from 1 to 100
num = int(input("Enter a number 1 to 100: "))
sum = 0
if num > 100 or num < 1:
    print("Please enter a valid number between 1 and 100.")
else:
    for i in range(1, num+1):
        sum += i
    print("Sum of numbers from 1 to", num, "is:", sum)

# using while loop to find the sum of numbers from 1 to 100
num1 = int(input("Enter a number 1 to 100: "))
count = 1
sum_while = 0
while count <= num1:
    sum_while += count
    count += 12
print("Sum of numbers from 1 to", num1, "is:", sum_while)


# Write a multiplication table for any number entered by user
T_num = int(input("Enter a number: "))
for i in range(1, 11):
    res = T_num * i
    print(f"{T_num}X{i}={res}")

# using while loop to print multiplication table
tab = int(input("Enter a number: "))
count = 1
while count < 11:
    result = tab * count
    print(f"{tab}X{count}={result}")
    count += 1