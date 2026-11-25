# Attendance Tracker
students = {}
threshold = 75

while True:
    print("\n1. Add student  2. Mark or update attendance")
    print("3. Display attendance  4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter student name: ").strip().title()
        if not name:
            print("Name cannot be empty.")
        elif name in students:
            print("Student already exists.")
        else:
            students[name] = []
            print("Student added.")

    elif choice == "2":
        name = input("Enter student name: ").strip().title()
        if name not in students:
            print("Student not found.")
            continue

        date = input("Enter class date (DD-MM-YYYY): ").strip()
        status = input("Enter P for Present or A for Absent: ").strip().upper()

        if not date or status not in ("P", "A"):
            print("Enter a date and a valid attendance status.")
            continue

        for record in students[name]:
            if record["date"] == date:
                record["status"] = status
                print("Attendance updated.")
                break
        else:
            students[name].append({"date": date, "status": status})
            print("Attendance added.")

    elif choice == "3":
        if not students:
            print("No students added.")
            continue

        print(f"\nAttendance Report (minimum {threshold}%)")

        for name, records in students.items():
            if not records:
                print(f"{name} | No attendance recorded")
                continue

            present = 0
            details = []

            for record in records:
                details.append(f"{record['date']}: {record['status']}")
                if record["status"] == "P":
                    present += 1

            total = len(records)
            percentage = present / total * 100
            result = "Below threshold" if percentage < threshold else "Meets threshold"

            print(f"{name} | {', '.join(details)}")
            print(f"Present: {present}/{total} | {percentage:.2f}% | {result}")

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")

print()

# Sales Dashboard
products = []

while True:
    print("\n1. Add or update product  2. Show sales summary  3. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        name = input("Enter product name: ").strip().title()

        try:
            quantity = int(input("Enter total quantity sold: "))
            price = float(input("Enter price per unit: "))
        except ValueError:
            print("Enter a whole number for quantity and a number for price.")
            continue

        if not name or quantity < 0 or not 0 <= price < float("inf"):
            print("Enter a product name and valid non-negative values.")
            continue

        for product in products:
            if product["name"] == name:
                product["quantity"] = quantity
                product["price"] = price
                print("Product updated.")
                break
        else:
            products.append({
                "name": name,
                "quantity": quantity,
                "price": price
            })
            print("Product added.")

    elif choice == "2":
        if not products:
            print("No sales records available.")
            continue

        total_sales = 0
        highest_quantity = max(product["quantity"] for product in products)
        top_products = []

        print("\nProduct Sales Summary")

        for product in products:
            name = product["name"]
            quantity = product["quantity"]
            price = product["price"]
            revenue = quantity * price
            total_sales += revenue

            print(f"{name} | Units: {quantity} | Revenue: Rs. {revenue:.2f}")

            if quantity == highest_quantity:
                top_products.append(name)

        print(f"Total sales: Rs. {total_sales:.2f}")

        if highest_quantity == 0:
            print("No units sold yet.")
        else:
            print(f"Highest-selling by units: {', '.join(top_products)} "
                  f"({highest_quantity} units each)")

    elif choice == "3":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
