import pandas as pd
from fpdf import FPDF

# Load CSV
df = pd.read_csv("expenses.csv")

# Calculate summary
total = df["Amount"].sum()
category_summary = df.groupby("Category")["Amount"].sum()

# Save to Excel
category_summary.to_excel("summary.xlsx", sheet_name="Summary")

print("✅ Excel file saved: summary.xlsx")

# Save to PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Expense Summary Report", ln=True, align="C")
pdf.ln(10)

pdf.cell(200, 10, txt=f"Total Expense: Rs {total}", ln=True)

pdf.ln(5)
for cat, amt in category_summary.items():
    pdf.cell(200, 10, txt=f"{cat}: Rs {amt}", ln=True)

pdf.output("summary.pdf")
print("✅ PDF file saved: summary.pdf")
