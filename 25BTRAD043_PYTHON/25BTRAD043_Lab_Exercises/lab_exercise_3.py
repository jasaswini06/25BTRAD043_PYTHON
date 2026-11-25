contacts = []

while True:
    print("\n1. Add  2. Search  3. Update  4. Delete  5. Display  6. Exit")
    choice = input("Enter choice: ").strip()

    if choice == "6":
        print("Contact book closed.")
        break

    if choice == "5":
        if not contacts:
            print("Contact book is empty.")
        else:
            print("All contacts:")
            for contact in contacts:
                print(f"{contact['name']} - {contact['phone']}")
        continue

    if choice not in ("1", "2", "3", "4"):
        print("Invalid choice.")
        continue

    name = input("Enter name: ").strip()
    if not name:
        print("Name cannot be empty.")
        continue

    found = None
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            found = contact
            break

    if choice == "1":
        if found is not None:
            print("A contact with that name already exists.")
        else:
            phone = input("Enter phone number: ").strip()
            contacts.append({"name": name, "phone": phone})
            print("Contact added.")

    elif found is None:
        print("Contact not found.")

    elif choice == "2":
        print(f"{found['name']} - {found['phone']}")

    elif choice == "3":
        found["phone"] = input("Enter new phone number: ").strip()
        print("Contact updated.")

    elif choice == "4":
        contacts.remove(found)
        print("Contact deleted.")

students = {}
total = int(input("Enter number of students: "))

while len(students) < total:
    name = input("Enter student name: ").strip()
    if not name or name in students:
        print("Enter a non-empty, unique name.")
        continue

    try:
        marks = int(input("Enter marks out of 100: "))
    except ValueError:
        print("Enter marks as a whole number.")
        continue

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        continue

    students[name] = marks

print("\nStudent Results")
for name, marks in students.items():
    if marks >= 90:
        grade = "A"
    elif marks >= 75:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"{name} - {marks}/100 - Grade {grade}")

text = input("Enter a sentence or survey responses: ").lower()

                                                          
for symbol in ",.!?;:":
    text = text.replace(symbol, " ")

words = text.split()
frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print("\nWord frequencies")
for word, count in frequency.items():
    print(f"{word} - {count}")
