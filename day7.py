# day 7 using pandas in CSV
import pandas as pd

data = pd.read_csv("expenses.csv")
print("Full data:")
print(data)

# Total expenses
print("Expenses:")
total = data["Amount"].sum()
print(f"Total Expenses: {total} ₹")

# catagory-wis expenses
print("Catagory-wise total")
cata_tol = data.groupby("Category")["Amount"].sum()
print(cata_tol)

# max amiunt spended
print("Highest spending catagory:")
maximum = data[data["Amount"] == data["Amount"].max()]
print(maximum)
