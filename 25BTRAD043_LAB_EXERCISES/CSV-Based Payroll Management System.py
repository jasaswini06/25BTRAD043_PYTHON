import csv

filename = "employees.csv"

# Demo: Create sample CSV if not existing
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["EmpID", "Name", "BasicSalary"])
    writer.writerow(["101", "Alice", "50000"])
    writer.writerow(["102", "Bob", "40000"])

# Process Payroll
print(
    f"{'ID':<6} {'Name':<10} {'Gross':<10} {'Deductions':<12} {'Net Salary':<10}"
)
print("-" * 50)

with open(filename, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        basic = float(row["BasicSalary"])
        gross = basic + (0.20 * basic) + (0.10 * basic)  # Basic + HRA + DA
        deductions = (0.12 * basic) + (0.05 * gross)  # PF + Tax
        net = gross - deductions

        print(
            f"{row['EmpID']:<6} {row['Name']:<10} {gross:<10.2f} {deductions:<12.2f} {net:<10.2f}"
        )