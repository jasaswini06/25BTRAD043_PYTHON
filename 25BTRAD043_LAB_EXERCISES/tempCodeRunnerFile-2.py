filename = "students.txt"

while True:
    print("\n1. Add  2. View All  3. Search  4. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "1":
        rno = input("Roll No: ")
        name = input("Name: ")
        marks = input("Marks: ")
        with open(filename, "a") as f:
            f.write(f"{rno},{name},{marks}\n")
        print("Record added.")

    elif choice == "2":
        try:
            with open(filename, "r") as f:
                print("\nRollNo | Name | Marks")
                print("-" * 25)
                for line in f:
                    print(line.strip().replace(",", " | "))
        except FileNotFoundError:
            print("No records found.")

    elif choice == "3":
        target = input("Enter Roll No to search: ").strip()
        found = False
        try:
            with open(filename, "r") as f:
                for line in f:
                    rno, name, marks = line.strip().split(",")
                    if rno == target:
                        print(f"Found -> Name: {name}, Marks: {marks}")
                        found = True
                        break
            if not found:
                print("Record not found.")
        except FileNotFoundError:
            print("No records found.")

    elif choice == "4":
        break
    else:
        print("Invalid choice.")