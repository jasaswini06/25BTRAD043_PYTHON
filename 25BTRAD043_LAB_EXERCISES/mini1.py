def calculate_grade(mark):
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    if mark >= 50:
        return "D"
    return "F"


def main():
    print("Student Grading System")
    name = input("Enter student name: ")

    try:
        number_of_subjects = int(input("Enter number of subjects: "))
        if number_of_subjects <= 0:
            print("Number of subjects must be greater than zero.")
            return

        marks = []
        for subject in range(1, number_of_subjects + 1):
            mark = float(input(f"Enter marks for subject {subject} (0-100): "))
            if not 0 <= mark <= 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(mark)
    except ValueError:
        print("Please enter valid numbers.")
        return

    average = sum(marks) / len(marks)
    result = "Pass" if average >= 50 else "Fail"

    print("\n--- Grade Report ---")
    print(f"Student: {name}")
    print(f"Total marks: {sum(marks):.2f}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {calculate_grade(average)}")
    print(f"Result: {result}")


if __name__ == "__main__":
    main()