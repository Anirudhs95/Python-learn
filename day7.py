import pandas as pd

data = pd.read_csv("expenses.csv")
print("Full data:")
print(data)

print("Expenses:")
total = data["Amount"].sum()
print(f"Total Expenses: {total} ₹")

print("Catagory-wise total")
cata_tol = data.groupby("Category")["Amount"].sum()
print(cata_tol)

print("Highest spending catagory:")
maximum = data[data["Amount"] == data["Amount"].max()]
print(maximum)
