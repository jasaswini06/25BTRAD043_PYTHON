import re
from pathlib import Path

                                                            
possible_paths = [
    Path.cwd() / "app.log",
    Path.cwd() / "25BTRAD043_Lab_Exercises" / "app.log",
]

log_file = next(
    (path for path in possible_paths if path.exists()),
    None,
)

if log_file is None:
    matches = list(Path.cwd().rglob("app.log"))
    log_file = matches[0] if matches else None

counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}

if log_file is None:
    print("Log file not found. Save app.log beside lab_exercise_4.ipynb.")
else:
    try:
        with open(log_file, "r", encoding="utf-8") as file:
            content = file.read()

        if not content.strip():
            print("The log file is empty.")
        else:
            keywords = re.findall(r"\b(ERROR|WARNING|INFO)\b", content)
            for keyword in keywords:
                counts[keyword] += 1

            print("Log Summary")
            for keyword, count in counts.items():
                print(f"{keyword}: {count}")

    except FileNotFoundError:
        print("Log file not found. Save app.log beside lab_exercise_4.ipynb.")

import json
from pathlib import Path

base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
data_file = base_dir / "students.json"

try:
    with open(data_file, "r", encoding="utf-8") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}


def show_student(usn, student):
    print(f"{usn} | {student['name']} | {student['marks']}/100")


while True:
    print("\n1. Add  2. Search  3. Update  4. Display  5. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "5":
        print("Program closed.")
        break

    if choice == "4":
        if not students:
            print("No student records found.")
        else:
            print("USN | Name | Marks")
            for usn, student in students.items():
                show_student(usn, student)
        continue

    if choice not in ("1", "2", "3"):
        print("Invalid choice.")
        continue

    usn = input("Enter USN: ").strip().upper()
    if not usn:
        print("USN cannot be empty.")
        continue

    if choice == "1" and usn in students:
        print("This USN already exists.")
        continue

    if choice in ("2", "3") and usn not in students:
        print("Student not found.")
        continue

    if choice == "2":
        show_student(usn, students[usn])
        continue

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        continue

    try:
        marks = int(input("Enter marks out of 100: "))
    except ValueError:
        print("Marks must be a whole number.")
        continue

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        continue

    students[usn] = {"name": name, "marks": marks}

    with open(data_file, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)

    if choice == "1":
        print("Student added.")
    else:
        print("Student updated.")

import csv
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path

base_dir = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
csv_file = base_dir / "employees.csv"
required_columns = {
    "employee_id", "name", "basic_salary", "allowance", "deduction_percent"
}
paise = Decimal("0.01")

try:
    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        employees = csv.DictReader(file)

        if not required_columns.issubset(employees.fieldnames or []):
            print("The CSV file is missing required columns.")
        else:
            print("Salary Summary (INR)")

            for row_number, employee in enumerate(employees, start=2):
                try:
                    employee_id = (employee["employee_id"] or "").strip()
                    name = (employee["name"] or "").strip()
                    basic = Decimal(employee["basic_salary"] or "")
                    allowance = Decimal(employee["allowance"] or "")
                    rate = Decimal(employee["deduction_percent"] or "")

                    if not all(value.is_finite()
                               for value in (basic, allowance, rate)):
                        raise ValueError

                    if (not employee_id or not name or basic < 0
                            or allowance < 0 or not 0 <= rate <= 100):
                        raise ValueError

                    gross = (basic + allowance).quantize(
                        paise, rounding=ROUND_HALF_UP
                    )
                    deduction = (gross * rate / 100).quantize(
                        paise, rounding=ROUND_HALF_UP
                    )
                    net = gross - deduction

                    print(f"{employee_id} | {name} | Gross: {gross:.2f} | "
                          f"Deduction: {deduction:.2f} | Net: {net:.2f}")

                except (InvalidOperation, ValueError):
                    print(f"Row {row_number} skipped because of invalid data.")

except FileNotFoundError:
    print("CSV file not found. Save employees.csv next to the notebook.")
