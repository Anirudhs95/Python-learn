import csv
from collections import defaultdict

total_expense = 0
categorial_total = defaultdict(float)

with open("expenses.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        Category = row[1]
        Amount = float(row[2])
        total_expense += Amount
        categorial_total[Category] += Amount

print("\n Total expenses:", total_expense)
print("Category wise breakdown:")

for cat, amt in categorial_total.items():
    print(f"{cat}:{amt}")
