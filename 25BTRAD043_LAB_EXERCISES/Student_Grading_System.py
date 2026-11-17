def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    students = {}
    num_students = int(input("Enter number of students: "))
    subjects = ["Subject 1", "Subject 2", "Subject 3"]

    for i in range(num_students):
        print(f"\nEntering details for student {i + 1}:")
        name = input("Enter student name: ").strip()
        marks = []
        for sub in subjects:
            while True:
                try:
                    score = float(input(f"  Enter marks for {sub} (out of 100): "))
                    if 0 <= score <= 100:
                        marks.append(score)
                        break
                    print("  Invalid score! Enter a value between 0 and 100.")
                except ValueError:
                    print("  Invalid input! Please enter a numeric value.")
        students[name] = marks

    # Display Report
    print("\n" + "=" * 65)
    print(f"{'Student Name':<18} {'Total':<10} {'Percentage':<14} {'Grade':<8}")
    print("=" * 65)

    for name, mark_list in students.items():
        total = sum(mark_list)
        percentage = total / len(mark_list)
        grade = calculate_grade(percentage)
        print(f"{name:<18} {total:<10.2f} {percentage:<14.2f}% {grade:<8}")

    print("=" * 65)


if __name__ == "__main__":
    main()